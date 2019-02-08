import turtle

# https://en.wikipedia.org/wiki/L-system


'''
variables : F
constants : + -
start : F
rules : (F -> F+F-F-F+F)
Here, F means "draw forward", + means "turn left 90 grados", 
  and - means " turn right 90 grados" (see turtle graphics).
'''

R = 'F+F-F-F+F'
teta = 90
inc = 20

FR = R

#2a Iteracion

nl = len(FR)
S = ''
for i in range(nl):
 if FR[i] == 'F':
  S = S + R
 else:
  S = S+FR[i]

FR = S

#3 iteracion

nl = len(FR)
S = ''
for i in range(nl):
 if FR[i] == 'F':
  S = S + R
 else:
  S = S+FR[i]

FR = S

# graficacion

nl = len(FR)
print(nl)

for i in range(nl):
 if FR[i] == 'F':
   turtle.forward(inc)
 elif FR[i] == '-':
   turtle.right(teta)
 elif FR[i] == '+':
   turtle.left(teta)


turtle.mainloop()
 
 
