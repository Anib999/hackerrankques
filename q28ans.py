# start here now
def merge_the_tools(string, k):
    # your code goes here
    newList = []
    for i in range(0, len(string), k):
        newList.append(
            "".join(dict.fromkeys(string[i:i+k]))
        )
    print(*newList, sep='\n')
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)