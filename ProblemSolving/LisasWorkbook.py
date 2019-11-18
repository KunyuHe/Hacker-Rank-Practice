def workbook(n, k, arr):
    page = 0
    for nums in arr:
        if nums % k == 0:
            chap_pages = nums // k
        else:
            chap_pages = nums // k + 1
        