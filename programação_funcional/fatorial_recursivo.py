def fatorial(n):

    return n * fatorial(n-1) if n - 1 > 0 else 1


if __name__ == '__main__':
    print(fatorial(0))
