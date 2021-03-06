import numpy as np


class NPCDatabase:
    def __init__(self, game):
        self.npc_asset = game.assets["NPC"]


class ConversationCommandList:
    def __init__(self, conversation, command_list):
        self.conversation = conversation
        self.opcode = command_list.base_opcode
        self.command_list = [c for c in getattr(command_list, "contents", [])]

    def display(self):
        # cc.command_list[0].args.targs
        kw = self.conversation.db.keyword_asset.keyword
        text = self.conversation.db.text_records
        for c in self.command_list:
            for t, arg in zip(c.args.targs, c.args.args):
                if t == "k":
                    print("KEYWORD", kw[arg])
                elif t == "t":
                    print("EMIT", text[arg].value)


class Conversation:
    def __init__(self, db, npc_name, operations):
        self.db = db
        self.operations = operations
        self.npc_name = npc_name
        self.components = [ConversationCommandList(self, cl) for cl in operations]

    def __repr__(self):
        return "Conversation with {}".format(self.npc_name)


class ConversationDatabase:
    def __init__(self, game):
        self.game = game
        self.interact_asset = game.assets["INTERACT"]
        offset = self.interact_asset.file_header.text_offset
        self.text_records = game.assets["TEXT"].text[offset:]
        self.keyword_asset = game.assets["KEYWORDS"]

        self.conv_by_id = {}
        self.conv_by_name = {}

        for i, conv in enumerate(self.interact_asset.npc_interactions):
            n = conv.npc_name.split("\x00")[0]
            c = Conversation(self, n, conv.operations)
            self.conv_by_id[i] = self.conv_by_name[conv.npc_name] = c

    def __contains__(self, key):
        return key in self.conv_by_id or key in self.conv_by_name

    def __getitem__(self, item):
        if item in self.conv_by_id:
            return self.conv_by_id[item]
        elif item in self.conv_by_name:
            return self.conv_by_name[item]
        else:
            raise KeyError(item)
