--- 
title: application_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateways
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

Creates, updates, deletes, gets or lists an <code>application_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_gateways" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateways" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_ssl_predefined_policy', value: 'get_ssl_predefined_policy' },
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
    <td><CopyableCode code="authenticationCertificates" /></td>
    <td><code>array</code></td>
    <td>Authentication certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Autoscale Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Backend address pool of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendHttpSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend http settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="customErrorConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom error configurations of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPredefinedSslPolicy" /></td>
    <td><code>string</code></td>
    <td>The default predefined SSL Policy applied on the application gateway resource. Known values are: "AppGwSslPolicy20150501", "AppGwSslPolicy20170401", "AppGwSslPolicy20170401S", "AppGwSslPolicy20220101", and "AppGwSslPolicy20220101S". (AppGwSslPolicy20150501, AppGwSslPolicy20170401, AppGwSslPolicy20170401S, AppGwSslPolicy20220101, AppGwSslPolicy20220101S)</td>
</tr>
<tr>
    <td><CopyableCode code="enableFips" /></td>
    <td><code>boolean</code></td>
    <td>Whether FIPS is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttp2" /></td>
    <td><code>boolean</code></td>
    <td>Whether HTTP2 is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="entraJWTValidationConfigs" /></td>
    <td><code>array</code></td>
    <td>Entra JWT validation configurations for the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="forceFirewallPolicyAssociation" /></td>
    <td><code>boolean</code></td>
    <td>If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Frontend IP addresses of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPorts" /></td>
    <td><code>array</code></td>
    <td>Frontend ports of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Subnets of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="globalConfiguration" /></td>
    <td><code>object</code></td>
    <td>Global Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>Http listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the application gateway, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="listeners" /></td>
    <td><code>array</code></td>
    <td>Listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="loadDistributionPolicies" /></td>
    <td><code>array</code></td>
    <td>Load distribution policies of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="operationalState" /></td>
    <td><code>string</code></td>
    <td>Operational state of the application gateway resource. Known values are: "Stopped", "Starting", "Running", and "Stopping". (Stopped, Starting, Running, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint connections on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>PrivateLink configurations on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Probes of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="redirectConfigurations" /></td>
    <td><code>array</code></td>
    <td>Redirect configurations of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="requestRoutingRules" /></td>
    <td><code>array</code></td>
    <td>Request routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="rewriteRuleSets" /></td>
    <td><code>array</code></td>
    <td>Rewrite rules for the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslCertificates" /></td>
    <td><code>array</code></td>
    <td>SSL certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPolicy" /></td>
    <td><code>object</code></td>
    <td>SSL policy of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslProfiles" /></td>
    <td><code>array</code></td>
    <td>SSL profiles of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedClientCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted client certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted Root certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="urlPathMaps" /></td>
    <td><code>array</code></td>
    <td>URL path map of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallConfiguration" /></td>
    <td><code>object</code></td>
    <td>Web application firewall configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><CopyableCode code="authenticationCertificates" /></td>
    <td><code>array</code></td>
    <td>Authentication certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Autoscale Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Backend address pool of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendHttpSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend http settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="customErrorConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom error configurations of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPredefinedSslPolicy" /></td>
    <td><code>string</code></td>
    <td>The default predefined SSL Policy applied on the application gateway resource. Known values are: "AppGwSslPolicy20150501", "AppGwSslPolicy20170401", "AppGwSslPolicy20170401S", "AppGwSslPolicy20220101", and "AppGwSslPolicy20220101S". (AppGwSslPolicy20150501, AppGwSslPolicy20170401, AppGwSslPolicy20170401S, AppGwSslPolicy20220101, AppGwSslPolicy20220101S)</td>
</tr>
<tr>
    <td><CopyableCode code="enableFips" /></td>
    <td><code>boolean</code></td>
    <td>Whether FIPS is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttp2" /></td>
    <td><code>boolean</code></td>
    <td>Whether HTTP2 is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="entraJWTValidationConfigs" /></td>
    <td><code>array</code></td>
    <td>Entra JWT validation configurations for the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="forceFirewallPolicyAssociation" /></td>
    <td><code>boolean</code></td>
    <td>If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Frontend IP addresses of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPorts" /></td>
    <td><code>array</code></td>
    <td>Frontend ports of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Subnets of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="globalConfiguration" /></td>
    <td><code>object</code></td>
    <td>Global Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>Http listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the application gateway, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="listeners" /></td>
    <td><code>array</code></td>
    <td>Listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="loadDistributionPolicies" /></td>
    <td><code>array</code></td>
    <td>Load distribution policies of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="operationalState" /></td>
    <td><code>string</code></td>
    <td>Operational state of the application gateway resource. Known values are: "Stopped", "Starting", "Running", and "Stopping". (Stopped, Starting, Running, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint connections on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>PrivateLink configurations on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Probes of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="redirectConfigurations" /></td>
    <td><code>array</code></td>
    <td>Redirect configurations of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="requestRoutingRules" /></td>
    <td><code>array</code></td>
    <td>Request routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="rewriteRuleSets" /></td>
    <td><code>array</code></td>
    <td>Rewrite rules for the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslCertificates" /></td>
    <td><code>array</code></td>
    <td>SSL certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPolicy" /></td>
    <td><code>object</code></td>
    <td>SSL policy of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslProfiles" /></td>
    <td><code>array</code></td>
    <td>SSL profiles of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedClientCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted client certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted Root certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="urlPathMaps" /></td>
    <td><code>array</code></td>
    <td>URL path map of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallConfiguration" /></td>
    <td><code>object</code></td>
    <td>Web application firewall configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_ssl_predefined_policy">

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
    <td>Name of the Ssl predefined policy.</td>
</tr>
<tr>
    <td><CopyableCode code="cipherSuites" /></td>
    <td><code>array</code></td>
    <td>Ssl cipher suites to be enabled in the specified order for application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="minProtocolVersion" /></td>
    <td><code>string</code></td>
    <td>Minimum version of Ssl protocol to be supported on application gateway. Known values are: "TLSv1_0", "TLSv1_1", "TLSv1_2", and "TLSv1_3". (TLSv1_0, TLSv1_1, TLSv1_2, TLSv1_3)</td>
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
    <td><CopyableCode code="authenticationCertificates" /></td>
    <td><code>array</code></td>
    <td>Authentication certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="autoscaleConfiguration" /></td>
    <td><code>object</code></td>
    <td>Autoscale Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="backendAddressPools" /></td>
    <td><code>array</code></td>
    <td>Backend address pool of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendHttpSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend http settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="backendSettingsCollection" /></td>
    <td><code>array</code></td>
    <td>Backend settings of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="customErrorConfigurations" /></td>
    <td><code>array</code></td>
    <td>Custom error configurations of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultPredefinedSslPolicy" /></td>
    <td><code>string</code></td>
    <td>The default predefined SSL Policy applied on the application gateway resource. Known values are: "AppGwSslPolicy20150501", "AppGwSslPolicy20170401", "AppGwSslPolicy20170401S", "AppGwSslPolicy20220101", and "AppGwSslPolicy20220101S". (AppGwSslPolicy20150501, AppGwSslPolicy20170401, AppGwSslPolicy20170401S, AppGwSslPolicy20220101, AppGwSslPolicy20220101S)</td>
</tr>
<tr>
    <td><CopyableCode code="enableFips" /></td>
    <td><code>boolean</code></td>
    <td>Whether FIPS is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHttp2" /></td>
    <td><code>boolean</code></td>
    <td>Whether HTTP2 is enabled on the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="entraJWTValidationConfigs" /></td>
    <td><code>array</code></td>
    <td>Entra JWT validation configurations for the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="firewallPolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="forceFirewallPolicyAssociation" /></td>
    <td><code>boolean</code></td>
    <td>If true, associates a firewall policy with an application gateway regardless whether the policy differs from the WAF Config.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Frontend IP addresses of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="frontendPorts" /></td>
    <td><code>array</code></td>
    <td>Frontend ports of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayIPConfigurations" /></td>
    <td><code>array</code></td>
    <td>Subnets of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="globalConfiguration" /></td>
    <td><code>object</code></td>
    <td>Global Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="httpListeners" /></td>
    <td><code>array</code></td>
    <td>Http listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the application gateway, if configured.</td>
</tr>
<tr>
    <td><CopyableCode code="listeners" /></td>
    <td><code>array</code></td>
    <td>Listeners of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="loadDistributionPolicies" /></td>
    <td><code>array</code></td>
    <td>Load distribution policies of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="operationalState" /></td>
    <td><code>string</code></td>
    <td>Operational state of the application gateway resource. Known values are: "Stopped", "Starting", "Running", and "Stopping". (Stopped, Starting, Running, Stopping)</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>Private Endpoint connections on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>PrivateLink configurations on application gateway.</td>
</tr>
<tr>
    <td><CopyableCode code="probes" /></td>
    <td><code>array</code></td>
    <td>Probes of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application gateway resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="redirectConfigurations" /></td>
    <td><code>array</code></td>
    <td>Redirect configurations of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="requestRoutingRules" /></td>
    <td><code>array</code></td>
    <td>Request routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGuid" /></td>
    <td><code>string</code></td>
    <td>The resource GUID property of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="rewriteRuleSets" /></td>
    <td><code>array</code></td>
    <td>Rewrite rules for the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="routingRules" /></td>
    <td><code>array</code></td>
    <td>Routing rules of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>SKU of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslCertificates" /></td>
    <td><code>array</code></td>
    <td>SSL certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="sslPolicy" /></td>
    <td><code>object</code></td>
    <td>SSL policy of the application gateway resource.</td>
</tr>
<tr>
    <td><CopyableCode code="sslProfiles" /></td>
    <td><code>array</code></td>
    <td>SSL profiles of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedClientCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted client certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="trustedRootCertificates" /></td>
    <td><code>array</code></td>
    <td>Trusted Root certificates of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="urlPathMaps" /></td>
    <td><code>array</code></td>
    <td>URL path map of the application gateway resource. For default limits, see `Application Gateway limits `_.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallConfiguration" /></td>
    <td><code>object</code></td>
    <td>Web application firewall configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>A list of availability zones denoting where the resource needs to come from.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified application gateway.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all application gateways in a resource group.</td>
</tr>
<tr>
    <td><a href="#get_ssl_predefined_policy"><CopyableCode code="get_ssl_predefined_policy" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-predefined_policy_name"><code>predefined_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets Ssl predefined policy with the specified policy name.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the application gateways in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified application gateway.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the specified application gateway tags.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified application gateway.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified application gateway.</td>
</tr>
<tr>
    <td><a href="#list_available_ssl_options"><CopyableCode code="list_available_ssl_options" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists available Ssl options for configuring Ssl policy.</td>
</tr>
<tr>
    <td><a href="#list_available_ssl_predefined_policies"><CopyableCode code="list_available_ssl_predefined_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all SSL predefined policies for configuring Ssl policy.</td>
</tr>
<tr>
    <td><a href="#list_available_server_variables"><CopyableCode code="list_available_server_variables" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available server variables.</td>
</tr>
<tr>
    <td><a href="#list_available_request_headers"><CopyableCode code="list_available_request_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available request headers.</td>
</tr>
<tr>
    <td><a href="#list_available_response_headers"><CopyableCode code="list_available_response_headers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available response headers.</td>
</tr>
<tr>
    <td><a href="#list_available_waf_rule_sets"><CopyableCode code="list_available_waf_rule_sets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available web application firewall rule sets.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts the specified application gateway.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops the specified application gateway in a resource group.</td>
</tr>
<tr>
    <td><a href="#backend_health"><CopyableCode code="backend_health" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the backend health of the specified application gateway in a resource group.</td>
</tr>
<tr>
    <td><a href="#backend_health_on_demand"><CopyableCode code="backend_health_on_demand" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-application_gateway_name"><code>application_gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group.</td>
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
<tr id="parameter-application_gateway_name">
    <td><CopyableCode code="application_gateway_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application gateway. Required.</td>
</tr>
<tr id="parameter-predefined_policy_name">
    <td><CopyableCode code="predefined_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the ssl predefined policy. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands BackendAddressPool and BackendHttpSettings referenced in backend health. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_ssl_predefined_policy', value: 'get_ssl_predefined_policy' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified application gateway.

```sql
SELECT
id,
name,
authenticationCertificates,
autoscaleConfiguration,
backendAddressPools,
backendHttpSettingsCollection,
backendSettingsCollection,
customErrorConfigurations,
defaultPredefinedSslPolicy,
enableFips,
enableHttp2,
entraJWTValidationConfigs,
etag,
firewallPolicy,
forceFirewallPolicyAssociation,
frontendIPConfigurations,
frontendPorts,
gatewayIPConfigurations,
globalConfiguration,
httpListeners,
identity,
listeners,
loadDistributionPolicies,
location,
operationalState,
privateEndpointConnections,
privateLinkConfigurations,
probes,
provisioningState,
redirectConfigurations,
requestRoutingRules,
resourceGuid,
rewriteRuleSets,
routingRules,
sku,
sslCertificates,
sslPolicy,
sslProfiles,
tags,
trustedClientCertificates,
trustedRootCertificates,
type,
urlPathMaps,
webApplicationFirewallConfiguration,
zones
FROM azure.network.application_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND application_gateway_name = '{{ application_gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all application gateways in a resource group.

```sql
SELECT
id,
name,
authenticationCertificates,
autoscaleConfiguration,
backendAddressPools,
backendHttpSettingsCollection,
backendSettingsCollection,
customErrorConfigurations,
defaultPredefinedSslPolicy,
enableFips,
enableHttp2,
entraJWTValidationConfigs,
etag,
firewallPolicy,
forceFirewallPolicyAssociation,
frontendIPConfigurations,
frontendPorts,
gatewayIPConfigurations,
globalConfiguration,
httpListeners,
identity,
listeners,
loadDistributionPolicies,
location,
operationalState,
privateEndpointConnections,
privateLinkConfigurations,
probes,
provisioningState,
redirectConfigurations,
requestRoutingRules,
resourceGuid,
rewriteRuleSets,
routingRules,
sku,
sslCertificates,
sslPolicy,
sslProfiles,
tags,
trustedClientCertificates,
trustedRootCertificates,
type,
urlPathMaps,
webApplicationFirewallConfiguration,
zones
FROM azure.network.application_gateways
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_ssl_predefined_policy">

Gets Ssl predefined policy with the specified policy name.

```sql
SELECT
id,
name,
cipherSuites,
minProtocolVersion
FROM azure.network.application_gateways
WHERE predefined_policy_name = '{{ predefined_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the application gateways in a subscription.

```sql
SELECT
id,
name,
authenticationCertificates,
autoscaleConfiguration,
backendAddressPools,
backendHttpSettingsCollection,
backendSettingsCollection,
customErrorConfigurations,
defaultPredefinedSslPolicy,
enableFips,
enableHttp2,
entraJWTValidationConfigs,
etag,
firewallPolicy,
forceFirewallPolicyAssociation,
frontendIPConfigurations,
frontendPorts,
gatewayIPConfigurations,
globalConfiguration,
httpListeners,
identity,
listeners,
loadDistributionPolicies,
location,
operationalState,
privateEndpointConnections,
privateLinkConfigurations,
probes,
provisioningState,
redirectConfigurations,
requestRoutingRules,
resourceGuid,
rewriteRuleSets,
routingRules,
sku,
sslCertificates,
sslPolicy,
sslProfiles,
tags,
trustedClientCertificates,
trustedRootCertificates,
type,
urlPathMaps,
webApplicationFirewallConfiguration,
zones
FROM azure.network.application_gateways
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

Creates or updates the specified application gateway.

```sql
INSERT INTO azure.network.application_gateways (
id,
location,
tags,
properties,
zones,
identity,
resource_group_name,
application_gateway_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ zones }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ application_gateway_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: application_gateways
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the application_gateways resource.
    - name: application_gateway_name
      value: "{{ application_gateway_name }}"
      description: Required parameter for the application_gateways resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the application_gateways resource.
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
        Properties of the application gateway.
      value:
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
              subnet:
                id: "{{ id }}"
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
              hsm:
                keyId: "{{ keyId }}"
                publicCertData: "{{ publicCertData }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        frontendIPConfigurations:
          - id: "{{ id }}"
            properties:
              privateIPAddress: "{{ privateIPAddress }}"
              privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
              subnet:
                id: "{{ id }}"
              publicIPAddress:
                id: "{{ id }}"
              privateLinkConfiguration:
                id: "{{ id }}"
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
              match:
                body: "{{ body }}"
                statusCodes:
                  - "{{ statusCodes }}"
              enableProbeProxyProtocolHeader: {{ enableProbeProxyProtocolHeader }}
              provisioningState: "{{ provisioningState }}"
              port: {{ port }}
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        backendAddressPools:
          - id: "{{ id }}"
            properties:
              backendIPConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    gatewayLoadBalancer: "{{ gatewayLoadBalancer }}"
                    virtualNetworkTaps: "{{ virtualNetworkTaps }}"
                    applicationGatewayBackendAddressPools: "{{ applicationGatewayBackendAddressPools }}"
                    loadBalancerBackendAddressPools: "{{ loadBalancerBackendAddressPools }}"
                    loadBalancerInboundNatRules: "{{ loadBalancerInboundNatRules }}"
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAddressPrefixLength: {{ privateIPAddressPrefixLength }}
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    privateIPAddressVersion: "{{ privateIPAddressVersion }}"
                    subnet: "{{ subnet }}"
                    primary: {{ primary }}
                    publicIPAddress: "{{ publicIPAddress }}"
                    applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                    provisioningState: "{{ provisioningState }}"
                    privateLinkConnectionProperties: "{{ privateLinkConnectionProperties }}"
                  etag: "{{ etag }}"
              backendAddresses:
                - fqdn: "{{ fqdn }}"
                  ipAddress: "{{ ipAddress }}"
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
              probe:
                id: "{{ id }}"
              authenticationCertificates:
                - id: "{{ id }}"
              trustedRootCertificates:
                - id: "{{ id }}"
              connectionDraining:
                enabled: {{ enabled }}
                drainTimeoutInSec: {{ drainTimeoutInSec }}
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
              probe:
                id: "{{ id }}"
              trustedRootCertificates:
                - id: "{{ id }}"
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
              frontendIPConfiguration:
                id: "{{ id }}"
              frontendPort:
                id: "{{ id }}"
              protocol: "{{ protocol }}"
              hostName: "{{ hostName }}"
              sslCertificate:
                id: "{{ id }}"
              sslProfile:
                id: "{{ id }}"
              requireServerNameIndication: {{ requireServerNameIndication }}
              provisioningState: "{{ provisioningState }}"
              customErrorConfigurations:
                - statusCode: "{{ statusCode }}"
                  customErrorPageUrl: "{{ customErrorPageUrl }}"
              firewallPolicy:
                id: "{{ id }}"
              hostNames:
                - "{{ hostNames }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        listeners:
          - id: "{{ id }}"
            properties:
              frontendIPConfiguration:
                id: "{{ id }}"
              frontendPort:
                id: "{{ id }}"
              protocol: "{{ protocol }}"
              sslCertificate:
                id: "{{ id }}"
              sslProfile:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
              hostNames:
                - "{{ hostNames }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        sslProfiles:
          - id: "{{ id }}"
            properties:
              trustedClientCertificates:
                - id: "{{ id }}"
              sslPolicy:
                disabledSslProtocols:
                  - "{{ disabledSslProtocols }}"
                policyType: "{{ policyType }}"
                policyName: "{{ policyName }}"
                cipherSuites:
                  - "{{ cipherSuites }}"
                minProtocolVersion: "{{ minProtocolVersion }}"
              clientAuthConfiguration:
                verifyClientCertIssuerDN: {{ verifyClientCertIssuerDN }}
                verifyClientRevocation: "{{ verifyClientRevocation }}"
                verifyClientAuthMode: "{{ verifyClientAuthMode }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        urlPathMaps:
          - id: "{{ id }}"
            properties:
              defaultBackendAddressPool:
                id: "{{ id }}"
              defaultBackendHttpSettings:
                id: "{{ id }}"
              defaultRewriteRuleSet:
                id: "{{ id }}"
              defaultRedirectConfiguration:
                id: "{{ id }}"
              defaultLoadDistributionPolicy:
                id: "{{ id }}"
              pathRules:
                - id: "{{ id }}"
                  properties:
                    paths: "{{ paths }}"
                    backendAddressPool: "{{ backendAddressPool }}"
                    backendHttpSettings: "{{ backendHttpSettings }}"
                    redirectConfiguration: "{{ redirectConfiguration }}"
                    rewriteRuleSet: "{{ rewriteRuleSet }}"
                    loadDistributionPolicy: "{{ loadDistributionPolicy }}"
                    provisioningState: "{{ provisioningState }}"
                    firewallPolicy: "{{ firewallPolicy }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        requestRoutingRules:
          - id: "{{ id }}"
            properties:
              ruleType: "{{ ruleType }}"
              priority: {{ priority }}
              backendAddressPool:
                id: "{{ id }}"
              backendHttpSettings:
                id: "{{ id }}"
              httpListener:
                id: "{{ id }}"
              urlPathMap:
                id: "{{ id }}"
              rewriteRuleSet:
                id: "{{ id }}"
              redirectConfiguration:
                id: "{{ id }}"
              loadDistributionPolicy:
                id: "{{ id }}"
              entraJWTValidationConfig:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        routingRules:
          - id: "{{ id }}"
            properties:
              ruleType: "{{ ruleType }}"
              priority: {{ priority }}
              backendAddressPool:
                id: "{{ id }}"
              backendSettings:
                id: "{{ id }}"
              listener:
                id: "{{ id }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        rewriteRuleSets:
          - id: "{{ id }}"
            properties:
              rewriteRules:
                - name: "{{ name }}"
                  ruleSequence: {{ ruleSequence }}
                  conditions: "{{ conditions }}"
                  actionSet:
                    requestHeaderConfigurations: "{{ requestHeaderConfigurations }}"
                    responseHeaderConfigurations: "{{ responseHeaderConfigurations }}"
                    urlConfiguration: "{{ urlConfiguration }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        redirectConfigurations:
          - id: "{{ id }}"
            properties:
              redirectType: "{{ redirectType }}"
              targetListener:
                id: "{{ id }}"
              targetUrl: "{{ targetUrl }}"
              includePath: {{ includePath }}
              includeQueryString: {{ includeQueryString }}
              requestRoutingRules:
                - id: "{{ id }}"
              urlPathMaps:
                - id: "{{ id }}"
              pathRules:
                - id: "{{ id }}"
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
              ipConfigurations:
                - id: "{{ id }}"
                  properties:
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
                    primary: {{ primary }}
                    provisioningState: "{{ provisioningState }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
            type: "{{ type }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
                name: "{{ name }}"
                type: "{{ type }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  subnet: "{{ subnet }}"
                  networkInterfaces: "{{ networkInterfaces }}"
                  provisioningState: "{{ provisioningState }}"
                  ipVersionType: "{{ ipVersionType }}"
                  privateLinkServiceConnections: "{{ privateLinkServiceConnections }}"
                  manualPrivateLinkServiceConnections: "{{ manualPrivateLinkServiceConnections }}"
                  customDnsConfigs: "{{ customDnsConfigs }}"
                  applicationSecurityGroups: "{{ applicationSecurityGroups }}"
                  ipConfigurations: "{{ ipConfigurations }}"
                  customNetworkInterfaceName: "{{ customNetworkInterfaceName }}"
                  billingSku: "{{ billingSku }}"
                extendedLocation:
                  name: "{{ name }}"
                  type: "{{ type }}"
                etag: "{{ etag }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
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
              loadDistributionTargets:
                - id: "{{ id }}"
                  properties:
                    weightPerServer: {{ weightPerServer }}
                    backendAddressPool: "{{ backendAddressPool }}"
                  name: "{{ name }}"
                  etag: "{{ etag }}"
                  type: "{{ type }}"
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
              audiences:
                - "{{ audiences }}"
              provisioningState: "{{ provisioningState }}"
            name: "{{ name }}"
            etag: "{{ etag }}"
        globalConfiguration:
          enableRequestBuffering: {{ enableRequestBuffering }}
          enableResponseBuffering: {{ enableResponseBuffering }}
        defaultPredefinedSslPolicy: "{{ defaultPredefinedSslPolicy }}"
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        A list of availability zones denoting where the resource needs to come from.
    - name: identity
      description: |
        The identity of the application gateway, if configured.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates the specified application gateway tags.

```sql
UPDATE azure.network.application_gateways
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_gateway_name = '{{ application_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type,
zones;
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

Creates or updates the specified application gateway.

```sql
REPLACE azure.network.application_gateways
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
zones = '{{ zones }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND application_gateway_name = '{{ application_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type,
zones;
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

Deletes the specified application gateway.

```sql
DELETE FROM azure.network.application_gateways
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND application_gateway_name = '{{ application_gateway_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_available_ssl_options"
    values={[
        { label: 'list_available_ssl_options', value: 'list_available_ssl_options' },
        { label: 'list_available_ssl_predefined_policies', value: 'list_available_ssl_predefined_policies' },
        { label: 'list_available_server_variables', value: 'list_available_server_variables' },
        { label: 'list_available_request_headers', value: 'list_available_request_headers' },
        { label: 'list_available_response_headers', value: 'list_available_response_headers' },
        { label: 'list_available_waf_rule_sets', value: 'list_available_waf_rule_sets' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'backend_health', value: 'backend_health' },
        { label: 'backend_health_on_demand', value: 'backend_health_on_demand' }
    ]}
>
<TabItem value="list_available_ssl_options">

Lists available Ssl options for configuring Ssl policy.

```sql
EXEC azure.network.application_gateways.list_available_ssl_options 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_available_ssl_predefined_policies">

Lists all SSL predefined policies for configuring Ssl policy.

```sql
EXEC azure.network.application_gateways.list_available_ssl_predefined_policies 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_available_server_variables">

Lists all available server variables.

```sql
EXEC azure.network.application_gateways.list_available_server_variables 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_available_request_headers">

Lists all available request headers.

```sql
EXEC azure.network.application_gateways.list_available_request_headers 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_available_response_headers">

Lists all available response headers.

```sql
EXEC azure.network.application_gateways.list_available_response_headers 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_available_waf_rule_sets">

Lists all available web application firewall rule sets.

```sql
EXEC azure.network.application_gateways.list_available_waf_rule_sets 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Starts the specified application gateway.

```sql
EXEC azure.network.application_gateways.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@application_gateway_name='{{ application_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stops the specified application gateway in a resource group.

```sql
EXEC azure.network.application_gateways.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@application_gateway_name='{{ application_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="backend_health">

Gets the backend health of the specified application gateway in a resource group.

```sql
EXEC azure.network.application_gateways.backend_health 
@resource_group_name='{{ resource_group_name }}' --required, 
@application_gateway_name='{{ application_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="backend_health_on_demand">

Gets the backend health for given combination of backend pool and http setting of the specified application gateway in a resource group.

```sql
EXEC azure.network.application_gateways.backend_health_on_demand 
@resource_group_name='{{ resource_group_name }}' --required, 
@application_gateway_name='{{ application_gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$expand='{{ $expand }}' 
@@json=
'{
"protocol": "{{ protocol }}", 
"host": "{{ host }}", 
"path": "{{ path }}", 
"timeout": {{ timeout }}, 
"pickHostNameFromBackendHttpSettings": {{ pickHostNameFromBackendHttpSettings }}, 
"enableProbeProxyProtocolHeader": {{ enableProbeProxyProtocolHeader }}, 
"match": "{{ match }}", 
"backendAddressPool": "{{ backendAddressPool }}", 
"backendHttpSettings": "{{ backendHttpSettings }}"
}'
;
```
</TabItem>
</Tabs>
