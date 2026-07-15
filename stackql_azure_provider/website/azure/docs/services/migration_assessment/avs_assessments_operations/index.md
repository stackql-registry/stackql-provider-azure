--- 
title: avs_assessments_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - avs_assessments_operations
  - migration_assessment
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

Creates, updates, deletes, gets or lists an <code>avs_assessments_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="avs_assessments_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migration_assessment.avs_assessments_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_group', value: 'list_by_group' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentErrorSummary" /></td>
    <td><code>object</code></td>
    <td>Gets the assessment error summary. This is the number of machines affected by each type of error in this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>Assessment type of the assessment. Known values are: "Unknown", "MachineAssessment", "AvsAssessment", "SqlAssessment", and "WebAppAssessment".</td>
</tr>
<tr>
    <td><CopyableCode code="azureLocation" /></td>
    <td><code>string</code></td>
    <td>Azure Location or Azure region where to which the machines will be migrated. Known values are: "Unknown", "EastAsia", "SoutheastAsia", "AustraliaEast", "AustraliaSoutheast", "BrazilSouth", "CanadaCentral", "CanadaEast", "WestEurope", "NorthEurope", "CentralIndia", "SouthIndia", "WestIndia", "JapanEast", "JapanWest", "KoreaCentral", "KoreaSouth", "UkWest", "UkSouth", "NorthCentralUs", "EastUs", "WestUs2", "SouthCentralUs", "CentralUs", "EastUs2", "WestUs", "WestCentralUs", "GermanyCentral", "GermanyNortheast", "ChinaNorth", "ChinaEast", "USGovArizona", "USGovTexas", "USGovIowa", "USGovVirginia", "USDoDCentral", "USDoDEast", "FranceCentral", "AustraliaCentral", "SouthAfricaNorth", "FranceSouth", "AustraliaCentral2", "SouthAfricaWest", "GermanyNorth", "GermanyWestCentral", "NorwayEast", "NorwayWest", "ChinaEast2", "ChinaNorth2", "SwitzerlandNorth", "SwitzerlandWest", "UAENorth", "UAECentral", "UsNatEast", "UsNatWest", "UsSecEast", "UsSecCentral", "UsSecWest", "SwedenCentral", and "QatarCentral".</td>
</tr>
<tr>
    <td><CopyableCode code="azureOfferCode" /></td>
    <td><code>string</code></td>
    <td>Azure Offer code according to which cost estimation is done. Known values are: "Unknown", "MSAZR0003P", "MSAZR0044P", "MSAZR0059P", "MSAZR0060P", "MSAZR0062P", "MSAZR0063P", "MSAZR0064P", "MSAZR0029P", "MSAZR0022P", "MSAZR0023P", "MSAZR0148P", "MSAZR0025P", "MSAZR0036P", "MSAZR0120P", "MSAZR0121P", "MSAZR0122P", "MSAZR0123P", "MSAZR0124P", "MSAZR0125P", "MSAZR0126P", "MSAZR0127P", "MSAZR0128P", "MSAZR0129P", "MSAZR0130P", "MSAZR0111P", "MSAZR0144P", "MSAZR0149P", "MSMCAZR0044P", "MSMCAZR0059P", "MSMCAZR0060P", "MSMCAZR0063P", "MSMCAZR0120P", "MSMCAZR0121P", "MSMCAZR0125P", "MSMCAZR0128P", "MSAZRDE0003P", "MSAZRDE0044P", "MSAZRUSGOV0003P", "EA", "MSAZR0243P", "SavingsPlan1Year", and "SavingsPlan3Year".</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted CPU utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and Time when assessment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency in which prices should be reported. Known values are: "Unknown", "USD", "DKK", "CAD", "IDR", "JPY", "KRW", "NZD", "NOK", "RUB", "SAR", "ZAR", "SEK", "TRY", "GBP", "MXN", "MYR", "INR", "HKD", "BRL", "TWD", "EUR", "CHF", "ARS", "AUD", "CNY", and "TRY".</td>
</tr>
<tr>
    <td><CopyableCode code="dedupeCompression" /></td>
    <td><code>number</code></td>
    <td>De-duplication compression.</td>
</tr>
<tr>
    <td><CopyableCode code="discountPercentage" /></td>
    <td><code>number</code></td>
    <td>Custom discount percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="failuresToTolerateAndRaidLevel" /></td>
    <td><code>string</code></td>
    <td>Failures to tolerate and RAID level in a common property. Known values are: "Unknown", "Ftt1Raid1", "Ftt1Raid5", "Ftt2Raid1", "Ftt2Raid6", and "Ftt3Raid1".</td>
