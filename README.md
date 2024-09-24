## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
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
    except ApiException as e:
        print("Exception when calling PublicApiApi->api_public_v2_collaborationhub_auth_token_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.collaboard.app/public*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PublicApiApi* | [**api_public_v2_collaborationhub_auth_token_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_auth_token_get) | **GET** /api/public/v2/collaborationhub/auth/token | Returns a user authorization token that can be used to make authenticated requests to the API.  This method uses the ApiKey provided in the Authorization header in the form Bearer {api-key}
*PublicApiApi* | [**api_public_v2_collaborationhub_auth_userinfo_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_auth_userinfo_get) | **GET** /api/public/v2/collaborationhub/auth/userinfo | Returns the current user details.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_owned_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_owned_get) | **GET** /api/public/v2/collaborationhub/projects/owned | Returns a paged list of all projects owned by the calling user.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_participating_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_participating_get) | **GET** /api/public/v2/collaborationhub/projects/participating | Returns a paged list of the project that the user participates in.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_post) | **POST** /api/public/v2/collaborationhub/projects | Creates a new project
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_copy_operation_id_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/copy/{operation_id} | Returns the status of the project copy operation
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_copy_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_copy_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/copy | Copies the project with the given ID as a new project.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_delete**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id} | Deletes the project with the given ID.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_files_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_files_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/files | Uploads a file on the server and creates the corresponding file tile.  This method will also trigger the image thumbnail generation, if applicable for the file type
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id} | Returns a project
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_invitationlink_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_invitationlink_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/invitationlink | Creates a link that can be used to invite a user to a project.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_patch**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_patch) | **PATCH** /api/public/v2/collaborationhub/projects/{project_id} | Updates the project with the given ID.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_tiles_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/tiles | Returns a paged list of the tiles of the given project.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_tiles_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/tiles | Creates a new tile.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_tiles_tile_id_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id}/tiles/{tile_id} | Deletes a tile.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_users_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_get) | **GET** /api/public/v2/collaborationhub/projects/{project_id}/users | Returns a list of all users participating in the given project.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_users_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_post) | **POST** /api/public/v2/collaborationhub/projects/{project_id}/users | Adds a participant to a project.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_users_put**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_put) | **PUT** /api/public/v2/collaborationhub/projects/{project_id}/users | Updates a project participant.
*PublicApiApi* | [**api_public_v2_collaborationhub_projects_project_id_users_username_delete**](docs/PublicApiApi.md#api_public_v2_collaborationhub_projects_project_id_users_username_delete) | **DELETE** /api/public/v2/collaborationhub/projects/{project_id}/users/{username} | Removes a participant from a project
*PublicApiApi* | [**api_public_v2_collaborationhub_subscriptions_license_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_license_get) | **GET** /api/public/v2/collaborationhub/subscriptions/license | Returns the current licensing information for the calling user.
*PublicApiApi* | [**api_public_v2_collaborationhub_subscriptions_subscription_id_users_get**](docs/PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_get) | **GET** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users | Removes a user from the given subscription.
*PublicApiApi* | [**api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_invite_post) | **POST** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users/invite | Invites a user to the given subscription. This method will send an invitation email to the user, which the user can either accept or reject.
*PublicApiApi* | [**api_public_v2_collaborationhub_subscriptions_subscription_id_users_post**](docs/PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_post) | **POST** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users | Adds a user to the given subscription.
*PublicApiApi* | [**api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete**](docs/PublicApiApi.md#api_public_v2_collaborationhub_subscriptions_subscription_id_users_username_delete) | **DELETE** /api/public/v2/collaborationhub/subscriptions/{subscription_id}/users/{username} | Removes a user from the given subscription.


## Documentation For Models

 - [ApiPublicV2CollaborationhubProjectsProjectIdFilesPostRequest](docs/ApiPublicV2CollaborationhubProjectsProjectIdFilesPostRequest.md)
 - [IBVCLServiceMetaEntitiesAuthenticatedUser](docs/IBVCLServiceMetaEntitiesAuthenticatedUser.md)
 - [IBVCLServiceMetaEntitiesAuthenticatedUserExt](docs/IBVCLServiceMetaEntitiesAuthenticatedUserExt.md)
 - [IBVCLServiceMetaEntitiesITileContent](docs/IBVCLServiceMetaEntitiesITileContent.md)
 - [IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum](docs/IBVCLServiceMetaEntitiesProjectParticipantPermissionEnum.md)
 - [IBVCLServiceMetaEntitiesProjectParticipationTypeEnum](docs/IBVCLServiceMetaEntitiesProjectParticipationTypeEnum.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20AddSubscriptionUserRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20CopyProjectRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectInvitationRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20CreateProjectRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20CreateTileRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserItem](docs/IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserItem.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20InviteSubscriptionUserRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectParticipantRequest.md)
 - [IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest](docs/IBVCLServiceMetaEntitiesRequestsPublicV20UpdateProjectRequest.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonCopyProjectCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonCreateProjectInvitationLinkCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonCreateTileCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetAuthTokenCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetLicenseInfoCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsItem](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetMyProjectsItem.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetParticipatingProjectsItem.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetProjectParticipantsItem.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetSubscriptionUsersItem.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetTilesByProjectIdCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonGetUserInfoCallResult.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonProject](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonProject.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserPermissionEnum](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserPermissionEnum.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserStatusEnum](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonSubscriptionUserStatusEnum.md)
 - [IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult](docs/IBVCLServiceMetaEntitiesResponsesPublicCommonUploadFileCallResult.md)
 - [IBVCLServiceMetaEntitiesStateMachineStatus](docs/IBVCLServiceMetaEntitiesStateMachineStatus.md)
 - [IBVCLServiceMetaEntitiesTileBlobStatus](docs/IBVCLServiceMetaEntitiesTileBlobStatus.md)
 - [IBVCLServiceMetaEntitiesTilePinnedStateEnum](docs/IBVCLServiceMetaEntitiesTilePinnedStateEnum.md)
 - [IBVCLServiceMetaEntitiesTileStatus](docs/IBVCLServiceMetaEntitiesTileStatus.md)
 - [IBVCLServiceMetaEntitiesTileType](docs/IBVCLServiceMetaEntitiesTileType.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication (JWT)


## Author




