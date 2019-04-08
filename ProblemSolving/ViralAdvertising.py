def viralAdvertising(n):
    delta_shared, cum_liked = 5, 0
    
    for i in range(n):
        delta_liked = delta_shared // 2
        cum_liked += delta_liked
        delta_shared = delta_liked * 3

    return cum_liked
