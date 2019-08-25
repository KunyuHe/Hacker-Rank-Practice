def permutationEquation(p):
    value_index = {val: i for i, val in enumerate(p)}
    output = []

    for x in range(1, len(p)+1):
        p = value_index[x] + 1
        output.append(value_index[p] + 1)

    return output