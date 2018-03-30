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


class Slide(Model):
    """A slide in a slideshow.

    :param type:
    :type type: str
    :param title:
    :type title: str
    :param items:
    :type items: list[str]
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'items': {'key': 'items', 'type': '[str]'},
    }

    def __init__(self, *, type: str=None, title: str=None, items=None, **kwargs) -> None:
        super(Slide, self).__init__(**kwargs)
        self.type = type
        self.title = title
        self.items = items
