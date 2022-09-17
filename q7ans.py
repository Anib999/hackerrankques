def print_formatted(number):
    # your code goes here
    binaryLen = 0
    for i in range(1, number+1):
        binaryLen = len(bin(i).lstrip('0b'))

    for i in range(1, number+1):
        print(str(i).rjust(binaryLen), str(oct(i).lstrip('0o')).rjust(binaryLen), str(hex(i).lstrip('0x').upper()).rjust(binaryLen), str(bin(i).lstrip('0b')).rjust(binaryLen))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)