</tr>
<tr>
    <td><CopyableCode code="groupType" /></td>
    <td><code>string</code></td>
    <td>Gets the group type for the assessment. Known values are: "Default", "Import", and "Import".</td>
</tr>
<tr>
    <td><CopyableCode code="isStretchClusterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Stretch Cluster Enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="limitingFactor" /></td>
    <td><code>string</code></td>
    <td>Limiting factor.</td>
</tr>
<tr>
    <td><CopyableCode code="memOvercommit" /></td>
    <td><code>number</code></td>
    <td>Memory overcommit.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeType" /></td>
    <td><code>string</code></td>
    <td>AVS node type. Known values are: "Unknown" and "AV36".</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfNodes" /></td>
    <td><code>integer</code></td>
    <td>Recommended number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="percentile" /></td>
    <td><code>string</code></td>
    <td>Percentile of the utilization data values to be considered while assessing machines. Known values are: "Percentile50", "Percentile90", "Percentile95", and "Percentile99".</td>
</tr>
<tr>
    <td><CopyableCode code="perfDataEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time to consider performance data for assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="perfDataStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time to consider performance data for assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="pricesTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="ramUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted RAM utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstance" /></td>
    <td><code>string</code></td>
    <td>Reserved instance. Known values are: "None", "RI1Year", and "RI3Year".</td>
</tr>
<tr>
    <td><CopyableCode code="scalingFactor" /></td>
    <td><code>number</code></td>
    <td>Percentage of buffer that user wants on performance metrics when recommending Azure sizes.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaVersion" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="stage" /></td>
    <td><code>string</code></td>
    <td>User configurable setting to display the Stage of Assessment. Known values are: "InProgress", "UnderReview", and "Approved".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Whether assessment is in valid state and all machines have been assessed. Known values are: "Created", "Updated", "Running", "Completed", "Invalid", "OutOfSync", "OutDated", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="storageUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted storage utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Assessment cloud suitability. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Assessment suitability explanation. Known values are: "Unknown", "NotApplicable", and "UnsupportedLocationForSelectedNode".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilitySummary" /></td>
    <td><code>object</code></td>
    <td>Cloud suitability summary for all the machines in the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeRange" /></td>
    <td><code>string</code></td>
    <td>Time Range for which the historic utilization data should be considered for assessment. Known values are: "Day", "Week", "Month", and "Custom".</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuCores" /></td>
    <td><code>number</code></td>
    <td>Predicted total CPU cores used.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMonthlyCost" /></td>
    <td><code>number</code></td>
    <td>Total monthly cost.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRamInGB" /></td>
    <td><code>number</code></td>
    <td>Predicted total RAM used in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageInGB" /></td>
    <td><code>number</code></td>
    <td>Predicted total Storage used in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and Time when assessment was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="vcpuOversubscription" /></td>
    <td><code>number</code></td>
    <td>VCPU over subscription.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_group">

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
    <td><CopyableCode code="assessmentErrorSummary" /></td>
    <td><code>object</code></td>
    <td>Gets the assessment error summary. This is the number of machines affected by each type of error in this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentType" /></td>
    <td><code>string</code></td>
    <td>Assessment type of the assessment. Known values are: "Unknown", "MachineAssessment", "AvsAssessment", "SqlAssessment", and "WebAppAssessment".</td>
</tr>
<tr>
    <td><CopyableCode code="azureLocation" /></td>
    <td><code>string</code></td>
    <td>Azure Location or Azure region where to which the machines will be migrated. Known values are: "Unknown", "EastAsia", "SoutheastAsia", "AustraliaEast", "AustraliaSoutheast", "BrazilSouth", "CanadaCentral", "CanadaEast", "WestEurope", "NorthEurope", "CentralIndia", "SouthIndia", "WestIndia", "JapanEast", "JapanWest", "KoreaCentral", "KoreaSouth", "UkWest", "UkSouth", "NorthCentralUs", "EastUs", "WestUs2", "SouthCentralUs", "CentralUs", "EastUs2", "WestUs", "WestCentralUs", "GermanyCentral", "GermanyNortheast", "ChinaNorth", "ChinaEast", "USGovArizona", "USGovTexas", "USGovIowa", "USGovVirginia", "USDoDCentral", "USDoDEast", "FranceCentral", "AustraliaCentral", "SouthAfricaNorth", "FranceSouth", "AustraliaCentral2", "SouthAfricaWest", "GermanyNorth", "GermanyWestCentral", "NorwayEast", "NorwayWest", "ChinaEast2", "ChinaNorth2", "SwitzerlandNorth", "SwitzerlandWest", "UAENorth", "UAECentral", "UsNatEast", "UsNatWest", "UsSecEast", "UsSecCentral", "UsSecWest", "SwedenCentral", and "QatarCentral".</td>
