def surfaceArea(A):
    h, w = len(A), len(A[0])
    # Top and bottom
    area = 2*h*w

    for i in range(h):
        for j in range(w):
            # Exposed adjacent, subtract overlapping ones
            if i == 0:
                upper_sub = 0
            else:
                upper_sub = A[i-1][j]

            if i == h-1:
                lower_sub = 0
            else:
                lower_sub = A[i+1][j]

            if j == 0:
                left_sub = 0
            else:
                left_sub = A[i][j-1]

            if j == w-1:
                right_sub = 0
            else:
                right_sub = A[i][j+1]

            area += max(0, A[i][j] - upper_sub) + max(0, A[i][j] - lower_sub)
            area += max(0, A[i][j] - left_sub) + max(0, A[i][j] - right_sub)

    return area
