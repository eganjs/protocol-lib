from protocol_lib import Collection, Reversible, Sequence


def test_sequence() -> None:
    impl: Sequence[int] = [7, 13, 42]

    assert 42 in impl
    assert 11 not in impl
    assert list(iter(impl)) == [7, 13, 42]
    assert list(reversed(impl)) == [42, 13, 7]
    assert len(impl) == 3
    assert impl[0] == 7
    assert impl.index(42) == 2
    assert impl.count(13) == 1


def test_sequence_structural_subclasses() -> None:
    assert issubclass(
        Sequence,
        (
            Collection,
            Reversible,
        ),
    )
