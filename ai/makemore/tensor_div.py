import torch

tensor = torch.tensor([
    [2, 4],
    [8, 16]
])
print(tensor)

tensor_sum = tensor.sum(dim=1, keepdim=True)
print(tensor_sum)
# tensor([[ 6],
#         [24]])

res = tensor / tensor_sum
print(res)
# tensor([[2/6=0.3333, 4/6=0.6667],
#         [8/24=0.3333, 16/24=0.6667]])
