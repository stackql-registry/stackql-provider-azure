--- 
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
  - alerts_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.alerts_management.alerts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'get_summary', value: 'get_summary' },
        { label: 'get_by_id_tenant', value: 'get_by_id_tenant' },
        { label: 'get_all', value: 'get_all' },
        { label: 'get_all_tenant', value: 'get_all_tenant' }
    ]}
>
<TabItem value="get_by_id">

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
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>Information specific to the monitor service that gives more contextual details about the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties that can hold any user defined key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="egressConfig" /></td>
    <td><code>object</code></td>
    <td>Config which would be used for displaying the data in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="essentials" /></td>
    <td><code>object</code></td>
    <td>This object contains consistent fields across different monitor services.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="get_summary">

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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="groupedby" /></td>
    <td><code>string</code></td>
    <td>Name of the field aggregated.</td>
</tr>
<tr>
    <td><CopyableCode code="smartGroupsCount" /></td>
    <td><code>integer</code></td>
    <td>Total count of the smart groups.</td>
</tr>
<tr>
    <td><CopyableCode code="total" /></td>
    <td><code>integer</code></td>
    <td>Total count of the result set.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>List of the items.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_id_tenant">

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
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>Information specific to the monitor service that gives more contextual details about the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties that can hold any user defined key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="egressConfig" /></td>
    <td><code>object</code></td>
    <td>Config which would be used for displaying the data in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="essentials" /></td>
    <td><code>object</code></td>
    <td>This object contains consistent fields across different monitor services.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="get_all">

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
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>Information specific to the monitor service that gives more contextual details about the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties that can hold any user defined key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="egressConfig" /></td>
    <td><code>object</code></td>
    <td>Config which would be used for displaying the data in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="essentials" /></td>
    <td><code>object</code></td>
    <td>This object contains consistent fields across different monitor services.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="get_all_tenant">

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
    <td><CopyableCode code="context" /></td>
    <td><code>object</code></td>
    <td>Information specific to the monitor service that gives more contextual details about the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Custom properties that can hold any user defined key-value pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="egressConfig" /></td>
    <td><code>object</code></td>
    <td>Config which would be used for displaying the data in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="essentials" /></td>
    <td><code>object</code></td>
    <td>This object contains consistent fields across different monitor services.</td>
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
    <td><a href="#get_by_id"><CopyableCode code="get_by_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get a specific alert. Get information related to a specific alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to get alert by id then use parent resource of scope. So in this example get alert by id call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;'.</td>
</tr>
<tr>
    <td><a href="#get_summary"><CopyableCode code="get_summary" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-groupby"><code>groupby</code></a></td>
    <td><a href="#parameter-includeSmartGroupsCount"><code>includeSmartGroupsCount</code></a>, <a href="#parameter-targetResource"><code>targetResource</code></a>, <a href="#parameter-targetResourceType"><code>targetResourceType</code></a>, <a href="#parameter-targetResourceGroup"><code>targetResourceGroup</code></a>, <a href="#parameter-monitorService"><code>monitorService</code></a>, <a href="#parameter-monitorCondition"><code>monitorCondition</code></a>, <a href="#parameter-severity"><code>severity</code></a>, <a href="#parameter-alertState"><code>alertState</code></a>, <a href="#parameter-alertRule"><code>alertRule</code></a>, <a href="#parameter-timeRange"><code>timeRange</code></a>, <a href="#parameter-customTimeRange"><code>customTimeRange</code></a></td>
    <td>Get a summarized count of your alerts grouped by various parameters (e.g. grouping by 'Severity' returns the count of alerts for each severity).</td>
</tr>
<tr>
    <td><a href="#get_by_id_tenant"><CopyableCode code="get_by_id_tenant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get a specific alert. Get information related to a specific alert.</td>
