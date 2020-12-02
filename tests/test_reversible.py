from protocol_lib import Iterator, Reversible


def test_reversible() -> None:
    class Impl:
        def __iter__(self) -> Iterator[int]:
            yield from [1, 2, 4, 8]

        def __reversed__(self) -> Iterator[int]:
            yield from [8, 4, 2, 1]

    impl: Reversible[int] = Impl()

    forwards = iter(impl)

    assert next(forwards) == 1
    assert next(forwards) == 2
    assert next(forwards) == 4
    assert next(forwards) == 8

    backwards = reversed(impl)

    assert next(backwards) == 8
    assert next(backwards) == 4
    assert next(backwards) == 2
    assert next(backwards) == 1
