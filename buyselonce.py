def stock_two(A):
    # brute force aproach
    A_len = len(A)
    profit = 0
    best2 = 0
    best = 0
    sell_day = 0
    for i in range(A_len - 1):
        for j in range(i + 1, A_len):
            profit = A[j] - A[i]
            if profit > best:
                best = profit
                sell_day = j
    for i in range(sell_day, A_len):
        for j in range(sell_day + 1, A_len):
            profit = A[j] - A[i]
            if profit > best2:
                best2 = profit
    best = max(0, best) + max(0, best2)
    return max(0, best)


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
profit = stock_two(A)
print(profit)
