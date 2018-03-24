##### we assume the range of the elements to be between 0-9 #####

def count_sort(inp):
    count = [0] * 10

    for i in inp:
        count[i] += 1

    length = len(count)

    for i in range(1, length, 1):
        count[i] += count[i-1]

    for i in range(length-1, 0,-1):
        count[i] = count[i-1]
    count[0] = 0

    length=len(inp)
    out = [0] * length

    print(count)
    for i in inp:
        a = count[i]
        out[a] = i
        count[i] += 1

    print(out)


inp = [2, 3, 4, 6, 6, 7, 1, 1, 1, 1, 1, 2, 3, 4, 6, 7]
count_sort(inp)