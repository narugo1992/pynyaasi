import collections.abc
from operator import itemgetter
from typing import List

from hbutils.scale import size_to_bytes_str
from hbutils.string import format_tree

from .size import SizeProxy, _text_to_bytes


class DirectoryTreeNode(collections.abc.Sequence):
    """
    Represents a node in a directory tree structure.

    :param str name: The name of the node.
    :param bool is_folder: Indicates if the node is a folder.

    :ivar name: The name of the node.
    :vartype name: str
    :ivar is_folder: Indicates if the node is a folder.
    :vartype is_folder: bool
    """

    def __init__(self, name: str, is_folder: bool):
        self._name = name
        self._is_folder = is_folder

    @property
    def name(self) -> str:
        """
        Get the name of the node.

        :return: The name of the node.
        :rtype: str
        """
        return self._name

    @property
    def is_folder(self) -> bool:
        """
        Check if the node is a folder.

        :return: True if the node is a folder, False if it's a file.
        :rtype: bool
        """
        return self._is_folder

    def __getitem__(self, index):
        return self._list_children()[index]

    def __len__(self):
        return len(self._list_children())

    def _size_raw(self) -> str:
        """
        Get the raw size of the node.

        :raise: NotImplementedError

        :return: The raw size of the node.
        :rtype: str
        """
        raise NotImplementedError  # pragma: no cover

    def _bytes_count(self) -> int:
        """
        Get the byte count of the node's size.

        :raise: NotImplementedError

        :return: The byte count of the node's size.
        :rtype: int
        """
        raise NotImplementedError  # pragma: no cover

    @property
    def size(self) -> SizeProxy:
        """
        Get a SizeProxy object representing the size of the node.

        :return: A SizeProxy object representing the size of the node.
        :rtype: SizeProxy
        """
        return SizeProxy(self._size_raw())

    def _list_children(self) -> List['DirectoryTreeNode']:
        """
        Get a list of children nodes.

        :raise: NotImplementedError

        :return: A list of children nodes.
        :rtype: List[DirectoryTreeNode]
        """
        raise NotImplementedError  # pragma: no cover

    def _title(self):
        return f'{self._name} [{"file" if not self._is_folder else "folder"}, {self._size_raw()}]'

    def _node_info(self):
        return self._title(), [child._node_info() for child in self._list_children()]

    def __str__(self):
        return format_tree(self._node_info(), format_node=itemgetter(0), get_children=itemgetter(1))

    def __repr__(self):
        return f'<{self.__class__.__name__} {self._title()}>'

    def _info(self):
        raise NotImplementedError  # pragma: no cover

    def __eq__(self, other):
        if self is other:
            return True
        elif type(other) == type(self):
            return self._info() == other._info()
        else:
            return False

    def __hash__(self):
        return hash(self._info())


class Directory(DirectoryTreeNode):
    """
    Represents a directory in a directory tree structure.

    :param str name: The name of the directory.
    :param List[DirectoryTreeNode] children: A list of child nodes.

    :ivar name: The name of the directory.
    :vartype name: str
    :ivar children: A list of child nodes.
    :vartype children: List[DirectoryTreeNode]
    """

    def __init__(self, name, children: List[DirectoryTreeNode]):
        DirectoryTreeNode.__init__(self, name, is_folder=True)
        self._children = children

    def _size_raw(self) -> str:
        """
        Get the raw size of the directory.

        :return: The raw size of the directory.
        :rtype: str
        """
        return size_to_bytes_str(self._bytes_count(), precision=1)

    def _bytes_count(self) -> int:
        """
        Get the byte count of the directory's size.

        :return: The byte count of the directory's size.
        :rtype: int
        """
        return sum([child._bytes_count() for child in self._children])

    def _list_children(self) -> List['DirectoryTreeNode']:
        """
        Get a list of child nodes.

        :return: A list of child nodes.
        :rtype: List[DirectoryTreeNode]
        """
        return self._children

    def _info(self):
        return self.name, tuple(self._children)


class File(DirectoryTreeNode):
    """
    Represents a file in a directory tree structure.

    :param str name: The name of the file.
    :param str size_raw: The raw size of the file.

    :ivar name: The name of the file.
    :vartype name: str
    :ivar size_raw: The raw size of the file.
    :vartype size_raw: str
    """

    def __init__(self, name, size_raw: str):
        DirectoryTreeNode.__init__(self, name, is_folder=False)
        self._size_raw_text = size_raw

    def _size_raw(self) -> str:
        """
        Get the raw size of the file.

        :return: The raw size of the file.
        :rtype: str
        """
        return self._size_raw_text

    def _bytes_count(self) -> int:
        """
        Get the byte count of the file's size.

        :return: The byte count of the file's size.
        :rtype: int
        """
        return _text_to_bytes(self._size_raw_text)

    def _list_children(self) -> List['DirectoryTreeNode']:
        """
        Get a list of child nodes (empty for files).

        :return: An empty list.
        :rtype: List[DirectoryTreeNode]
        """
        return []

    def _info(self):
        return self.name, self._size_raw_text
