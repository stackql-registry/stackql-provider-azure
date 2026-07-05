--- 
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - security
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

Creates, updates, deletes, gets or lists an <code>alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alerts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_resource_group_level"
    values={[
        { label: 'get_resource_group_level', value: 'get_resource_group_level' },
        { label: 'list_resource_group_level_by_region', value: 'list_resource_group_level_by_region' },
        { label: 'get_subscription_level', value: 'get_subscription_level' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_subscription_level_by_region', value: 'list_subscription_level_by_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_resource_group_level">

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
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_resource_group_level_by_region">

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
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_subscription_level">

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
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_subscription_level_by_region">

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
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="alertDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="alertType" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the detection logic (all alert instances from the same detection logic will have the same alertType).</td>
</tr>
<tr>
    <td><CopyableCode code="alertUri" /></td>
    <td><code>string</code></td>
    <td>A direct link to the alert page in Azure Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="compromisedEntity" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource most related to this alert.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationKey" /></td>
    <td><code>string</code></td>
    <td>Key for corelating related alerts. Alerts with the same correlation key considered to be related.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the suspicious activity that was detected.</td>
</tr>
<tr>
    <td><CopyableCode code="endTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the last event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="entities" /></td>
    <td><code>array</code></td>
    <td>A list of entities related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLinks" /></td>
    <td><code>array</code></td>
    <td>Links related to the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="intent" /></td>
    <td><code>string</code></td>
    <td>The kill chain related intent behind the alert. For list of supported values, and explanations of Azure Security Center's supported kill chain intents. Known values are: "Unknown", "PreAttack", "InitialAccess", "Persistence", "PrivilegeEscalation", "DefenseEvasion", "CredentialAccess", "Discovery", "LateralMovement", "Execution", "Collection", "Exfiltration", "CommandAndControl", "Impact", "Probing", and "Exploitation". (Unknown, PreAttack, InitialAccess, Persistence, PrivilegeEscalation, DefenseEvasion, CredentialAccess, Discovery, LateralMovement, Execution, Collection, Exfiltration, CommandAndControl, Impact, Probing, Exploitation)</td>
</tr>
<tr>
    <td><CopyableCode code="isIncident" /></td>
    <td><code>boolean</code></td>
    <td>This field determines whether the alert is an incident (a compound grouping of several alerts) or a single alert.</td>
</tr>
<tr>
    <td><CopyableCode code="processingEndTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC processing end time of the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="productComponentName" /></td>
    <td><code>string</code></td>
    <td>The name of Azure Security Center pricing tier which powering this alert. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-pricing `_.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The name of the product which published this alert (Microsoft Sentinel, Microsoft Defender for Identity, Microsoft Defender for Endpoint, Microsoft Defender for Office, Microsoft Defender for Cloud Apps, and so on).</td>
</tr>
<tr>
    <td><CopyableCode code="remediationSteps" /></td>
    <td><code>array</code></td>
    <td>Manual action items to take to remediate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceIdentifiers" /></td>
    <td><code>array</code></td>
    <td>The resource identifiers that can be used to direct the alert to the right product exposure group (tenant, workspace, subscription etc.). There can be multiple identifiers of different type per alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The risk level of the threat that was detected. Learn more: `https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified `_. Known values are: "Informational", "Low", "Medium", and "High". (Informational, Low, Medium, High)</td>
</tr>
<tr>
    <td><CopyableCode code="startTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time of the first event or activity included in the alert in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The life cycle status of the alert. Known values are: "Active", "InProgress", "Resolved", and "Dismissed". (Active, InProgress, Resolved, Dismissed)</td>
</tr>
<tr>
    <td><CopyableCode code="subTechniques" /></td>
    <td><code>array</code></td>
    <td>Kill chain related sub-techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="supportingEvidence" /></td>
    <td><code>object</code></td>
    <td>Changing set of properties depending on the supportingEvidence type.</td>
</tr>
<tr>
    <td><CopyableCode code="systemAlertId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="techniques" /></td>
    <td><code>array</code></td>
    <td>kill chain related techniques behind the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="timeGeneratedUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The UTC time the alert was generated in ISO8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vendorName" /></td>
    <td><code>string</code></td>
    <td>The name of the vendor that raises the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
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
    <td><a href="#get_resource_group_level"><CopyableCode code="get_resource_group_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an alert that is associated a resource group or a resource in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_resource_group_level_by_region"><CopyableCode code="list_resource_group_level_by_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the alerts that are associated with the resource group that are stored in a specific location.</td>
</tr>
<tr>
    <td><a href="#get_subscription_level"><CopyableCode code="get_subscription_level" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an alert that is associated with a subscription.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the alerts that are associated with the resource group.</td>
</tr>
<tr>
    <td><a href="#list_subscription_level_by_region"><CopyableCode code="list_subscription_level_by_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the alerts that are associated with the subscription that are stored in a specific location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all the alerts that are associated with the subscription.</td>
</tr>
<tr>
    <td><a href="#update_subscription_level_state_to_dismiss"><CopyableCode code="update_subscription_level_state_to_dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_subscription_level_state_to_resolve"><CopyableCode code="update_subscription_level_state_to_resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_subscription_level_state_to_activate"><CopyableCode code="update_subscription_level_state_to_activate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_subscription_level_state_to_in_progress"><CopyableCode code="update_subscription_level_state_to_in_progress" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_resource_group_level_state_to_resolve"><CopyableCode code="update_resource_group_level_state_to_resolve" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_resource_group_level_state_to_dismiss"><CopyableCode code="update_resource_group_level_state_to_dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_resource_group_level_state_to_activate"><CopyableCode code="update_resource_group_level_state_to_activate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#update_resource_group_level_state_to_in_progress"><CopyableCode code="update_resource_group_level_state_to_in_progress" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-alert_name"><code>alert_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the alert's state.</td>
</tr>
<tr>
    <td><a href="#simulate"><CopyableCode code="simulate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Simulate security alerts.</td>
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
<tr id="parameter-alert_name">
    <td><CopyableCode code="alert_name" /></td>
    <td><code>string</code></td>
    <td>Name of the alert object. Required.</td>
</tr>
<tr id="parameter-asc_location">
    <td><CopyableCode code="asc_location" /></td>
    <td><code>string</code></td>
    <td>The location where ASC stores the data of the subscription. can be retrieved from Get locations. Required.</td>
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
    defaultValue="get_resource_group_level"
    values={[
        { label: 'get_resource_group_level', value: 'get_resource_group_level' },
        { label: 'list_resource_group_level_by_region', value: 'list_resource_group_level_by_region' },
        { label: 'get_subscription_level', value: 'get_subscription_level' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_subscription_level_by_region', value: 'list_subscription_level_by_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_resource_group_level">

Get an alert that is associated a resource group or a resource in a resource group.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND asc_location = '{{ asc_location }}' -- required
AND alert_name = '{{ alert_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_resource_group_level_by_region">

List all the alerts that are associated with the resource group that are stored in a specific location.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE asc_location = '{{ asc_location }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_subscription_level">

Get an alert that is associated with a subscription.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE asc_location = '{{ asc_location }}' -- required
AND alert_name = '{{ alert_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all the alerts that are associated with the resource group.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_subscription_level_by_region">

List all the alerts that are associated with the subscription that are stored in a specific location.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all the alerts that are associated with the subscription.

```sql
SELECT
id,
name,
alertDisplayName,
alertType,
alertUri,
compromisedEntity,
correlationKey,
description,
endTimeUtc,
entities,
extendedLinks,
extendedProperties,
intent,
isIncident,
processingEndTimeUtc,
productComponentName,
productName,
remediationSteps,
resourceIdentifiers,
severity,
startTimeUtc,
status,
subTechniques,
supportingEvidence,
systemAlertId,
systemData,
techniques,
timeGeneratedUtc,
type,
vendorName,
version
FROM azure.security.alerts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_subscription_level_state_to_dismiss"
    values={[
        { label: 'update_subscription_level_state_to_dismiss', value: 'update_subscription_level_state_to_dismiss' },
        { label: 'update_subscription_level_state_to_resolve', value: 'update_subscription_level_state_to_resolve' },
        { label: 'update_subscription_level_state_to_activate', value: 'update_subscription_level_state_to_activate' },
        { label: 'update_subscription_level_state_to_in_progress', value: 'update_subscription_level_state_to_in_progress' },
        { label: 'update_resource_group_level_state_to_resolve', value: 'update_resource_group_level_state_to_resolve' },
        { label: 'update_resource_group_level_state_to_dismiss', value: 'update_resource_group_level_state_to_dismiss' },
        { label: 'update_resource_group_level_state_to_activate', value: 'update_resource_group_level_state_to_activate' },
        { label: 'update_resource_group_level_state_to_in_progress', value: 'update_resource_group_level_state_to_in_progress' },
        { label: 'simulate', value: 'simulate' }
    ]}
>
<TabItem value="update_subscription_level_state_to_dismiss">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_subscription_level_state_to_dismiss 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_subscription_level_state_to_resolve">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_subscription_level_state_to_resolve 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_subscription_level_state_to_activate">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_subscription_level_state_to_activate 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_subscription_level_state_to_in_progress">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_subscription_level_state_to_in_progress 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_resource_group_level_state_to_resolve">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_resource_group_level_state_to_resolve 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_resource_group_level_state_to_dismiss">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_resource_group_level_state_to_dismiss 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_resource_group_level_state_to_activate">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_resource_group_level_state_to_activate 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_resource_group_level_state_to_in_progress">

Update the alert's state.

```sql
EXEC azure.security.alerts.update_resource_group_level_state_to_in_progress 
@resource_group_name='{{ resource_group_name }}' --required, 
@asc_location='{{ asc_location }}' --required, 
@alert_name='{{ alert_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="simulate">

Simulate security alerts.

```sql
EXEC azure.security.alerts.simulate 
@asc_location='{{ asc_location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
