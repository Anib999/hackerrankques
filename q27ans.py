def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    # print(string.upper())
    s = 0
    k = 0
    for i in range(len(string)):
        if string[i] in vowels:
            k += len(string) - i
        else:
            s += len(string) - i
    if(k>s):
        print('Kevin', k)
    elif(s==k):
        print('Draw')
    else:
        print('Stuart', s)


if __name__ == '__main__':
    s = input()
    minion_game(s)