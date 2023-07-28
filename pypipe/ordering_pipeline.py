from typing import Callable, TypeVar, MutableSequence, Sequence

from .pipeline import Pipeline


T = TypeVar("T")


class OrderingPipeline(Pipeline):
    def __init__(self, iterable: Sequence[T] | MutableSequence[T]) -> None:
        super().__init__(iterable)
        self.__is_reversed = False
    
    def map(self, func: Callable[[T], T]) -> 'OrderingPipeline':
        return super().map(func)

    def filter(self, func: Callable[[T], bool]) -> 'OrderingPipeline':
        return super().filter(func)
    
    def reduce(self, func: Callable[[T, T], T], initial: T) -> T:
        return super().reduce(func, initial)
    
    def reverse(self) -> 'OrderingPipeline':
        self.__is_reversed = not self.__is_reversed
        return self
    
    def inverse(self) -> 'OrderingPipeline':
        return self.reverse()
    
    def to_list(self) -> list[T]:
        if self.__is_reversed:
            return list(reversed(list(self._iterable)))
        return list(self._iterable)
