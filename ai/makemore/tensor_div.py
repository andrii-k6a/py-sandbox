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

# broadcasting semantics:
# https://pytorch.org/docs/stable/notes/broadcasting.html
# https://numpy.org/doc/stable/user/basics.broadcasting.html
res = tensor / tensor_sum
print(res)
# the smaller array is “broadcast” across the larger array so that they have compatible shapes
# tensor([[2/6=0.3333, 4/6=0.6667],
#         [8/24=0.3333, 16/24=0.6667]])
