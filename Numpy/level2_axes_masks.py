"""Level 2 — Axes, aggregation, boolean masks, sorting and unique.

Rules for every function in this file (unless its docstring says otherwise):
- No Python for/while loops or comprehensions.
- Don't modify the input arrays.
- Where a docstring says "no warnings", the function must not emit any
  RuntimeWarning (e.g. 'invalid value encountered in divide').
"""

import numpy as np


def standardise_columns(X):
    """2.1 Z-score each COLUMN of a 2-D array: subtract the column mean, then divide
    by the column standard deviation (NumPy's default std, ddof=0).

    - A column counts as constant when its std is below 1e-12. Constant columns
      must come out as all zeros (not NaN, not garbage).
    - Return float64, same shape. No warnings.
    - Test it with a column of seven copies of 0.1, and work out why `std == 0`
      is the wrong check.

    standardise_columns(np.array([[1., 10.], [3., 10.]])) -> [[-1, 0], [1, 0]]
    """


def replace_outliers(x, k=3.0):
    """2.2 x[i] is an outlier if |x[i] - mean(x)| > k * std(x), using the mean and
    std of the WHOLE original array. Replace every outlier with the MEDIAN of the
    non-outliers. Return a float64 copy. You may assume k >= 1.

    replace_outliers(np.array([1., 2., 3., 2., 100.]), k=1.5) -> [1, 2, 3, 2, 2]

    Bonus (answer in a comment): why does k >= 1 guarantee at least one non-outlier?
    """
    ...


def top_k_per_row(X, k):
    """2.3 Return the column indices of the k largest values in each row of X,
    largest first. Shape (n_rows, k). Assume values in a row are distinct and
    1 <= k <= n_cols.

    top_k_per_row(np.array([[0.1, 0.9, 0.4], [7., 2., 5.]]), 2) -> [[1, 2], [0, 2]]
    """
    ...


def rank_by_frequency(token_ids):
    """2.4 Count how often each id occurs in a 1-D int array. Return (ids, counts),
    ordered by count from highest to lowest; ties go to the SMALLER id first.

    rank_by_frequency(np.array([5, 3, 5, 9, 3, 1, 5])) -> ([5, 3, 1, 9], [3, 2, 1, 1])
    """
    ...


def unique_in_order(a):
    """2.5 Return the distinct values of a 1-D array in the order they FIRST appear
    (np.unique sorts; this must not). Must work on string arrays too.
    No dict or set tricks.

    unique_in_order(np.array([4, 1, 4, 2, 1, 7])) -> [4, 1, 2, 7]
    """
    ...


def masked_row_mean(X, mask):
    """2.6 Mean of each row of X, counting ONLY the positions where `mask` is True.

    X: (n, m) floats. mask: (n, m) bools.
    - A row with no True entries gives NaN.
    - X may contain NaN or inf at masked-OUT positions; they must not affect the
      result.
    - Return shape (n,), float64. No warnings.

    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mask = [[T, F, T], [F, F, F], [F, T, F]]
    masked_row_mean(X, mask) -> [2., nan, 8.]
    """
    ...