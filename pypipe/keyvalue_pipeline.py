from typing import Callable, MutableMapping, Mapping, Tuple, TypeVar

from .pipeline import Pipeline


K = TypeVar("K")
V = TypeVar("V")


class KeyValuePipeline(Pipeline):
    def __init__(self, iterable: Mapping[K, V] | MutableMapping[K, V]) -> None:
        super().__init__(iterable.items())

    @staticmethod
    def __refunc(func):
        return lambda item: func(item[0], item[1])
    
    @staticmethod
    def __reduce_refunc(func):
        return lambda acc, item: func(acc[0], acc[1], item[0], item[1])

    def map(self, func: Callable[[K, V], Tuple[K, V]]) -> 'KeyValuePipeline':
        return super().map(KeyValuePipeline.__refunc(func))

    def filter(self, func: Callable[[K, V], bool]) -> 'KeyValuePipeline':
        return super().filter(self.__refunc(func))
    
    def reduce(self, func: Callable[[K, V, K, V], Tuple[K, V]], initial: Tuple[K, V]) -> Tuple[K, V]:
        return super().reduce(self.__reduce_refunc(func), initial)

    def reduce_inner(self, func: Callable[[K, V, K, V], Tuple[K, V]]) -> Tuple[K, V]:
        iterable = list(dict(self._iterable).items())
        return KeyValuePipeline(dict(iterable[1:])).reduce(func, iterable[0])
    
    def to_dict(self) -> dict[K, V]:
        return dict(self._iterable)
