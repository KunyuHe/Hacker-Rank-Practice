def angryProfessor(k, a):
    count = 0

    for time in a:
        if time <= 0:
            count += 1

    return ["YES", "NO"][count >= k]
