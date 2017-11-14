# python memo.py -a "Life is too short"
import sys

option = sys.argv[1]

#print(option)
#print(memo)

if option == '-a': # input
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)