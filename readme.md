# PyPipe - Functional wrappers for iterables

Yep, like in _cool_ languages (StreamAPI in Java, LINQ in C#)

## Installation

```
pip install git+https://github.com/MrRboby/pypipe
```

## How to use

```python
from pypipe import pipe


iterable = [1, 2, 3, 4, 5]  # any Iterable

result = pipe(iterable) \
            .map(lambda num: num ** 2) \
            .filter(lambda num: num % 2 == 0) \
            .to_list()  # [4, 16]
```

See detailed examples in `examples.py`.

## Currently available wrappers

* `map`
* `filter`
* `filter_false`
* `reduce`
* `accumulate`
* `zip`
* `zip_longest`
* `reverse` (for ordering sequences, like lists or tuples)
* `sum`
* `prod`
* `all`
* `any`
* `to_list`
* `to_set`
* `to_dict` (for mapping sequences, like dicts)

## Changelog

* __0.3 (29.07.2023)__
    * Basic aggregation methods (sum, prod, all, any)
    * Combine reduce and reduce_inner methods
    * Zip and Longest Zip method
    * Accumulation method
    * Haskell-like aliases for accumulate functions (scanl, scanr, scanl1, scanr1)
* __0.2 (28.07.2023)__
    * Reduce method for mapping sequences
    * Inner reduce method
    * Reversed reduce method for ordering sequences
    * Filter-false method
    * Haskell-like aliases for reduce functions (fold, foldl, foldr, foldl1, foldr1)
* __0.1 (28.07.2023)__
    * Functional wrappers for iterables (map, filter, reduce)
    * Output pipelines to list, set and dict
    * Separate wrappers for sequences (like lists or tuples) and mappings (like dicts)

## TODO

* Infinite iterators and generators compatibility
* Integration with database adapter libraries
* Integration with NumPy arrays and Pandas DataFrames and Series
