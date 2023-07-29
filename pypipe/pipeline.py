from typing import Callable, Iterable, TypeVar
from functools import reduce
from itertools import accumulate, filterfalse, zip_longest
from math import prod


T = TypeVar("T")
O = TypeVar("O")


class Pipeline:
    def __init__(self, iterable: Iterable[T]) -> None:
        self._iterable: Iterable[T] = iterable
    
    def map(self, func: Callable[[T], T]) -> 'Pipeline':
        self._iterable = map(func, self._iterable)
        return self

    def filter(self, func: Callable[[T], bool]) -> 'Pipeline':
        self._iterable = filter(func, self._iterable)
        return self
    
    def filter_false(self, func: Callable[[T], bool]) -> 'Pipeline':
        self._iterable = filterfalse(func, self._iterable)
        return self
    
    def reduce(self, func: Callable[[T, T], T], initial: T | None = None) -> T:
        if initial is None:
            return reduce(func, self._iterable)
        return reduce(func, self._iterable, initial)
    
    def fold(self, func: Callable[[T, T], T], initial: T) -> T:
        return self.reduce(func, initial)
    
    def foldl(self, func: Callable[[T, T], T], initial: T) -> T:
        return self.reduce(func, initial)
    
    def foldl1(self, func: Callable[[T, T], T]) -> T:
        return self.reduce(func)
    
    def sum(self, initial: T = 0) -> T:
        return sum(self._iterable, start=initial)
    
    def prod(self, initial: T = 1) -> T:
        return prod(self._iterable, start=initial)
    
    def all(self) -> bool:
        return all(self._iterable)
    
    def any(self) -> bool:
        return any(self._iterable)
    
    def accumulate(self, func: Callable[[T, T], T], initial: T | None = None) -> 'Pipeline':
        return self.__class__(accumulate(self._iterable, func, initial=initial))
    
    def scanl(self, func: Callable[[T, T], T], initial: T) -> 'Pipeline':
        return self.accumulate(func, initial)
    
    def scanl1(self, func: Callable[[T, T], T]) -> 'Pipeline':
        return self.accumulate(func)
    
    def zip(self, other: Iterable[O] | 'Pipeline') -> 'Pipeline':
        if isinstance(other, Pipeline):
            return self.__class__(zip(self._iterable, other._iterable))
        return self.__class__(zip(self._iterable, other))
    
    def zip_longest(self, other: Iterable[O] | 'Pipeline', fill_value: T | O | None = None) -> 'Pipeline':
        if isinstance(other, Pipeline):
            return self.__class__(zip_longest(self._iterable, other._iterable, fillvalue=fill_value))
        return self.__class__(zip_longest(self._iterable, other, fillvalue=fill_value))

    def to_list(self) -> list[T]:
        return list(self._iterable)
    
    def to_set(self) -> set[T]:
        return set(self._iterable)
