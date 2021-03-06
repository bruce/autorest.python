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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.bool_model_operations import BoolModelOperations
from . import models


class AutoRestBoolTestServiceConfiguration(Configuration):
    """Configuration for AutoRestBoolTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestBoolTestServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestbooltestservice/{}'.format(VERSION))


class AutoRestBoolTestService(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestBoolTestServiceConfiguration

    :ivar bool_model: BoolModel operations
    :vartype bool_model: bodyboolean.operations.BoolModelOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestBoolTestServiceConfiguration(base_url)
        super(AutoRestBoolTestService, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.bool_model = BoolModelOperations(
            self._client, self.config, self._serialize, self._deserialize)
