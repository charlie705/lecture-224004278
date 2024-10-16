def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        try:
            user_input = int(input("Enter a positive integer: "))
            if user_input <= 0:
                raise ValueError("The number must be a positive integer.")
            break  # Valid input, exit the loop
        except ValueError as e:
            print(e)

    primes = [num for num in range(2, user_input + 1) if is_prime(num)]
    
    print(f"Prime numbers less than or equal to {user_input}:")
    print(primes)

if __name__==  "__main__":
    main()
    