from protocol_lib import Collection, Mapping


def test_mapping() -> None:
    impl: Mapping[str, int] = {"severn": 7, "two": 2, "five": 5}

    assert "two" in impl
    assert "three" not in impl
    assert list(iter(impl)) == ["severn", "two", "five"]
    assert len(impl) == 3
    assert impl["severn"] == 7
    assert list(impl.keys()) == ["severn", "two", "five"]
    assert list(impl.items()) == [("severn", 7), ("two", 2), ("five", 5)]
    assert list(impl.values()) == [7, 2, 5]


def test_sequence_structural_subclasses() -> None:
    assert issubclass(
        Mapping,
        (Collection,),
    )
