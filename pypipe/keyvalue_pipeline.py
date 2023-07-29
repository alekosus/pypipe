from typing import Callable, MutableMapping, Mapping, Tuple, TypeVar

from .pipeline import Pipeline


K = TypeVar("K")
V = TypeVar("V")


class KeyValuePipeline(Pipeline):
    def __init__(self, iterable: Mapping[K, V] | MutableMapping[K, V]) -> None:
        if isinstance(iterable, Mapping):
            super().__init__(iterable.items())
        else:
            super().__init__(iterable)

    @staticmethod
    def __refunc(func):
        return lambda item: func(item[0], item[1])
    
    @staticmethod
    def __reduce_refunc(func):
        return lambda acc, item: func(acc[0], acc[1], item[0], item[1])

    def map(self, func: Callable[[K, V], Tuple[K, V]]) -> 'KeyValuePipeline':
        return super().map(KeyValuePipeline.__refunc(func))

    def filter(self, func: Callable[[K, V], bool]) -> 'KeyValuePipeline':
        return super().filter(KeyValuePipeline.__refunc(func))
    
    def reduce(self, func: Callable[[K, V, K, V], Tuple[K, V]], initial: Tuple[K, V] | None = None) -> Tuple[K, V]:
        return super().reduce(KeyValuePipeline.__reduce_refunc(func), initial)
    
    def accumulate(self, func: Callable[[K, V, K, V], Tuple[K, V]], initial: Tuple[K, V] | None = None) -> 'KeyValuePipeline':
        return super().accumulate(KeyValuePipeline.__reduce_refunc(func), initial)

    def sum(self, initial: Tuple[K, V] = (0, 0)) -> Tuple[K, V]:
        return self.reduce(lambda acc_key, acc_value, key, value: (acc_key+key, acc_value+value), initial)
    
    def prod(self, initial: Tuple[K, V] = (1, 1)) -> Tuple[K, V]:
        return self.reduce(lambda acc_key, acc_value, key, value: (acc_key*key, acc_value*value), initial)
    
    def all(self) -> Tuple[bool, bool]:
        return self.reduce(lambda acc_key, acc_value, key, value: (bool(acc_key and key), bool(acc_value and value)))
    
    def any(self) -> Tuple[bool, bool]:
        return self.reduce(lambda acc_key, acc_value, key, value: (bool(acc_key or key), bool(acc_value or value)))
    
    def to_dict(self) -> dict[K, V]:
        return dict(self._iterable)