</tr>
<tr>
    <td><CopyableCode code="azureOfferCode" /></td>
    <td><code>string</code></td>
    <td>Azure Offer code according to which cost estimation is done. Known values are: "Unknown", "MSAZR0003P", "MSAZR0044P", "MSAZR0059P", "MSAZR0060P", "MSAZR0062P", "MSAZR0063P", "MSAZR0064P", "MSAZR0029P", "MSAZR0022P", "MSAZR0023P", "MSAZR0148P", "MSAZR0025P", "MSAZR0036P", "MSAZR0120P", "MSAZR0121P", "MSAZR0122P", "MSAZR0123P", "MSAZR0124P", "MSAZR0125P", "MSAZR0126P", "MSAZR0127P", "MSAZR0128P", "MSAZR0129P", "MSAZR0130P", "MSAZR0111P", "MSAZR0144P", "MSAZR0149P", "MSMCAZR0044P", "MSMCAZR0059P", "MSMCAZR0060P", "MSMCAZR0063P", "MSMCAZR0120P", "MSMCAZR0121P", "MSMCAZR0125P", "MSMCAZR0128P", "MSAZRDE0003P", "MSAZRDE0044P", "MSAZRUSGOV0003P", "EA", "MSAZR0243P", "SavingsPlan1Year", and "SavingsPlan3Year".</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="cpuUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted CPU utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and Time when assessment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="currency" /></td>
    <td><code>string</code></td>
    <td>Currency in which prices should be reported. Known values are: "Unknown", "USD", "DKK", "CAD", "IDR", "JPY", "KRW", "NZD", "NOK", "RUB", "SAR", "ZAR", "SEK", "TRY", "GBP", "MXN", "MYR", "INR", "HKD", "BRL", "TWD", "EUR", "CHF", "ARS", "AUD", "CNY", and "TRY".</td>
</tr>
<tr>
    <td><CopyableCode code="dedupeCompression" /></td>
    <td><code>number</code></td>
    <td>De-duplication compression.</td>
</tr>
<tr>
    <td><CopyableCode code="discountPercentage" /></td>
    <td><code>number</code></td>
    <td>Custom discount percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="failuresToTolerateAndRaidLevel" /></td>
    <td><code>string</code></td>
    <td>Failures to tolerate and RAID level in a common property. Known values are: "Unknown", "Ftt1Raid1", "Ftt1Raid5", "Ftt2Raid1", "Ftt2Raid6", and "Ftt3Raid1".</td>
</tr>
<tr>
    <td><CopyableCode code="groupType" /></td>
    <td><code>string</code></td>
    <td>Gets the group type for the assessment. Known values are: "Default", "Import", and "Import".</td>
</tr>
<tr>
    <td><CopyableCode code="isStretchClusterEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Is Stretch Cluster Enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="limitingFactor" /></td>
    <td><code>string</code></td>
    <td>Limiting factor.</td>
</tr>
<tr>
    <td><CopyableCode code="memOvercommit" /></td>
    <td><code>number</code></td>
    <td>Memory overcommit.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeType" /></td>
    <td><code>string</code></td>
    <td>AVS node type. Known values are: "Unknown" and "AV36".</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfMachines" /></td>
    <td><code>integer</code></td>
    <td>Number of machines part of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfNodes" /></td>
    <td><code>integer</code></td>
    <td>Recommended number of nodes.</td>
</tr>
<tr>
    <td><CopyableCode code="percentile" /></td>
    <td><code>string</code></td>
    <td>Percentile of the utilization data values to be considered while assessing machines. Known values are: "Percentile50", "Percentile90", "Percentile95", and "Percentile99".</td>
</tr>
<tr>
    <td><CopyableCode code="perfDataEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the end time to consider performance data for assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="perfDataStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the start time to consider performance data for assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="pricesTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".</td>
