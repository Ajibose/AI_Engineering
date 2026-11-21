# Part 0 — Predict the output

## Q1
```python
a = np.arange(6); b = a[2:4]; b[:] = 0
# final value of a?
```
- **Prediction:** [0 1 0 0 4 5]
- **Actual:**
- **Why:** Because slicing creates a view in numpy so changing anything in the new array created by the slicing reflects in the original array
- **Verdict:** Correct


## Q2
```python
# 2. Final value of a?
a = np.arange(6); b = a[[2, 3]]; b[:] = 0
```
- **Prediction:** [0 1 2 3 4 5]
- **Actual:**
- **Why:** Fancy Indexing in numpy returns a copy not a view so changing elements in the new array does not affect the original one
- **Verdict:** Correct

## Q3
```python
# 3. Final value of a?
a = np.arange(6); a[::2][1:][0] = 99
```
- **Prediction:** 
- **Actual:** [0, 1, 99, 3, 4, 5]
- **Why:** Don't know
- **Verdict:** A slice of a slice is still a view of the original, so writing through a chain of slices changes a. To find the position, track it through each step: [::2] gives 0, 2, 4; [1:] gives 2, 4; [0] gives 2.

## Q4
```python
# 4. Final value of x?
x = np.array([1, 2, 3]); y = x; y = y + 1
```
- **Prediction:**  [2, 3, 4]
- **Actual:**
- **Why:** y = x creates a view so broadcasting on array y also affects the original array x
- **Verdict:** y = x gives the same array a second name; it isn’t a view. y = y + 1 builds a new array and moves y onto it, so x is unchanged. y += 1 changes the array in place, so x sees the change

## Q5
```python
# 5. Final value of x?
x = np.array([1, 2, 3]); y = x; y += 1
```
- **Prediction:**  [2, 3, 4]
- **Actual:**
- **Why:** y = x creates a view so broadcasting on array y also affects the original array x
- **Verdict:**  Correct prediction but wrong "Why" -  same object plus an in-place operation

## Q6
```python
# 6. Final value of a?
a = np.array([1, 2, 3]); a[0] = 2.9
```
- **Prediction:**  [2.9, 2, 3]
- **Actual:** [2, 2, 3]
- **Why:** changing the element at an index reflects in the original array
- **Verdict:** An array’s dtype is fixed at creation. Assigning a value converts it to that dtype, and float to int truncates towards zero, so 2.9 becomes 2. Assignment never changes the dtype.

## Q7
```python
# 7. Final value of a?
a = np.array([1, 2, 3]); a /= 2
```
- **Prediction:**  [0.5, 1.0, 1.5]
- **Actual:** error: `UFuncTypeError: Cannot cast ufunc 'divide' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'`
- **Why:** The scalar is broadcasted across all elements in the array a
- **Verdict:** In-place maths (`/=`, `+=`, ...) can't store float results in an int array: NumPy raises an error (same_kind rule). Plain assignment (`a[0] = 2.9`) does convert silently. Use `a = a / 2` to get a new float array, or `a //= 2` to stay with whole numbers.

## Q8
```python
# 8.
np.array([1, 2, 3], dtype=np.int8) * 100
```
- **Prediction:**  array([100, 200, 300])
- **Actual:** `array([100, -56, 44], dtype=int8)`
- **Why:** The scalar is broadcasted across all elements in the array 
- **Verdict:** A Python int takes the array's dtype, so int8 × 100 stays int8. int8 only holds -128 to 127, and values outside that range wrap around silently (subtract 256): 200 becomes -56 and 300 becomes 44. No error, no warning.


# Q9
```python
# 9.
np.array([3], dtype=np.uint8) - np.array([5], dtype=np.uint8)
```
- **Prediction:**  array([-2])
- **Actual:** `[254]`
- **Why:** element-wise operation is done on the arrays
- **Verdict:** NumPy picks the result dtype from the input types, never from the values, so uint8 − uint8 stays uint8, which holds only 0 to 255. -2 wraps around (add 256) to 254. Convert first (`astype(np.int16)`) when results can go negative.

## Q10
```python
# 10.
len(np.arange(0.5, 0.8, 0.1))
```
- **Prediction:**  array([0.5, 0,6, 0.7, 0.8])
- **Actual:** `4`, and the array is `[0.5, 0.6, 0.7, 0.7999999999999999]`
- **Why:** arange creates an array starting from th o.5 specified up to 0.8 with 0.1 as the step
- **Verdict:** ⚠ Right count, wrong reason. arange normally excludes stop (`arange(0, 5)` has no 5). Here float rounding makes `(0.8 - 0.5) / 0.1` equal 3.0000000000000004, which rounds up to 4 elements. With a float step, use `np.linspace(start, stop, count)`.

