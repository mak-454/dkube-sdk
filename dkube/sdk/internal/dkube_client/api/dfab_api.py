# coding: utf-8

"""
    Dkube api server

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dkube_client.api_client import ApiClient


class DfabApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cluster_status(self, **kwargs):  # noqa: E501
        """API to fetch the status of various clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cluster_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.cluster_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def cluster_status_with_http_info(self, **kwargs):  # noqa: E501
        """API to fetch the status of various clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cluster_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/admin/cluster', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_create_one_or_update(self, data, **kwargs):  # noqa: E501
        """API to create a new group if not present and update group with pools and users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_create_one_or_update(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data12 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.groups_create_one_or_update_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.groups_create_one_or_update_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def groups_create_one_or_update_with_http_info(self, data, **kwargs):  # noqa: E501
        """API to create a new group if not present and update group with pools and users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_create_one_or_update_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data12 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_create_one_or_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `groups_create_one_or_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/groups/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_delete_list(self, data, **kwargs):  # noqa: E501
        """API to delete a list of groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_delete_list(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data13 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.groups_delete_list_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.groups_delete_list_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def groups_delete_list_with_http_info(self, data, **kwargs):  # noqa: E501
        """API to delete a list of groups  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_delete_list_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data13 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_delete_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `groups_delete_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/groups/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_get_collection_all(self, **kwargs):  # noqa: E501
        """API to get all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_collection_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.groups_get_collection_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.groups_get_collection_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def groups_get_collection_all_with_http_info(self, **kwargs):  # noqa: E501
        """API to get all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_collection_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_collection_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/groups/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def groups_get_collection_one(self, group, **kwargs):  # noqa: E501
        """API to get all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_collection_one(group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: (required)
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.groups_get_collection_one_with_http_info(group, **kwargs)  # noqa: E501
        else:
            (data) = self.groups_get_collection_one_with_http_info(group, **kwargs)  # noqa: E501
            return data

    def groups_get_collection_one_with_http_info(self, group, **kwargs):  # noqa: E501
        """API to get all the groups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.groups_get_collection_one_with_http_info(group, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str group: (required)
        :return: InlineResponse20029
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method groups_get_collection_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group' is set
        if ('group' not in params or
                params['group'] is None):
            raise ValueError("Missing the required parameter `group` when calling `groups_get_collection_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'group' in params:
            path_params['group'] = params['group']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/groups/{group}/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20029',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def nodes_get_all(self, **kwargs):  # noqa: E501
        """API to get collection of nodes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.nodes_get_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20032
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.nodes_get_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.nodes_get_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def nodes_get_all_with_http_info(self, **kwargs):  # noqa: E501
        """API to get collection of nodes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.nodes_get_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20032
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method nodes_get_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/nodes/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20032',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pools_create_one_or_update(self, data, **kwargs):  # noqa: E501
        """API to create a new pool if not present and update group with pools and users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_create_one_or_update(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data14 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pools_create_one_or_update_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.pools_create_one_or_update_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def pools_create_one_or_update_with_http_info(self, data, **kwargs):  # noqa: E501
        """API to create a new pool if not present and update group with pools and users.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_create_one_or_update_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data14 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pools_create_one_or_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `pools_create_one_or_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/pools/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pools_delete_list(self, data, **kwargs):  # noqa: E501
        """API to delete a list of pools  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_delete_list(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data15 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pools_delete_list_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.pools_delete_list_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def pools_delete_list_with_http_info(self, data, **kwargs):  # noqa: E501
        """API to delete a list of pools  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_delete_list_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data15 data: (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pools_delete_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `pools_delete_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/pools/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pools_get_collection_all(self, **kwargs):  # noqa: E501
        """API to get all the pools.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_get_collection_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pools_get_collection_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.pools_get_collection_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def pools_get_collection_all_with_http_info(self, **kwargs):  # noqa: E501
        """API to get all the pools.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_get_collection_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: InlineResponse20030
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pools_get_collection_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/pools/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20030',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pools_get_collection_one(self, pool, **kwargs):  # noqa: E501
        """API to get collection of single pool.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_get_collection_one(pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pool: (required)
        :return: InlineResponse20031
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pools_get_collection_one_with_http_info(pool, **kwargs)  # noqa: E501
        else:
            (data) = self.pools_get_collection_one_with_http_info(pool, **kwargs)  # noqa: E501
            return data

    def pools_get_collection_one_with_http_info(self, pool, **kwargs):  # noqa: E501
        """API to get collection of single pool.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pools_get_collection_one_with_http_info(pool, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pool: (required)
        :return: InlineResponse20031
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pool']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pools_get_collection_one" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pool' is set
        if ('pool' not in params or
                params['pool'] is None):
            raise ValueError("Missing the required parameter `pool` when calling `pools_get_collection_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pool' in params:
            path_params['pool'] = params['pool']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/keyauth.api.v1+json', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['d3apikey']  # noqa: E501

        return self.api_client.call_api(
            '/pools/{pool}/collection', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20031',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)