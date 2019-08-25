# Enter your code here. Read input from STDIN. Print output to STDOUT

def split(string):
    left, right = "", ""

    for i in range(len(string)):
        if i % 2 == 0:
            left += string[i]
        else:
            right += string[i]

    print(left, right)


t = int(input())
for i in range(t):
    split(str(input()))
