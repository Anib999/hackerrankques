# | . -
# WELCOME
# n is odd m is 3 times n
n, m = map(int, input().split())
# for i in range(int(n)):
#     for j in range(int(m)):
#         print('.|.', end='-')
#     print(i)

# num = n

# for i in range(1, num+1):
#     # print(i, 'first')
#     i = i - (num//2 +1)
#     # print(i, 'second')
#     if i < 0:
#         i = -i
#     # print(i, 'last')
#     if i == 0:
#         print("-" * i + "WELCOME" * (num - i*2) + "-"*i)
#     else:
#         print("-" * i + ".|." * (num - i*2) + "-"*i)
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
# print(pattern[::-1])

# N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
# for i in xrange(1,N,2): 
#     print 3*(N-i)/2*"-"+".|."*i+"-"*(3*(N-i)/2)
# print "-"*((3*N-7)/2)+"WELCOME"+"-"*((3*N-7)/2)
# for i in xrange(N-2,-1,-2): 
#     print (3*(N-i)/2)*"-"+".|."*i+"-"*(3*(N-i)/2)