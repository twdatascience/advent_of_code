stones = list(map(int, open("2024-12-11/input11.txt").read().strip().split()))


def blink(start):
    new_stones = []
    for stone in start:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            split_loc = len(str(stone)) // 2
            first = int(str(stone)[:split_loc])
            second = int(str(stone)[split_loc:])
            new_stones.append(first)
            new_stones.append(second)
        else:
            new = stone * 2024
            new_stones.append(new)
    
    return new_stones


for i in range(25):
    if i == 0:
        new_s = blink(stones)
    else:
        new_s = blink(new_s)

print(len(new_s))