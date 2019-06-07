"""
Copyright 2019 Dragos Cirjan <dragos.cirjan@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import abc

class DeleteBase:
    """
    Common starter interface, for constants.
    """

    OPTION_SOFT_DELETE = '__soft_delete'
    """
    Implement in options, if you wish to soft delete items.
    """


class Delete(DeleteBase):
    """
    Interface for implementing CRUD Delete (Destroy) method.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

    @abc.abstractmethod
    def delete(self, items, criteria: list = [], options: dict = {}):
        """
        Delete resource(s) from the database.

        delete({ "text": "I really have to iron" })

        or

        delete([
          { "text": "I really have to iron" },
          { "text": "Do laundry" }
        ])

        or

        delete([], [
          ( 'id', '>', 10 )
        ])

        or

        delete([], [
          ( 'id', '>', 10 )
        ], { '__soft_delete': True })

        :param items: dict|list     can be a single element or an array of elements
        :param criteria: list       (list of tuples) implementing criteria by which to delete
        :param options: dict        TODO: Not used, to be defined
        :return: None
        """
        pass



class DeleteQuery(DeleteBase):
    """
    Interface for implementing CRUD Delete (Destroy) query.
    """

    @abc.abstractmethod
    def delete(self, items, criteria: list = [], options: dict = {}) -> str:
        """
        Generate string query for `Delete.delete` method.

        :see Delete.delete
        :param items: dict|list     can be a single element or an array of elements
        :param criteria: list       (list of tuples) implementing criteria by which to delete
        :param options: dict        TODO: Not used, to be defined
        :return: str
        """
        pass
