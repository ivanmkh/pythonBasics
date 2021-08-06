# Write a Python program which accepts a sequence
# of comma-separated numbers from user and generate
# a list and a tuple with those numbers.

def run():
    sequence = input("Enter the sequence of comma-separated numbers: ");

    lst = list(map(int, sequence.split(",")))
    tpl = tuple(map(int, sequence.split(",")))

    print(lst);
    print(tpl);