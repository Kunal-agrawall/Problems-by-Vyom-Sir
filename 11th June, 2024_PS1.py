'''
Problem Statement 1:
Write a program in python that will find the sum of all prime numbers in a given range. 
The range will be specified as command line parameters. 
The first command line parameter, N1 which is a positive integer, will contain the lower bound of the range. 
The second command line parameter N2, which is also a positive integer will the upper bound of the range. 
The program should consider all the prime numbers within the range, excluding the upper and lower bound. 
Print the output in integer format. 
Other than the integer number, no other extra information should be printed.
'''
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_and_sum(lower, upper):
    primes = [num for num in range(lower + 1, upper) if is_prime(num)]
    return primes, sum(primes)

def main():
    try:
        lower = int(input("Enter the lower bound of the range: "))
        upper = int(input("Enter the upper bound of the range: "))
        if lower < 0 or upper < 0 or lower >= upper:
            print("Both bounds should be positive integers and lower bound should be less than upper bound.")
            return
    except ValueError:
        print("Please enter valid integers for the range.")
        return

    primes, primes_sum = find_primes_and_sum(lower, upper)
    print(f"Prime numbers in the range ({lower}, {upper}): {primes}")
    print(f"Sum of prime numbers in the range ({lower}, {upper}): {primes_sum}")

if __name__ == "__main__":
    main()
