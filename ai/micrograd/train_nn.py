from ai.micrograd.nn import MLP

mlp = MLP(3, [4, 4, 1])

xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0]
]
ys = [1.0, -1.0, -1.0, 1.0]

# gradient decent
for k in range(100):
    # forward pass
    ypred = [mlp(x) for x in xs]
    loss = sum([(yout - ygt) ** 2 for ygt, yout in zip(ys, ypred)])

    # zero grad and backward pass
    mlp.zero_grad()
    loss.backward()

    # step size
    for p in mlp.parameters():
        p.data += -0.1 * p.grad

    print(f"{k} - Loss: {loss.data} - Predictions: {ypred}")

print(ys)
print(ypred)
print(f'Final {len(mlp.parameters())} NN parameters (weights and biases)', mlp.parameters())