## Q10
```python
# 10.
len(np.arange(0.5, 0.8, 0.1))
```
- **Prediction:**  array([0.5, 0,6, 0.7, 0.8])
- **Actual:** `4`, and the array is `[0.5, 0.6, 0.7, 0.7999999999999999]`
- **Why:** arange creates an array starting from th o.5 specified up to 0.8 with 0.1 as the step
- **Verdict:** ⚠ Right count, wrong reason. arange normally excludes stop (`arange(0, 5)` has no 5). Here float rounding makes `(0.8 - 0.5) / 0.1` equal 3.0000000000000004, which rounds up to 4 elements. With a float step, use `np.linspace(start, stop, count)`.

# Q12
```python
# 12.
(np.arange(3) - np.arange(3).reshape(3, 1)).shape
```
- **Prediction:**  (3, 3)
- **Actual:** 
- **Why:** Both arrays are compatibale for broadcasting. (1, 3) - (3, 1) which gives the final shape (3, 3)
- **Verdict:** Correct

# Q13
```python
# 13.
(np.ones((2, 3)) + np.ones(2)).shape
```
- **Prediction:** error
- **Actual:** 
- **Why:** ValueError, both resulting arrays are not compatible for broadcasting
- **Verdict:**

# Q14
```python
# 14.
np.ones((2, 3, 4)).sum(axis=(0, 2)).shape
```
- **Prediction:**  [8, 8, 8]
- **Actual:** `(3,)`
- **Why:** both blocks and columns colapse so will add all same rows across each across both blocks
- **Verdict:** Summing over axes 0 and 2 removes them and leaves axis 1, so the shape is (3,), with each value 2 × 4 = 8. Next time, answer in the form asked (a shape, not values).

# Q15
```python
# 15.
X = np.arange(12).reshape(3, 4); np.shares_memory(X.T.ravel(), X)
```
- **Prediction:** True, both ravel and transpose create a view  
- **Actual:** `False`
- **Why:** 
- **Verdict:**ravel returns a view only when it can: a view must read memory with one fixed step. X.T.ravel() needs 0, 4, 8, 1, … (steps +4, +4, -7), which no single step gives, so it copies. The beginners guide's "ravel is a view" is the usual case, not the rule. Check with np.shares_memory.

# Q16
```python
# 16.
X = np.arange(12).reshape(3, 4); X.T.reshape(4, 3)[0]
```
- **Prediction:**  [0, 4, 8]
- **Actual:** 
- **Why:** 
- **Verdict:** Correct

# Q17
```python
# 17.
np.array([[1, 2], [3, 4]])[[0, 1], [0, 1]]
```
- **Prediction:**  [1, 4]
- **Actual:** 
- **Why:**  Pairs the two list so it becomes (0, 0), (1, 1)
- **Verdict:** Correct


# Q18
```python
# 18.
a = np.arange(5); a[a > 1 & a < 4]
```
- **Prediction:**  [2, 3]
- **Actual:** error: `ValueError: The truth value of an array with more than one element is ambiguous`
- **Why:**  And operation on all elements of the array
- **Verdict:** `&` binds tighter than `>` and `<`, so this parses as `a > (1 & a) < 4`, a chained comparison that uses `and` on arrays, which raises. Always wrap each condition: `a[(a > 1) & (a < 4)]`. Use `&` `|` `~`, never `and` `or` `not`, with arrays.

# Q19
```python
# 19.
np.unique([3, 1, 3, 2, 1], return_index=True)[1]
```
- **Prediction:**  [3 1 2], [0, 1 3]
- **Actual:** `array([1, 3, 0])`
- **Why:**  Both unique array and the indexes of unique element get returned
- **Verdict:** np.unique returns the values **sorted** ([1, 2, 3]), and return_index gives the first position of each sorted value: 1 at 1, 2 at 3, 3 at 0, so [1, 3, 0]. The trailing [1] picks only the positions from the (values, positions) pair.

## Q20
```python
# 20. Final value of a?
a = np.zeros(3, dtype=int); idx = np.array([0, 0, 1]); a[idx] += 1
```
- **Prediction:**  [1, 1, 1]
- **Actual:** `array([1, 1, 0])`
- **Why:**
- **Verdict:** ✗ `a[idx] += 1` runs as `a[idx] = a[idx] + 1`: read a copy ([0, 0, 0]), add 1 ([1, 1, 1]), then write the result back into `a`. All the reads happen before the write-back, so repeated index 0 is written 1 twice and counts once. Position 2 isn't in idx, so it stays 0. Fancy indexing copies when reading, but on the left of `=` it writes into the original. Use `np.add.at(a, idx, 1)` to make repeats count: [2, 1, 0].

## Q21
```python
# 21. Value of b?
a = np.array([3, 1, 2]); b = a.sort()
```
- **Prediction:**  [1, 2, 3]
- **Actual:** `None` (and `a` itself is now `[1, 2, 3]`)
- **Why:**
- **Verdict:** ✗ `a.sort()` sorts in place and returns None, like Python's `list.sort()`. `np.sort(a)` is the version that returns a new sorted array and leaves `a` unchanged. In-place methods usually return None; if unsure, print what they return.




