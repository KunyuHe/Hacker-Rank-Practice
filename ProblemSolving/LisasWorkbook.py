def workbook(n, k, arr):
    cnt = 0

    page = 0
    for i in range(n):
        nums = arr[i]
        n_last_page = nums % k

        # Get the number of pages
        if n_last_page == 0:
            chap_pages = nums // k
            n_last_page = k
        else:
            chap_pages = nums // k + 1

        question = 1
        for j in range(chap_pages):
            page += 1
            if page in range(question,
                             question + [k, n_last_page][int(j==chap_pages-1)]):
                cnt += 1
            question += k

    return cnt
