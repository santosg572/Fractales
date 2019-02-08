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
 
 
