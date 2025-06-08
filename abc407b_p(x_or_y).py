x, y = map(int, input().split())

c = 0
for i in range(1, 7):
	for j in range(1, 7):
		if i + j >= x or abs(i - j) >= y:
			c += 1
print(c / 36)
