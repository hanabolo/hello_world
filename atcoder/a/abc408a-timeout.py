import sys

def main():
	n, s = sys.stdin.readline().split(' ')
	t = sys.stdin.readline().split(' ')

	last = 0
	for i in range(int(n)):
		if int(t[i]) - last > int(s):
			print('No')
			sys.exit()
		last = int(t[i])

	print('Yes')

if __name__ == '__main__':
	main()
