--- 
title: web_application_firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - web_application_firewall_policies
  - network
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

Creates, updates, deletes, gets or lists a <code>web_application_firewall_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="web_application_firewall_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.web_application_firewall_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayForContainers" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway for containers.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGateways" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateways.</td>
</tr>
<tr>
    <td><CopyableCode code="customRules" /></td>
    <td><code>array</code></td>
    <td>The custom rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway http listeners.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedRules" /></td>
    <td><code>object</code></td>
    <td>Describes the managedRules structure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="pathBasedRules" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway path rules.</td>
</tr>
<tr>
    <td><CopyableCode code="policySettings" /></td>
    <td><code>object</code></td>
    <td>The PolicySettings for policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the web application firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the policy. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayForContainers" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway for containers.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGateways" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateways.</td>
</tr>
<tr>
    <td><CopyableCode code="customRules" /></td>
    <td><code>array</code></td>
    <td>The custom rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway http listeners.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedRules" /></td>
    <td><code>object</code></td>
    <td>Describes the managedRules structure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="pathBasedRules" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway path rules.</td>
</tr>
<tr>
    <td><CopyableCode code="policySettings" /></td>
    <td><code>object</code></td>
    <td>The PolicySettings for policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the web application firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the policy. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGatewayForContainers" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway for containers.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationGateways" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateways.</td>
</tr>
<tr>
    <td><CopyableCode code="customRules" /></td>
    <td><code>array</code></td>
    <td>The custom rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway http listeners.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="managedRules" /></td>
    <td><code>object</code></td>
    <td>Describes the managedRules structure. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="pathBasedRules" /></td>
    <td><code>array</code></td>
    <td>A collection of references to application gateway path rules.</td>
</tr>
<tr>
    <td><CopyableCode code="policySettings" /></td>
    <td><code>object</code></td>
    <td>The PolicySettings for policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the web application firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the policy. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve protection policy with specified name within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the protection policies within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the WAF policies in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or update policy with specified rule set name within a resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or update policy with specified rule set name within a resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes Policy.</td>
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
<tr id="parameter-policy_name">
    <td><CopyableCode code="policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the policy. Required.</td>
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
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Retrieve protection policy with specified name within a resource group.

```sql
SELECT
id,
name,
applicationGatewayForContainers,
applicationGateways,
customRules,
etag,
httpListeners,
location,
managedRules,
pathBasedRules,
policySettings,
provisioningState,
resourceState,
tags,
type
FROM azure.network.web_application_firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND policy_name = '{{ policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all of the protection policies within a resource group.

```sql
SELECT
id,
name,
applicationGatewayForContainers,
applicationGateways,
customRules,
etag,
httpListeners,
location,
managedRules,
pathBasedRules,
policySettings,
provisioningState,
resourceState,
tags,
type
FROM azure.network.web_application_firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the WAF policies in a subscription.

