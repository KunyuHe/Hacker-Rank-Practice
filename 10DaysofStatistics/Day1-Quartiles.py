# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
nums = sorted(list(map(int, input().split())))

def median(ar, size):
    if size % 2 == 0:
        return int((ar[int(size / 2) - 1] + ar[int(size / 2)]) / 2)
    else:
        return int(ar[int((size - 1) / 2)])

if size % 2 == 0:
    lower, upper = nums[:int(size / 2)], nums[int(size / 2):]
else:
    lower, upper = nums[:int((size - 1) / 2)], nums[int((size + 1) / 2):]

print(median(lower, len(lower)))
print(median(nums, size))
print(median(upper, len(upper)))

