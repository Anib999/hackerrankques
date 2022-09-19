# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    # for i in A:
    #     for j in B:
    #         lister.append((i, j))

    newList = [
        (x, y)
            for x in A
                for y in B
    ]
    newList.sort()
    print(*newList, sep=' ')