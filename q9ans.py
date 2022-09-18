if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    neslist = list(set(arr))
    neslist.sort()

    print(neslist[-2])

    # newlist = [x for x in arr if x < max(arr)]

    # print(newlist)