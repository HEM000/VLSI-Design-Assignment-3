import random
from operator import*

f = open("TRACEFILE.txt", 'a+')
f.truncate(0)

for i in range(10):
    testcase = []

    a = f'{random.getrandbits(32):=032b}'
    b = f'{random.getrandbits(32):=032b}'
    cin = f'{random.getrandbits(1):=01b}'

    sum = bin(add(int(a, 2), int(b, 2)) + int(cin, 2))[2:]
    cout = '0'

    if len(sum) > 32:
        cout = sum[0]
        sum = sum[1:]
    
    if len(sum) < 32:
        sum = (32-len(sum))*'0'+ sum

    testcase.append(a+b+cin)
    testcase.append(' ')
    testcase.append(sum+cout)
    testcase.append(' ')
    testcase.append('111111111111111111111111111111111\n')

    f.writelines(testcase)

    print(testcase)
f.close()
