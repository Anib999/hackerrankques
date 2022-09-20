if __name__ == '__main__':
    N = int(input())
    lister = []
    for i in range(N):
        inputCommand = input().split()
        if inputCommand != []:
            if inputCommand[0] == 'insert':
                lister.insert(int(inputCommand[1]), int(inputCommand[2]))
            elif inputCommand[0] == 'remove':
                lister.remove(int(inputCommand[1]))
            elif inputCommand[0] == 'append':
                lister.append(int(inputCommand[1]))
            elif inputCommand[0] == 'sort':
                lister.sort()
            elif inputCommand[0] == 'pop':
                lister.pop()
            elif inputCommand[0] == 'reverse':
                lister.reverse()
            elif inputCommand[0] == 'print':
                print(lister)