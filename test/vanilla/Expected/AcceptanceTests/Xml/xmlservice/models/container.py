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


class Container(Model):
    """An Azure Storage container.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param properties: Required.
    :type properties: ~xmlservice.models.ContainerProperties
    :param metadata:
    :type metadata: dict[str, str]
    """

    _validation = {
        'name': {'required': True},
        'properties': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'properties': {'key': 'Properties', 'type': 'ContainerProperties'},
        'metadata': {'key': 'Metadata', 'type': '{str}'},
    }
    _xml_map = {
        'name': 'Container'
    }
    _xml_attribute_map = {
        'name': {'name': 'Name'},
        'properties': {'name': 'Properties'},
        'metadata': {'name': 'Metadata'},
    }

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.metadata = kwargs.get('metadata', None)