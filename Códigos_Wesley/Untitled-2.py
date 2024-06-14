def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    print(len(prime_numbers))     
    return (len(prime_numbers), prime_numbers)

start_num = int(input("Digite o número inicial do intervalo: "))
end_num = int(input('Digite o número final do intervalo: '))



print("Números primos no intervalo de", start_num, "a", end_num, ":", find_primes(start_num,end_num))
