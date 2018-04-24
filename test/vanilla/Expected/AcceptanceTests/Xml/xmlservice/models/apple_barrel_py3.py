# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AppleBarrel(Model):
    """A barrel of apples.

    :param good_apples:
    :type good_apples: list[str]
    :param bad_apples:
    :type bad_apples: list[str]
    """

    _attribute_map = {
        'good_apples': {'key': 'GoodApples', 'type': '[str]', 'xml': {'name': 'GoodApples', 'wrapped': True, 'wrappedName': 'Apple'}},
        'bad_apples': {'key': 'BadApples', 'type': '[str]', 'xml': {'name': 'BadApples', 'wrapped': True, 'wrappedName': 'Apple'}},
    }
    _xml_map = {
        'name': 'AppleBarrel'
    }

    def __init__(self, *, good_apples=None, bad_apples=None, **kwargs) -> None:
        super(AppleBarrel, self).__init__(**kwargs)
        self.good_apples = good_apples
        self.bad_apples = bad_apples
