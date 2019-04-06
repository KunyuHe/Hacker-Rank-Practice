# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
nums = list(map(int, input().split()))
weights = list(map(int, input().split()))

weighted_sum = 0

for i in range(size):
    weighted_sum += nums[i] * weights[i]

print(round(weighted_sum / sum(weights), 1))
