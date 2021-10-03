from protocol_lib import ISized


def test_sized() -> None:
    class Impl:
        def __len__(self) -> int:
            return 42

    impl: ISized = Impl()

    assert len(impl) == 42
