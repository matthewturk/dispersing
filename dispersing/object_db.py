class ObjectDatabase:
    def __init__(self, game):
        self.object_asset = game.assets["OBJECTS"]
        self.objects_by_id = {}
        self.objects_by_name = {}
        self.images_by_id = {}
        self.images_by_name = {}
        self.id_to_name = {}
        text_asset = game.assets["TEXT"]
        for i, obj in enumerate(self.object_asset.object):
            small_id = obj.image_id + 100
            big_id = obj.image_id + 333
            name = text_asset.text[obj.text_record].value.decode("ascii")
            self.id_to_name[i] = name
            self.objects_by_id[i] = obj
            self.objects_by_name[name] = obj
            self.images_by_id[i] = (
                game.resources.sprites[small_id],
                game.resources.sprites[big_id],
            )
            self.images_by_name[name] = self.images_by_id[i]

    def __contains__(self, key):
        return key in self.objects_by_id or key in self.objects_by_name

    def __getitem__(self, item):
        if item in self.objects_by_id:
            return (self.objects_by_id[item], self.images_by_id[item])
        elif item in self.objects_by_name:
            return (self.objects_by_name[item], self.images_by_name[item])
        else:
            raise KeyError(item)
