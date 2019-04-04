def bonAppetit(bill, k, b):
    if sum(bill[:k] + bill[k+1:]) / 2 == b:
        print("Bon Appetit")
    else:
        print(bill[k] / 2)
