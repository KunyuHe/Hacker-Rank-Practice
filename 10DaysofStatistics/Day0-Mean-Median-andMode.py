# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
nums = sorted(list(map(int, input().split())))
print(round(sum(nums) / size, 1))


if size % 2 == 0:
    print(round((nums[int(size / 2) - 1] + nums[int(size / 2)]) / 2, 1))
else:
    print(nums[int((size - 1) / 2)])


mode, max_freq = None, 0
for num in nums:
    freq = nums.count(num)
    if freq > max_freq:
        mode, max_freq = num, freq
print(mode)
