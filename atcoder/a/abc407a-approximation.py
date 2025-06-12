a, b = map(int, input().split())
quotient = a / b
quotient_round = a // b
remainder = a % b

if remainder == 0:
	print(quotient_round)
elif quotient - quotient_round > (quotient_round + 1) - quotient:
	print(quotient_round + 1)
else:
	print(quotient_round)
