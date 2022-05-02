primes = []
for target_num in range(100, 222):
  is_prime = True
  for i in range(2, target_num):
    if target_num % i == 0:
      is_prime = False
  if is_prime:
    primes.append(target_num)

print(primes)


def is_prime(num):
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
            return False
    return True


def prime_num_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
            num += 1
        else:
            num += 1
