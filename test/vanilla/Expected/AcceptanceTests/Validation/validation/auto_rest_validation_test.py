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
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models


class AutoRestValidationTestConfiguration(Configuration):
    """Configuration for AutoRestValidationTest
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestValidationTestConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestvalidationtest/{}'.format(VERSION))

        self.subscription_id = subscription_id


class AutoRestValidationTest(SDKClient):
    """Test Infrastructure for AutoRest. No server backend exists for these tests.

    :ivar config: Configuration for client.
    :vartype config: AutoRestValidationTestConfiguration

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, base_url=None):

        self.config = AutoRestValidationTestConfiguration(subscription_id, base_url)
        super(AutoRestValidationTest, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def validation_of_method_parameters(
            self, resource_group_name, id, custom_headers=None, raw=False, **operation_config):
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars
         with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Product or ClientRawResponse if raw=true
        :rtype: ~validation.models.Product or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<validation.models.ErrorException>`
        """
        # Construct URL
        url = self.validation_of_method_parameters.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("self.api_version", self.api_version, 'str', pattern=r'\d{2}-\d{2}-\d{4}')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    validation_of_method_parameters.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    def validation_of_body(
            self, resource_group_name, id, body=None, custom_headers=None, raw=False, **operation_config):
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars
         with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: ~validation.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Product or ClientRawResponse if raw=true
        :rtype: ~validation.models.Product or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<validation.models.ErrorException>`
        """
        # Construct URL
        url = self.validation_of_body.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("self.api_version", self.api_version, 'str', pattern=r'\d{2}-\d{2}-\d{4}')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    validation_of_body.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    def get_with_constant_in_path(
            self, custom_headers=None, raw=False, **operation_config):
        """

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        constant_param = "constant"

        # Construct URL
        url = self.get_with_constant_in_path.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_with_constant_in_path.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}

    def post_with_constant_in_body(
            self, body=None, custom_headers=None, raw=False, **operation_config):
        """

        :param body:
        :type body: ~validation.models.Product
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Product or ClientRawResponse if raw=true
        :rtype: ~validation.models.Product or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        constant_param = "constant"

        # Construct URL
        url = self.post_with_constant_in_body.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    post_with_constant_in_body.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}
