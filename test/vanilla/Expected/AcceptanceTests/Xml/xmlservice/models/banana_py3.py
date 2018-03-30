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


class Banana(Model):
    """A banana.

    :param name:
    :type name: str
    :param flavor:
    :type flavor: str
    :param expiration: The time at which you should reconsider eating this
     banana
    :type expiration: datetime
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'flavor': {'key': 'flavor', 'type': 'str'},
        'expiration': {'key': 'expiration', 'type': 'iso-8601'},
    }

    def __init__(self, *, name: str=None, flavor: str=None, expiration=None, **kwargs) -> None:
        super(Banana, self).__init__(**kwargs)
        self.name = name
        self.flavor = flavor
        self.expiration = expiration
