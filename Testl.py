if __name__ == '__main__':

    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])


scores = sorted(set( map(lambda x : x[1] , students)))
second_low_score = scores[1]
sec_low_students = list(filter(lambda x: x[1] == second_low_score, students))

for student, marks in sorted(sec_low_students):
    print(student)

