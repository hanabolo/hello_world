import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

s = set(range(1, m + 1))

if s - set(a):
	print(0)
	sys.exit()

for i in range(n):
	a = a[:-1]
	if s - set(a):
		print(i + 1)
		sys.exit()

print(n)