</tr>
<tr>
    <td><a href="#get_all"><CopyableCode code="get_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-targetResource"><code>targetResource</code></a>, <a href="#parameter-targetResourceType"><code>targetResourceType</code></a>, <a href="#parameter-targetResourceGroup"><code>targetResourceGroup</code></a>, <a href="#parameter-monitorService"><code>monitorService</code></a>, <a href="#parameter-monitorCondition"><code>monitorCondition</code></a>, <a href="#parameter-severity"><code>severity</code></a>, <a href="#parameter-alertState"><code>alertState</code></a>, <a href="#parameter-alertRule"><code>alertRule</code></a>, <a href="#parameter-smartGroupId"><code>smartGroupId</code></a>, <a href="#parameter-includeContext"><code>includeContext</code></a>, <a href="#parameter-includeEgressConfig"><code>includeEgressConfig</code></a>, <a href="#parameter-pageCount"><code>pageCount</code></a>, <a href="#parameter-sortBy"><code>sortBy</code></a>, <a href="#parameter-sortOrder"><code>sortOrder</code></a>, <a href="#parameter-select"><code>select</code></a>, <a href="#parameter-timeRange"><code>timeRange</code></a>, <a href="#parameter-customTimeRange"><code>customTimeRange</code></a></td>
    <td>List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.</td>
</tr>
<tr>
    <td><a href="#get_all_tenant"><CopyableCode code="get_all_tenant" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-targetResource"><code>targetResource</code></a>, <a href="#parameter-targetResourceType"><code>targetResourceType</code></a>, <a href="#parameter-targetResourceGroup"><code>targetResourceGroup</code></a>, <a href="#parameter-monitorService"><code>monitorService</code></a>, <a href="#parameter-monitorCondition"><code>monitorCondition</code></a>, <a href="#parameter-severity"><code>severity</code></a>, <a href="#parameter-alertState"><code>alertState</code></a>, <a href="#parameter-alertRule"><code>alertRule</code></a>, <a href="#parameter-smartGroupId"><code>smartGroupId</code></a>, <a href="#parameter-includeContext"><code>includeContext</code></a>, <a href="#parameter-includeEgressConfig"><code>includeEgressConfig</code></a>, <a href="#parameter-pageCount"><code>pageCount</code></a>, <a href="#parameter-sortBy"><code>sortBy</code></a>, <a href="#parameter-sortOrder"><code>sortOrder</code></a>, <a href="#parameter-select"><code>select</code></a>, <a href="#parameter-timeRange"><code>timeRange</code></a>, <a href="#parameter-customTimeRange"><code>customTimeRange</code></a></td>
    <td>List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.</td>
</tr>
<tr>
    <td><a href="#get_history_tenant"><CopyableCode code="get_history_tenant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get the history of an alert, which captures any monitor condition changes (Fired/Resolved), alert state changes (New/Acknowledged/Closed) and applied action rules for that particular alert.</td>
</tr>
<tr>
    <td><a href="#get_history"><CopyableCode code="get_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get the history of an alert, which captures any monitor condition changes (Fired/Resolved), alert state changes (New/Acknowledged/Closed) and applied action rules for that particular alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to get history of this particular alert then use parent resource of scope. So in this example get history call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;/history'.</td>
</tr>
<tr>
    <td><a href="#get_enrichments"><CopyableCode code="get_enrichments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a></td>
    <td></td>
    <td>Get the enrichments of an alert. It returns a collection of one object named default.</td>
</tr>
<tr>
    <td><a href="#change_state_tenant"><CopyableCode code="change_state_tenant" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-newState"><code>newState</code></a></td>
    <td></td>
    <td>Change the state of an alert.</td>
</tr>
<tr>
    <td><a href="#change_state"><CopyableCode code="change_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_id"><code>alert_id</code></a>, <a href="#parameter-newState"><code>newState</code></a></td>
    <td></td>
    <td>Change the state of an alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to change state of this particular alert then use parent resource of scope. So in this example change state call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;'.</td>
</tr>
<tr>
    <td><a href="#meta_data"><CopyableCode code="meta_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-identifier"><code>identifier</code></a></td>
    <td></td>
    <td>List alerts meta data information based on value of identifier parameter.</td>
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
<tr id="parameter-alert_id">
    <td><CopyableCode code="alert_id" /></td>
    <td><code>string</code></td>
    <td>Unique ID of an alert instance. Required.</td>
</tr>
<tr id="parameter-groupby">
    <td><CopyableCode code="groupby" /></td>
    <td><code>string</code></td>
    <td>This parameter allows the result set to be grouped by input fields. For example, groupby=severity,alertstate. Known values are: "severity", "alertState", "monitorCondition", "monitorService", "signalType", and "alertRule". Required.</td>
