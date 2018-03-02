import math

def heapify(x, pos):
    length = len(x)

    n = (math.floor((length) / 2))
    if (pos >= n):
        return x
    else:
        right = 2 * pos + 2
        left = 2 * pos + 1
        maximum = pos
        if (left < length and x[left] > x[maximum]):
            maximum = left

        if (right < length and x[right] > x[maximum]):
            maximum = right

        if (maximum == pos):
            return x

        x[maximum], x[pos] = x[pos], x[maximum]
        heapify(x, maximum)


def build_heap(x):
    n = math.floor(len(x) / 2)
    for i in reversed(range(n)):
        heapify(x, i)
    return x


def extract_max(x):
    maxi = x[0]
    x[-1], x[0] = x[0], x[-1]
    x = x[0:-1]
    heapify(x, 0)
    return x, maxi


def heap_sort(x):
    a = []
    x = build_heap(x)
    length = len(x)
    for i in range(length):
        x, maxi = extract_max(x)
        a.append(maxi)

    return a


inp=[13,222,35,46,577,68,7,2,111,223,1,44444,55,333333,1]
output=heap_sort(inp)
print(output)