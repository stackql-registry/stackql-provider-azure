--- 
title: organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - organizations
  - elastic
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="organizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.organizations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#get_api_key"><CopyableCode code="get_api_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch the User API Key from the internal database, if it was generated and stored during the creation of the Elasticsearch Organization. Fetch the User API Key from the internal database, if it was generated and stored during the creation of the Elasticsearch Organization.</td>
</tr>
<tr>
    <td><a href="#get_elastic_to_azure_subscription_mapping"><CopyableCode code="get_elastic_to_azure_subscription_mapping" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve mapping details between the Elastic Organization and Azure Subscription for the logged-in user. Retrieve mapping details between the Elastic Organization and Azure Subscription for the logged-in user.</td>
</tr>
<tr>
    <td><a href="#resubscribe"><CopyableCode code="resubscribe" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resubscribe the Elasticsearch Organization. Resubscribe the Elasticsearch Organization.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
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

## Lifecycle Methods

<Tabs
    defaultValue="get_api_key"
    values={[
        { label: 'get_api_key', value: 'get_api_key' },
        { label: 'get_elastic_to_azure_subscription_mapping', value: 'get_elastic_to_azure_subscription_mapping' },
        { label: 'resubscribe', value: 'resubscribe' }
    ]}
>
<TabItem value="get_api_key">

Fetch the User API Key from the internal database, if it was generated and stored during the creation of the Elasticsearch Organization. Fetch the User API Key from the internal database, if it was generated and stored during the creation of the Elasticsearch Organization.

```sql
EXEC azure_isv.elastic.organizations.get_api_key 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"emailId": "{{ emailId }}"
}'
;
```
</TabItem>
<TabItem value="get_elastic_to_azure_subscription_mapping">

Retrieve mapping details between the Elastic Organization and Azure Subscription for the logged-in user. Retrieve mapping details between the Elastic Organization and Azure Subscription for the logged-in user.

```sql
EXEC azure_isv.elastic.organizations.get_elastic_to_azure_subscription_mapping 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resubscribe">

Resubscribe the Elasticsearch Organization. Resubscribe the Elasticsearch Organization.

```sql
EXEC azure_isv.elastic.organizations.resubscribe 
@resource_group_name='{{ resource_group_name }}' --required, 
@monitor_name='{{ monitor_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"planId": "{{ planId }}", 
"term": "{{ term }}", 
"subscriptionId": "{{ subscriptionId }}", 
"resourceGroup": "{{ resourceGroup }}", 
"organizationId": "{{ organizationId }}"
}'
;
```
</TabItem>
</Tabs>
