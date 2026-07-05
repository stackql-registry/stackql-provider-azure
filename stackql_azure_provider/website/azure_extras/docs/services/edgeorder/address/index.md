--- 
title: address
hide_title: false
hide_table_of_contents: false
keywords:
  - address
  - edgeorder
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>address</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="address" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.edgeorder.address" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_address_by_name"
    values={[
        { label: 'get_address_by_name', value: 'get_address_by_name' }
    ]}
>
<TabItem value="get_address_by_name">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressValidationStatus" /></td>
    <td><code>string</code></td>
    <td>Status of address validation. Known values are: "Valid", "Invalid", and "Ambiguous".</td>
</tr>
<tr>
    <td><CopyableCode code="contactDetails" /></td>
    <td><code>object</code></td>
    <td>Contact details for the address. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="shippingAddress" /></td>
    <td><code>object</code></td>
    <td>Shipping details for the address.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Represents resource creation and update time.</td>
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
    <td><a href="#get_address_by_name"><CopyableCode code="get_address_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-address_name"><code>address_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified address.</td>
</tr>
<tr>
    <td><a href="#create_address"><CopyableCode code="create_address" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-address_name"><code>address_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new address with the specified parameters. Existing address can be updated with this API.</td>
</tr>
<tr>
    <td><a href="#update_address"><CopyableCode code="update_address" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-address_name"><code>address_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Updates the properties of an existing address.</td>
</tr>
<tr>
    <td><a href="#delete_address_by_name"><CopyableCode code="delete_address_by_name" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-address_name"><code>address_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an address.</td>
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
<tr id="parameter-address_name">
    <td><CopyableCode code="address_name" /></td>
    <td><code>string</code></td>
    <td>The name of the address Resource within the specified resource group. address names must be between 3 and 24 characters in length and use any alphanumeric and underscore only. Required.</td>
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
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>Defines the If-Match condition. The patch will be performed only if the ETag of the job on the server matches this value. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_address_by_name"
    values={[
        { label: 'get_address_by_name', value: 'get_address_by_name' }
    ]}
>
<TabItem value="get_address_by_name">

Gets information about the specified address.

```sql
SELECT
id,
name,
addressValidationStatus,
contactDetails,
location,
shippingAddress,
systemData,
tags,
type
FROM azure_extras.edgeorder.address
WHERE address_name = '{{ address_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_address"
    values={[
        { label: 'create_address', value: 'create_address' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_address">

Creates a new address with the specified parameters. Existing address can be updated with this API.

```sql
INSERT INTO azure_extras.edgeorder.address (
tags,
location,
properties,
address_name,
resource_group_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ address_name }}',
'{{ resource_group_name }}',
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
- name: address
  props:
    - name: address_name
      value: "{{ address_name }}"
      description: Required parameter for the address resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the address resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the address resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      value:
        shippingAddress:
          streetAddress1: "{{ streetAddress1 }}"
          streetAddress2: "{{ streetAddress2 }}"
          streetAddress3: "{{ streetAddress3 }}"
          city: "{{ city }}"
          stateOrProvince: "{{ stateOrProvince }}"
          country: "{{ country }}"
          postalCode: "{{ postalCode }}"
          zipExtendedCode: "{{ zipExtendedCode }}"
          companyName: "{{ companyName }}"
          addressType: "{{ addressType }}"
        contactDetails:
          contactName: "{{ contactName }}"
          phone: "{{ phone }}"
          phoneExtension: "{{ phoneExtension }}"
          mobile: "{{ mobile }}"
          emailList:
            - "{{ emailList }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_address"
    values={[
        { label: 'update_address', value: 'update_address' }
    ]}
>
<TabItem value="update_address">

Updates the properties of an existing address.

```sql
UPDATE azure_extras.edgeorder.address
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
address_name = '{{ address_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND If-Match = '{{ If-Match}}'
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
    defaultValue="delete_address_by_name"
    values={[
        { label: 'delete_address_by_name', value: 'delete_address_by_name' }
    ]}
>
<TabItem value="delete_address_by_name">

Deletes an address.

```sql
DELETE FROM azure_extras.edgeorder.address
WHERE address_name = '{{ address_name }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
