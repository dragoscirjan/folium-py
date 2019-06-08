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


class Create:
    """
    Interface for implementing CRUD Create method.
    :see https://en.wikipedia.org/wiki/Create,_read,_update_and_delete
    """

    @abc.abstractmethod
    def create(self, items, criteria: dict = {}) -> list:
        """
        Create new resource(s).
        Can receive a item or a set of items to create.

        create({ "text": "I really have to iron" })

        or

        create([
          { "text": "I really have to iron" },
          { "text": "Do laundry" }
        ])

        :param items: dict|list     can be a single element or an array of elements
        :param criteria: dict       TODO: Not used, to be defined
        :return: list               will return an array of ids for the models that have been saved in the database
        """
        pass


class CreateQuery:
    """
    Interface for implementing CRUD Create query.
    """

    @abc.abstractmethod
    def create(self, items, criteria: dict = {}) -> str:
        """
        Generate string query for `Create.create` method.

        :see Create.create
        :param items: dict|list     can be a single element or an array of elements
        :param criteria: dict       TODO: Not used, to be defined
        :return: str
        """
        pass
