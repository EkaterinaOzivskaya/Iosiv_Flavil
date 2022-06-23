total = 0
n, k = int(input()), int(input())#n - число людей, k - шаг, с которым они убивают друг друга
m = [i for i in range(1, n + 1)]
while len(m) > 1:   
    for i in m:
        total += 1
        if total == k :
            if  m.index(i) != len(m) - 1:
                m.remove(i)
                total = 1
            else:
                m.remove(i)
                total = 0
print(*m)    
#*m- выводит выжившего человека
