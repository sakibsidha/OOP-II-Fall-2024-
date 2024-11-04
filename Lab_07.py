import numpy as np
num = np.array([10, 20, 30])
print(num)
print(type(num))

# 1D
arr1 = np.array([2, 4, 5, 6])
print(arr1)
# 2D
arr2 = np.array([[2, 4, 5, 6], [2, 4, 5, 6]])
print(arr2)

# 3D
arr3 = np.array([[[2, 4, 5, 6], [2, 4, 5, 6]], [[2, 4, 5, 6], [2, 4, 5, 6]]])
print(arr3)

# Comprehension
out = np.array([[x for x in range(2, 21, 2)], [x for x in range(1, 21, 2)]])
print(out)

# array attributes
ary = np.array([[1, 2, 3], [4, 5, 6]])
print(ary.dtype)
print(ary.ndim)
print(ary.shape)
print(ary.itemsize)

# array operations
print(ary > 5)

# numpy methods
grades = np.array([[87, 96, 78], [100, 87, 98], [94, 77, 98], [100, 81, 82]])
print(grades)
print(grades.max())
print(grades.min())
print(grades.sum())
print(grades.std())
print(grades.mean())
print(grades.var())
print(grades.mean(axis = 0))
print(grades.mean(axis = 1))

# shallow copies
num1 = np.arange(1, 6)
print(num1)
num2 = num1.view()
print(num2)
print(id(num1), id(num2))
num2[1] *= 5
print(num2)
print(num2)

# deep copies
num1 = np.arange(1, 6)
print(num1)
num2 = num1.copy()
print(num2)
num2[2] *= 5
print(num2)
print(num1)

# lab task
# 1
score = np.array([85, 90, 78, 92, 88])
score = score.astype('f')
print(score)

# 2
a_score = score.copy()
print(a_score + 5)

# 3
print(score.shape)
print(score.ndim)
print(score.size)
print(score.itemsize)
print(score.dtype)
score.sort()
print(score)

# 4
x = np.where(score > 80)
print(x)

# 5
print(score.max())
print(score.min())
print(score.std())
print(score.var())
print(score.sum())
print(score.mean())
print(score.mean(axis=0))

# 6
print(score[::2])
print(score[-3:-1])
print(score[1:4])










