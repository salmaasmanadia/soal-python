# mencari kpk dan fpb dengan library python : numpy
# import numpy as np

# a = input('Masukkan Angka pertama: ')
# b = input('Masukkan Angka kedua: ')

# num1 = int(a)
# num2 = int(b)

# kpk = np.lcm(num1, num2)
# fpb = np.gcd(num1, num2)

# print('KPK: ' + str(kpk))
# print('FPB: ' + str(fpb))

# MANUAL
# langkah 1 : input dua bilangan a dan b
a = int(input('Masukkan Bilangan Pertama: '))
b = int(input('Masukkan Bilangan Kedua: '))

# langkah 2 : buat 2 list kosong
list1=[]
list2=[]

# lagkah 3 : Masukkan nilai dari 1 sampai dengan a atau b pada list1
for i in range(1, a+1):
    list1.append(i)
# print(list1)
# langkah 4 : Masukkan nilai  pada list1 yang memenuhi syarat bahwa dibagi habis bilangan a dan b kedalam list2
for x in list1:
    if a%x==0 and b%x==0:
        list2.append(x)
# print(list2)
if a==0 or b==0:
    print('\nKPK dan FPB = 0')
else:
    # langkah 5 : FPB adalah elemen terbesar pada list2
    print(f'\nFPB dari {a} dan {b} = {list2[len(list2)-1]}')
    # langkah 6 : KPK adalah hasil kali dua elemen a dan b di bagi dengan FPB dari a dan b
    print('KPK dari {} dan {} = {:.0f}'.format(a,b, a*b/list2[len(list2)-1]))   

