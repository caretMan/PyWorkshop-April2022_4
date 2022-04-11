NK = list(map(int, input().split()))
N, K = NK[0], NK[1]
print(N - K % N)