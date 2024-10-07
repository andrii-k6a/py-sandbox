import torch


def two_dim_tensor():
    # Create a 2D tensor
    tensor = torch.tensor([
        [1, 2],
        [3, 4]
    ])

    # Dimension (dim) represents the level of nestedness within a tensor
    # Negative dimension indices count backward from the last dimension:
    # dim=-1 refers to the last dimension (which is 1 in the case of a 2D tensor, i.e., columns).
    # dim=-2 refers to the second-to-last dimension (which is 0 in a 2D tensor, i.e., rows).

    # Sum along dimension 0 (column-wise)
    sum_dim0 = torch.sum(tensor, dim=0)  # columns are summed: (1+3, 2+4) -> tensor([4, 6])
    print(sum_dim0)

    # Sum along dimension 1 (row-wise)
    sum_dim1 = torch.sum(tensor, dim=1)  # rows are summed: (1+2, 3+4) -> tensor([3, 7])
    print(sum_dim1)

    # Sum along dimension 1, keeping dimensions
    sum_kd = torch.sum(tensor, dim=1, keepdim=True)  # row sums are preserved with dimension size 1 -> tensor([[3],[7]])
    print(sum_kd)

    # Sum over all elements in the tensor
    sum_all = torch.sum(tensor)  # all elements are summed to produce a scalar -> tensor(10)
    print(sum_all)


def three_dim_tensor():
    # Create a 3D tensor
    # Shape of the tensor: (3, 4, 5)
    # Represents 3 matrices, each with 4 rows and 5 columns.
    tensor = torch.tensor([
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40]
        ],
        [
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60]
        ]
    ])

    sum_dim0 = torch.sum(tensor, dim=0)
    print('torch.sum(tensor, dim=0)\n', sum_dim0, '\n')
    # [[1+21+41=63, 2+22+42=66,...],
    #  [6+26+46=78,...],
    #  ...]]
    # shape: (4, 5)
    # tensor([[63, 66, 69, 72, 75],
    #         [78, 81, 84, 87, 90],
    #         [93, 96, 99, 102, 105],
    #         [108, 111, 114, 117, 120]])

    sum_dim1 = torch.sum(tensor, dim=1)
    print('torch.sum(tensor, dim=1)\n', sum_dim1, '\n')
    # [[1+6+11+16=34, 2+7+12+17=38,...],
    #  [21+26+31+36=114,...],
    #  ...]]
    # shape: (3, 5)
    # tensor([[34, 38, 42, 46, 50],
    #         [114, 118, 122, 126, 130],
    #         [194, 198, 202, 206, 210]])

    sum_dim2 = torch.sum(tensor, dim=2)
    print('torch.sum(tensor, dim=2)\n', sum_dim2, '\n')
    # [[1+2+3+4+5=15, 6+7+8+9+10=40,...],
    #  [21+22+23+24+25=115,...],
    #  ...]]
    # shape: (3, 4)
    # tensor([[15, 40, 65, 90],
    #         [115, 140, 165, 190],
    #         [215, 240, 265, 290]])

    sum_dim0_kd = torch.sum(tensor, dim=0, keepdim=True)
    print('torch.sum(tensor, dim=0, keepdim=True\n', sum_dim0_kd, '\n')
    # tensor([[[63, 66, 69, 72, 75],
    #          [78, 81, 84, 87, 90],
    #          [93, 96, 99, 102, 105],
    #          [108, 111, 114, 117, 120]]])

    sum_dim1_kd = torch.sum(tensor, dim=1, keepdim=True)
    print('torch.sum(tensor, dim=1, keepdim=True)\n', sum_dim1_kd, '\n')
    # tensor([[[34, 38, 42, 46, 50]],
    #         [[114, 118, 122, 126, 130]],
    #         [[194, 198, 202, 206, 210]]])

    sum_dim2_kd = torch.sum(tensor, dim=2, keepdim=True)
    print('torch.sum(tensor, dim=2, keepdim=True)\n', sum_dim2_kd, '\n')
    # tensor([[[15],
    #          [40],
    #          [65],
    #          [90]],
    #
    #         [[115],
    #          [140],
    #          [165],
    #          [190]],
    #
    #         [[215],
    #          [240],
    #          [265],
    #          [290]]])
