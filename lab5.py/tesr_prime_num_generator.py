def prime_num_generator():
    for n in range(2,666):  
        for x in range(2, n): 
            if n % x == 0: 
                break
        else:  
            yield n
        n += 1


a = prime_num_generator()
b = prime_num_generator()
i = 0;
needed_num = 0;
while(i <= 101):
    needed_num = next(b)
    print(needed_num)
    i = i + 1




@pytest.mark.parametrize("expected_result", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
def test_prime_num_generator(expected_result):
    assert next(a) == expected_result

@pytest.mark.parametrize("expected_result", [557])
def test_prime_num_generator_2(expected_result):
    assert needed_num == expected_result
