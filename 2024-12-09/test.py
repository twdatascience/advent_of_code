import sys
import re
from collections import defaultdict, Counter, deque
import pdb

sys.setrecursionlimit(10**6)
p1 = 0
p2 = 0
D = open("2024-12-09/input9.txt").read().strip()

def solve(part2):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i,c in enumerate(D):
        if i%2==0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1
    pdb.set_trace()
    for (pos, sz, file_id) in reversed(A):
        for space_i,(space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos+i] == file_id, f'{FINAL[pos+i]=}'
                    FINAL[pos+i] = None
                    FINAL[space_pos+i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz-sz)
                break

    ans = 0
    for i,c in enumerate(FINAL):
        if c is not None:
            ans += i*c
    return ans

p1 = solve(False)
p2 = solve(True)
print(p1)
print(p2)

# p1 = 6385338159127
# p2 = 6415163624282