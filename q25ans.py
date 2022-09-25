from string import ascii_lowercase
def print_rangoli(size):
    for i in range(1,2*size):
        j = ascii_lowercase[abs(size-i):size]
        j = j[-1:0:-1] + j
        print( '-'.join(j).center(4*size-3,'-'))
    # for i in range(size):
    #     for j in range(size):
    #         print(chr(65 + i), end=" ")
    #     print()
    # stoper = 65+int(size)
    # for i in range(65, stoper):
    #     print(chr(65 + i), end=" ")
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)