</tr>
<tr>
    <td><CopyableCode code="ramUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted RAM utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedInstance" /></td>
    <td><code>string</code></td>
    <td>Reserved instance. Known values are: "None", "RI1Year", and "RI3Year".</td>
</tr>
<tr>
    <td><CopyableCode code="scalingFactor" /></td>
    <td><code>number</code></td>
    <td>Percentage of buffer that user wants on performance metrics when recommending Azure sizes.</td>
</tr>
<tr>
    <td><CopyableCode code="schemaVersion" /></td>
    <td><code>string</code></td>
    <td>Schema version.</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="stage" /></td>
    <td><code>string</code></td>
    <td>User configurable setting to display the Stage of Assessment. Known values are: "InProgress", "UnderReview", and "Approved".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Whether assessment is in valid state and all machines have been assessed. Known values are: "Created", "Updated", "Running", "Completed", "Invalid", "OutOfSync", "OutDated", and "Deleted".</td>
</tr>
<tr>
    <td><CopyableCode code="storageUtilization" /></td>
    <td><code>number</code></td>
    <td>Predicted storage utilization.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Assessment cloud suitability. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Assessment suitability explanation. Known values are: "Unknown", "NotApplicable", and "UnsupportedLocationForSelectedNode".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilitySummary" /></td>
    <td><code>object</code></td>
    <td>Cloud suitability summary for all the machines in the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timeRange" /></td>
    <td><code>string</code></td>
    <td>Time Range for which the historic utilization data should be considered for assessment. Known values are: "Day", "Week", "Month", and "Custom".</td>
</tr>
<tr>
    <td><CopyableCode code="totalCpuCores" /></td>
    <td><code>number</code></td>
    <td>Predicted total CPU cores used.</td>
</tr>
<tr>
    <td><CopyableCode code="totalMonthlyCost" /></td>
    <td><code>number</code></td>
    <td>Total monthly cost.</td>
</tr>
<tr>
    <td><CopyableCode code="totalRamInGB" /></td>
    <td><code>number</code></td>
    <td>Predicted total RAM used in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="totalStorageInGB" /></td>
    <td><code>number</code></td>
    <td>Predicted total Storage used in GB.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and Time when assessment was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="vcpuOversubscription" /></td>
    <td><code>number</code></td>
    <td>VCPU over subscription.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AvsAssessment.</td>
</tr>
<tr>
    <td><a href="#list_by_group"><CopyableCode code="list_by_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List AvsAssessment resources by Group.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a AvsAssessment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a AvsAssessment.</td>
</tr>
<tr>
    <td><a href="#download_url"><CopyableCode code="download_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get download URL for the assessment report. Get the URL for downloading the assessment in a report format.</td>
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
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>AVS Assessment ARM name. Required.</td>
</tr>
<tr id="parameter-group_name">
    <td><CopyableCode code="group_name" /></td>
    <td><code>string</code></td>
    <td>Group ARM name. Required.</td>
</tr>
<tr id="parameter-project_name">
    <td><CopyableCode code="project_name" /></td>
    <td><code>string</code></td>
    <td>Assessment Project Name. Required.</td>
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
        { label: 'list_by_group', value: 'list_by_group' }
    ]}
>
<TabItem value="get">

Get a AvsAssessment.

```sql
SELECT
id,
name,
assessmentErrorSummary,
assessmentType,
azureLocation,
azureOfferCode,
confidenceRatingInPercentage,
cpuUtilization,
createdTimestamp,
currency,
dedupeCompression,
discountPercentage,
failuresToTolerateAndRaidLevel,
groupType,
isStretchClusterEnabled,
limitingFactor,
memOvercommit,
nodeType,
numberOfMachines,
numberOfNodes,
percentile,
perfDataEndTime,
perfDataStartTime,
pricesTimestamp,
provisioningState,
ramUtilization,
reservedInstance,
scalingFactor,
schemaVersion,
sizingCriterion,
stage,
status,
storageUtilization,
suitability,
suitabilityExplanation,
suitabilitySummary,
systemData,
timeRange,
totalCpuCores,
totalMonthlyCost,
totalRamInGB,
totalStorageInGB,
type,
updatedTimestamp,
vcpuOversubscription
FROM azure.migration_assessment.avs_assessments_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_group">

List AvsAssessment resources by Group.

```sql
SELECT
id,
name,
assessmentErrorSummary,
assessmentType,
azureLocation,
azureOfferCode,
confidenceRatingInPercentage,
cpuUtilization,
createdTimestamp,
currency,
dedupeCompression,
discountPercentage,
failuresToTolerateAndRaidLevel,
groupType,
isStretchClusterEnabled,
limitingFactor,
memOvercommit,
nodeType,
numberOfMachines,
numberOfNodes,
percentile,
perfDataEndTime,
perfDataStartTime,
pricesTimestamp,
provisioningState,
ramUtilization,
reservedInstance,
scalingFactor,
schemaVersion,
sizingCriterion,
stage,
status,
storageUtilization,
suitability,
suitabilityExplanation,
suitabilitySummary,
systemData,
timeRange,
totalCpuCores,
totalMonthlyCost,
totalRamInGB,
totalStorageInGB,
type,
updatedTimestamp,
vcpuOversubscription
FROM azure.migration_assessment.avs_assessments_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a AvsAssessment.

