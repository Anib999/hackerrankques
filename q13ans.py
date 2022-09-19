# # Enter your code here. Read input from STDIN. Print output to STDOUT
# def createCombi(arr, leng):
#     totalLoop =  int(leng)
#     #  if leng != 0 else len(arr)

#     if totalLoop == 0:
#         return [[]]

#     lis = []

#     for i in range(0, totalLoop):
#         m = arr[i]
#         remList = arr[i + 1:]
#         remCom = createCombi(remList, totalLoop - 1)
#         for j in remCom:
#             lis.append([m, *j])
#     return lis

# def createCombinew(x, leng):
#     final = [[]]
#     l = int(leng) if leng != 0 else len(x)
#     groups = [list(x)] * l
#     for i in groups:
#         final = [x+[y] for x in final for y in i]
#     for k in final:
#         yield ''.join(k)

# if __name__ == '__main__':
#     [*name], leng = input().upper().split()
#     # print(createCombi(name, leng))
#     newL = list(createCombinew(name, leng))
#     newL.sort()
#     print(newL)
#     # les = [[a,b] for a in name for b in name if a != b ]
#     # sorter = [(a + b) for a,b in les]
#     # sorter.sort()
#     # print(sorter)
from itertools import permutations

S = input().upper().split()

for i in sorted(permutations(S[0], int(S[1]))):
    print(''.join(i))