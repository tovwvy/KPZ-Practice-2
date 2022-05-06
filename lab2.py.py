def prime_num_generator():
    for n in range(2, 666): 
        for x in range(2, n):  
            if n % x == 0:  
                break
        else:  
            yield n
        n += 1


a = prime_num_generator()

  while True:
    print(next(a))
