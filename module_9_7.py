def is_prime(func):
    def wrapper(a,b,c):
        summa = func(a,b,c)
        # print (summa)
        count = 0
        for i in range(1, summa +1):
            if summa % 1 == 0:
                count += 1
        if count == 2:
            print("Простое")
        else:
            print("Составное")
        return summa
    return wrapper

@is_prime
def sum_three(a,b,c):
    sum = int(a+b+c)
    return sum

result = sum_three(1, 1, 7)
print(result)
