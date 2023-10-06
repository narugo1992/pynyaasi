import collections.abc
from operator import itemgetter
from typing import List

from hbutils.scale import size_to_bytes_str
from hbutils.string import format_tree

from .size import SizeProxy, _text_to_bytes


class DirectoryTreeNode(collections.abc.Sequence):
    def __init__(self, name: str, is_folder: bool):
        self._name = name
        self._is_folder = is_folder

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_folder(self) -> bool:
        return self._is_folder

    def __getitem__(self, index):
        return self._list_children()[index]

    def __len__(self):
        return len(self._list_children())

    def _size_raw(self) -> str:
        raise NotImplementedError  # pragma: no cover

    def _bytes_count(self) -> int:
        raise NotImplementedError  # pragma: no cover

    @property
    def size(self) -> SizeProxy:
        return SizeProxy(self._size_raw())

    def _list_children(self) -> List['DirectoryTreeNode']:
        raise NotImplementedError  # pragma: no cover

    def _title(self):
        return f'{self._name} [{"file" if not self._is_folder else "folder"}, {self._size_raw()}]'

    def _node_info(self):
        return self._title(), [child._node_info() for child in self._list_children()]

    def __str__(self):
        return format_tree(self._node_info(), format_node=itemgetter(0), get_children=itemgetter(1))

    def __repr__(self):
        return f'<{self.__class__.__name__} {self._title()}>'


class Directory(DirectoryTreeNode):
    def __init__(self, name, children: List[DirectoryTreeNode]):
        DirectoryTreeNode.__init__(self, name, is_folder=True)
        self._children = children

    def _size_raw(self) -> str:
        return size_to_bytes_str(self._bytes_count(), precision=1)

    def _bytes_count(self) -> int:
        return sum([child._bytes_count() for child in self._children])

    def _list_children(self) -> List['DirectoryTreeNode']:
        return self._children


class File(DirectoryTreeNode):
    def __init__(self, name, size_raw: str):
        DirectoryTreeNode.__init__(self, name, is_folder=False)
        self._size_raw_text = size_raw

    def _size_raw(self) -> str:
        return self._size_raw_text

    def _bytes_count(self) -> int:
        return _text_to_bytes(self._size_raw_text)

    def _list_children(self) -> List['DirectoryTreeNode']:
        return []
