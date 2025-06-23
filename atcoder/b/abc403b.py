import sys

t = input()
u = input()

for i in range(len(t)):
	if len(t) - i < len(u):
		break

	matched = True
	for j in range(len(u)):
		if t[i + j] == '?':
			continue
		elif t[i + j] != u[j]:
			matched = False
	if matched:
		print('Yes')
		sys.exit()

print('No')
