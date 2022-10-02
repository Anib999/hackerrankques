# start here now
def merge_the_tools(string, k):
    # your code goes here
    stringArr = list(string)
    for i in range(0, len(stringArr), k):
        yield stringArr[i:i + k]
    

if __name__ == '__main__':
    string, k = input(), int(input())
    x = list(merge_the_tools(string, k))
    print(x)