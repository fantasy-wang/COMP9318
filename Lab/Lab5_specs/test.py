
import numpy as np

data = np.loadtxt('asset/data.txt', dtype = float)
print(data)



def dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


matrix = np.zeros((5, 5))
print(matrix)

for i in range(len(data)):
    for j in range(i, len(data)):
        if j == i:
            matrix[i][j] = 0
        else:
            matrix[j][i] = matrix[i][j] = dot_product(data[i], data[j])

print(matrix)

max_value = np.max(matrix)
print(max_value)

index = np.where(matrix >= max_value)
print(index)


#
# import submission as submission
#
# k = 3
# print(submission.hc(data, k))
#
#
# def compute_error(data, labels, k):
#     n, d = data.shape
#     centers = []
#     for i in range(k):
#         centers.append([0 for j in range(d)])
#
#     for i in range(n):
#         centers[labels[i]] = [x + y for x, y in zip(centers[labels[i]], data[i])]
#
#     error = 0
#     for i in range(n):
#         error += dot_product(centers[labels[i]], data[i])
#     return error
#
#
# compute_error(data, submission.hc(data, k), k)
#
