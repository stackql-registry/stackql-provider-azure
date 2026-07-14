--- 
title: jwt_authenticators
hide_title: false
hide_table_of_contents: false
keywords:
  - jwt_authenticators
  - container_service
  - azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure resources using SQL
custom_edit_url: null
image: /img/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>jwt_authenticators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="jwt_authenticators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_service.jwt_authenticators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_cluster', value: 'list_by_managed_cluster' }
    ]}
>
<TabItem value="get">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="claimMappings" /></td>
    <td><code>object</code></td>
    <td>The mappings that define how user attributes are extracted from the token claims. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="claimValidationRules" /></td>
    <td><code>array</code></td>
    <td>The rules that are applied to validate token claims to authenticate users. All the expressions must evaluate to true for validation to succeed.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>object</code></td>
    <td>The JWT OIDC issuer details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the JWT authenticator. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userValidationRules" /></td>
    <td><code>array</code></td>
    <td>The rules that are applied to the mapped user before completing authentication. All the expressions must evaluate to true for validation to succeed.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_managed_cluster">

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="claimMappings" /></td>
    <td><code>object</code></td>
    <td>The mappings that define how user attributes are extracted from the token claims. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="claimValidationRules" /></td>
    <td><code>array</code></td>
    <td>The rules that are applied to validate token claims to authenticate users. All the expressions must evaluate to true for validation to succeed.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>object</code></td>
    <td>The JWT OIDC issuer details. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The current provisioning state of the JWT authenticator. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userValidationRules" /></td>
    <td><code>array</code></td>
    <td>The rules that are applied to the mapped user before completing authentication. All the expressions must evaluate to true for validation to succeed.</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-jwt_authenticator_name"><code>jwt_authenticator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified JWT authenticator of a managed cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_managed_cluster"><CopyableCode code="list_by_managed_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of JWT authenticators in the specified managed cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-jwt_authenticator_name"><code>jwt_authenticator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates JWT authenticator in the managed cluster and updates the managed cluster to apply the settings.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-jwt_authenticator_name"><code>jwt_authenticator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates JWT authenticator in the managed cluster and updates the managed cluster to apply the settings.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-jwt_authenticator_name"><code>jwt_authenticator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a JWT authenticator and updates the managed cluster to apply the settings.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-jwt_authenticator_name">
    <td><CopyableCode code="jwt_authenticator_name" /></td>
    <td><code>string</code></td>
    <td>The name of the JWT authenticator. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed cluster resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_managed_cluster', value: 'list_by_managed_cluster' }
    ]}
>
<TabItem value="get">

Gets the specified JWT authenticator of a managed cluster.

```sql
SELECT
id,
name,
claimMappings,
claimValidationRules,
issuer,
provisioningState,
systemData,
type,
userValidationRules
FROM azure.container_service.jwt_authenticators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND jwt_authenticator_name = '{{ jwt_authenticator_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_managed_cluster">

Gets a list of JWT authenticators in the specified managed cluster.

```sql
SELECT
id,
name,
claimMappings,
claimValidationRules,
issuer,
provisioningState,
systemData,
type,
userValidationRules
FROM azure.container_service.jwt_authenticators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates JWT authenticator in the managed cluster and updates the managed cluster to apply the settings.

```sql
INSERT INTO azure.container_service.jwt_authenticators (
properties,
resource_group_name,
resource_name,
jwt_authenticator_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ jwt_authenticator_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: jwt_authenticators
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the jwt_authenticators resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the jwt_authenticators resource.
    - name: jwt_authenticator_name
      value: "{{ jwt_authenticator_name }}"
      description: Required parameter for the jwt_authenticators resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the jwt_authenticators resource.
    - name: properties
      description: |
        The properties of JWTAuthenticator. For details on how to configure the properties of a JWT authenticator, please refer to the Kubernetes documentation: \`https://kubernetes.io/docs/reference/access-authn-authz/authentication/#using-authentication-configuration \`_. Please note that not all fields available in the Kubernetes documentation are supported by AKS. For troubleshooting, please see \`https://aka.ms/aks-external-issuers-docs \`_. Required.
      value:
        provisioningState: "{{ provisioningState }}"
        issuer:
          url: "{{ url }}"
          audiences:
            - "{{ audiences }}"
        claimValidationRules:
          - expression: "{{ expression }}"
            message: "{{ message }}"
        claimMappings:
          username:
            expression: "{{ expression }}"
          groups:
            expression: "{{ expression }}"
          uid:
            expression: "{{ expression }}"
          extra:
            - key: "{{ key }}"
              valueExpression: "{{ valueExpression }}"
        userValidationRules:
          - expression: "{{ expression }}"
            message: "{{ message }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates JWT authenticator in the managed cluster and updates the managed cluster to apply the settings.

```sql
REPLACE azure.container_service.jwt_authenticators
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND jwt_authenticator_name = '{{ jwt_authenticator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a JWT authenticator and updates the managed cluster to apply the settings.

```sql
DELETE FROM azure.container_service.jwt_authenticators
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND jwt_authenticator_name = '{{ jwt_authenticator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
