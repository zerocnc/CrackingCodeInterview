# Useful code blocks

### Array

#### *_3 Ways to initialize an array in Python_*

#### *Method 1: Using for loop and Python range() function*

Python for loop and range() function together can be used to initialize an array with a default value.

Syntax:

```python
[value for element in range(num)]
```
Python range() function accepts a number as argument and returns a sequence of numbers which starts from 0 and ends by the specified number, incrementing by 1 each time.

Python for loop would place 0(default-value) for every element in the array between the range specified in the range() function.

Example:

```python
arr = []
arr = [ 0 for i in range(5) ]
print(arr)
```

#### *Method 2: Python NumPy module to create and initilize array*

Python NumPy module can be used to create arrays and manipulate the data in it efficiently. The numpy.empty() function creates an array of a specified size with a default value = ‘None’.

Syntax:
```python
numpy.empty(size, dtype=object)
```

Example:
```python
import nump as np
arr = np.empty(10, dtype=object)
print(arr)
```

#### *Method 3: Direct Method to initialize a Python array*

While declaring the array, we can initialize the data values using the below command:

```python
array-name = [defulat-value] * size
```

Example:
```python
arr_num = [0] * 5
print(arr_num)
 
arr_str = ['P'] * 10
print(arr_str)
```

As seen in the above example, we have created two arrays with the default values as ‘0’ and ‘P’ along with the specified size with it.

### To iterate though an array in reverse.

To iterate though an array in reverse.
```python
for i in reversed(range(length) ):
    # code here
```