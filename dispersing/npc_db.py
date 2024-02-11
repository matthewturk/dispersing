from IPython.display import display
import ipywidgets


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

    def _ipython_display_(self):
        attrs = [
            "npc_id",
            "head_id",
            "flags",
            "col3",
            "col4",
            "col5",
            "col6",
            "sprite_id",
            "body_sprite",
            "action_dmg_ndice",
            "action_dmg_nsides",
            "agility",
            "col11",
            "col12",
            "col13",
            "behavior_flags",
        ]
        html = (
            f"<h3>{self.name}</h3>"
            + "<table>\n<tr>"
            + "".join(f"<th>{attr}</th>" for attr in attrs)
            + "</tr>\n"
            + "".join(f"<td>{getattr(self.record, attr)}</td>" for attr in attrs)
            + "</tr>\n"
        )
        out_head = ipywidgets.Output()
        with out_head:
            display(self.images["head"])
        out_sprite = ipywidgets.Output()
        with out_sprite:
            display(self.images["sprite"])
        display(
            ipywidgets.VBox(
                [ipywidgets.HTML(html), ipywidgets.HBox([out_head, out_sprite])]
            )
        )


class NPCDatabase(dict):
    def __init__(self, game):
        super(dict, self).__init__()
        self.game = game
        for i, npc in enumerate(game.assets["NPC"].npcs):
            npc_obj = NPC(i, game, npc)
            self[i] = self[npc_obj.name] = npc_obj

    def _ipython_display_(self):
        npc_id = ipywidgets.IntSlider(min=0, max=len(self) // 2 - 1, step=1)
        npc_id.value = 0
        out = ipywidgets.Output()

        def change_npc(event):
            with out:
                out.clear_output(wait=True)
                display(self[event["new"]])

        npc_id.observe(change_npc, "value")

        display(ipywidgets.VBox([npc_id, out]))


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
                else:
                    print("ARG", t, arg)

    def _return_table_row_(self, i=-1):
        kw = self.conversation.db.keyword_asset.keyword
        text = self.conversation.db.text_records
        objs = self.conversation.db.game.objects
        html = []
        html.append(f"<tr><td>{i: 3d}</td><td><b>{self.opcode}</b></td></tr>")
        for c in self.command_list:
            for t, arg in zip(c.args.targs, c.args.args):
                html.append(f"</tr><td><b>{c.opcode}</b></td>")
                if t == "k":
                    html.append(f"<td>KEYWORD</td><td>{kw[arg]}</td>")
                elif t == "t":
                    html.append(
                        f"<td>EMIT</td><td>{text[arg].value.decode('ascii')}</td>"
                    )
                elif t == "o":
                    html.append(f"<td>OBJECT</td><td>{objs[arg].name}</td>")
                else:
                    html.append(f"<td>ARG</td><td>{t} {arg}</td>")
        return "\n".join(html)

    def _ipython_display_(
        self,
    ):
        display(ipywidgets.HTML("<table>" + self._return_table_row_() + "</table>"))


class Conversation:
    def __init__(self, db, npc_name, operations):
        self.db = db
        self.operations = operations
        self.npc_name = npc_name
        self.components = [ConversationCommandList(self, cl) for cl in operations]

    def __repr__(self):
        return "Conversation with {}".format(self.npc_name)

    def _ipython_display_(self):
        table_rows = [c._return_table_row_(i) for (i, c) in enumerate(self.components)]
        display(ipywidgets.HTML("<table>" + "".join(table_rows) + "</table>"))


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

    def find_opcode(self, opcode_num):
        found = {}
        for i, conv in self.conv_by_id.items():
            for component in conv.components:
                if any(c.opcode.value == opcode_num for c in component.command_list):
                    found[i] = conv
        return found
