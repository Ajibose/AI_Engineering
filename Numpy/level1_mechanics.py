"""Level 1 — Array mechanics: creation, dtypes, slicing, views vs copies.

Rules for every function in this file (unless its docstring says otherwise):
- No Python for/while loops or comprehensions.
- Don't modify the input arrays.
"""

import numpy as np


def checkerboard(n_rows, n_cols):
    """1.1 Return an (n_rows, n_cols) int8 array of 0s and 1s in a checkerboard
    pattern, with 0 in the top-left corner.

    No loops: create the array, then fill it using slices with steps.

    checkerboard(3, 4) ->
    [[0 1 0 1]
     [1 0 1 0]
     [0 1 0 1]]
    """

    board = np.ones((n_rows, n_cols), dtype=np.int8)
    board[::2, ::2] = 0
    board[1::2, 1::2] = 0

    print(board)
    return board


def strided_view(a):
    """1.2 Return every other row of the 2-D array `a`, starting from the LAST row
    and going up, with the columns reversed. The result must be a VIEW of `a`.

    strided_view(np.arange(12).reshape(4, 3)) ->
    [[11 10  9]
     [ 5  4  3]]
    """

    # [[0 1 2]
    #  [3 4 5]
    #  [6 7 8]
    #  [9 10 11]]
    
    return a[::-2, ::-1]


def safe_tail(a, k):
    """1.3 Return a COPY of the last k elements of the 1-D array `a`.

    k == 0 -> empty array. k >= len(a) -> copy of the whole array.
    k < 0 -> ValueError. Changing the result must never change `a`.
    """
    if k < 0:
      raise ValueError()
    elif k >= len(a):
      return a.copy()

    start = len(a) - k
    end = len(a)

    return a[start:end].copy()


def nbytes_for(shape, dtype):
    """1.4 Return how many bytes an array with this shape and dtype would use,
    as a Python int, WITHOUT creating the array. Must work for shape ().

    nbytes_for((1000, 1000), np.float32)    -> 4000000
    nbytes_for((7_000_000_000,), "float16") -> 14000000000
    """
    type_size = np.dtype(dtype).itemsize

    total_size = type_size * math.prod(shape)

    return total_size


def to_uint8_image(x):
    """1.5 Convert float pixel values to uint8: round like np.round, then clamp
    to [0, 255]. Don't modify `x`.

    to_uint8_image(np.array([-3.0, 2.5, 3.5, 254.6, 300.0])) -> [0, 2, 4, 255, 255]
    """
    return np.round(x).clip(0, 255).astype(np.uint8)


def inclusive_grid(start, stop, step):
    """1.6 Return float64 values from start to stop INCLUDING stop, step apart.
    The length must be exact and the last value must equal stop exactly.

    inclusive_grid(0.0, 1.0, 0.25)     -> [0, 0.25, 0.5, 0.75, 1.0]
    len(inclusive_grid(0.0, 1.0, 0.1)) -> 11
    """

    no_of_elements = 1 + ((stop - start) / step)

    return np.linspace(start, stop, round(no_of_elements), endpoint=True)

