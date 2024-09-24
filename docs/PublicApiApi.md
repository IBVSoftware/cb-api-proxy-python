# openapi_client.PublicApiApi

All URIs are relative to *https://api.collaboard.app/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_public_v2_collaborationhub_auth_token_get**](PublicApiApi.md#api_public_v2_collaborationhub_auth_token_get) | **GET** /api/public/v2/collaborationhub/auth/token | Returns a user authorization token that can be used to make authenticated requests to the API.  This method uses the ApiKey provided in the Authorization header in the form Bearer {api-key}
[**api_public_v2_collaborationhub_auth_userinfo_get**](PublicApiApi.md#api_public_v2_collaborationhub_auth_userinfo_get) | **GET** /api/public/v2/collaborationhub/auth/userinfo | Returns the current user details.
[**api_public_v2_collaborationhub_projects_owned_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_owned_get) | **GET** /api/public/v2/collaborationhub/projects/owned | Returns a paged list of all projects owned by the calling user.
[**api_public_v2_collaborationhub_projects_participating_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_participating_get) | **GET** /api/public/v2/collaborationhub/projects/participating | Returns a paged list of the project that the user participates in.
[**api_public_v2_collaborationhub_projects_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_post) | **POST** /api/public/v2/collaborationhub/projects | Creates a new project
[**api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/copy/{operation_id} | Returns the status of the project copy operation
[**api_public_v2_collaborationhub_projects_project_id_copy_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_copy_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/copy | Copies the project with the given ID as a new project.
[**api_public_v2_collaborationhub_projects_project_id_delete**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id} | Deletes the project with the given ID.
[**api_public_v2_collaborationhub_projects_project_id_files_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_files_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/files | Uploads a file on the server and creates the corresponding file tile.  This method will also trigger the image thumbnail generation, if applicable for the file type
[**api_public_v2_collaborationhub_projects_project_id_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id} | Returns a project
[**api_public_v2_collaborationhub_projects_project_id_invitationlink_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_invitationlink_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/invitationlink | Creates a link that can be used to invite a user to a project.
[**api_public_v2_collaborationhub_projects_project_id_patch**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_patch) | **PATCH** /api/public/v2/collaborationhub/projects/{project_id} | Updates the project with the given ID.
[**api_public_v2_collaborationhub_projects_project_id_tiles_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/tiles | Returns a paged list of the tiles of the given project.
[**api_public_v2_collaborationhub_projects_project_id_tiles_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/tiles | Creates a new tile.
[**api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id}/tiles/{tile_id} | Deletes a tile.
[**api_public_v2_collaborationhub_projects_project_id_users_get**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/users | Returns a list of all users participating in the given project.
[**api_public_v2_collaborationhub_projects_project_id_users_post**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/users | Adds a participant to a project.
[**api_public_v2_collaborationhub_projects_project_id_users_put**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_put) | **PUT** /api/public/v2/collaborationhub/projects/{project_id}/users | Updates a project participant.
[**api_public_v2_collaborationhub_projects_project_id_users_username_delete**](PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_username_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id}/users/{username} | Removes a participant from a project
[**api_public_v2_collaborationhub_subscriptions_license_get**](PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_license_get) | **GET** /api/public/v2/collaborationhub/subscriptions/license | Returns the current licensing information for the calling user.
[**api_public_v2_collaborationhub_subscriptions_subscription_id_users_get**](PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_get) | **GET** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users | Removes a user from the given subscription.
[**api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post**](PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post) | **POST** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users/invite | Invites a user to the given subscription. This method will send an invitation email to the user, which the user can either accept or reject.
[**api_public_v2_collaborationhub_subscriptions_subscription_id_users_post**](PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_post) | **POST** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users | Adds a user to the given subscription.
[**api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete**](PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete) | **DELETE** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users/{username} | Removes a user from the given subscription.


# **api_public_v2_collaborationhub_auth_token_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult api_public_v2_collaborationhub_auth_token_get()

Returns a user authorization token that can be used to make authenticated requests to the API.  This method uses the ApiKey provided in the Authorization header in the form Bearer {api-key}

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_auth_token_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)

    try:
        # Returns a user authorization token that can be used to make authenticated requests to the API.  This method uses the ApiKey provided in the Authorization header in the form Bearer {api-key}
        api_response = api_instance.api_public_v2_collaborationhub_auth_token_get()
        print("The response of PublicApiApi->api_public_v2_collaborationhub_auth_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_auth_token_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_auth_userinfo_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult api_public_v2_collaborationhub_auth_userinfo_get()

Returns the current user details.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_user_info_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)

    try:
        # Returns the current user details.
        api_response = api_instance.api_public_v2_collaborationhub_auth_userinfo_get()
        print("The response of PublicApiApi->api_public_v2_collaborationhub_auth_userinfo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_auth_userinfo_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_owned_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult api_public_v2_collaborationhub_projects_owned_get(page_size=page_size, page_number=page_number)

Returns a paged list of all projects owned by the calling user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_my_projects_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    page_size = 56 # int | The page size (optional)
    page_number = 56 # int | The current page number (optional)

    try:
        # Returns a paged list of all projects owned by the calling user.
        api_response = api_instance.api_public_v2_collaborationhub_projects_owned_get(page_size=page_size, page_number=page_number)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_owned_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_owned_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The page size | [optional] 
 **page_number** | **int**| The current page number | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_participating_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult api_public_v2_collaborationhub_projects_participating_get(page_size=page_size, page_number=page_number)

Returns a paged list of the project that the user participates in.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_participating_projects_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    page_size = 56 # int | The page size (optional)
    page_number = 56 # int | The current page number (optional)

    try:
        # Returns a paged list of the project that the user participates in.
        api_response = api_instance.api_public_v2_collaborationhub_projects_participating_get(page_size=page_size, page_number=page_number)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_participating_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_participating_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The page size | [optional] 
 **page_number** | **int**| The current page number | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult api_public_v2_collaborationhub_projects_post(ibvcl_service_meta_entities_requests_public_v20_create_project_request=ibvcl_service_meta_entities_requests_public_v20_create_project_request)

Creates a new project

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_create_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    ibvcl_service_meta_entities_requests_public_v20_create_project_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest |  (optional)

    try:
        # Creates a new project
        api_response = api_instance.api_public_v2_collaborationhub_projects_post(ibvcl_service_meta_entities_requests_public_v20_create_project_request=ibvcl_service_meta_entities_requests_public_v20_create_project_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ibvcl_service_meta_entities_requests_public_v20_create_project_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get(project_id, operation_id)

Returns the status of the project copy operation

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_copy_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 
    operation_id = 56 # int | 

    try:
        # Returns the status of the project copy operation
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get(project_id, operation_id)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **operation_id** | **int**|  | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_copy_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult api_public_v2_collaborationhub_projects_project_id_copy_post(project_id, ibvcl_service_meta_entities_requests_public_v20_copy_project_request=ibvcl_service_meta_entities_requests_public_v20_copy_project_request)

Copies the project with the given ID as a new project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_copy_project_request import IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_copy_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 
    ibvcl_service_meta_entities_requests_public_v20_copy_project_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest |  (optional)

    try:
        # Copies the project with the given ID as a new project.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_copy_post(project_id, ibvcl_service_meta_entities_requests_public_v20_copy_project_request=ibvcl_service_meta_entities_requests_public_v20_copy_project_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_copy_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_copy_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **ibvcl_service_meta_entities_requests_public_v20_copy_project_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_delete**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_delete(project_id)

Deletes the project with the given ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 

    try:
        # Deletes the project with the given ID.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_delete(project_id)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_files_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult api_public_v2_collaborationhub_projects_project_id_files_post(project_id, form_file=form_file)

Uploads a file on the server and creates the corresponding file tile.  This method will also trigger the image thumbnail generation, if applicable for the file type

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_upload_file_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 
    form_file = None # bytearray |  (optional)

    try:
        # Uploads a file on the server and creates the corresponding file tile.  This method will also trigger the image thumbnail generation, if applicable for the file type
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_files_post(project_id, form_file=form_file)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **form_file** | **bytearray**|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult api_public_v2_collaborationhub_projects_project_id_get(project_id)

Returns a project

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_project_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 

    try:
        # Returns a project
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_get(project_id)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_invitationlink_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult api_public_v2_collaborationhub_projects_project_id_invitationlink_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request=ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request)

Creates a link that can be used to invite a user to a project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_create_project_invitation_link_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 
    ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest |  (optional)

    try:
        # Creates a link that can be used to invite a user to a project.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_invitationlink_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request=ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_invitationlink_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_invitationlink_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_patch**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_patch(project_id, ibvcl_service_meta_entities_requests_public_v20_update_project_request=ibvcl_service_meta_entities_requests_public_v20_update_project_request)

Updates the project with the given ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_update_project_request import IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | 
    ibvcl_service_meta_entities_requests_public_v20_update_project_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest |  (optional)

    try:
        # Updates the project with the given ID.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_patch(project_id, ibvcl_service_meta_entities_requests_public_v20_update_project_request=ibvcl_service_meta_entities_requests_public_v20_update_project_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | 
 **ibvcl_service_meta_entities_requests_public_v20_update_project_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_tiles_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult api_public_v2_collaborationhub_projects_project_id_tiles_get(project_id, page_size=page_size, page_number=page_number)

Returns a paged list of the tiles of the given project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_tiles_by_project_id_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    page_size = 56 # int | The page size (optional)
    page_number = 56 # int | The current page number (optional)

    try:
        # Returns a paged list of the tiles of the given project.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_tiles_get(project_id, page_size=page_size, page_number=page_number)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **page_size** | **int**| The page size | [optional] 
 **page_number** | **int**| The current page number | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_tiles_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult api_public_v2_collaborationhub_projects_project_id_tiles_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_tile_request=ibvcl_service_meta_entities_requests_public_v20_create_tile_request)

Creates a new tile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_tile_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_create_tile_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    ibvcl_service_meta_entities_requests_public_v20_create_tile_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest | The data of the tile to be created (optional)

    try:
        # Creates a new tile.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_tiles_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_tile_request=ibvcl_service_meta_entities_requests_public_v20_create_tile_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **ibvcl_service_meta_entities_requests_public_v20_create_tile_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest.md)| The data of the tile to be created | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete(project_id, tile_id)

Deletes a tile.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    tile_id = 'tile_id_example' # str | The tile ID

    try:
        # Deletes a tile.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete(project_id, tile_id)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **tile_id** | **str**| The tile ID | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_users_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult api_public_v2_collaborationhub_projects_project_id_users_get(project_id, page_size=page_size, page_number=page_number)

Returns a list of all users participating in the given project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_project_participants_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    page_size = 56 # int | The page size (optional)
    page_number = 56 # int | The current page number (optional)

    try:
        # Returns a list of all users participating in the given project.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_users_get(project_id, page_size=page_size, page_number=page_number)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **page_size** | **int**| The page size | [optional] 
 **page_number** | **int**| The current page number | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_users_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_users_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request=ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request)

Adds a participant to a project.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request import IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest |  (optional)

    try:
        # Adds a participant to a project.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_users_post(project_id, ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request=ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **ibvcl_service_meta_entities_requests_public_v20_create_project_invitation_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_users_put**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_users_put(project_id, ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request=ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request)

Updates a project participant.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request import IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest |  (optional)

    try:
        # Updates a project participant.
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_users_put(project_id, ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request=ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **ibvcl_service_meta_entities_requests_public_v20_update_project_participant_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_projects_project_id_users_username_delete**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_projects_project_id_users_username_delete(project_id, username)

Removes a participant from a project

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    project_id = 56 # int | The project ID
    username = 'username_example' # str | The participant's username

    try:
        # Removes a participant from a project
        api_response = api_instance.api_public_v2_collaborationhub_projects_project_id_users_username_delete(project_id, username)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_username_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_projects_project_id_users_username_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The project ID | 
 **username** | **str**| The participant&#39;s username | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_subscriptions_license_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult api_public_v2_collaborationhub_subscriptions_license_get()

Returns the current licensing information for the calling user.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_license_info_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)

    try:
        # Returns the current licensing information for the calling user.
        api_response = api_instance.api_public_v2_collaborationhub_subscriptions_license_get()
        print("The response of PublicApiApi->api_public_v2_collaborationhub_subscriptions_license_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_subscriptions_license_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_subscriptions_subscription_id_users_get**
> IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult api_public_v2_collaborationhub_subscriptions_subscription_id_users_get(subscription_id, page_size=page_size, page_number=page_number)

Removes a user from the given subscription.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_get_subscription_users_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    subscription_id = 56 # int | 
    page_size = 56 # int | The page size (optional)
    page_number = 56 # int | The current page number (optional)

    try:
        # Removes a user from the given subscription.
        api_response = api_instance.api_public_v2_collaborationhub_subscriptions_subscription_id_users_get(subscription_id, page_size=page_size, page_number=page_number)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **page_size** | **int**| The page size | [optional] 
 **page_number** | **int**| The current page number | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post(subscription_id, ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request=ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request)

Invites a user to the given subscription. This method will send an invitation email to the user, which the user can either accept or reject.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request import IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    subscription_id = 56 # int | 
    ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest |  (optional)

    try:
        # Invites a user to the given subscription. This method will send an invitation email to the user, which the user can either accept or reject.
        api_response = api_instance.api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post(subscription_id, ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request=ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **ibvcl_service_meta_entities_requests_public_v20_invite_subscription_user_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_subscriptions_subscription_id_users_post**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_subscriptions_subscription_id_users_post(subscription_id, ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request=ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request)

Adds a user to the given subscription.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request import IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    subscription_id = 56 # int | 
    ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request = openapi_client.IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest() # IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest |  (optional)

    try:
        # Adds a user to the given subscription.
        api_response = api_instance.api_public_v2_collaborationhub_subscriptions_subscription_id_users_post(subscription_id, ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request=ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**|  | 
 **ibvcl_service_meta_entities_requests_public_v20_add_subscription_user_request** | [**IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest**](IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest.md)|  | [optional] 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0, application/*+json; x-api-version=2.0
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete**
> IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete(subscription_id, username)

Removes a user from the given subscription.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import openapi_client
from openapi_client.models.ibvcl_service_meta_entities_responses_public_common_call_result import IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.collaboard.app/public
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.collaboard.app/public"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PublicApiApi(api_client)
    subscription_id = 56 # int | The subscription id
    username = 'username_example' # str | The username to remove

    try:
        # Removes a user from the given subscription.
        api_response = api_instance.api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete(subscription_id, username)
        print("The response of PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **int**| The subscription id | 
 **username** | **str**| The username to remove | 

### Return type

[**IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult**](IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain; x-api-version=2.0, application/json; x-api-version=2.0, text/json; x-api-version=2.0

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

