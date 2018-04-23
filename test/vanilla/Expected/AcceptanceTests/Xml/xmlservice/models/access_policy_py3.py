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


class AccessPolicy(Model):
    """An Access policy.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. the date-time the policy is active
    :type start: datetime
    :param expiry: Required. the date-time the policy expires
    :type expiry: datetime
    :param permission: Required. the permissions for the acl policy
    :type permission: str
    """

    _validation = {
        'start': {'required': True},
        'expiry': {'required': True},
        'permission': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'iso-8601'},
        'expiry': {'key': 'Expiry', 'type': 'iso-8601'},
        'permission': {'key': 'Permission', 'type': 'str'},
    }
    _xml_map = {
        'name': 'AccessPolicy'
    }
    _xml_attribute_map = {
        'start': {'name': 'Start'},
        'expiry': {'name': 'Expiry'},
        'permission': {'name': 'Permission'},
    }

    def __init__(self, *, start, expiry, permission: str, **kwargs) -> None:
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = start
        self.expiry = expiry
        self.permission = permission