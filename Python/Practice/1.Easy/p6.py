def parallel_resistance(res):
    r_total = 0
    for i in res:
        div = 1/i
        r_total += div
    return 1/r_total


print(parallel_resistance([6, 3]))
print(parallel_resistance([10, 20, 10]))
print(parallel_resistance([500, 500, 500]))
