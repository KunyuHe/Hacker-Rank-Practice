def breakingRecords(scores):
    score_min = score_max = scores.pop(0)
    min_count = max_count = 0

    for score in scores:
        if score < score_min:
            score_min = score
            min_count += 1
        if score > score_max:
            score_max = score
            max_count += 1

    return max_count, min_count
