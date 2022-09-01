# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

#prompts user for input
score = input('Enter a Score: ')
try:
    f_score = float(score)
    if f_score >= 0.9 and f_score <= 1.0:
        print('A')
    elif f_score >= 0.8 and f_score < .9:
        print('B')
    elif f_score >= 0.7 and f_score < .8:
        print('C')
    elif f_score >= .6 and f_score < .7:
        print('D')
    elif f_score < 0.6:
        print('F')
    else:
        print('Bad Score')
except:
    print('enter a number')
