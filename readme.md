# PyPipe - Functional wrappers for iterables

Yep, like in _cool_ languages (StreamAPI in Java, LINQ in C#)

## How to use

```python
from pypipe import pipe


iterable = [1, 2, 3, 4, 5]  # any Iterable

result = pipe(iterable) \
            .map(lambda num: num ** 2) \
            .filter(lambda num: num % 2 == 0) \
            .to_list()  # [4, 16]
```

See detailed examples in `example.py`.

## Currently available wrappers

* `map`
* `filter`
* `reduce` (not available for dictionaries)
* `reverse` (for ordering sequences, like lists or tuples)
* `to_list`
* `to_set`
* `to_dict` (for mapping sequences, like dicts)

## TODO

* Infinite iterators and generators compatibility
* Integration with database adapter libraries
* Integration with NumPy arrays and Pandas DataFrames and Series