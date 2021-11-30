def sieve_of_eratosthenes_flowchart(n):

	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if prime[p] == True:
			for i in range(p * p, n + 1, p):
				prime[i] = False
		p += 1

	for p in range(2, n + 1):
		if prime[p]:
			print(p)

if __name__ == '__main__':
	n = int(input("Give me a number: "))
	print (f"Prime numbers in the range up to {n} are: ")
	sieve_of_eratosthenes_flowchart(n)