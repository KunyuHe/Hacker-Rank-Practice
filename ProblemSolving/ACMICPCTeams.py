def acmTeam1(topic):
    n, m = len(topic), len(topic[0])
    max_comb, max_count = 0, 0

    for i in range(n):
        for j in range(i+1, n):
            sum_comb = 0
            for x in range(m):
                sum_comb += max(int(topic[i][x]), int(topic[j][x]))
            if sum_comb > max_comb:
                max_comb = sum_comb
                max_count = 1
            elif sum_comb == max_comb:
                max_count += 1

    return max_comb, max_count


def acmTeam2(topics):
    max_comb, max_count = 0, 0
    for comb in combinations(topics, 2):
        sum_comb = bin(((int(comb[0], 2) | int(comb[1], 2)))).count('1')

        if sum_comb > max_comb:
            max_comb = sum_comb
            max_count = 1
        elif sum_comb == max_comb:
            max_count += 1

    return max_comb, max_count
