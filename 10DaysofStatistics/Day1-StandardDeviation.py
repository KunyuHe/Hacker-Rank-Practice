# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
nums = sorted(list(map(int, input().split())))

mean = sum(nums) / size
total = 0

for num in nums:
    total += (num - mean) ** 2

print(round((total / size) ** 0.5, 1))
