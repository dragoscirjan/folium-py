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

from folium.crud import Delete as CrudDelete, DeleteQuery as CrudDeleteQuery


class Delete(CrudDelete):
    """
    Interface for implementing REST Delete method.
    :see https://en.wikipedia.org/wiki/Representational_state_transfer
    """

class DeleteQuery(CrudDeleteQuery):
    """
    Interface for implementing REST Delete method.
    :see https://en.wikipedia.org/wiki/Representational_state_transfer
    """
