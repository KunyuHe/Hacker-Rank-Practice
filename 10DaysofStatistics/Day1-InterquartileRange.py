# Enter your code here. Read input from STDIN. Print output to STDOUT


def median(ar, size):
    if size % 2 == 0:
        return (ar[int(size / 2) - 1] + ar[int(size / 2)]) / 2
    else:
        return ar[int((size - 1) / 2)]

size = int(input())
nums = list(map(int, input().split()))
freqs = list(map(int, input().split()))

ar = []
for i in range(size):
    for _ in range(freqs[i]):
        ar.append(nums[i])
ar.sort()

size = sum(freqs)
if size % 2 == 0:
    lower, upper = ar[:int(size / 2)], ar[int(size / 2):]
else:
    lower, upper = ar[:int((size - 1) / 2)], ar[int((size + 1) / 2):]

print("{:.1f}".format(median(upper, len(upper)) - median(lower, len(lower))))
