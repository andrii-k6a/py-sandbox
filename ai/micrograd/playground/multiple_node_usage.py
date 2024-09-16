from ai.micrograd.engine import Value
from ai.micrograd.viewer import draw_dot

# (a * b) * (a + b)
a = Value(-2.0, label='a')
b = Value(3.0, label='b')
d = a * b    ; d.label = 'd'
e = a + b    ; e.label = 'e'
f = d * e    ; f.label = 'f'

f.backward()

dot = draw_dot(f)
dot.render('multiple-usage-graph', format='png') # Save the graph as a PNG file
