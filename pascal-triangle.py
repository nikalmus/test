def pascal(num):
    row = []
    for n in range(num):
        row = [1 if i == 0 or i == n else row[i-1] + row[i] for i in range(n+1)]
        yield row


def draw(f, num):
   for row in f(num):
       print (' '.join(map(str, row)).center(num*2)+'\n')


num = 5

print(pascal(num))
draw(pascal,  num)