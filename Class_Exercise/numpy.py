import numpy as np

score = np.array([85, 90, 78, 92, 88])

# 1
score_float = score.astype(float)
print("Score as float:", score_float)


# 2
a_score = score.copy()
a_score += 5
print("a_score:", a_score)
print("Original score:", score)


# 3
print("Shape:", score.shape)
print("Number of dimensions (ndim):", score.ndim)
print("Size:", score.size)
print("Item size (in bytes):", score.itemsize)
print("Data type:", score.dtype)
print("Sorted score:", np.sort(score))


# 4
indices = np.where(score > 80)
print("Indices of scores greater than 80:", indices[0])


# 5
print("Minimum score:", score.min())
print("Maximum score:", score.max())
print("Standard deviation:", score.std())
print("Variance:", score.var())
print("Sum of scores:", score.sum())
print("Mean score:", score.mean())


# 6 
print("score[:2]:", score[:2])
print("score[3:]:", score[3:])
print("score[1:4]:", score[1:4])
