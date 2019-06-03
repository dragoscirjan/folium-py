import abc
import json
import pprint
import typing

T = typing.TypeVar('T')

class ModelValidationError(Exception):
    """
    Exception thrown by data validation for Models
    """


class Model(object):
    """
    Model Interface
    """

    @abc.abstractmethod
    def __init__(self, data={}):
        """
        Constructor
        :param data: dict|str
        """
        pass

    @abc.abstractmethod
    @staticmethod
    def from_dict(data: dict, klass: typing.Type[T]) -> T:
        """
        Obtain Model from Dictionary
        :param data: dict
        :param klass: T
        :return: T
        """
        pass

    @abc.abstractmethod
    @staticmethod
    def from_json(data: str, klass: typing.Type[T]) -> T:
        """
        Obtain Model from JSON String
        :param data: str
        :param klass: T
        :return: T
        """
        pass

    @abc.abstractmethod
    def to_dict(self) -> dict:
        """
        Convert Model to Dictionary
        :return: dict
        """
        pass

    @abc.abstractmethod
    def to_json(self):
        """
        Convert Model to JSON String
        :return: str
        """
        pass

    @abc.abstractmethod
    def to_str(self):
        """
        Convert Model to 'pretty' String
        :return: str
        """
        pass


class BaseModel(Model):

    _attribute_types = {}
    """
    Key represents property name, while value represents the type of the property
    :type dict
    """

    def __init__(self, data={}):
        if type(data) == str:
            data = json.loads(data)
        self.validate()
        for key in self._attribute_types.keys():
            if hasattr(data, key):
                setattr(self, key, data.get(key, None))
        pass

    @staticmethod
    def from_dict(data: dict, klass: typing.Type[T]) -> T:
        """
        Obtain Model from Dictionary
        :param data: dict
        :param klass: T
        :return: T
        """
        return klass(data)

    @staticmethod
    def from_json(data: str, klass: typing.Type[T]) -> T:
        """
        Obtain Model from JSON String
        :param data: str
        :param klass: T
        :return: T
        """
        return klass.from_dict(json.loads(data))

    def to_dict(self) -> dict:
        """
        Convert Model to Dictionary
        Borrowed from [Swagger](https://swagger.io/) generated code. Wonder if it's not a bit too much.
        :return: dict
        """
        result = {}

        for attr in self._attribute_types.keys():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Convert Model to JSON String
        :return: str
        """
        return json.dumps(self.to_dict())

    def to_str(self):
        """
        Convert Model to a pretty String
        :return: str
        """
        return pprint.pformat(self.to_dict())

    @abc.abstractmethod
    def validate(self, data: dict = None) -> bool:
        """
        Validate data given to Model.
        :raises ModelValidationError
        :param data: dict
        :return: bool True if data is valid, False otherwise
        """
        pass

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
