stones = list(map(int, open("2024-12-11/input11.txt").read().strip().split()))


memory = {}

def solve(stone, blinks):
    if blinks == 0:
        return 1
    elif (stone, blinks) in memory:
        return memory[(stone, blinks)]
    elif stone == 0:
        val = solve(1, blinks - 1)
    elif len(str(stone)) % 2 == 0:
        loc = len(str(stone)) // 2
        val = solve(int(str(stone)[:loc]), blinks - 1) + solve(int(str(stone)[loc:]), blinks - 1)
    else:
        val = solve(stone * 2024, blinks - 1)
    memory[(stone, blinks)] = val
    return val

count = 0
for stone in stones:
    count += solve(stone, 75)

print(count)