</tr>
<tr id="parameter-identifier">
    <td><CopyableCode code="identifier" /></td>
    <td><code>string</code></td>
    <td>Identification of the information to be retrieved by API call. "MonitorServiceList" Required.</td>
</tr>
<tr id="parameter-newState">
    <td><CopyableCode code="newState" /></td>
    <td><code>string</code></td>
    <td>New state of the alert. Known values are: "New", "Acknowledged", and "Closed". Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>undefined. Required.</td>
</tr>
<tr id="parameter-alertRule">
    <td><CopyableCode code="alertRule" /></td>
    <td><code>string</code></td>
    <td>Filter by specific alert rule. Default value is to select all. Default value is None.</td>
</tr>
<tr id="parameter-alertState">
    <td><CopyableCode code="alertState" /></td>
    <td><code>string</code></td>
    <td>Filter by state of the alert instance. Default value is to select all. Known values are: "New", "Acknowledged", and "Closed". Default value is None.</td>
</tr>
<tr id="parameter-customTimeRange">
    <td><CopyableCode code="customTimeRange" /></td>
    <td><code>string</code></td>
    <td>Filter by custom time range in the format / where time is in (ISO-8601 format)'. Permissible values is within 30 days from query time. Either timeRange or customTimeRange could be used but not both. Default is none. Default value is None.</td>
</tr>
<tr id="parameter-includeContext">
    <td><CopyableCode code="includeContext" /></td>
    <td><code>boolean</code></td>
    <td>Include context which has contextual data specific to the monitor service. Default value is false'. Default value is None.</td>
</tr>
<tr id="parameter-includeEgressConfig">
    <td><CopyableCode code="includeEgressConfig" /></td>
    <td><code>boolean</code></td>
    <td>Include egress config which would be used for displaying the content in portal. Default value is 'false'. Default value is None.</td>
</tr>
<tr id="parameter-includeSmartGroupsCount">
    <td><CopyableCode code="includeSmartGroupsCount" /></td>
    <td><code>boolean</code></td>
    <td>Include count of the SmartGroups as part of the summary. Default value is 'false'. Default value is None.</td>
</tr>
<tr id="parameter-monitorCondition">
    <td><CopyableCode code="monitorCondition" /></td>
    <td><code>string</code></td>
    <td>Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all. Known values are: "Fired" and "Resolved". Default value is None.</td>
</tr>
<tr id="parameter-monitorService">
    <td><CopyableCode code="monitorService" /></td>
    <td><code>string</code></td>
    <td>Filter by monitor service which generates the alert instance. Default value is select all. Known values are: "Application Insights", "ActivityLog Administrative", "ActivityLog Security", "ActivityLog Recommendation", "ActivityLog Policy", "ActivityLog Autoscale", "Log Analytics", "Nagios", "Platform", "SCOM", "ServiceHealth", "SmartDetector", "VM Insights", "Zabbix", and "Resource Health". Default value is None.</td>
</tr>
<tr id="parameter-pageCount">
    <td><CopyableCode code="pageCount" /></td>
    <td><code>integer</code></td>
    <td>Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the "includeContent" filter is selected, maximum value allowed is 25. Default value is 25. Default value is None.</td>
</tr>
<tr id="parameter-select">
    <td><CopyableCode code="select" /></td>
    <td><code>string</code></td>
    <td>This filter allows to selection of the fields(comma separated) which would be part of the essential section. This would allow to project only the required fields rather than getting entire content. Default is to fetch all the fields in the essentials section. Default value is None.</td>
</tr>
<tr id="parameter-severity">
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>Filter by severity. Default value is select all. Known values are: "Sev0", "Sev1", "Sev2", "Sev3", and "Sev4". Default value is None.</td>
</tr>
<tr id="parameter-smartGroupId">
    <td><CopyableCode code="smartGroupId" /></td>
    <td><code>string</code></td>
    <td>Filter the alerts list by the Smart Group Id. Default value is none. Default value is None.</td>
