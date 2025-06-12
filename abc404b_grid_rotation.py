n = int(input())
s = []
for i in range(n):
	s.append(input())
t = []
for i in range(n):
	t.append(input())

diff_list = [0, 0, 0, 0]
for i in range(n):
	for j in range(n):
		if s[i][j] != t[i][j]:
			diff_list[0] = diff_list[0] + 1	
		if s[(n - 1) - j][i] != t[i][j]:
			diff_list[1] = diff_list[1] + 1
		if s[(n - 1) - i][(n - 1) - j] != t[i][j]:
			diff_list[2] = diff_list[2] + 1
		if s[j][(n - 1) - i] != t[i][j]:
			diff_list[3] = diff_list[3] + 1

ans = n * n
for rotate in range(len(diff_list)):
	ans = min(ans, diff_list[rotate] + rotate)

print(ans)
