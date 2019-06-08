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


class Update:
    """
    Interface for implementing CRUD Update (Modify) method.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

    @abc.abstractmethod
    def update(self, items, criteria: list = [], options: dict = {}) -> list:
        """
        Update/replace a resource or set of resources in the database.
        If a resource does not exists when passed to the update method, it will be created.

        If `criteria` is given, method will then function as an 'update/patch' handler, not as a 'replace' one.
        If `criteria` is given and `items` are multiple, function will apply all all items as patch.
        If `criteria` is not give, and resource is not having an ID, method will try to create the resource.

        update({ "text": "I really have to iron" }, [ ( 'id', 10 ) ]) # behave as patch (update)

        or

        update([
          { "text": "I really have to iron", "id": 10 }, # this item will be replaced
          { "text": "Do laundry" ] # this item will be created
        ])

        :param items: dict|list     can be a single element or an array of elements
        :param criteria: list       (list of tuples) criteria to filter database data
        :param options: dict        TODO: to be defined
        :return: list               will return the ids of the elements updated
        """
        pass

class UpdateQuery:
    """
    Interface for implementing CRUD Update (Modify) method.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

    @abc.abstractmethod
    def update(self, items, criteria: list = [], options: dict = {}) -> str:
        """
        Generate string query for `Update.update` method.

        :see Update.update
        :param items: dict|list     can be a single element or an array of elements
        :param criteria: list       (list of tuples) criteria to filter database data
        :param options: dict        TODO: to be defined
        :return: str
        """
        pass