</tr>
<tr id="parameter-sortBy">
    <td><CopyableCode code="sortBy" /></td>
    <td><code>string</code></td>
    <td>Sort the query results by input field, Default value is 'lastModifiedDateTime'. Known values are: "name", "severity", "alertState", "monitorCondition", "targetResource", "targetResourceName", "targetResourceGroup", "targetResourceType", "startDateTime", and "lastModifiedDateTime". Default value is None.</td>
</tr>
<tr id="parameter-sortOrder">
    <td><CopyableCode code="sortOrder" /></td>
    <td><code>string</code></td>
    <td>Sort the query results order in either ascending or descending. Default value is 'desc' for time fields and 'asc' for others. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
<tr id="parameter-targetResource">
    <td><CopyableCode code="targetResource" /></td>
    <td><code>string</code></td>
    <td>Filter by target resource( which is full ARM ID) Default value is select all. Default value is None.</td>
</tr>
<tr id="parameter-targetResourceGroup">
    <td><CopyableCode code="targetResourceGroup" /></td>
    <td><code>string</code></td>
    <td>Filter by target resource group name. Default value is select all. Default value is None.</td>
</tr>
<tr id="parameter-targetResourceType">
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>Filter by target resource type. Default value is select all. Default value is None.</td>
</tr>
<tr id="parameter-timeRange">
    <td><CopyableCode code="timeRange" /></td>
    <td><code>string</code></td>
    <td>Filter by time range by below listed values. Default value is 1 day. Known values are: "1h", "1d", "7d", and "30d". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_id"
    values={[
        { label: 'get_by_id', value: 'get_by_id' },
        { label: 'get_summary', value: 'get_summary' },
        { label: 'get_by_id_tenant', value: 'get_by_id_tenant' },
        { label: 'get_all', value: 'get_all' },
        { label: 'get_all_tenant', value: 'get_all_tenant' }
    ]}
>
<TabItem value="get_by_id">

Get a specific alert. Get information related to a specific alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to get alert by id then use parent resource of scope. So in this example get alert by id call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;'.

```sql
SELECT
id,
name,
context,
customProperties,
egressConfig,
essentials,
systemData,
type
FROM azure.alerts_management.alerts
WHERE scope = '{{ scope }}' -- required
AND alert_id = '{{ alert_id }}' -- required
;
```
</TabItem>
<TabItem value="get_summary">

Get a summarized count of your alerts grouped by various parameters (e.g. grouping by 'Severity' returns the count of alerts for each severity).

```sql
SELECT
id,
name,
groupedby,
smartGroupsCount,
total,
type,
values
FROM azure.alerts_management.alerts
WHERE scope = '{{ scope }}' -- required
AND groupby = '{{ groupby }}' -- required
AND includeSmartGroupsCount = '{{ includeSmartGroupsCount }}'
AND targetResource = '{{ targetResource }}'
AND targetResourceType = '{{ targetResourceType }}'
AND targetResourceGroup = '{{ targetResourceGroup }}'
AND monitorService = '{{ monitorService }}'
AND monitorCondition = '{{ monitorCondition }}'
AND severity = '{{ severity }}'
AND alertState = '{{ alertState }}'
AND alertRule = '{{ alertRule }}'
AND timeRange = '{{ timeRange }}'
AND customTimeRange = '{{ customTimeRange }}'
;
```
</TabItem>
<TabItem value="get_by_id_tenant">

Get a specific alert. Get information related to a specific alert.

```sql
SELECT
id,
name,
context,
customProperties,
egressConfig,
essentials,
systemData,
type
FROM azure.alerts_management.alerts
WHERE alert_id = '{{ alert_id }}' -- required
;
```
</TabItem>
<TabItem value="get_all">

List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.

```sql
SELECT
id,
name,
context,
customProperties,
egressConfig,
essentials,
systemData,
type
FROM azure.alerts_management.alerts
WHERE scope = '{{ scope }}' -- required
AND targetResource = '{{ targetResource }}'
AND targetResourceType = '{{ targetResourceType }}'
AND targetResourceGroup = '{{ targetResourceGroup }}'
AND monitorService = '{{ monitorService }}'
AND monitorCondition = '{{ monitorCondition }}'
AND severity = '{{ severity }}'
AND alertState = '{{ alertState }}'
AND alertRule = '{{ alertRule }}'
AND smartGroupId = '{{ smartGroupId }}'
AND includeContext = '{{ includeContext }}'
AND includeEgressConfig = '{{ includeEgressConfig }}'
AND pageCount = '{{ pageCount }}'
AND sortBy = '{{ sortBy }}'
AND sortOrder = '{{ sortOrder }}'
AND select = '{{ select }}'
AND timeRange = '{{ timeRange }}'
AND customTimeRange = '{{ customTimeRange }}'
;
```
</TabItem>
<TabItem value="get_all_tenant">

