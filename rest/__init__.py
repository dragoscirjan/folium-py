from .create import Create
from .fetch import Fetch
from .retrieve import Retrieve
from .replace import Replace
from .update import Update
from .delete import Delete


class REST(Create, Fetch, Retrieve, Replace, Update, Delete):
    """
    Interface for implementing REST methods.
    :see https://en.wikipedia.org/wiki/Representational_state_transfer
    """
