def second_largest(arr):
    max_num = max(arr)
    arr.remove(max_num)
    if not arr:
        return float('-inf')
    else:
        return max(arr)

def f():
    numbers = []
    while True:
        n = int(input())
        if n == 0:
            break
        numbers.append(n)
    print("Второй по величине элемент:", second_largest(numbers))

f()
