import abc

from .create import Create
from .read import Read
from .update import Update
from .delete import Delete


class CRUD(Create, Read, Update, Delete):
    """
    Interface for implementing CRUD methods.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

    # @abc.abstractmethod
    # def create(self, items, criteria: dict = {}) -> list:
    #     pass
    #
    # @abc.abstractmethod
    # def read(self, criteria: list = [], fields: list = [], options: dict = {}):
    #     pass
    #
    # @abc.abstractmethod
    # def update(self, items, criteria: list = [], options: dict = {}):
    #     pass
    #
    # @abc.abstractmethod
    # def delete(self, items, criteria: list = [], options: dict = {}):
    #     pass
