from protocol_lib import IHashable


def test_hashable() -> None:
    class Impl:
        def __hash__(self) -> int:
            return 42

    impl: IHashable = Impl()

    assert hash(impl) == 42
