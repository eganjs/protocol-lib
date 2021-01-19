from protocol_lib import Collection, MutableSequence, Reversible, Sequence


def test_sequence() -> None:
    impl: Sequence[str] = ["7", "13", "42"]

    assert "42" in impl
    assert "11" not in impl
    assert list(iter(impl)) == ["7", "13", "42"]
    assert list(reversed(impl)) == ["42", "13", "7"]
    assert len(impl) == 3
    assert impl[0] == "7"
    assert impl.index("42") == 2
    assert impl.count("13") == 1


def test_sequence_structural_subclasses() -> None:
    assert issubclass(
        Sequence,
        (
            Collection,
            Reversible,
        ),
    )


def test_mutable_sequence() -> None:
    impl: MutableSequence[str] = ["7", "13", "42"]

    impl[2] = "17"
    assert impl == ["7", "13", "17"]

    del impl[1]
    assert impl == ["7", "17"]

    impl.append("144")
    assert impl == ["7", "17", "144"]

    impl.insert(2, "2")
    assert impl == ["7", "17", "2", "144"]

    impl.reverse()
    assert impl == ["144", "2", "17", "7"]

    impl.extend(["a", "b", "c"])
    assert impl == ["144", "2", "17", "7", "a", "b", "c"]

    assert impl.pop() == "c"
    assert impl == ["144", "2", "17", "7", "a", "b"]

    assert impl.pop(2) == "17"
    assert impl == ["144", "2", "7", "a", "b"]

    impl.remove("2")
    assert impl == ["144", "7", "a", "b"]

    impl += ["one", "two"]
    assert impl == ["144", "7", "a", "b", "one", "two"]

    impl.clear()
    assert not impl


def test_mutable_sequence_structural_subclasses() -> None:
    assert issubclass(MutableSequence, Sequence)  # type: ignore
