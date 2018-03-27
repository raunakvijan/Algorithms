def count_sort(input, count, digit):

    output = [0] * len(input)
    for i in range(1,10):
        count[i]+=count[i-1]

    for i in range(9, 0,-1):
        count[i] = count[i-1]
    count[0]=0
    for i in input:
        dig = i//(10**(digit))
        dig = dig % 10
        output[count[int(dig)]] = i
        count[int(dig)] += 1

    return  output

def radix_sort(inp, digits):
    length=len(inp)
    for digit in range(0,digits):
        count = [0] * 10

        for no in inp:
            number = no // (10 **(digit))
            a=(number % (10))
            count[int(a)] += 1
        inp = count_sort(inp, count,digit)
    return inp

inp = [1112,3334,55,7,8,8,4444,44556,77664,4235,543,122,4]
digits = 5
print(radix_sort(inp,digits))
