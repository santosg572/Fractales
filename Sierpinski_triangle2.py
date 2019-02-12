import turtle

# https://en.wikipedia.org/wiki/L-system


'''
The Sierpinski triangle drawn using an L-system.

variables : F G
constants : + −
start : F−G−G
rules : (F → F−G+F+G−F), (G → GG)
angle : 120°
Here, F and G both mean "draw forward", + means "turn left by angle", and − means "turn right by angle".

'''

F = 'F-G-G'
R1 = 'F-G+F+G-F'
R2 = 'GG'
teta = 120
inc = 20

for j in range(3):
 lf = len(F)
 FN = ''

 for i in range(lf):
    if F[i] == 'F':
       FN = FN + R1
    if F[i] == 'G':
       FN = FN + R2
    if F[i] == '+':
       FN = FN + F[i]
    if F[i] == '-':
       FN = FN + F[i]

 F = FN
 print(F)

 lf = len(F)
 FN = ''

 for i in range(lf):
    if F[i] == 'F':
       FN = FN + R1
    if F[i] == 'G':
       FN = FN + R2
    if F[i] == '+':
       FN = FN + F[i]
    if F[i] == '-':
       FN = FN + F[i]

 F = FN      
 print(F)

# graficacion

FR = F

nl = len(FR)
print(nl)

turtle.up()
turtle.goto(-200,-200)
turtle.down()

for i in range(nl):
 if FR[i] in {'F', 'G'}:
   turtle.forward(inc)
 elif FR[i] == '+':
   turtle.right(teta)
 elif FR[i] == '-':
   turtle.left(teta)

turtle.mainloop()
 
 
