import turtle

# Koch curve
# variables : F
# constants : + −
# start : F
# rules : (F → F+F−F−F+F)
# Here, F means "draw forward", + means "turn left 90°", and − means "turn right 90°" (see turtle graphics).

F = 'F+F−F−F+F'
teta = 90
del = 20

nl = len(F)
for i in range(nl):
 if F[i] == 'F':
   turtle.forward(del)
 elseif F[i] == '+'
   turtle.right(teta)
 elseif F[i] == '-'
   turtle.left(teta)
 meanloop()
 
 
