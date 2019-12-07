cimport cython
import numpy as np
cimport numpy as np

DEF MAX_ALGO3_HIST = 0x1000

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
@cython.initializedcheck(False)
def unpack_sprite_algo3(const np.uint8_t[:] s, np.uint64_t d_size):
    #cdef np.uint8_t[:] s = np.frombuffer(in_s, dtype="uint8")
    cdef np.uint8_t[:] history = np.zeros(MAX_ALGO3_HIST, dtype='u1')
    cdef np.uint64_t it, si, pos, d_pos, di, cx, bx
    cdef np.uint64_t v1, v2
    cdef np.uint8_t v
    cdef np.uint8_t[:] d = np.zeros(d_size, dtype="u1")
    it = 0xFEE
    si = pos = d_pos = di = cx = 0
    history[:] = 0xFE
    # Not sure why this doesn't get optimized out
    cdef np.uint64_t ns = len(s)
    while pos < ns:
        si >>= 1
        if (si & 0x100) == 0:
            si = s[pos]
            pos += 1
            si |= 0xFF00
        if (si & 1) != 0:
            v = s[pos]
            pos += 1
            d[d_pos] = v
            d_pos += 1
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
            for cx in range(di+1):
                bx = (v1 + cx) & 0xFFF
                v = history[bx]
                d[d_pos + cx] = v
                history[it] = v
                it = (it+1) & 0xFFF
            d_pos += di + 1
    return np.asarray(d, dtype='uint8')
