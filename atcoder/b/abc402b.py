q = int(input())
queue = []
for i in range(q):
	query = input().split()
	if query[0] == '1':
		queue.append(query[1])
	elif query[0] == '2':
		print(queue.pop(0))
