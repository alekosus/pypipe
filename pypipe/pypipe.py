from typing import (
    Iterable, 
    Sequence, 
    MutableSequence, 
    Mapping, 
    MutableMapping
)

from .pipeline import Pipeline
from .ordering_pipeline import OrderingPipeline
from .keyvalue_pipeline import KeyValuePipeline


def pipe(iterable: Iterable):
    if isinstance(iterable, (Sequence, MutableSequence)):
        return OrderingPipeline(iterable)

    if isinstance(iterable, (Mapping, MutableMapping)):
        return KeyValuePipeline(iterable)
    
    return Pipeline(iterable)
