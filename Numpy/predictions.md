# Part 0 — Predict the output

## Q1
```python
a = np.arange(6); b = a[2:4]; b[:] = 0
# final value of a?
```
- **Prediction:** [0 1 0 0 4 5]
- **Actual:**
- **Why:** Because slicing creates a view in numpy so changing anything in the new array created by the slicing reflects in the original array
- **Verdict:**


## Q2
```python
# 2. Final value of a?
a = np.arange(6); b = a[[2, 3]]; b[:] = 0
```
- **Prediction:** [0 1 2 3 4 5]
- **Actual:**
- **Why:** Fancy Indexing in numpy returns a copy not a view so changing elements in the new array does not affect the original one
- **Verdict:**

## Q3
```python
# 3. Final value of a?
a = np.arange(6); a[::2][1:][0] = 99
```
- **Prediction:** 
- **Actual:**
- **Why:** Don't know
- **Verdict:**

## Q4
```python
# 4. Final value of x?
x = np.array([1, 2, 3]); y = x; y = y + 1
```
- **Prediction:**  [2, 3, 4]
- **Actual:**
- **Why:** y = x creates a view so broadcasting on array y also affects the original array x
- **Verdict:**

## Q5
```python
# 5. Final value of x?
x = np.array([1, 2, 3]); y = x; y += 1
```
- **Prediction:**  [2, 3, 4]
- **Actual:**
- **Why:** y = x creates a view so broadcasting on array y also affects the original array x
- **Verdict:**

## Q6
```python
# 6. Final value of a?
a = np.array([1, 2, 3]); a[0] = 2.9
```
- **Prediction:**  [2.9, 2, 3]
- **Actual:**
- **Why:** changing the element at an index reflects in the original array
- **Verdict:**

## Q7
```python
# 7. Final value of a?
a = np.array([1, 2, 3]); a /= 2
```
- **Prediction:**  [0.5, 1.0, 1.5]
- **Actual:**
- **Why:** The scalar is broadcasted across all elements in the array a
- **Verdict:**

## Q8
```python
# 8.
np.array([1, 2, 3], dtype=np.int8) * 100
```
- **Prediction:**  array([100, 200, 300])
- **Actual:**
- **Why:** The scalar is broadcasted across all elements in the array 
- **Verdict:**


# Q9
```python
# 9.
np.array([3], dtype=np.uint8) - np.array([5], dtype=np.uint8)
```
- **Prediction:**  array([-2])
- **Actual:**
- **Why:** element-wise operation is done on the arrays
- **Verdict:**

# Q10
```python
# 10.
len(np.arange(0.5, 0.8, 0.1))
```
- **Prediction:**  array([0.5, 0,6, 0.7, 0.8])
- **Actual:**
- **Why:** arange creates an array starting from th o.5 specified up to 0.8 with 0.1 as the step
- **Verdict:**

# Q11
```python
# 11.
np.round([0.5, 1.5, 2.5])
```
- **Prediction:**  
- **Actual:**
- **Why:** Don't know
- **Verdict:**

# Q12
```python
# 12.
(np.arange(3) - np.arange(3).reshape(3, 1)).shape
```
- **Prediction:**  (3, 3)
- **Actual:** 
- **Why:** Both arrays are compatibale for broadcasting. (1, 3) - (3, 1) which gives the final shape (3, 3)
- **Verdict:**

# Q13
```python
# 13.
(np.ones((2, 3)) + np.ones(2)).shape
```
- **Prediction:** (3, 3) 
- **Actual:** 
- **Why:** ValueError, both resulting arrays are not compatible for broadcasting
- **Verdict:**

# Q14
```python
# 14.
np.ones((2, 3, 4)).sum(axis=(0, 2)).shape
```
- **Prediction:**  [8, 8, 8]
- **Actual:** 
- **Why:** both blocks and columns colapse so will add all same rows across each across both blocks
- **Verdict:**

# Q15
```python
# 15.
X = np.arange(12).reshape(3, 4); np.shares_memory(X.T.ravel(), X)
```
- **Prediction:**  
- **Actual:** True, both ravel and transpose create a view
- **Why:** 
- **Verdict:**

# Q16
```python
# 16.
X = np.arange(12).reshape(3, 4); X.T.reshape(4, 3)[0]
```
- **Prediction:**  [0, 4, 8]
- **Actual:** 
- **Why:** 
- **Verdict:**

# Q17
```python
# 17.
np.array([[1, 2], [3, 4]])[[0, 1], [0, 1]]
```
- **Prediction:**  [1, 4]
- **Actual:** 
- **Why:**  Pairs the two list so it becomes (0, 0), (1, 1)
- **Verdict:**


# Q18
```python
# 18.
a = np.arange(5); a[a > 1 & a < 4]
```
- **Prediction:**  [2, 3]
- **Actual:** 
- **Why:**  And operation on all elements of the array
- **Verdict:**

# Q19
```python
# 19.
np.unique([3, 1, 3, 2, 1], return_index=True)[1]
```
- **Prediction:**  [3 1 2], [0, 1 3]
- **Actual:** 
- **Why:**  Both unique array and the indexes of unique element get returned
- **Verdict:**

# Q20
```python
# 20. Final value of a?
a = np.zeros(3, dtype=int); idx = np.array([0, 0, 1]); a[idx] += 1
```
- **Prediction:**  [1, 1, 1]
- **Actual:** 
- **Why:**
- **Verdict:**

# Q21
```python
# 21. Value of b?
a = np.array([3, 1, 2]); b = a.sort()
```
- **Prediction:**  [1, 2, 3]
- **Actual:** 
- **Why:**
- **Verdict:**




