# define a function to find a average marks
def find_average_marks(marks):
    total_subjects = len(marks)  # count the total items in a list
    total_marks = sum(marks)  # compute the total marks
    average_of_marks = total_marks / total_subjects # put the formula to find avaerage of marks
    return average_of_marks
# def the function to compute the grade of marks based on average marks
def compute_grade(average_of_marks):  
    if average_of_marks >= 80:
        grade = 'A'
    elif average_of_marks >= 60:
        grade = 'B'
    elif average_of_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade
if __name__ == '__main__':
    marks = [55, 64, 75, 80, 65]
    print(find_average_marks(marks))
    print("grade which is obtain base on average_marks is:", compute_grade(find_average_marks(marks)))