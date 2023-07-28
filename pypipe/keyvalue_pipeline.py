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

    def map(self, func: Callable[[K, V], Tuple[K, V]]) -> 'KeyValuePipeline':
        return super().map(KeyValuePipeline.__refunc(func))

    def filter(self, func: Callable[[K, V], bool]) -> 'KeyValuePipeline':
        return super().filter(self.__refunc(func))
    
    def reduce(self, func: Callable[[K, V, K, V], Tuple[K, V]], initial: Tuple[K, V]) -> Tuple[K, V]:
        raise NotImplementedError("Reduce method is currently unavailable for mapping sequences")
    
    def to_list(self) -> list[Tuple[K, V]]:
        return super().to_list()
    
    def to_set(self) -> set[Tuple[K, V]]:
        return super().to_set()
    
    def to_dict(self) -> dict[K, V]:
        return dict(self._iterable)
