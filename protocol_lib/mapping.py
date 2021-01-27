from typing import TypeVar, Union, Tuple, Optional

from typing_extensions import Protocol, runtime_checkable

from .iterable import Iterable, Iterator

__all__ = [
    "Mapping",
]


K = TypeVar("K")
V = TypeVar("V")


@runtime_checkable
class Mapping(Protocol[K, V]):
    def __contains__(self, item: V) -> bool:
        ...

    def __getitem__(self, index: K) -> V:
        ...

    def __iter__(self) -> Iterator[K]:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __ne__(self, other: object) -> bool:
        ...

    def get(self, key: K, default: Optional[V] = ...) -> V:
        ...

    def items(self) -> Iterator[Tuple[K, V]]:
        ...

    def keys(self) -> Iterator[K]:
        ...

    def values(self) -> Iterator[V]:
        ...
