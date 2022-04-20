def H_to_min(H, H_ans):
  sum = 0
  for i in range(len(H)):
    if H[i] > H_ans:
      sum += H_ans
    else:
      sum += H[i]
  return sum

def binary(H_ans, step):
  H_new = H_to_min(H, H_ans)
  H_new1 = H_to_min(H, H_ans + 1)
  if step <= 1:
    step = 2
  if H_ans * N <= H_new + M and (H_ans + 1) * N > H_new1 + M:
    return H_ans
  if H_ans * N <= H_new + M:
    step = step // 2
    return binary(H_ans + step, step)
  if H_ans * N > H_new + M:
    step = step // 2
    return binary(H_ans - step, step)

N = int(input())
H = list(map(int, input().split()))
M = int(input())
print(binary(min(H), min(H)))
