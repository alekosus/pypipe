from typing import Callable, Iterable, TypeVar
from functools import reduce
from itertools import filterfalse
from math import prod


T = TypeVar("T")


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
    
    def reduce(self, func: Callable[[T, T], T], initial: T) -> T:
        return reduce(func, self._iterable, initial)
    
    def reduce_inner(self, func: Callable[[T, T], T]) -> T:
        iterator = iter(self._iterable)
        initial = next(iterator)
        return Pipeline(iterator).reduce(func, initial)
    
    def fold(self, func: Callable[[T, T], T], initial: T) -> T:
        return self.reduce(func, initial)
    
    def foldl(self, func: Callable[[T, T], T], initial: T) -> T:
        return self.reduce(func, initial)
    
    def foldl1(self, func: Callable[[T, T], T]) -> T:
        return self.reduce_inner(func)
    
    def sum(self, initial: T = 0) -> T:
        return sum(self._iterable, start=initial)
    
    def prod(self, initial: T = 1) -> T:
        return prod(self._iterable, start=initial)
    
    def all(self) -> bool:
        return all(self._iterable)
    
    def any(self) -> bool:
        return any(self._iterable)
    
    def to_list(self) -> list[T]:
        return list(self._iterable)
    
    def to_set(self) -> set[T]:
        return set(self._iterable)
