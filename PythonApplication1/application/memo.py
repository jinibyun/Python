# assumption: how to run
# python memo.py -a "Life is too short"
# python memo.py -a "You need python"


import sys

option = sys.argv[1] #note: sys.argv[0] cotains file name ("memo.py")

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