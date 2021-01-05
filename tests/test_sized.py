from protocol_lib import Sized


def test_sized() -> None:
    class Impl:
        def __len__(self) -> int:
            return 42

    impl: Sized = Impl()

    assert len(impl) == 42
