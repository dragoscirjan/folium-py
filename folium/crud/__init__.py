import abc

from .create import *
from .read import *
from .update import *
from .delete import *


class CRUD(Create, Read, Update, Delete):
    """
    Interface for implementing CRUD methods.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

class CRUDQuery(CreateQuery, ReadQuery, UpdateQuery, DeleteQuery):
    """
    Interface for implementing CRUD query methods.
    """
