from ai.micrograd.nn import MLP
from ai.micrograd.viewer import draw_dot

mlp = MLP(3, [4, 4, 1])

x = [2.0, 3.0, -1.0]
y = mlp(x)

xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0]
]
ys = [1.0, -1.0, -1.0, 1.0]
ypred = [mlp(x) for x in xs]
print('Predictions', ypred)

loss = sum([(yout - ygt) ** 2 for ygt, yout in zip(ys, ypred)])
print('Loss', loss)

loss.backward()

print('Grad value example', mlp.layers[0].neurons[0].w[0].grad)

draw_dot(loss).render('loss', format='png')

mlp_parameters = mlp.parameters()
print(f'All {len(mlp_parameters)} NN parameters (weights and biases)', mlp_parameters)
