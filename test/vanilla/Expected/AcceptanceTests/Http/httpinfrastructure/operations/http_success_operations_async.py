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
from .http_success_operations import HttpSuccessOperations as _HttpSuccessOperations


class HttpSuccessOperations(_HttpSuccessOperations):
    """HttpSuccessOperations operations."""

    async def head200_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Return 200 status code if successful.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head200_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.head(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    head200_async.metadata = {'url': '/http/success/200'}

    async def get200_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get 200 success.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or ClientRawResponse if raw=true
        :rtype: bool or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get200_async.metadata['url']

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

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get200_async.metadata = {'url': '/http/success/200'}

    async def put200_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Put boolean value true returning 200 success.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put200_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
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
    put200_async.metadata = {'url': '/http/success/200'}

    async def patch200_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Patch true Boolean value in request returning 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch200_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    patch200_async.metadata = {'url': '/http/success/200'}

    async def post200_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Post bollean value true in request that returns a 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post200_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post200_async.metadata = {'url': '/http/success/200'}

    async def delete200_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Delete simple boolean value true returns 200.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete200_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete200_async.metadata = {'url': '/http/success/200'}

    async def put201_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Put true Boolean value in request returns 201.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put201_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put201_async.metadata = {'url': '/http/success/201'}

    async def post201_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Post true Boolean value in request returns 201 (Created).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post201_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [201]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post201_async.metadata = {'url': '/http/success/201'}

    async def put202_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Put true Boolean value in request returns 202 (Accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put202_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put202_async.metadata = {'url': '/http/success/202'}

    async def patch202_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Patch true Boolean value in request returns 202.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch202_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    patch202_async.metadata = {'url': '/http/success/202'}

    async def post202_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Post true Boolean value in request returns 202 (Accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post202_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post202_async.metadata = {'url': '/http/success/202'}

    async def delete202_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Delete true Boolean value in request returns 202 (accepted).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete202_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [202]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete202_async.metadata = {'url': '/http/success/202'}

    async def head204_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Return 204 status code if successful.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head204_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.head(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    head204_async.metadata = {'url': '/http/success/204'}

    async def put204_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Put true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put204_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put204_async.metadata = {'url': '/http/success/204'}

    async def patch204_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Patch true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch204_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    patch204_async.metadata = {'url': '/http/success/204'}

    async def post204_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Post true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post204_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    post204_async.metadata = {'url': '/http/success/204'}

    async def delete204_async(
            self, boolean_value=None, *, custom_headers=None, raw=False, **operation_config):
        """Delete true Boolean value in request returns 204 (no content).

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete204_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = await self._client.async_send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete204_async.metadata = {'url': '/http/success/204'}

    async def head404_async(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Return 404 status code.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head404_async.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.head(url, query_parameters)
        response = await self._client.async_send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204, 404]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    head404_async.metadata = {'url': '/http/success/404'}
