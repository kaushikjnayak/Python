from collections import namedtuple
N, Students = int(input()) , namedtuple( 'student', input().split())
print ( '{:.2f}'.format(sum ( [ int(student.MARKS) for student in  [ Students(*input().split())  for i in range(N) ] ]) / N  ))

