# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.item import Item
from openapi_server.models.link import Link
from openapi_server import util

from openapi_server.models.item import Item  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501

class FeatureCollectionGeoJSON(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, features=None, links=None, time_stamp=None, number_matched=None, number_returned=None):  # noqa: E501
        """FeatureCollectionGeoJSON - a model defined in OpenAPI

        :param type: The type of this FeatureCollectionGeoJSON.  # noqa: E501
        :type type: str
        :param features: The features of this FeatureCollectionGeoJSON.  # noqa: E501
        :type features: List[Item]
        :param links: The links of this FeatureCollectionGeoJSON.  # noqa: E501
        :type links: List[Link]
        :param time_stamp: The time_stamp of this FeatureCollectionGeoJSON.  # noqa: E501
        :type time_stamp: datetime
        :param number_matched: The number_matched of this FeatureCollectionGeoJSON.  # noqa: E501
        :type number_matched: int
        :param number_returned: The number_returned of this FeatureCollectionGeoJSON.  # noqa: E501
        :type number_returned: int
        """
        self.openapi_types = {
            'type': str,
            'features': List[Item],
            'links': List[Link],
            'time_stamp': datetime,
            'number_matched': int,
            'number_returned': int
        }

        self.attribute_map = {
            'type': 'type',
            'features': 'features',
            'links': 'links',
            'time_stamp': 'timeStamp',
            'number_matched': 'numberMatched',
            'number_returned': 'numberReturned'
        }

        self._type = type
        self._features = features
        self._links = links
        self._time_stamp = time_stamp
        self._number_matched = number_matched
        self._number_returned = number_returned

    @classmethod
    def from_dict(cls, dikt) -> 'FeatureCollectionGeoJSON':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The featureCollectionGeoJSON of this FeatureCollectionGeoJSON.  # noqa: E501
        :rtype: FeatureCollectionGeoJSON
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this FeatureCollectionGeoJSON.


        :return: The type of this FeatureCollectionGeoJSON.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FeatureCollectionGeoJSON.


        :param type: The type of this FeatureCollectionGeoJSON.
        :type type: str
        """
        allowed_values = ["FeatureCollection"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def features(self):
        """Gets the features of this FeatureCollectionGeoJSON.


        :return: The features of this FeatureCollectionGeoJSON.
        :rtype: List[Item]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this FeatureCollectionGeoJSON.


        :param features: The features of this FeatureCollectionGeoJSON.
        :type features: List[Item]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def links(self):
        """Gets the links of this FeatureCollectionGeoJSON.


        :return: The links of this FeatureCollectionGeoJSON.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FeatureCollectionGeoJSON.


        :param links: The links of this FeatureCollectionGeoJSON.
        :type links: List[Link]
        """

        self._links = links

    @property
    def time_stamp(self):
        """Gets the time_stamp of this FeatureCollectionGeoJSON.

        This property indicates the time and date when the response was generated.  # noqa: E501

        :return: The time_stamp of this FeatureCollectionGeoJSON.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this FeatureCollectionGeoJSON.

        This property indicates the time and date when the response was generated.  # noqa: E501

        :param time_stamp: The time_stamp of this FeatureCollectionGeoJSON.
        :type time_stamp: datetime
        """

        self._time_stamp = time_stamp

    @property
    def number_matched(self):
        """Gets the number_matched of this FeatureCollectionGeoJSON.

        The number of features of the feature type that match the selection parameters like `bbox`.  # noqa: E501

        :return: The number_matched of this FeatureCollectionGeoJSON.
        :rtype: int
        """
        return self._number_matched

    @number_matched.setter
    def number_matched(self, number_matched):
        """Sets the number_matched of this FeatureCollectionGeoJSON.

        The number of features of the feature type that match the selection parameters like `bbox`.  # noqa: E501

        :param number_matched: The number_matched of this FeatureCollectionGeoJSON.
        :type number_matched: int
        """
        if number_matched is not None and number_matched < 0:  # noqa: E501
            raise ValueError("Invalid value for `number_matched`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_matched = number_matched

    @property
    def number_returned(self):
        """Gets the number_returned of this FeatureCollectionGeoJSON.

        The number of features in the feature collection.  A server may omit this information in a response, if the information about the number of features is not known or difficult to compute.  If the value is provided, the value shall be identical to the number of items in the \"features\" array.  # noqa: E501

        :return: The number_returned of this FeatureCollectionGeoJSON.
        :rtype: int
        """
        return self._number_returned

    @number_returned.setter
    def number_returned(self, number_returned):
        """Sets the number_returned of this FeatureCollectionGeoJSON.

        The number of features in the feature collection.  A server may omit this information in a response, if the information about the number of features is not known or difficult to compute.  If the value is provided, the value shall be identical to the number of items in the \"features\" array.  # noqa: E501

        :param number_returned: The number_returned of this FeatureCollectionGeoJSON.
        :type number_returned: int
        """
        if number_returned is not None and number_returned < 0:  # noqa: E501
            raise ValueError("Invalid value for `number_returned`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_returned = number_returned