
import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

updated_temp = temperature + 2

print("Updated temperature readings:", updated_temp)

temp_fahrenheit = (9 / 5) * updated_temp + 32

print("Temperature in Fahrenheit:", temp_fahrenheit)

high_temp = updated_temp[updated_temp > 32]

print("Temperatures above 32°C:", high_temp)

total_high = np.sum(updated_temp > 32)

print("Total readings above 32°C:", total_high)

print("NumPy vectorization performs calculations on the complete array together.")
print("Boolean indexing helps in extracting values that satisfy a given condition.")
print("These approaches make the program shorter and usually more efficient than loops.")


steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("Sum of all steps:", steps.sum())

print("Average number of steps:", steps.mean())

print("Highest step count:", steps.max())
print("Lowest step count:", steps.min())

print("Steps completed on each day:", steps.sum(axis=0))

print("Steps completed by each user:", steps.sum(axis=1))

max_position = steps.argmax()
user_day = np.unravel_index(max_position, steps.shape)

print("Highest value:", steps[user_day])
print("Position of maximum value:", user_day)
print("The maximum value belongs to user 4 on day 3.")


original = np.array([1, 2, 3, 4, 5, 6])

print("Starting array:", original)

part = original[1:4]

print("Selected portion:", part)

part[0] = 999

print("Array after changing the slice:", original)
print("Modified slice:", part)

copied_part = original[1:4].copy()
copied_part[0] = 500

print("Original array after copy modification:", original)
print("Separate copied array:", copied_part)

matrix = np.arange(1, 13).reshape(3, 4)

print("Generated 3 x 4 matrix:")
print(matrix)

print("Top row:", matrix[0])
print("Bottom row:", matrix[-1])
print("Second column:", matrix[:, 1])

print("Selected rows and columns:")
print(matrix[0:2, 1:3])

flattened = matrix.flatten()
raveled = matrix.ravel()

print("Array created with flatten:", flattened)
print("Array created with ravel:", raveled)

raveled[0] = 100

print("Ravel after changing first element:", raveled)
print("Matrix after changing ravel:")
print(matrix)

flattened[1] = 200

print("Flattened array after modification:", flattened)
print("Matrix after changing flattened array:")
print(matrix)

print("Matrix shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)
print("Number of elements:", matrix.size)
print("Type of data:", matrix.dtype)


X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

print("Dimensions of X:", X.ndim)
print("Size of X:", X.shape)

XT = X.T

print("Transpose of X:")
print(XT)

print("After transposing, the rows of X become its columns.")

XTX = XT @ X

print("Result of X transpose multiplied by X:")
print(XTX)

XTX_inv = np.linalg.inv(XTX)

print("Inverse matrix:")
print(XTX_inv)

beta = XTX_inv @ XT @ y

print("Calculated OLS values:")
print(beta)

print("Coefficient for sleep:", beta[0])
print("Coefficient for activity:", beta[1])
print("Coefficient for stress:", beta[2])

print("These values show how the predicted assistance score changes")
print("when one feature changes and the remaining features stay fixed.")

new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("Input values for new user:", new_user)
print("Estimated assistance score:", predicted_score)