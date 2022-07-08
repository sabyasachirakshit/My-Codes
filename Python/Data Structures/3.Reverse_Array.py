def reverse_array(Arr, start, end):
    while start < end:
        Arr[start], Arr[end] = Arr[end], Arr[start]
        start += 1
        end -= 1


A = [1, 2, 3, 4, 5, 6]
print("Array-", A)
reverse_array(A, 0, 5)
print("Reversed Array-", A)
