from ai.micrograd.nn import MLP
from ai.micrograd.viewer import draw_dot

inp = [2.0, 3.0, -1.0]
mlp = MLP(3, [4, 4, 1])
print(mlp)

res = mlp(inp)

print(res)

dot = draw_dot(res)
dot.render('mlp', format='png')
