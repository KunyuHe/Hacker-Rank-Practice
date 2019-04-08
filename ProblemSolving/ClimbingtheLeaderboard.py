# Start from the lowest

def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)), reverse=True)

    result = []
    l = len(scores)

    for score in alice:
        while (l > 0) and (score >= scores[l - 1]):
            l -= 1
        result.append(l + 1)
    return result
