def pascal(number):
    rows = []
    for n in range(number):
        rows.append([])
        for i in range(n+1):
            if i == 0 or i == n:
                rows[n].append(1)
            else:
                rows[n].append(rows[n-1][i-1] + rows[n-1][i])
    return rows


def draw(f, number):
   for row in f(number):
       print (' '.join(map(str, row)).center(number*2)+'\n')


num = 5

print(pascal(num))
draw(pascal,  num)
