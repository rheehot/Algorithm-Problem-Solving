import sys
sys.stdin = open('10250_ACM 호텔.txt', 'rt')

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    answer = str(N%H)
    if len(str(N//H + 1)) == 1:
        answer += '0'
    answer += str(N//H + 1)
    print(answer)