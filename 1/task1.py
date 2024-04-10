import numpy as np

x = np.array([[2,-1],[-3,4]])
y = np.array([[1,2],[3,4]])

result1 = x + y
result2 = x - y
result3 = 3 * x
result4 = np.dot(x,y)

print("x=")
print(x)
print("y=")
print(y)
print("x+y=")
print(result1)
print("x-y=")
print(result2)
print("3x=")
print(result3)
print("xy=")
print(result4)
