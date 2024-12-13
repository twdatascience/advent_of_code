with open('2024-12-02/input.txt', 'r') as f:
    content = f.read().strip().split('\n')

ans = 0
for report in content:
    values = list(map(int, report.split()))
    safepos = set([1, 2, 3])
    safeneg = set([-1, -2, -3])
    for i in range(1, len(values)):
        safepos.add(values[i] - values[i - 1])
        safeneg.add(values[i] - values[i - 1])

    if len(safepos) == 3 or len(safeneg) == 3:
        ans += 1

print(ans)