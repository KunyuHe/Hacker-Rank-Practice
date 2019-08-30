def is_valid(s, last=None):
    # If it is an empty string or just one letter, it meets the criteria
    if len(s) in [0, 1]:
        return True

    # Initialize the character to check
    if not last:
        last = s[0]

    # Check the condition
    if not s[0] == s[-1] == last:
        return False

    return is_valid(s[1:-1], last)


def substrCount(n, s):
    cnt = 0

    for start in range(n):
        for end in range(start+1, n+1):
            cnt += int(is_valid(s[start:end]))

    return cnt
