# Write a Python program to accept a filename
# from the user and print the extension of that.

def run():
    filename = input('Enter the filename: ');

    extension = filename.split('.')[1];

    print('Extension is ', extension);