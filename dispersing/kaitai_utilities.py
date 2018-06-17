def common_attributes(obj_collection):
    shared_attributes = set()
    for obj in obj_collection:
        obj_attributes = set()
        for aname in (_ for _ in dir(obj) if not _.startswith("_")):
            attr = getattr(obj, aname)
            if callable(attr): continue
            obj_attributes.add( (aname, type(attr)) )
        if len(shared_attributes) == 0:
            shared_attributes.update(obj_attributes)
        else:
            shared_attributes.intersection_update(obj_attributes)
    return [_[0] for _ in sorted(shared_attributes)]

def collect_attributes(obj_collection, attr_list):
    values = {_:[] for _ in attr_list}
    for obj in obj_collection:
        for attr in attr_list:
            values[attr].append(getattr(obj, attr))
    return values


