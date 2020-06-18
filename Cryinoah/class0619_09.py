student_list = ['KDH', 'PKR', 'LJS', 'JWS', 'HY', 'LSH', 'CMH', 'KDH', 'LHY', 'LSY', 'LSH', 'HJW']
teacher_list = ['JSH']

someone = 'JJJ'

if someone in student_list:
    print(f'{someone} is a student')
else:
    if someone not in teacher_list:
        print(f'Who is {someone}?')
    else:
        print(f'{someone} is a teacher')
