QUESTION 1

[10,3, 5, 1, 2, 91, 3]

def answer(number):
  minimum = number[0]
  maximum = number[0]

  for i in number:
    if i < minimum:
      minimum = i
    if i > maximum:
      maximum = i
  return (minimum, maximum)

print(answer( [10,3, 5, 1, 2, 91, 3]))


QUESTION 2

def answer(number , arg1, arg2):
    minimum = arg1
    for a in range(arg1 + 1, arg2):
 
        if number[a] < number[minimum]:
            minimum = a 
 
    temp = number[minimum]
    number[minimum] = number[arg1]
    number[arg1] = temp
 
    if arg1 + 1 < arg2:
        answer(number, arg1 + 1, arg2)
    else:
        print(number)

number = [3, 5, 8, 4, 1, 9, -2]

answer(number, 0, len(number))
