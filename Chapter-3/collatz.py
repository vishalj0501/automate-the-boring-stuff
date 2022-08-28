def collatz(number):
    if number%2==0:
        a=number//2
        print(a)
        return a

    elif number%2==1:
        b=3*number+1
        print(b)
        return b

try:
    print("Enter a Number: ")
    n=int(input())

    while True:
        n=collatz(n)
        if n==1:
            break

except:
    print("Input: Not an Integer!")