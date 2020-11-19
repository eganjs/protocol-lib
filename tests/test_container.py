from protocol_lib import Container


def test_container() -> None:
    class Impl:
        def __contains__(self, item: int) -> bool:
            return item == 42

    impl: Container[int] = Impl()

    assert 42 in impl
    assert 10 not in impl
