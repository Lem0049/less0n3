# for namber in range(1, 40):
#     if namber % 3 ==0 and namber % 5 ==0:
#         print('FizzBuzz', end=' ')
#     elif namber % 3 == 0:
#         print('Fizz', end=' ')
#     elif namber % 5 == 0:
#         print('Buzz', end=" ")
#     else:
#         print(namber, end=" ")


s = [s for s, k in range(1, 40) if k % 3 == 0]
print(s)