```sql
INSERT INTO azure.migration_assessment.avs_assessments_operations (
properties,
resource_group_name,
project_name,
group_name,
assessment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ project_name }}',
'{{ group_name }}',
'{{ assessment_name }}',
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
- name: avs_assessments_operations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the avs_assessments_operations resource.
    - name: project_name
      value: "{{ project_name }}"
      description: Required parameter for the avs_assessments_operations resource.
    - name: group_name
      value: "{{ group_name }}"
      description: Required parameter for the avs_assessments_operations resource.
    - name: assessment_name
      value: "{{ assessment_name }}"
      description: Required parameter for the avs_assessments_operations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the avs_assessments_operations resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        assessmentErrorSummary: "{{ assessmentErrorSummary }}"
        failuresToTolerateAndRaidLevel: "{{ failuresToTolerateAndRaidLevel }}"
        vcpuOversubscription: {{ vcpuOversubscription }}
        nodeType: "{{ nodeType }}"
        reservedInstance: "{{ reservedInstance }}"
        totalMonthlyCost: {{ totalMonthlyCost }}
        suitability: "{{ suitability }}"
        suitabilityExplanation: "{{ suitabilityExplanation }}"
        numberOfNodes: {{ numberOfNodes }}
        cpuUtilization: {{ cpuUtilization }}
        ramUtilization: {{ ramUtilization }}
        storageUtilization: {{ storageUtilization }}
        totalCpuCores: {{ totalCpuCores }}
        totalRamInGB: {{ totalRamInGB }}
        totalStorageInGB: {{ totalStorageInGB }}
        numberOfMachines: {{ numberOfMachines }}
        suitabilitySummary: "{{ suitabilitySummary }}"
        memOvercommit: {{ memOvercommit }}
        dedupeCompression: {{ dedupeCompression }}
        limitingFactor: "{{ limitingFactor }}"
        isStretchClusterEnabled: {{ isStretchClusterEnabled }}
        groupType: "{{ groupType }}"
        assessmentType: "{{ assessmentType }}"
        azureLocation: "{{ azureLocation }}"
        azureOfferCode: "{{ azureOfferCode }}"
        currency: "{{ currency }}"
        scalingFactor: {{ scalingFactor }}
        percentile: "{{ percentile }}"
        timeRange: "{{ timeRange }}"
        perfDataStartTime: "{{ perfDataStartTime }}"
        perfDataEndTime: "{{ perfDataEndTime }}"
        stage: "{{ stage }}"
        discountPercentage: {{ discountPercentage }}
        sizingCriterion: "{{ sizingCriterion }}"
        confidenceRatingInPercentage: {{ confidenceRatingInPercentage }}
        pricesTimestamp: "{{ pricesTimestamp }}"
        createdTimestamp: "{{ createdTimestamp }}"
        updatedTimestamp: "{{ updatedTimestamp }}"
        status: "{{ status }}"
        schemaVersion: "{{ schemaVersion }}"
`}</CodeBlock>

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

Delete a AvsAssessment.

```sql
DELETE FROM azure.migration_assessment.avs_assessments_operations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND project_name = '{{ project_name }}' --required
AND group_name = '{{ group_name }}' --required
AND assessment_name = '{{ assessment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="download_url"
    values={[
        { label: 'download_url', value: 'download_url' }
    ]}
>
<TabItem value="download_url">

Get download URL for the assessment report. Get the URL for downloading the assessment in a report format.

```sql
EXEC azure.migration_assessment.avs_assessments_operations.download_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@project_name='{{ project_name }}' --required, 
@group_name='{{ group_name }}' --required, 
@assessment_name='{{ assessment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
