from typing import Callable, Iterable, TypeVar
from functools import reduce


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
    
    def reduce(self, func: Callable[[T, T], T], initial: T) -> T:
        return reduce(func, self._iterable, initial)
    
    def to_list(self) -> list[T]:
        return list(self._iterable)
    
    def to_set(self) -> set[T]:
        return set(self._iterable)
