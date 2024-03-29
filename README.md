# protocol-lib

![Build](https://github.com/eganjs/protocol-lib/workflows/ci/badge.svg)

Protocols for better structural typing

## Goals

Implement Protocols for:
- [x] Container
- [x] Hashable
- [x] Iterable
- [x] Iterator
- [x] Reversible
- [ ] ~~Generator~~
- [x] Sized
- [ ] Callable
- [x] Collection
- [x] Sequence
- [x] MutableSequence
- [ ] ByteString
- [ ] Set
- [ ] MutableSet
- [x] Mapping
- [ ] MutableMapping
- [ ] MappingView
- [ ] ItemsView
- [ ] KeysView
- [ ] ValuesView
- [ ] Awaitable
- [ ] Coroutine
- [ ] AsyncIterable
- [ ] AsyncIterator
- [ ] AsyncGenerator

## Notes

Generator is not currently implemented in this library. This is due to challenges encountered when attempting to implement it.

## Updating project config

To edit project configuration, update the `.projenrc.js` file in the root of the project and run `make projen`.
