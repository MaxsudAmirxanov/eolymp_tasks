def min_operations(n):
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        operations += 1
    return operations

def main():
    n = int(input())
    print(min_operations(n))

if __name__ == "__main__":
    main()
