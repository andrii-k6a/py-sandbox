from micrograd.nn import MLP
from micrograd.viewer import draw_dot

x = [2.0, 3.0, -1.0]
mlp = MLP(3, [4, 4, 1])

xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0]
]
ys = [1.0, -1.0, -1.0, 1.0]
ypred = [mlp(x) for x in xs]
print(ypred)

loss = sum([(yout - ygt) ** 2 for ygt, yout in zip(ys, ypred)])
print(loss)

loss.backward()

print(mlp.layers[0].neurons[0].w[0].grad)

dot = draw_dot(loss)
dot.render('loss', format='png')
