# Enter your code here. Read input from STDIN. Print output to STDOUT
totalInput = int(input())
totalList = input().split()
print(all(int(ele) > 0 for ele in totalList) and any(list(reversed(ele)) == list(ele) for ele in totalList))