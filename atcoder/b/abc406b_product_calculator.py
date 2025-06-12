n, k = map(int, input().split())
a = list(map(int, input().split()))

result = 1
for i in range(n):
	result = result * a[i]
	if result // (10 ** k) != 0:
		result = 1

print(result)
