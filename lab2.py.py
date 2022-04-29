primes = []
for target_num in range(100, 222):
  is_prime = True
  for i in range(2, target_num):
    if target_num % i == 0:
      is_prime = False
  if is_prime:
    primes.append(target_num)

print(primes)