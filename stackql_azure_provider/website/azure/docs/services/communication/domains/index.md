--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - communication
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_email_service_resource', value: 'list_by_email_service_resource' }
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
    <td><CopyableCode code="dataLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the Domains resource data is stored at rest.</td>
</tr>
<tr>
    <td><CopyableCode code="domainManagement" /></td>
    <td><code>string</code></td>
    <td>Describes how a Domains resource is being managed. Required. Known values are: "AzureManaged", "CustomerManaged", and "CustomerManagedInExchangeOnline". (AzureManaged, CustomerManaged, CustomerManagedInExchangeOnline)</td>
</tr>
<tr>
    <td><CopyableCode code="fromSenderDomain" /></td>
    <td><code>string</code></td>
    <td>P2 sender domain that is displayed to the email recipients [RFC 5322].</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mailFromSenderDomain" /></td>
    <td><code>string</code></td>
    <td>P1 sender domain that is present on the email envelope [RFC 5321].</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving". (Unknown, Succeeded, Failed, Canceled, Running, Creating, Updating, Deleting, Moving)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userEngagementTracking" /></td>
    <td><code>string</code></td>
    <td>Describes whether user engagement tracking is enabled or disabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="verificationRecords" /></td>
    <td><code>object</code></td>
    <td>List of DnsRecord.</td>
</tr>
<tr>
    <td><CopyableCode code="verificationStates" /></td>
    <td><code>object</code></td>
    <td>List of VerificationStatusRecord.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_email_service_resource">

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
    <td><CopyableCode code="dataLocation" /></td>
    <td><code>string</code></td>
    <td>The location where the Domains resource data is stored at rest.</td>
</tr>
<tr>
    <td><CopyableCode code="domainManagement" /></td>
    <td><code>string</code></td>
    <td>Describes how a Domains resource is being managed. Required. Known values are: "AzureManaged", "CustomerManaged", and "CustomerManagedInExchangeOnline". (AzureManaged, CustomerManaged, CustomerManagedInExchangeOnline)</td>
</tr>
<tr>
    <td><CopyableCode code="fromSenderDomain" /></td>
    <td><code>string</code></td>
    <td>P2 sender domain that is displayed to the email recipients [RFC 5322].</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mailFromSenderDomain" /></td>
    <td><code>string</code></td>
    <td>P1 sender domain that is present on the email envelope [RFC 5321].</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Running", "Creating", "Updating", "Deleting", and "Moving". (Unknown, Succeeded, Failed, Canceled, Running, Creating, Updating, Deleting, Moving)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userEngagementTracking" /></td>
    <td><code>string</code></td>
    <td>Describes whether user engagement tracking is enabled or disabled. Known values are: "Disabled" and "Enabled". (Disabled, Enabled)</td>
</tr>
<tr>
    <td><CopyableCode code="verificationRecords" /></td>
    <td><code>object</code></td>
    <td>List of DnsRecord.</td>
</tr>
<tr>
    <td><CopyableCode code="verificationStates" /></td>
    <td><code>object</code></td>
    <td>List of VerificationStatusRecord.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get. Get the Domains resource and its properties.</td>
</tr>
<tr>
    <td><a href="#list_by_email_service_resource"><CopyableCode code="list_by_email_service_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List by EmailService. Handles requests to list all Domains resources under the parent EmailServices resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create Or Update. Add a new Domains resource under the parent EmailService resource or update an existing Domains resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update. Operation to update an existing Domains resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create Or Update. Add a new Domains resource under the parent EmailService resource or update an existing Domains resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete. Operation to delete a Domains resource.</td>
</tr>
<tr>
    <td><a href="#initiate_verification"><CopyableCode code="initiate_verification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-verificationType"><code>verificationType</code></a></td>
    <td></td>
    <td>Initiate Verification. Initiate verification of DNS record.</td>
</tr>
<tr>
    <td><a href="#cancel_verification"><CopyableCode code="cancel_verification" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-email_service_name"><code>email_service_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-verificationType"><code>verificationType</code></a></td>
    <td></td>
    <td>Cancel Verification. Cancel verification of DNS record.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Domains resource. Required.</td>
</tr>
<tr id="parameter-email_service_name">
    <td><CopyableCode code="email_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the EmailService resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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
        { label: 'list_by_email_service_resource', value: 'list_by_email_service_resource' }
    ]}
