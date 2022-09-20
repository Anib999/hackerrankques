if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    del integer_list[n:]
    print(hash(tuple(integer_list)))