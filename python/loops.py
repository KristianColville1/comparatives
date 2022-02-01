a = '23'
d = '342'
j = '2'

# above are 3 basic integer variables.

# this is a for loop

for c in d:
    print(c + a + j)


# this is a bad while loop, this will break your computer. It never ends

# while(a < d):
#     a += j
#     print(j)

# below is a while loop implemented correctly

apples = 10
oranges = 32423
tomatoes = 34

# while(apples < oranges):
#     apples += tomatoes
#     print('Picking apples all day.. when will it end..')

# I decided to build a counter for the while loop to see how many iterations it took to complete its task.

iterations = 0
while(apples < oranges):
    apples += tomatoes

    iterations += 1

print(iterations)

# It took 954 iterations to complete my while loop, abit much for an example so its commented out.