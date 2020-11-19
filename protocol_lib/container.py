from typing import Protocol, TypeVar, runtime_checkable

__all__ = ["Container"]


T = TypeVar("T", contravariant=True)


@runtime_checkable
class Container(Protocol[T]):
    def __contains__(self, item: T) -> bool:
        ...