```sql
SELECT
id,
name,
applicationGatewayForContainers,
applicationGateways,
customRules,
etag,
httpListeners,
location,
managedRules,
pathBasedRules,
policySettings,
provisioningState,
resourceState,
tags,
type
FROM azure.network.web_application_firewall_policies
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or update policy with specified rule set name within a resource group.

```sql
INSERT INTO azure.network.web_application_firewall_policies (
id,
location,
tags,
properties,
resource_group_name,
policy_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: web_application_firewall_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the web_application_firewall_policies resource.
    - name: policy_name
      value: "{{ policy_name }}"
      description: Required parameter for the web_application_firewall_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the web_application_firewall_policies resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the web application firewall policy.
      value:
        policySettings:
          state: "{{ state }}"
          mode: "{{ mode }}"
          requestBodyCheck: {{ requestBodyCheck }}
          requestBodyInspectLimitInKB: {{ requestBodyInspectLimitInKB }}
          requestBodyEnforcement: {{ requestBodyEnforcement }}
          maxRequestBodySizeInKb: {{ maxRequestBodySizeInKb }}
          fileUploadEnforcement: {{ fileUploadEnforcement }}
          fileUploadLimitInMb: {{ fileUploadLimitInMb }}
          customBlockResponseStatusCode: {{ customBlockResponseStatusCode }}
          customBlockResponseBody: "{{ customBlockResponseBody }}"
          logScrubbing:
            state: "{{ state }}"
            scrubbingRules:
              - matchVariable: "{{ matchVariable }}"
                selectorMatchOperator: "{{ selectorMatchOperator }}"
                selector: "{{ selector }}"
                state: "{{ state }}"
          jsChallengeCookieExpirationInMins: {{ jsChallengeCookieExpirationInMins }}
          captchaExpirationInMins: {{ captchaExpirationInMins }}
        customRules:
          - name: "{{ name }}"
            etag: "{{ etag }}"
            priority: {{ priority }}
            state: "{{ state }}"
            rateLimitDuration: "{{ rateLimitDuration }}"
            rateLimitThreshold: {{ rateLimitThreshold }}
            ruleType: "{{ ruleType }}"
            matchConditions: "{{ matchConditions }}"
            groupByUserSession: "{{ groupByUserSession }}"
            action: "{{ action }}"
        applicationGateways:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            location: "{{ location }}"
            tags: "{{ tags }}"
            properties:
              sku:
                name: "{{ name }}"
                tier: "{{ tier }}"
                capacity: {{ capacity }}
                family: "{{ family }}"
              sslPolicy:
                disabledSslProtocols:
                  - "{{ disabledSslProtocols }}"
                policyType: "{{ policyType }}"
                policyName: "{{ policyName }}"
                cipherSuites:
                  - "{{ cipherSuites }}"
                minProtocolVersion: "{{ minProtocolVersion }}"
              operationalState: "{{ operationalState }}"
              gatewayIPConfigurations:
                - id: "{{ id }}"
                  properties:
                    subnet: "{{ subnet }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              authenticationCertificates:
                - id: "{{ id }}"
                  properties:
                    data: "{{ data }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              trustedRootCertificates:
                - id: "{{ id }}"
                  properties:
                    data: "{{ data }}"
                    keyVaultSecretId: "{{ keyVaultSecretId }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              trustedClientCertificates:
                - id: "{{ id }}"
                  properties:
                    data: "{{ data }}"
                    validatedCertData: "{{ validatedCertData }}"
                    clientCertIssuerDN: "{{ clientCertIssuerDN }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              sslCertificates:
                - id: "{{ id }}"
                  properties:
                    data: "{{ data }}"
                    password: "{{ password }}"
                    publicCertData: "{{ publicCertData }}"
                    keyVaultSecretId: "{{ keyVaultSecretId }}"
                    hsm: "{{ hsm }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              frontendIPConfigurations:
                - id: "{{ id }}"
                  properties:
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
                    publicIPAddress: "{{ publicIPAddress }}"
                    privateLinkConfiguration: "{{ privateLinkConfiguration }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              frontendPorts:
                - id: "{{ id }}"
                  properties:
                    port: {{ port }}
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              probes:
                - id: "{{ id }}"
                  properties:
                    protocol: "{{ protocol }}"
                    host: "{{ host }}"
                    path: "{{ path }}"
                    interval: {{ interval }}
                    timeout: {{ timeout }}
                    unhealthyThreshold: {{ unhealthyThreshold }}
                    pickHostNameFromBackendHttpSettings: {{ pickHostNameFromBackendHttpSettings }}
                    pickHostNameFromBackendSettings: {{ pickHostNameFromBackendSettings }}
                    minServers: {{ minServers }}
                    match: "{{ match }}"
                    enableProbeProxyProtocolHeader: {{ enableProbeProxyProtocolHeader }}
                    provisioningState: "{{ provisioningState }}"
                    port: {{ port }}
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              backendAddressPools:
                - id: "{{ id }}"
                  properties:
                    backendIPConfigurations: "{{ backendIPConfigurations }}"
                    backendAddresses: "{{ backendAddresses }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              backendHttpSettingsCollection:
                - id: "{{ id }}"
                  properties:
                    port: {{ port }}
                    protocol: "{{ protocol }}"
                    cookieBasedAffinity: "{{ cookieBasedAffinity }}"
                    requestTimeout: {{ requestTimeout }}
                    probe: "{{ probe }}"
                    authenticationCertificates: "{{ authenticationCertificates }}"
                    trustedRootCertificates: "{{ trustedRootCertificates }}"
                    connectionDraining: "{{ connectionDraining }}"
                    hostName: "{{ hostName }}"
                    pickHostNameFromBackendAddress: {{ pickHostNameFromBackendAddress }}
                    affinityCookieName: "{{ affinityCookieName }}"
                    probeEnabled: {{ probeEnabled }}
                    path: "{{ path }}"
                    dedicatedBackendConnection: {{ dedicatedBackendConnection }}
                    validateCertChainAndExpiry: {{ validateCertChainAndExpiry }}
                    validateSNI: {{ validateSNI }}
                    sniName: "{{ sniName }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              backendSettingsCollection:
                - id: "{{ id }}"
                  properties:
                    port: {{ port }}
                    protocol: "{{ protocol }}"
                    timeout: {{ timeout }}
                    probe: "{{ probe }}"
                    trustedRootCertificates: "{{ trustedRootCertificates }}"
                    hostName: "{{ hostName }}"
                    pickHostNameFromBackendAddress: {{ pickHostNameFromBackendAddress }}
                    enableL4ClientIpPreservation: {{ enableL4ClientIpPreservation }}
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              httpListeners:
                - id: "{{ id }}"
                  properties:
                    frontendIPConfiguration: "{{ frontendIPConfiguration }}"
                    frontendPort: "{{ frontendPort }}"
                    protocol: "{{ protocol }}"
                    hostName: "{{ hostName }}"
                    sslCertificate: "{{ sslCertificate }}"
                    sslProfile: "{{ sslProfile }}"
                    requireServerNameIndication: {{ requireServerNameIndication }}
                    provisioningState: "{{ provisioningState }}"
                    customErrorConfigurations: "{{ customErrorConfigurations }}"
                    firewallPolicy: "{{ firewallPolicy }}"
                    hostNames: "{{ hostNames }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              listeners:
                - id: "{{ id }}"
                  properties:
                    frontendIPConfiguration: "{{ frontendIPConfiguration }}"
                    frontendPort: "{{ frontendPort }}"
                    protocol: "{{ protocol }}"
                    sslCertificate: "{{ sslCertificate }}"
                    sslProfile: "{{ sslProfile }}"
                    provisioningState: "{{ provisioningState }}"
                    hostNames: "{{ hostNames }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              sslProfiles:
                - id: "{{ id }}"
                  properties:
                    trustedClientCertificates: "{{ trustedClientCertificates }}"
                    sslPolicy: "{{ sslPolicy }}"
                    clientAuthConfiguration: "{{ clientAuthConfiguration }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              urlPathMaps:
                - id: "{{ id }}"
                  properties:
                    defaultBackendAddressPool: "{{ defaultBackendAddressPool }}"
                    defaultBackendHttpSettings: "{{ defaultBackendHttpSettings }}"
                    defaultRewriteRuleSet: "{{ defaultRewriteRuleSet }}"
                    defaultRedirectConfiguration: "{{ defaultRedirectConfiguration }}"
                    defaultLoadDistributionPolicy: "{{ defaultLoadDistributionPolicy }}"
                    pathRules: "{{ pathRules }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              requestRoutingRules:
                - id: "{{ id }}"
                  properties:
                    ruleType: "{{ ruleType }}"
                    priority: {{ priority }}
                    backendAddressPool: "{{ backendAddressPool }}"
                    backendHttpSettings: "{{ backendHttpSettings }}"
                    httpListener: "{{ httpListener }}"
                    urlPathMap: "{{ urlPathMap }}"
                    rewriteRuleSet: "{{ rewriteRuleSet }}"
                    redirectConfiguration: "{{ redirectConfiguration }}"
                    loadDistributionPolicy: "{{ loadDistributionPolicy }}"
                    entraJWTValidationConfig: "{{ entraJWTValidationConfig }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              routingRules:
                - id: "{{ id }}"
                  properties:
                    ruleType: "{{ ruleType }}"
                    priority: {{ priority }}
                    backendAddressPool: "{{ backendAddressPool }}"
                    backendSettings: "{{ backendSettings }}"
                    listener: "{{ listener }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              rewriteRuleSets:
                - id: "{{ id }}"
                  properties:
                    rewriteRules: "{{ rewriteRules }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
              redirectConfigurations:
                - id: "{{ id }}"
                  properties:
                    redirectType: "{{ redirectType }}"
                    targetListener: "{{ targetListener }}"
                    targetUrl: "{{ targetUrl }}"
                    includePath: {{ includePath }}
                    includeQueryString: {{ includeQueryString }}
                    requestRoutingRules: "{{ requestRoutingRules }}"
                    urlPathMaps: "{{ urlPathMaps }}"
                    pathRules: "{{ pathRules }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              webApplicationFirewallConfiguration:
                enabled: {{ enabled }}
                firewallMode: "{{ firewallMode }}"
                ruleSetType: "{{ ruleSetType }}"
                ruleSetVersion: "{{ ruleSetVersion }}"
                disabledRuleGroups:
                  - ruleGroupName: "{{ ruleGroupName }}"
                    rules: "{{ rules }}"
                requestBodyCheck: {{ requestBodyCheck }}
                maxRequestBodySize: {{ maxRequestBodySize }}
                maxRequestBodySizeInKb: {{ maxRequestBodySizeInKb }}
                fileUploadLimitInMb: {{ fileUploadLimitInMb }}
                exclusions:
                  - matchVariable: "{{ matchVariable }}"
                    selectorMatchOperator: "{{ selectorMatchOperator }}"
                    selector: "{{ selector }}"
              firewallPolicy:
                id: "{{ id }}"
              enableHttp2: {{ enableHttp2 }}
              enableFips: {{ enableFips }}
              autoscaleConfiguration:
                minCapacity: {{ minCapacity }}
                maxCapacity: {{ maxCapacity }}
              privateLinkConfigurations:
                - id: "{{ id }}"
                  properties:
                    ipConfigurations: "{{ ipConfigurations }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              privateEndpointConnections:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    privateEndpoint: "{{ privateEndpoint }}"
                    privateLinkServiceConnectionState: "{{ privateLinkServiceConnectionState }}"
                    provisioningState: "{{ provisioningState }}"
                    linkIdentifier: "{{ linkIdentifier }}"
                  etag: "{{ etag }}"
              resourceGuid: "{{ resourceGuid }}"
              provisioningState: "{{ provisioningState }}"
              customErrorConfigurations:
                - statusCode: "{{ statusCode }}"
                  customErrorPageUrl: "{{ customErrorPageUrl }}"
              forceFirewallPolicyAssociation: {{ forceFirewallPolicyAssociation }}
              loadDistributionPolicies:
                - id: "{{ id }}"
                  properties:
                    loadDistributionTargets: "{{ loadDistributionTargets }}"
                    loadDistributionAlgorithm: "{{ loadDistributionAlgorithm }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              entraJWTValidationConfigs:
                - id: "{{ id }}"
                  properties:
                    unAuthorizedRequestAction: "{{ unAuthorizedRequestAction }}"
                    tenantId: "{{ tenantId }}"
                    clientId: "{{ clientId }}"
                    audiences: "{{ audiences }}"
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
              globalConfiguration:
                enableRequestBuffering: {{ enableRequestBuffering }}
                enableResponseBuffering: {{ enableResponseBuffering }}
              defaultPredefinedSslPolicy: "{{ defaultPredefinedSslPolicy }}"
            etag: "{{ etag }}"
            zones: "{{ zones }}"
            identity:
              principalId: "{{ principalId }}"
              tenantId: "{{ tenantId }}"
              type: "{{ type }}"
              userAssignedIdentities: "{{ userAssignedIdentities }}"
        provisioningState: "{{ provisioningState }}"
        resourceState: "{{ resourceState }}"
        managedRules:
          exceptions:
            - matchVariable: "{{ matchVariable }}"
              values: "{{ values }}"
              valueMatchOperator: "{{ valueMatchOperator }}"
              selectorMatchOperator: "{{ selectorMatchOperator }}"
              selector: "{{ selector }}"
              exceptionManagedRuleSets: "{{ exceptionManagedRuleSets }}"
          exclusions:
            - matchVariable: "{{ matchVariable }}"
              selectorMatchOperator: "{{ selectorMatchOperator }}"
              selector: "{{ selector }}"
              exclusionManagedRuleSets: "{{ exclusionManagedRuleSets }}"
          managedRuleSets:
            - ruleSetType: "{{ ruleSetType }}"
              ruleSetVersion: "{{ ruleSetVersion }}"
              ruleGroupOverrides: "{{ ruleGroupOverrides }}"
              computedDisabledRules: "{{ computedDisabledRules }}"
        httpListeners:
          - id: "{{ id }}"
        pathBasedRules:
          - id: "{{ id }}"
        applicationGatewayForContainers:
          - id: "{{ id }}"
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

Creates or update policy with specified rule set name within a resource group.

```sql
REPLACE azure.network.web_application_firewall_policies
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
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

Deletes Policy.

```sql
DELETE FROM azure.network.web_application_firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
