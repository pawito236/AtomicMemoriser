import random

col = [1,1,1,1,1,1,1,
        2,2,2,2,2,2,
        3,3,3,3,3,
        4,4,4,4,4,
        5,5,5,5,5,
        6,6,6,6,6,
        7,7,7,7,7,
        8,8,8,8,8,8]

row = [1,2,3,4,5,6,7,
        2,3,4,5,6,7,
        2,3,4,5,6,
        2,3,4,5,6,
        2,3,4,5,6,
        2,3,4,5,6,
        2,3,4,5,6,
        1,2,3,4,5,6]

atom = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr',
        'Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra',
        'B', 'Al', 'Ga', 'In', 'Tl',
        'C', 'Si', 'Ge', 'Sn', 'Pb',
        'N', 'P', 'As', 'Sb', 'Bi',
        'O', 'S', 'Se', 'Te', 'Po',
        'F', 'Cl', 'Br', 'I', 'At',
        'He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']

num = random.randint(0,43)
# print(num, col[num], row[num], atom[num])
def atomic_1(num) :
    print('ธาตุนี้คือไรน้าาาาา หมู่ที่ : ' + str(col[num]) + '  คาบที่ : '+ str(row[num]))
    ans = str(input('ผมมั่นใจว่าเป็น!!! ->>> '))
    if (ans == str(atom[num])) :
        print('เก่งมากกกกก')
    else :
        print('พยายามใหม่นะ คำตอบคือ : ' + atom[num])

def atomic_2(num) :
    print('ธาตุนี้คือ', atom[num])
    ans1, ans2 = input('อยู่ในหมู่และก็คาบอะไรเอ่ย? ').split()
    if (int(ans1) == int(col[num]) and int(ans2) == int(row[num])) :
        print('เก่งมากกกกก')
    else :
        print('พยายามใหม่นะ คำตอบคือ :  หมู่ที่ : ' + str(col[num]) + '  คาบที่ : '+ str(row[num]))

def atomic_3(num) :
    print('ธาตุนี้คือไรน้าาาาา หมู่ที่ : ' + str(col[num]) + '  คาบที่ : '+ str(row[num]))

def atomic_4(num) :
    print('ธาตุนี้คือ', atom[num])

atomic_1(num)
