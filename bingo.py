import random
# Made by @sumitcoders

def check(l1,l2):
    for i in range(len(l1)):
        n = l1[i]
        if n in l2:
            pass
        else:
            return False
    return True


number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
for i in range (5):
    x = random.choice(number)
    number.remove(x)
    r1.append(x)
for i in range (5):
    x = random.choice(number)
    number.remove(x)
    r2.append(x)
for i in range (5):
    x = random.choice(number)
    number.remove(x)
    r3.append(x)
for i in range (5):
    x = random.choice(number)
    number.remove(x)
    r4.append(x)
for i in range (5):
    x = random.choice(number)
    number.remove(x)
    r5.append(x)

print('____________________________________________________________')
c1 = [r1[0],r2[0],r3[0],r4[0],r5[0]]#v row 1
c2 = [r1[0],r2[1],r3[2],r4[3],r5[4]]#diagonal \
c3 = [r1[4],r2[3],r3[2],r4[1],r5[0]]#diagonal /
c4 = [r1[1],r2[1],r3[1],r4[1],r5[1]]#v row 2
c5 = [r1[2],r2[2],r3[2],r4[2],r5[2]]#v row 3
c6 = [r1[3],r2[3],r3[3],r4[3],r5[3]]#v row 4
c7 = [r1[4],r2[4],r3[4],r4[4],r5[4]]#v row 5
c8 = [r1[0],r1[1],r1[2],r1[3],r1[4]]#h row 1
c9 = [r2[0],r2[1],r2[2],r2[3],r2[4]]#h row 2
c10 = [r3[0],r3[1],r3[2],r3[3],r3[4]]#h row 3
c11 = [r4[0],r4[1],r4[2],r4[3],r4[4]]#h row 4
c12 = [r5[0],r5[1],r5[2],r5[3],r5[4]]#h row 5
left = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
marked = []
bingo = 0
c = True
while True:
    if c == True:
        cguess = random.choice(left)
        left.remove(cguess)
        marked.append(cguess)
        print(f'Here is the number by computer: ',cguess)
    uguess = (input('Enter your number: '))
    if uguess.lower() == 'bingo':
        if len(marked) >= 15:
            print('you won!!')
            exit()
        else:
            print("Don't cheat! continue and try after next number.")
    elif int(uguess) in left:
        c = True
        marked.append(int(uguess))
        left.remove(int(uguess))
    else:
        print('number is already selected or is out of index')
        c = False
    if len(marked) >= 15:
        bingo = 0
        if check(c1,marked) == True:
            bingo = bingo+1
        if check(c2,marked) == True:
            bingo = bingo+1
        if check(c3,marked) == True:
            bingo = bingo+1
        if check(c4,marked) == True:
            bingo = bingo+1
        if check(c5,marked) == True:
            bingo = bingo+1
        if check(c6,marked) == True:
            bingo = bingo+1
        if check(c7,marked) == True:
            bingo = bingo+1
        if check(c8,marked) == True:
            bingo = bingo+1
        if check(c9,marked) == True:
            bingo = bingo+1
        if check(c10,marked) == True:
            bingo = bingo+1
        if check(c11,marked) == True:
            bingo = bingo+1
        if check(c12,marked) == True:
            bingo = bingo+1
    if bingo >=5:
        print('machine won!')
        print(r1)
        print(r2)
        print(r3)
        print(r4)
        print(r5)
        exit()
        
        
    


