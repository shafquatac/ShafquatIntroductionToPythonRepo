if __name__ == '__main__':
    # sum(2,4)
    a = -1
    b = abs(a)
    print(b)


def sum(start, end):

    sum = 0
    for item in range(start, end):
        sum = sum + item
    return sum
    print(sum(0, 10))