List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.

```sql
SELECT
id,
name,
context,
customProperties,
egressConfig,
essentials,
systemData,
type
FROM azure.alerts_management.alerts
WHERE targetResource = '{{ targetResource }}'
AND targetResourceType = '{{ targetResourceType }}'
AND targetResourceGroup = '{{ targetResourceGroup }}'
AND monitorService = '{{ monitorService }}'
AND monitorCondition = '{{ monitorCondition }}'
AND severity = '{{ severity }}'
AND alertState = '{{ alertState }}'
AND alertRule = '{{ alertRule }}'
AND smartGroupId = '{{ smartGroupId }}'
AND includeContext = '{{ includeContext }}'
AND includeEgressConfig = '{{ includeEgressConfig }}'
AND pageCount = '{{ pageCount }}'
AND sortBy = '{{ sortBy }}'
AND sortOrder = '{{ sortOrder }}'
AND select = '{{ select }}'
AND timeRange = '{{ timeRange }}'
AND customTimeRange = '{{ customTimeRange }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_history_tenant"
    values={[
        { label: 'get_history_tenant', value: 'get_history_tenant' },
        { label: 'get_history', value: 'get_history' },
        { label: 'get_enrichments', value: 'get_enrichments' },
        { label: 'change_state_tenant', value: 'change_state_tenant' },
        { label: 'change_state', value: 'change_state' },
        { label: 'meta_data', value: 'meta_data' }
    ]}
>
<TabItem value="get_history_tenant">

Get the history of an alert, which captures any monitor condition changes (Fired/Resolved), alert state changes (New/Acknowledged/Closed) and applied action rules for that particular alert.

```sql
EXEC azure.alerts_management.alerts.get_history_tenant 
@alert_id='{{ alert_id }}' --required
;
```
</TabItem>
<TabItem value="get_history">

Get the history of an alert, which captures any monitor condition changes (Fired/Resolved), alert state changes (New/Acknowledged/Closed) and applied action rules for that particular alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to get history of this particular alert then use parent resource of scope. So in this example get history call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;/history'.

```sql
EXEC azure.alerts_management.alerts.get_history 
@scope='{{ scope }}' --required, 
@alert_id='{{ alert_id }}' --required
;
```
</TabItem>
<TabItem value="get_enrichments">

Get the enrichments of an alert. It returns a collection of one object named default.

```sql
EXEC azure.alerts_management.alerts.get_enrichments 
@scope='{{ scope }}' --required, 
@alert_id='{{ alert_id }}' --required
;
```
</TabItem>
<TabItem value="change_state_tenant">

Change the state of an alert.

```sql
EXEC azure.alerts_management.alerts.change_state_tenant 
@alert_id='{{ alert_id }}' --required, 
@newState='{{ newState }}' --required 
@@json=
'{
"comments": "{{ comments }}"
}'
;
```
</TabItem>
<TabItem value="change_state">

Change the state of an alert. If scope is a deleted resource then please use scope as parent resource of the delete resource. For example if my alert id is '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.Compute/virtualMachines/vm1/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;' and 'vm1' is deleted then if you want to change state of this particular alert then use parent resource of scope. So in this example change state call will look like this: '/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.AlertsManagement/alerts/&#123;alertId&#125;'.

```sql
EXEC azure.alerts_management.alerts.change_state 
@scope='{{ scope }}' --required, 
@alert_id='{{ alert_id }}' --required, 
@newState='{{ newState }}' --required 
@@json=
'{
"comments": "{{ comments }}"
}'
;
```
</TabItem>
<TabItem value="meta_data">

List alerts meta data information based on value of identifier parameter.

```sql
EXEC azure.alerts_management.alerts.meta_data 
@identifier='{{ identifier }}' --required
;
```
</TabItem>
</Tabs>
