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

from msrest.pipeline import ClientRawResponse

from .. import models
from .implicit_operations import ImplicitOperations as _ImplicitOperations


class ImplicitOperations(_ImplicitOperations):
    """ImplicitOperations operations."""

    async def get_required_path_async(
            self, path_parameter, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required path parameter.

        :param path_parameter:
        :type path_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_path_async.metadata['url']
        path_format_arguments = {
            'pathParameter': self._serialize.url("path_parameter", path_parameter, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_path_async.metadata = {'url': '/reqopt/implicit/required/path/{pathParameter}'}

    async def put_optional_query_async(
            self, query_parameter=None, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional query parameter.

        :param query_parameter:
        :type query_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_query_async.metadata['url']

        # Construct parameters
        query_parameters = {}
        if query_parameter is not None:
            query_parameters['queryParameter'] = self._serialize.query("query_parameter", query_parameter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_query_async.metadata = {'url': '/reqopt/implicit/optional/query'}

    async def put_optional_header_async(
            self, query_parameter=None, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional header parameter.

        :param query_parameter:
        :type query_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_header_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if query_parameter is not None:
            header_parameters['queryParameter'] = self._serialize.header("query_parameter", query_parameter, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_header_async.metadata = {'url': '/reqopt/implicit/optional/header'}

    async def put_optional_body_async(
            self, body_parameter=None, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional body parameter.

        :param body_parameter:
        :type body_parameter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.put_optional_body_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_optional_body_async.metadata = {'url': '/reqopt/implicit/optional/body'}

    async def get_required_global_path_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required path parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_path_async.metadata['url']
        path_format_arguments = {
            'required-global-path': self._serialize.url("self.config.required_global_path", self.config.required_global_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_global_path_async.metadata = {'url': '/reqopt/global/required/path/{required-global-path}'}

    async def get_required_global_query_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly required query parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_required_global_query_async.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['required-global-query'] = self._serialize.query("self.config.required_global_query", self.config.required_global_query, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_required_global_query_async.metadata = {'url': '/reqopt/global/required/query'}

    async def get_optional_global_query_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Test implicitly optional query parameter.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Error or ClientRawResponse if raw=true
        :rtype: ~requiredoptional.models.Error or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<requiredoptional.models.ErrorException>`
        """
        # Construct URL
        url = self.get_optional_global_query_async.metadata['url']

        # Construct parameters
        query_parameters = {}
        if self.config.optional_global_query is not None:
            query_parameters['optional-global-query'] = self._serialize.query("self.config.optional_global_query", self.config.optional_global_query, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code < 200 or response.status_code >= 300:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    get_optional_global_query_async.metadata = {'url': '/reqopt/global/optional/query'}
