# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

def run():
    n = int(input("Enter the number, please: "));

    print(n + n * n + n*n*n);