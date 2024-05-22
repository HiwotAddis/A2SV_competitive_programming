from collections import defaultdict
n, m = map(int, input().split())

group_a_indices = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_a_indices[word].append(i)
for _ in range(m):
    word = input().strip()
    if word in group_a_indices:
        print(' '.join(map(str, group_a_indices[word])))
    else:
        print(-1)
