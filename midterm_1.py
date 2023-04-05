#1

def  triangle(size,symbol = '#' ):
     ls = [] 
     for i in range(1,size + 1):
        ls.append([[symbol] * i])
        print(ls)
print(triangle(3,'&'))


#2

def gcd(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if((a % i == 0) and (b % i == 0)):
            gcd = i
             
    return gcd
print('Their Greates common divisor is:', gcd(int(input('Enter the first number:')),int(input('Enter the second number:'))))


#3

count = 0
def fib(n):
    global count
    count += 1
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(22))
print(count)


#4

def prime_factors(n):
    ls = []
    for i in range(2, n + 1):
        if n % i == 0:
            count = 0
            for x in range(1, i):
                if i % x == 0:
                    count += 1
            if count < 2:
                ls.append(i)
    return list(set(ls))

print(prime_factors(100))


#5
ls = [4,5,2]
def jumping_frog(ls,h):
    s=True
    for i in range(len(ls)-1):
        if abs(ls[i+1]-ls[i])<=h:
            s=True
        else:
            s=False
            print('Game over')
            return

    print('Frog wins')
jumping_frog(ls,2)
