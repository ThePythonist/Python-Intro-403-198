primes = []

for i in range(1, 100):
    for j in range(2, i):
        if i % j == 0:  # shomarandeyi peyda beshe
            break
    else:
        primes.append(i)  # zamani ejra mishe ke for break nashe

print(primes)
