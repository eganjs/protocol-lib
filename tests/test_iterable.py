from protocol_lib import Iterable, Iterator


def test_iterable_and_iterator() -> None:
    class ImplIterator:
        def __init__(self) -> None:
            self.value = 0

        def __iter__(self) -> "ImplIterator":
            return self

        def __next__(self) -> int:
            self.value += 42
            return self.value

    class ImplIterable:
        def __iter__(self) -> ImplIterator:
            return ImplIterator()

    impl_iterable: Iterable[int] = ImplIterable()
    impl_iterator: Iterator[int] = iter(impl_iterable)

    assert next(impl_iterator) == 42
    assert next(iter(impl_iterator)) == 84


def test_iterator_structural_subclasses() -> None:
    assert issubclass(Iterator, Iterable)
