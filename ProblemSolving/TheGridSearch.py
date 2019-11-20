def gridSearch(G, P):
    p_h, p_w = len(P), len(P[0])
    search_h, search_w = len(G) - p_h + 1, len(G[0]) - p_w + 1
    nrow_match = 0

    for i in range(search_h):
        for j in range(search_w):
            if G[i][j:j+p_w] == P[0]:
                nrow_match += 1
                # dfs
                for m in range(1, p_h):
                    if G[i+m][j:j+p_w] == P[m]:
                        nrow_match += 1
                    else:
                        nrow_match = 0
                        break
                if nrow_match == p_h:
                    return "YES"

    return "NO"
