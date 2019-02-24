def stock_one(A):
    # brute force aproach
    A_len = len(A)
    profit = 0
    best = 0
    for i in range(A_len - 1):
        for j in range(i + 1, A_len):
            profit = A[j] - A[i]
            if profit > best:
                best = profit
    if best:
        return best

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
profit = stock_one(A)
print(profit)
