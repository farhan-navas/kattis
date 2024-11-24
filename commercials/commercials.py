import sys

def get_input():
    n, p = map(int, sys.stdin.readline().strip().split())
    n_arr = list(map(int, sys.stdin.readline().strip().split()))
    return n, p, n_arr

def commercials(n, p, students):
    dp = [0] * n
    dp[0] = max(students[0] - p, 0)
    for i in range(1, n):
        profit = students[i] - p
        dp[i] = max(dp[i-1]+ profit, profit, 0)

    print(max(dp))

n, p, n_arr = get_input()
commercials(n, p, n_arr)

