import random
import discord
def critografia(inputs):
    afabeto = ['a' , 'b' , 'c' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'V' , 'W' , 'X' , 'Y' , 'Z']
    key = ''
    comprimento = inputs
    for i in range(comprimento):
        a = random.randint(1, 2)
        if a == 1:
            key += random.choice(afabeto)
        else:
            key += str(random.randint(0, 9))
    return key

