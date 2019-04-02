def plusMinus(arr):
    pos, neg, total = 0, 0, len(arr)
    
    for num in arr:
        pos += num > 0
        neg += num < 0
    zero = total - pos - neg
    
    list(map(lambda x: print("{:.6f}".format(round(x/total, 6))),
             [pos, neg, zero]))
