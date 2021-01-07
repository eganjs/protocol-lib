from protocol_lib import Collection, Iterable, Iterator, Sized


def test_collection() -> None:
    impl: Collection[int] = [7, 13, 42]

    assert 42 in impl
    assert 11 not in impl
    assert list(iter(impl)) == [7, 13, 42]
    assert len(impl) == 3


def test_collection_structural_subclasses() -> None:
    assert issubclass(
        Collection,
        (
            Sized,
            Iterable,
            Iterator,
        ),
    )