>
<TabItem value="get">

Get. Get the Domains resource and its properties.

```sql
SELECT
id,
name,
dataLocation,
domainManagement,
fromSenderDomain,
location,
mailFromSenderDomain,
provisioningState,
systemData,
tags,
type,
userEngagementTracking,
verificationRecords,
verificationStates
FROM azure.communication.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND email_service_name = '{{ email_service_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_email_service_resource">

List by EmailService. Handles requests to list all Domains resources under the parent EmailServices resource.

```sql
SELECT
id,
name,
dataLocation,
domainManagement,
fromSenderDomain,
location,
mailFromSenderDomain,
provisioningState,
systemData,
tags,
type,
userEngagementTracking,
verificationRecords,
verificationStates
FROM azure.communication.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND email_service_name = '{{ email_service_name }}' -- required
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

Create Or Update. Add a new Domains resource under the parent EmailService resource or update an existing Domains resource.

```sql
INSERT INTO azure.communication.domains (
tags,
location,
properties,
resource_group_name,
email_service_name,
domain_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ email_service_name }}',
'{{ domain_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the domains resource.
    - name: email_service_name
      value: "{{ email_service_name }}"
      description: Required parameter for the domains resource.
    - name: domain_name
      value: "{{ domain_name }}"
      description: Required parameter for the domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the domains resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The properties of a Domains resource.
      value:
        provisioningState: "{{ provisioningState }}"
        dataLocation: "{{ dataLocation }}"
        fromSenderDomain: "{{ fromSenderDomain }}"
        mailFromSenderDomain: "{{ mailFromSenderDomain }}"
        domainManagement: "{{ domainManagement }}"
        verificationStates:
          Domain:
            status: "{{ status }}"
            errorCode: "{{ errorCode }}"
          SPF:
            status: "{{ status }}"
            errorCode: "{{ errorCode }}"
          DKIM:
            status: "{{ status }}"
            errorCode: "{{ errorCode }}"
          DKIM2:
            status: "{{ status }}"
            errorCode: "{{ errorCode }}"
          DMARC:
            status: "{{ status }}"
            errorCode: "{{ errorCode }}"
        verificationRecords:
          Domain:
            type: "{{ type }}"
            name: "{{ name }}"
            value: "{{ value }}"
            ttl: {{ ttl }}
          SPF:
            type: "{{ type }}"
            name: "{{ name }}"
            value: "{{ value }}"
            ttl: {{ ttl }}
          DKIM:
            type: "{{ type }}"
            name: "{{ name }}"
            value: "{{ value }}"
            ttl: {{ ttl }}
          DKIM2:
            type: "{{ type }}"
            name: "{{ name }}"
            value: "{{ value }}"
            ttl: {{ ttl }}
          DMARC:
            type: "{{ type }}"
            name: "{{ name }}"
            value: "{{ value }}"
            ttl: {{ ttl }}
        userEngagementTracking: "{{ userEngagementTracking }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update. Operation to update an existing Domains resource.

```sql
UPDATE azure.communication.domains
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND email_service_name = '{{ email_service_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type;
```
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

Create Or Update. Add a new Domains resource under the parent EmailService resource or update an existing Domains resource.

```sql
REPLACE azure.communication.domains
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND email_service_name = '{{ email_service_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Delete. Operation to delete a Domains resource.

```sql
DELETE FROM azure.communication.domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND email_service_name = '{{ email_service_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="initiate_verification"
    values={[
        { label: 'initiate_verification', value: 'initiate_verification' },
        { label: 'cancel_verification', value: 'cancel_verification' }
    ]}
>
<TabItem value="initiate_verification">

Initiate Verification. Initiate verification of DNS record.

```sql
EXEC azure.communication.domains.initiate_verification 
@resource_group_name='{{ resource_group_name }}' --required, 
@email_service_name='{{ email_service_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"verificationType": "{{ verificationType }}"
}'
;
```
</TabItem>
<TabItem value="cancel_verification">

Cancel Verification. Cancel verification of DNS record.

```sql
EXEC azure.communication.domains.cancel_verification 
@resource_group_name='{{ resource_group_name }}' --required, 
@email_service_name='{{ email_service_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"verificationType": "{{ verificationType }}"
}'
;
```
</TabItem>
</Tabs>
