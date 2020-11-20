from protocol_lib import Hashable


def test_hashable() -> None:
    class Impl:
        def __hash__(self) -> int:
            return 42

    impl: Hashable = Impl()

    assert hash(impl) == 42
