import random
numbers="0123456789"
upperletter="ABCDEFGHIKLMNOQRSTUVW"
lowerletter = "abcdefghiklmnoqrstuvw"
specialcharacter="!§$%&/()=?`_:;,.-#+*'"
list = numbers+upperletter+lowerletter+specialcharacter
length=12
pswd=""

#loop
for i in range(1, length):
    temp = list[random.randint(0, len(list)-1)]
    pswd += temp
print(pswd)

