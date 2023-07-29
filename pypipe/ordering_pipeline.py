from typing import Callable, TypeVar, MutableSequence, Sequence

from .pipeline import Pipeline


T = TypeVar("T")


class OrderingPipeline(Pipeline):
    def __init__(self, iterable: Sequence[T] | MutableSequence[T]) -> None:
        super().__init__(iterable)
        self.__is_reversed = False

    def reduce(self, func: Callable[[T, T], T], initial: T | None = None) -> T:
        if self.__is_reversed:
            return OrderingPipeline(reversed(list(self._iterable))).reduce(func, initial)
        return super().reduce(func, initial)
    
    def reduce_reverse(self, func: Callable[[T, T], T], initial: T | None = None) -> T:
        if self.__is_reversed:
            return super().reduce(func, initial)
        return OrderingPipeline(reversed(list(self._iterable))).reduce(func, initial)

    def foldr(self, func: Callable[[T, T], T], initial: T) -> T:
        return self.reduce_reverse(func, initial)
    
    def foldr1(self, func: Callable[[T, T], T]) -> T:
        return self.reduce_reverse(func)
    
    def reverse(self) -> 'OrderingPipeline':
        self.__is_reversed = not self.__is_reversed
        return self
    
    def inverse(self) -> 'OrderingPipeline':
        return self.reverse()
    
    def to_list(self) -> list[T]:
        if self.__is_reversed:
            return list(reversed(list(self._iterable)))
        return list(self._iterable)
