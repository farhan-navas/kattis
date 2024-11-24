import sys
from random import sample

def get_input():
    return sys.stdin.readline().strip()

def guess_word(n):
    letters = ['A', 'I', 'P', 'Z']
    res = ''
    for i in range(int(n)):
        letters = sample(letters, 4)
        found_letter = False
        for j in range(3):
            res += letters[j]
            print(res, flush=True)
            n = int(get_input())
            if n == 2:
                return
            elif n == 1:
                found_letter = True
                break
            res = res[:-1]
        
        if not found_letter:
            res += letters[3]
    
    print(res, flush=True)


n = get_input()
guess_word(n)