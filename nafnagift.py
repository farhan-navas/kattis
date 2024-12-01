import sys

def get_input():
    l1 = sys.stdin.readline().strip()
    l2 = sys.stdin.readline().strip()
    return l1, l2

def scs(l1, l2):
    # len(l1) is the inside array -> x-axis, len(l2) is the outside array -> y-axis
    l1_len = len(l1) + 1
    l2_len = len(l2) + 1
    res = [['' for _ in range(l1_len)] for _ in range(l2_len)]

    for x in range(l2_len):
        res[x][0] = l2[:x]

    for y in range(l1_len):
        res[0][y] = l1[:y]

    for i in range(1, l2_len):
        for j in range(1, l1_len):
            if l1[j-1] == l2[i-1]:
                res[i][j] = res[i-1][j-1] +l1[j-1]
            else:
                if (len(res[i][j-1]) < len(res[i-1][j])):
                    res[i][j] = res[i][j-1] + l1[j-1]

                else:
                    res[i][j] = res[i-1][j] + l2[i-1]
    
    print(res[l2_len-1][l1_len-1])
    

l1, l2 = get_input()
scs(l1, l2)