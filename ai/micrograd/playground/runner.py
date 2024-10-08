from ai.micrograd.engine import Value
from ai.micrograd.viewer import draw_dot

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')

d = a * b  # -6.0
d.label = 'd'

e = d + c  # 4.0
e.label = 'e'

f = Value(-2.0, label='f')

G = e * f  # -8.0; G = (a*b + c) * f = a*b*f + c*f
G.label = 'G'

G.backward()

print(G)
print(G._prev)
print(G._op)

dot = draw_dot(G)
dot.render('graph', format='png')  # Save the graph as a PNG file
