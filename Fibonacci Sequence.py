"Function that allows to select a Fibonacci Sequence with a specific range, raised by 2."

def fibonacci_sequence(n):
    a = 0
    b = 1 
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(n):
            c = a + b
            a = b
            b = c 
            print(c) 

fibonacci_sequence(10)
