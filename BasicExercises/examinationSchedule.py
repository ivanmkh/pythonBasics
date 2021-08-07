# Write a Python program to display the examination schedule. (extract the date from exam_st_date).

def run():
    exam_st_date = input('Enter the exam_st_date: ');

    examStDate = exam_st_date.replace(', ', '/');

    print('Examination date is ', examStDate);