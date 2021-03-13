class NPC:
    def __init__(self, index, game, record):
        self.game = game
        self.record = record
        self.index = index
        head_offset = game.assets["INIT"].sprite_offsets.people
        sprite_offset = game.assets["INIT"].sprite_offsets.npc
        self.images = {
            "head": game.resources.sprites[head_offset + record.head_id],
            "sprite": game.resources.sprites[sprite_offset + record.sprite_id],
        }
        # TODO: find this 170
        self.name = game.assets["TEXT"].text[index + 170].value.decode("ascii")
        if record.head_id:
            self.display_name = (
                game.assets["TEXT"].text[record.head_id + 170].value.decode("ascii")
            )


class NPCDatabase(dict):
    def __init__(self, game):
        super(dict, self).__init__()
        self.game = game
        for i, npc in enumerate(game.assets["NPC"].npcs):
            npc_obj = NPC(i, game, npc)
            self[i] = self[npc_obj.name] = npc_obj


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
