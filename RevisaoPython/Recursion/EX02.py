def fatorial(n):
    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n-1)
        print(f"Fatorial de {n} = {fat}")
        return fat

print(fatorial(4))