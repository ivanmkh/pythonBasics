# Write a Python program to display the first and last colors from the following list

def run():
    colors = input('Enter the color list: ');
    colorList = list(map(str, colors.split(',')));
    print(colorList[0], colorList[-1]);
