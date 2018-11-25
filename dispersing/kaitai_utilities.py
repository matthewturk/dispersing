import numpy as np

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

def unpack_sprite_algo3(s):
    s = np.frombuffer(s, dtype="u1")
    history = np.zeros(0x1000, dtype='u1')
    history[:] = 0xFE
    it = 0xFEE
    si = 0
    pos = 0
    d = []
    while pos < s.size:
        si >>= 1
        if (si & 0x100) == 0:
            si = s[pos]
            pos += 1
            si |= 0xFF00
        if (si & 1) != 0:
            v = s[pos]
            pos += 1
            d.append(v)
            history[it] = v
            it = (it+1) & 0xFFF
        else:
            v1 = s[pos]
            pos += 1
            v2 = s[pos]
            pos += 1
            v1 |= (v2 & 0xF0) << 4
            di = (v2 & 0x0F) + 2
            cx = 0
            while cx <= di:
                bx = (v1 + cx) & 0xFFF
                v = history[bx]
                d.append(v)
                history[it] = v
                it = (it+1) & 0xFFF
                cx += 1
    return np.array(d, dtype='uint8')
