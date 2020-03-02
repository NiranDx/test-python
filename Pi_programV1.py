import math
num_steps = 1000000

step =1.0/num_steps
exam_sum = 0
for x in range(1,num_steps):
    temp = (x+0.5)*step
    exam_sum = exam_sum+4.0/(1.0+temp*temp)

pi =step *exam_sum
print(pi)