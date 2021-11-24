def prime_checker(number):
    is_prime = True
    for count in range(2,number):
        if number % count == 0:
            is_prime= False

    if(is_prime):
        print(f"{n} is a prime number")
    else:
            print(f"{n} is not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
