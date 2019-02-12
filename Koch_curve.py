import turtle

# Koch curve
# variables : F
# constants : + −
# start : F
# rules : (F → F+F−F−F+F)
# Here, F means "draw forward", + means "turn left 90°", and − means "turn right 90°" (see turtle graphics).

F = 'F+F-F-F+F'
teta = 90
del1 = 20



# dos iteracion

FN = F
nfl = len(FN)
FS = ''

for i in range(nfl):
   if FN[i] == 'F':
      FS = FS + F
   else:
      FS = FS + FN[i]

# tres iteraciones

FN = FS
nfl = len(FN)
FS = ''

for i in range(nfl):
   if FN[i] == 'F':
      FS = FS + F
   else:
      FS = FS + FN[i]



F = FS

nl = len(F)
print(F)

turtle.up()
turtle.goto(-300, -100)
turtle.down()

for i in range(nl):
   if F[i] == 'F':
      turtle.forward(del1)
   elif F[i] == '-':
      turtle.right(teta)
   elif F[i] == '+':
      turtle.left(teta)

turtle.mainloop()
 
 
