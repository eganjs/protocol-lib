from protocol_lib import ICollection, IIterable, IIterator, ISized


def test_collection() -> None:
    impl: ICollection[int] = [7, 13, 42]

    assert 42 in impl
    assert 11 not in impl
    assert list(iter(impl)) == [7, 13, 42]
    assert len(impl) == 3


def test_collection_structural_subclasses() -> None:
    assert issubclass(
        ICollection,
        (
            ISized,
            IIterable,
            IIterator,
        ),
    )
