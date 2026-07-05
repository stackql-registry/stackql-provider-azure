--- 
title: assessed_sql_machines_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessed_sql_machines_operations
  - migrationassessment
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

Creates, updates, deletes, gets or lists an <code>assessed_sql_machines_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessed_sql_machines_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrationassessment.assessed_sql_machines_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_assessment_v2', value: 'list_by_sql_assessment_v2' }
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
    <td><CopyableCode code="biosGuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the BIOS GUID for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bootType" /></td>
    <td><code>string</code></td>
    <td>Boot type of machine discovered in private data center. Known values are: "Unknown", "EFI", "BIOS", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="costComponents" /></td>
    <td><code>array</code></td>
    <td>Gets the collection of cost components.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Data center machine ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>Data center management server ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>Data center management server name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>Gets the list of data disks that were assessed as part of this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the FQDN for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationGuidelines" /></td>
    <td><code>array</code></td>
    <td>Gets the list of migration guidelines applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyBandwidthCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly networking cost.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyComputeCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly compute cost calculated for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyStorageCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly total storage cost.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>Gets the list of network adapters that were assessed as part of this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemArchitecture" /></td>
    <td><code>string</code></td>
    <td>Operating system architecture as reported by datacenter management solution. Known values are: "Unknown", "X86", and "X64".</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemName" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemType" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Cores Utilized noted during time period T. Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageMemoryUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Memory Utilized noted during time period T. .. code-block:: Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmFamily" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Recommended Azure VM Family for the machine. Known values are: "Unknown", "Basic_A0_A4", "Standard_A0_A7", "Standard_A8_A11", "Av2_series", "D_series", "Dv2_series", "DS_series", "DSv2_series", "F_series", "Fs_series", "G_series", "GS_series", "H_series", "Ls_series", "Dsv3_series", "Dv3_series", "Fsv2_series", "Ev3_series", "Esv3_series", "M_series", "DC_Series", "Lsv2_series", "Ev4_series", "Esv4_series", "Edv4_series", "Edsv4_series", "Dv4_series", "Dsv4_series", "Ddv4_series", "Ddsv4_series", "Easv4_series", "Dasv4_series", "Mv2_series", "Eav4_series", "Dav4_series", "Msv2_series", "Mdsv2_series", "Dv5_series", "Dsv5_series", "Ddv5_series", "Ddsv5_series", "Dasv5_series", "Dadsv5_series", "Ev5_series", "Esv5_series", "Edv5_series", "Edsv5_series", "Easv5_series", "Eadsv5_series", "Ebsv5_series", and "Ebdsv5_series".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSize" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Recommended Azure Size for the machine. Known values are: "Unknown", "Basic_A0", "Basic_A1", "Basic_A2", "Basic_A3", "Basic_A4", "Standard_A0", "Standard_A1", "Standard_A2", "Standard_A3", "Standard_A4", "Standard_A5", "Standard_A6", "Standard_A7", "Standard_A8", "Standard_A9", "Standard_A10", "Standard_A11", "Standard_A1_v2", "Standard_A2_v2", "Standard_A4_v2", "Standard_A8_v2", "Standard_A2m_v2", "Standard_A4m_v2", "Standard_A8m_v2", "Standard_D1", "Standard_D2", "Standard_D3", "Standard_D4", "Standard_D11", "Standard_D12", "Standard_D13", "Standard_D14", "Standard_D1_v2", "Standard_D2_v2", "Standard_D3_v2", "Standard_D4_v2", "Standard_D5_v2", "Standard_D11_v2", "Standard_D12_v2", "Standard_D13_v2", "Standard_D14_v2", "Standard_D15_v2", "Standard_DS1", "Standard_DS2", "Standard_DS3", "Standard_DS4", "Standard_DS11", "Standard_DS12", "Standard_DS13", "Standard_DS14", "Standard_DS1_v2", "Standard_DS2_v2", "Standard_DS3_v2", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_DS11_v2", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2", "Standard_F1", "Standard_F2", "Standard_F4", "Standard_F8", "Standard_F16", "Standard_F1s", "Standard_F2s", "Standard_F4s", "Standard_F8s", "Standard_F16s", "Standard_G1", "Standard_G2", "Standard_G3", "Standard_G4", "Standard_G5", "Standard_GS1", "Standard_GS2", "Standard_GS3", "Standard_GS4", "Standard_GS5", "Standard_H8", "Standard_H16", "Standard_H8m", "Standard_H16m", "Standard_H16r", "Standard_H16mr", "Standard_L4s", "Standard_L8s", "Standard_L16s", "Standard_L32s", "Standard_D2s_v3", "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3", "Standard_D64s_v3", "Standard_D2_v3", "Standard_D4_v3", "Standard_D8_v3", "Standard_D16_v3", "Standard_D32_v3", "Standard_D64_v3", "Standard_F2s_v2", "Standard_F4s_v2", "Standard_F8s_v2", "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_E2_v3", "Standard_E4_v3", "Standard_E8_v3", "Standard_E16_v3", "Standard_E32_v3", "Standard_E64_v3", "Standard_E2s_v3", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E32s_v3", "Standard_E64s_v3", "Standard_M64s", "Standard_M64ms", "Standard_M128s", "Standard_M128ms", "Standard_DC2s", "Standard_DC4s", "Standard_E20_v3", "Standard_E20s_v3", "Standard_E64i_v3", "Standard_E64is_v3", "Standard_M8ms", "Standard_M16ms", "Standard_M32ls", "Standard_M32ms", "Standard_M32ts", "Standard_M64", "Standard_M64ls", "Standard_M64m", "Standard_M128", "Standard_M128m", "Standard_L8s_v2", "Standard_L16s_v2", "Standard_L32s_v2", "Standard_L48s_v2", "Standard_L64s_v2", "Standard_L80s_v2", "Standard_D2_v4", "Standard_D4_v4", "Standard_D8_v4", "Standard_D16_v4", "Standard_D32_v4", "Standard_D48_v4", "Standard_D64_v4", "Standard_D2s_v4", "Standard_D4s_v4", "Standard_D8s_v4", "Standard_D16s_v4", "Standard_D32s_v4", "Standard_D48s_v4", "Standard_D64s_v4", "Standard_D2d_v4", "Standard_D4d_v4", "Standard_D8d_v4", "Standard_D16d_v4", "Standard_D32d_v4", "Standard_D48d_v4", "Standard_D64d_v4", "Standard_D2ds_v4", "Standard_D4ds_v4", "Standard_D8ds_v4", "Standard_D16ds_v4", "Standard_D32ds_v4", "Standard_D48ds_v4", "Standard_D64ds_v4", "Standard_E2_v4", "Standard_E4_v4", "Standard_E8_v4", "Standard_E16_v4", "Standard_E20_v4", "Standard_E32_v4", "Standard_E48_v4", "Standard_E64_v4", "Standard_E2s_v4", "Standard_E4s_v4", "Standard_E8s_v4", "Standard_E16s_v4", "Standard_E20s_v4", "Standard_E32s_v4", "Standard_E48s_v4", "Standard_E64s_v4", "Standard_E2d_v4", "Standard_E4d_v4", "Standard_E8d_v4", "Standard_E16d_v4", "Standard_E20d_v4", "Standard_E32d_v4", "Standard_E48d_v4", "Standard_E64d_v4", "Standard_E2ds_v4", "Standard_E4ds_v4", "Standard_E8ds_v4", "Standard_E16ds_v4", "Standard_E20ds_v4", "Standard_E32ds_v4", "Standard_E48ds_v4", "Standard_E64ds_v4", "Standard_E2as_v4", "Standard_E4as_v4", "Standard_E8as_v4", "Standard_E16as_v4", "Standard_E20as_v4", "Standard_E32as_v4", "Standard_E48as_v4", "Standard_E64as_v4", "Standard_E96as_v4", "Standard_D2as_v4", "Standard_D4as_v4", "Standard_D8as_v4", "Standard_D16as_v4", "Standard_D32as_v4", "Standard_D48as_v4", "Standard_D64as_v4", "Standard_D96as_v4", "Standard_M208ms_v2", "Standard_M208s_v2", "Standard_M416ms_v2", "Standard_M416s_v2", "Standard_F48s_v2", "Standard_E48_v3", "Standard_E48s_v3", "Standard_E80is_v4", "Standard_E80ids_v4", "Standard_E2a_v4", "Standard_E4a_v4", "Standard_E8a_v4", "Standard_E16a_v4", "Standard_E20a_v4", "Standard_E32a_v4", "Standard_E48a_v4", "Standard_E64a_v4", "Standard_E96a_v4", "Standard_D2a_v4", "Standard_D4a_v4", "Standard_D8a_v4", "Standard_D16a_v4", "Standard_D32a_v4", "Standard_D48a_v4", "Standard_D64a_v4", "Standard_D96a_v4", "Standard_M32ms_v2", "Standard_M64s_v2", "Standard_M64ms_v2", "Standard_M128s_v2", "Standard_M128ms_v2", "Standard_M192is_v2", "Standard_M192ims_v2", "Standard_M32dms_v2", "Standard_M64ds_v2", "Standard_M64dms_v2", "Standard_M128ds_v2", "Standard_M128dms_v2", "Standard_M192ids_v2", "Standard_M192idms_v2", "Standard_D2_v5", "Standard_D4_v5", "Standard_D8_v5", "Standard_D16_v5", "Standard_D32_v5", "Standard_D48_v5", "Standard_D64_v5", "Standard_D96_v5", "Standard_D2s_v5", "Standard_D4s_v5", "Standard_D8s_v5", "Standard_D16s_v5", "Standard_D32s_v5", "Standard_D48s_v5", "Standard_D64s_v5", "Standard_D96s_v5", "Standard_D2d_v5", "Standard_D4d_v5", "Standard_D8d_v5", "Standard_D16d_v5", "Standard_D32d_v5", "Standard_D48d_v5", "Standard_D64d_v5", "Standard_D96d_v5", "Standard_D2ds_v5", "Standard_D4ds_v5", "Standard_D8ds_v5", "Standard_D16ds_v5", "Standard_D32ds_v5", "Standard_D48ds_v5", "Standard_D64ds_v5", "Standard_D96ds_v5", "Standard_D2as_v5", "Standard_D4as_v5", "Standard_D8as_v5", "Standard_D16as_v5", "Standard_D32as_v5", "Standard_D48as_v5", "Standard_D64as_v5", "Standard_D96as_v5", "Standard_D2ads_v5", "Standard_D4ads_v5", "Standard_D8ads_v5", "Standard_D16ads_v5", "Standard_D32ads_v5", "Standard_D48ads_v5", "Standard_D64ads_v5", "Standard_D96ads_v5", "Standard_E2_v5", "Standard_E4_v5", "Standard_E8_v5", "Standard_E16_v5", "Standard_E20_v5", "Standard_E32_v5", "Standard_E48_v5", "Standard_E64_v5", "Standard_E96_v5", "Standard_E104i_v5", "Standard_E2s_v5", "Standard_E4s_v5", "Standard_E8s_v5", "Standard_E16s_v5", "Standard_E20s_v5", "Standard_E32s_v5", "Standard_E48s_v5", "Standard_E64s_v5", "Standard_E96s_v5", "Standard_E104is_v5", "Standard_E2d_v5", "Standard_E4d_v5", "Standard_E8d_v5", "Standard_E16d_v5", "Standard_E20d_v5", "Standard_E32d_v5", "Standard_E48d_v5", "Standard_E64d_v5", "Standard_E96d_v5", "Standard_E104id_v5", "Standard_E2ds_v5", "Standard_E4ds_v5", "Standard_E8ds_v5", "Standard_E16ds_v5", "Standard_E20ds_v5", "Standard_E32ds_v5", "Standard_E48ds_v5", "Standard_E64ds_v5", "Standard_E96ds_v5", "Standard_E104ids_v5", "Standard_E2as_v5", "Standard_E4as_v5", "Standard_E8as_v5", "Standard_E16as_v5", "Standard_E20as_v5", "Standard_E32as_v5", "Standard_E48as_v5", "Standard_E64as_v5", "Standard_E96as_v5", "Standard_E2ads_v5", "Standard_E4ads_v5", "Standard_E8ads_v5", "Standard_E16ads_v5", "Standard_E20ads_v5", "Standard_E32ads_v5", "Standard_E48ads_v5", "Standard_E64ads_v5", "Standard_E96ads_v5", "Standard_M8_2ms", "Standard_M8_4ms", "Standard_M16_4ms", "Standard_M16_8ms", "Standard_M32_8ms", "Standard_M32_16ms", "Standard_M64_32ms", "Standard_M64_16ms", "Standard_M128_64ms", "Standard_M128_32ms", "Standard_E4_2s_v3", "Standard_E8_4s_v3", "Standard_E8_2s_v3", "Standard_E16_8s_v3", "Standard_E16_4s_v3", "Standard_E32_16s_v3", "Standard_E32_8s_v3", "Standard_E64_32s_v3", "Standard_E64_16s_v3", "Standard_E4_2s_v4", "Standard_E8_4s_v4", "Standard_E8_2s_v4", "Standard_E16_8s_v4", "Standard_E16_4s_v4", "Standard_E32_16s_v4", "Standard_E32_8s_v4", "Standard_E64_32s_v4", "Standard_E64_16s_v4", "Standard_E4_2ds_v4", "Standard_E8_4ds_v4", "Standard_E8_2ds_v4", "Standard_E16_8ds_v4", "Standard_E16_4ds_v4", "Standard_E32_16ds_v4", "Standard_E32_8ds_v4", "Standard_E64_32ds_v4", "Standard_E64_16ds_v4", "Standard_E4_2as_v4", "Standard_E8_4as_v4", "Standard_E8_2as_v4", "Standard_E16_8as_v4", "Standard_E16_4as_v4", "Standard_E32_16as_v4", "Standard_E32_8as_v4", "Standard_E64_32as_v4", "Standard_E64_16as_v4", "Standard_E96_48as_v4", "Standard_E96_24as_v4", "Standard_E4_2ads_v5", "Standard_E8_4ads_v5", "Standard_E8_2ads_v5", "Standard_E16_8ads_v5", "Standard_E16_4ads_v5", "Standard_E32_16ads_v5", "Standard_E32_8ads_v5", "Standard_E64_32ads_v5", "Standard_E64_16ads_v5", "Standard_E96_48ads_v5", "Standard_E96_24ads_v5", "Standard_E4_2s_v5", "Standard_E8_4s_v5", "Standard_E8_2s_v5", "Standard_E16_8s_v5", "Standard_E16_4s_v5", "Standard_E32_16s_v5", "Standard_E32_8s_v5", "Standard_E64_32s_v5", "Standard_E64_16s_v5", "Standard_E96_48s_v5", "Standard_E96_24s_v5", "Standard_E4_2ds_v5", "Standard_E8_4ds_v5", "Standard_E8_2ds_v5", "Standard_E16_8ds_v5", "Standard_E16_4ds_v5", "Standard_E32_16ds_v5", "Standard_E32_8ds_v5", "Standard_E64_32ds_v5", "Standard_E64_16ds_v5", "Standard_E96_48ds_v5", "Standard_E96_24ds_v5", "Standard_E4_2as_v5", "Standard_E8_4as_v5", "Standard_E8_2as_v5", "Standard_E16_8as_v5", "Standard_E16_4as_v5", "Standard_E32_16as_v5", "Standard_E32_8as_v5", "Standard_E64_32as_v5", "Standard_E64_16as_v5", "Standard_E96_48as_v5", "Standard_E96_24as_v5", "Standard_GS4_8", "Standard_GS4_4", "Standard_GS5_16", "Standard_GS5_8", "Standard_DS11_1_v2", "Standard_DS12_2_v2", "Standard_DS12_1_v2", "Standard_DS13_4_v2", "Standard_DS13_2_v2", "Standard_DS14_8_v2", "Standard_DS14_4_v2", "Standard_M416_208s_v2", "Standard_M416_208ms_v2", "Standard_E2bs_v5", "Standard_E4bs_v5", "Standard_E8bs_v5", "Standard_E16bs_v5", "Standard_E32bs_v5", "Standard_E48bs_v5", "Standard_E64bs_v5", "Standard_E2bds_v5", "Standard_E4bds_v5", "Standard_E8bds_v5", "Standard_E16bds_v5", "Standard_E32bds_v5", "Standard_E48bds_v5", and "Standard_E64bds_v5".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSizeMegabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the Megabytes of memory for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSizeNumberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the Number of cores for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="securitySuitability" /></td>
    <td><code>string</code></td>
    <td>Gets the suitability for Microsoft cloud defender. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstances" /></td>
    <td><code>array</code></td>
    <td>Gets the list of SQL instances discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether machine is suitable for the cloud platform selected. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityDetail" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the detailed messages that were set on the machine during evaluation. Known values are: "None", "RecommendedSizeHasLessNetworkAdapters", "CannotReportComputeCost", "CannotReportStorageCost", "CannotReportBandwidthCosts", "PercentageOfCoresUtilizedMissing", "PercentageOfMemoryUtilizedMissing", "PercentageOfCoresUtilizedOutOfRange", and "PercentageOfMemoryUtilizedOutOfRange".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the explanation if machine is not suitable for cloud. Known values are: "Unknown", "NotApplicable", "GuestOperatingSystemArchitectureNotSupported", "GuestOperatingSystemNotSupported", "BootTypeNotSupported", "MoreDisksThanSupported", "NoSuitableVmSizeFound", "OneOrMoreDisksNotSuitable", "OneOrMoreAdaptersNotSuitable", "InternalErrorOccurredDuringComputeEvaluation", "InternalErrorOccurredDuringStorageEvaluation", "InternalErrorOccurredDuringNetworkEvaluation", "NoVmSizeSupportsStoragePerformance", "NoVmSizeSupportsNetworkPerformance", "NoVmSizeForSelectedPricingTier", "NoVmSizeForSelectedAzureLocation", "CheckRedHatLinuxVersion", "CheckOpenSuseLinuxVersion", "CheckWindowsServer2008R2Version", "CheckCentOsVersion", "CheckDebianLinuxVersion", "CheckSuseLinuxVersion", "CheckOracleLinuxVersion", "CheckUbuntuLinuxVersion", "CheckCoreOsLinuxVersion", "WindowsServerVersionConditionallySupported", "NoGuestOperatingSystemConditionallySupported", "WindowsClientVersionsConditionallySupported", "BootTypeUnknown", "GuestOperatingSystemUnknown", "WindowsServerVersionsSupportedWithCaveat", "WindowsOSNoLongerUnderMSSupport", "EndorsedWithConditionsLinuxDistributions", "UnendorsedLinuxDistributions", "NoVmSizeForStandardPricingTier", "NoVmSizeForBasicPricingTier", "NoVmSizeInSelectedFamilyFound", "NoEaPriceFoundForVmSize", and "NoVmSizeFoundForOfferCurrencyReservedInstance".</td>
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
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine last updated.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sql_assessment_v2">

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
    <td><CopyableCode code="biosGuid" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the BIOS GUID for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="bootType" /></td>
    <td><code>string</code></td>
    <td>Boot type of machine discovered in private data center. Known values are: "Unknown", "EFI", "BIOS", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="confidenceRatingInPercentage" /></td>
    <td><code>number</code></td>
    <td>Confidence Rating in Percentage.</td>
</tr>
<tr>
    <td><CopyableCode code="costComponents" /></td>
    <td><code>array</code></td>
    <td>Gets the collection of cost components.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine first created.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterMachineArmId" /></td>
    <td><code>string</code></td>
    <td>Data center machine ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerArmId" /></td>
    <td><code>string</code></td>
    <td>Data center management server ARM id.</td>
</tr>
<tr>
    <td><CopyableCode code="datacenterManagementServerName" /></td>
    <td><code>string</code></td>
    <td>Data center management server name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="disks" /></td>
    <td><code>object</code></td>
    <td>Gets the list of data disks that were assessed as part of this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display Name of the Machine.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the FQDN for the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="megabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Megabytes of memory found allocated for the machine in private data center.</td>
</tr>
<tr>
    <td><CopyableCode code="migrationGuidelines" /></td>
    <td><code>array</code></td>
    <td>Gets the list of migration guidelines applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyBandwidthCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly networking cost.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyComputeCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly compute cost calculated for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="monthlyStorageCost" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the monthly total storage cost.</td>
</tr>
<tr>
    <td><CopyableCode code="networkAdapters" /></td>
    <td><code>object</code></td>
    <td>Gets the list of network adapters that were assessed as part of this assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Number of CPU cores found on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemArchitecture" /></td>
    <td><code>string</code></td>
    <td>Operating system architecture as reported by datacenter management solution. Known values are: "Unknown", "X86", and "X64".</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemName" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemType" /></td>
    <td><code>string</code></td>
    <td>Operating system as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemVersion" /></td>
    <td><code>string</code></td>
    <td>Operating system version as reported by datacenter management solution.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageCoresUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Cores Utilized noted during time period T. Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="percentageMemoryUtilization" /></td>
    <td><code>number</code></td>
    <td>Percentile of Percentage of Memory Utilized noted during time period T. .. code-block:: Here N and T are settings on Assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="productSupportStatus" /></td>
    <td><code>object</code></td>
    <td>Gets the product support status related details.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmFamily" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Recommended Azure VM Family for the machine. Known values are: "Unknown", "Basic_A0_A4", "Standard_A0_A7", "Standard_A8_A11", "Av2_series", "D_series", "Dv2_series", "DS_series", "DSv2_series", "F_series", "Fs_series", "G_series", "GS_series", "H_series", "Ls_series", "Dsv3_series", "Dv3_series", "Fsv2_series", "Ev3_series", "Esv3_series", "M_series", "DC_Series", "Lsv2_series", "Ev4_series", "Esv4_series", "Edv4_series", "Edsv4_series", "Dv4_series", "Dsv4_series", "Ddv4_series", "Ddsv4_series", "Easv4_series", "Dasv4_series", "Mv2_series", "Eav4_series", "Dav4_series", "Msv2_series", "Mdsv2_series", "Dv5_series", "Dsv5_series", "Ddv5_series", "Ddsv5_series", "Dasv5_series", "Dadsv5_series", "Ev5_series", "Esv5_series", "Edv5_series", "Edsv5_series", "Easv5_series", "Eadsv5_series", "Ebsv5_series", and "Ebdsv5_series".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSize" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Recommended Azure Size for the machine. Known values are: "Unknown", "Basic_A0", "Basic_A1", "Basic_A2", "Basic_A3", "Basic_A4", "Standard_A0", "Standard_A1", "Standard_A2", "Standard_A3", "Standard_A4", "Standard_A5", "Standard_A6", "Standard_A7", "Standard_A8", "Standard_A9", "Standard_A10", "Standard_A11", "Standard_A1_v2", "Standard_A2_v2", "Standard_A4_v2", "Standard_A8_v2", "Standard_A2m_v2", "Standard_A4m_v2", "Standard_A8m_v2", "Standard_D1", "Standard_D2", "Standard_D3", "Standard_D4", "Standard_D11", "Standard_D12", "Standard_D13", "Standard_D14", "Standard_D1_v2", "Standard_D2_v2", "Standard_D3_v2", "Standard_D4_v2", "Standard_D5_v2", "Standard_D11_v2", "Standard_D12_v2", "Standard_D13_v2", "Standard_D14_v2", "Standard_D15_v2", "Standard_DS1", "Standard_DS2", "Standard_DS3", "Standard_DS4", "Standard_DS11", "Standard_DS12", "Standard_DS13", "Standard_DS14", "Standard_DS1_v2", "Standard_DS2_v2", "Standard_DS3_v2", "Standard_DS4_v2", "Standard_DS5_v2", "Standard_DS11_v2", "Standard_DS12_v2", "Standard_DS13_v2", "Standard_DS14_v2", "Standard_DS15_v2", "Standard_F1", "Standard_F2", "Standard_F4", "Standard_F8", "Standard_F16", "Standard_F1s", "Standard_F2s", "Standard_F4s", "Standard_F8s", "Standard_F16s", "Standard_G1", "Standard_G2", "Standard_G3", "Standard_G4", "Standard_G5", "Standard_GS1", "Standard_GS2", "Standard_GS3", "Standard_GS4", "Standard_GS5", "Standard_H8", "Standard_H16", "Standard_H8m", "Standard_H16m", "Standard_H16r", "Standard_H16mr", "Standard_L4s", "Standard_L8s", "Standard_L16s", "Standard_L32s", "Standard_D2s_v3", "Standard_D4s_v3", "Standard_D8s_v3", "Standard_D16s_v3", "Standard_D32s_v3", "Standard_D64s_v3", "Standard_D2_v3", "Standard_D4_v3", "Standard_D8_v3", "Standard_D16_v3", "Standard_D32_v3", "Standard_D64_v3", "Standard_F2s_v2", "Standard_F4s_v2", "Standard_F8s_v2", "Standard_F16s_v2", "Standard_F32s_v2", "Standard_F64s_v2", "Standard_F72s_v2", "Standard_E2_v3", "Standard_E4_v3", "Standard_E8_v3", "Standard_E16_v3", "Standard_E32_v3", "Standard_E64_v3", "Standard_E2s_v3", "Standard_E4s_v3", "Standard_E8s_v3", "Standard_E16s_v3", "Standard_E32s_v3", "Standard_E64s_v3", "Standard_M64s", "Standard_M64ms", "Standard_M128s", "Standard_M128ms", "Standard_DC2s", "Standard_DC4s", "Standard_E20_v3", "Standard_E20s_v3", "Standard_E64i_v3", "Standard_E64is_v3", "Standard_M8ms", "Standard_M16ms", "Standard_M32ls", "Standard_M32ms", "Standard_M32ts", "Standard_M64", "Standard_M64ls", "Standard_M64m", "Standard_M128", "Standard_M128m", "Standard_L8s_v2", "Standard_L16s_v2", "Standard_L32s_v2", "Standard_L48s_v2", "Standard_L64s_v2", "Standard_L80s_v2", "Standard_D2_v4", "Standard_D4_v4", "Standard_D8_v4", "Standard_D16_v4", "Standard_D32_v4", "Standard_D48_v4", "Standard_D64_v4", "Standard_D2s_v4", "Standard_D4s_v4", "Standard_D8s_v4", "Standard_D16s_v4", "Standard_D32s_v4", "Standard_D48s_v4", "Standard_D64s_v4", "Standard_D2d_v4", "Standard_D4d_v4", "Standard_D8d_v4", "Standard_D16d_v4", "Standard_D32d_v4", "Standard_D48d_v4", "Standard_D64d_v4", "Standard_D2ds_v4", "Standard_D4ds_v4", "Standard_D8ds_v4", "Standard_D16ds_v4", "Standard_D32ds_v4", "Standard_D48ds_v4", "Standard_D64ds_v4", "Standard_E2_v4", "Standard_E4_v4", "Standard_E8_v4", "Standard_E16_v4", "Standard_E20_v4", "Standard_E32_v4", "Standard_E48_v4", "Standard_E64_v4", "Standard_E2s_v4", "Standard_E4s_v4", "Standard_E8s_v4", "Standard_E16s_v4", "Standard_E20s_v4", "Standard_E32s_v4", "Standard_E48s_v4", "Standard_E64s_v4", "Standard_E2d_v4", "Standard_E4d_v4", "Standard_E8d_v4", "Standard_E16d_v4", "Standard_E20d_v4", "Standard_E32d_v4", "Standard_E48d_v4", "Standard_E64d_v4", "Standard_E2ds_v4", "Standard_E4ds_v4", "Standard_E8ds_v4", "Standard_E16ds_v4", "Standard_E20ds_v4", "Standard_E32ds_v4", "Standard_E48ds_v4", "Standard_E64ds_v4", "Standard_E2as_v4", "Standard_E4as_v4", "Standard_E8as_v4", "Standard_E16as_v4", "Standard_E20as_v4", "Standard_E32as_v4", "Standard_E48as_v4", "Standard_E64as_v4", "Standard_E96as_v4", "Standard_D2as_v4", "Standard_D4as_v4", "Standard_D8as_v4", "Standard_D16as_v4", "Standard_D32as_v4", "Standard_D48as_v4", "Standard_D64as_v4", "Standard_D96as_v4", "Standard_M208ms_v2", "Standard_M208s_v2", "Standard_M416ms_v2", "Standard_M416s_v2", "Standard_F48s_v2", "Standard_E48_v3", "Standard_E48s_v3", "Standard_E80is_v4", "Standard_E80ids_v4", "Standard_E2a_v4", "Standard_E4a_v4", "Standard_E8a_v4", "Standard_E16a_v4", "Standard_E20a_v4", "Standard_E32a_v4", "Standard_E48a_v4", "Standard_E64a_v4", "Standard_E96a_v4", "Standard_D2a_v4", "Standard_D4a_v4", "Standard_D8a_v4", "Standard_D16a_v4", "Standard_D32a_v4", "Standard_D48a_v4", "Standard_D64a_v4", "Standard_D96a_v4", "Standard_M32ms_v2", "Standard_M64s_v2", "Standard_M64ms_v2", "Standard_M128s_v2", "Standard_M128ms_v2", "Standard_M192is_v2", "Standard_M192ims_v2", "Standard_M32dms_v2", "Standard_M64ds_v2", "Standard_M64dms_v2", "Standard_M128ds_v2", "Standard_M128dms_v2", "Standard_M192ids_v2", "Standard_M192idms_v2", "Standard_D2_v5", "Standard_D4_v5", "Standard_D8_v5", "Standard_D16_v5", "Standard_D32_v5", "Standard_D48_v5", "Standard_D64_v5", "Standard_D96_v5", "Standard_D2s_v5", "Standard_D4s_v5", "Standard_D8s_v5", "Standard_D16s_v5", "Standard_D32s_v5", "Standard_D48s_v5", "Standard_D64s_v5", "Standard_D96s_v5", "Standard_D2d_v5", "Standard_D4d_v5", "Standard_D8d_v5", "Standard_D16d_v5", "Standard_D32d_v5", "Standard_D48d_v5", "Standard_D64d_v5", "Standard_D96d_v5", "Standard_D2ds_v5", "Standard_D4ds_v5", "Standard_D8ds_v5", "Standard_D16ds_v5", "Standard_D32ds_v5", "Standard_D48ds_v5", "Standard_D64ds_v5", "Standard_D96ds_v5", "Standard_D2as_v5", "Standard_D4as_v5", "Standard_D8as_v5", "Standard_D16as_v5", "Standard_D32as_v5", "Standard_D48as_v5", "Standard_D64as_v5", "Standard_D96as_v5", "Standard_D2ads_v5", "Standard_D4ads_v5", "Standard_D8ads_v5", "Standard_D16ads_v5", "Standard_D32ads_v5", "Standard_D48ads_v5", "Standard_D64ads_v5", "Standard_D96ads_v5", "Standard_E2_v5", "Standard_E4_v5", "Standard_E8_v5", "Standard_E16_v5", "Standard_E20_v5", "Standard_E32_v5", "Standard_E48_v5", "Standard_E64_v5", "Standard_E96_v5", "Standard_E104i_v5", "Standard_E2s_v5", "Standard_E4s_v5", "Standard_E8s_v5", "Standard_E16s_v5", "Standard_E20s_v5", "Standard_E32s_v5", "Standard_E48s_v5", "Standard_E64s_v5", "Standard_E96s_v5", "Standard_E104is_v5", "Standard_E2d_v5", "Standard_E4d_v5", "Standard_E8d_v5", "Standard_E16d_v5", "Standard_E20d_v5", "Standard_E32d_v5", "Standard_E48d_v5", "Standard_E64d_v5", "Standard_E96d_v5", "Standard_E104id_v5", "Standard_E2ds_v5", "Standard_E4ds_v5", "Standard_E8ds_v5", "Standard_E16ds_v5", "Standard_E20ds_v5", "Standard_E32ds_v5", "Standard_E48ds_v5", "Standard_E64ds_v5", "Standard_E96ds_v5", "Standard_E104ids_v5", "Standard_E2as_v5", "Standard_E4as_v5", "Standard_E8as_v5", "Standard_E16as_v5", "Standard_E20as_v5", "Standard_E32as_v5", "Standard_E48as_v5", "Standard_E64as_v5", "Standard_E96as_v5", "Standard_E2ads_v5", "Standard_E4ads_v5", "Standard_E8ads_v5", "Standard_E16ads_v5", "Standard_E20ads_v5", "Standard_E32ads_v5", "Standard_E48ads_v5", "Standard_E64ads_v5", "Standard_E96ads_v5", "Standard_M8_2ms", "Standard_M8_4ms", "Standard_M16_4ms", "Standard_M16_8ms", "Standard_M32_8ms", "Standard_M32_16ms", "Standard_M64_32ms", "Standard_M64_16ms", "Standard_M128_64ms", "Standard_M128_32ms", "Standard_E4_2s_v3", "Standard_E8_4s_v3", "Standard_E8_2s_v3", "Standard_E16_8s_v3", "Standard_E16_4s_v3", "Standard_E32_16s_v3", "Standard_E32_8s_v3", "Standard_E64_32s_v3", "Standard_E64_16s_v3", "Standard_E4_2s_v4", "Standard_E8_4s_v4", "Standard_E8_2s_v4", "Standard_E16_8s_v4", "Standard_E16_4s_v4", "Standard_E32_16s_v4", "Standard_E32_8s_v4", "Standard_E64_32s_v4", "Standard_E64_16s_v4", "Standard_E4_2ds_v4", "Standard_E8_4ds_v4", "Standard_E8_2ds_v4", "Standard_E16_8ds_v4", "Standard_E16_4ds_v4", "Standard_E32_16ds_v4", "Standard_E32_8ds_v4", "Standard_E64_32ds_v4", "Standard_E64_16ds_v4", "Standard_E4_2as_v4", "Standard_E8_4as_v4", "Standard_E8_2as_v4", "Standard_E16_8as_v4", "Standard_E16_4as_v4", "Standard_E32_16as_v4", "Standard_E32_8as_v4", "Standard_E64_32as_v4", "Standard_E64_16as_v4", "Standard_E96_48as_v4", "Standard_E96_24as_v4", "Standard_E4_2ads_v5", "Standard_E8_4ads_v5", "Standard_E8_2ads_v5", "Standard_E16_8ads_v5", "Standard_E16_4ads_v5", "Standard_E32_16ads_v5", "Standard_E32_8ads_v5", "Standard_E64_32ads_v5", "Standard_E64_16ads_v5", "Standard_E96_48ads_v5", "Standard_E96_24ads_v5", "Standard_E4_2s_v5", "Standard_E8_4s_v5", "Standard_E8_2s_v5", "Standard_E16_8s_v5", "Standard_E16_4s_v5", "Standard_E32_16s_v5", "Standard_E32_8s_v5", "Standard_E64_32s_v5", "Standard_E64_16s_v5", "Standard_E96_48s_v5", "Standard_E96_24s_v5", "Standard_E4_2ds_v5", "Standard_E8_4ds_v5", "Standard_E8_2ds_v5", "Standard_E16_8ds_v5", "Standard_E16_4ds_v5", "Standard_E32_16ds_v5", "Standard_E32_8ds_v5", "Standard_E64_32ds_v5", "Standard_E64_16ds_v5", "Standard_E96_48ds_v5", "Standard_E96_24ds_v5", "Standard_E4_2as_v5", "Standard_E8_4as_v5", "Standard_E8_2as_v5", "Standard_E16_8as_v5", "Standard_E16_4as_v5", "Standard_E32_16as_v5", "Standard_E32_8as_v5", "Standard_E64_32as_v5", "Standard_E64_16as_v5", "Standard_E96_48as_v5", "Standard_E96_24as_v5", "Standard_GS4_8", "Standard_GS4_4", "Standard_GS5_16", "Standard_GS5_8", "Standard_DS11_1_v2", "Standard_DS12_2_v2", "Standard_DS12_1_v2", "Standard_DS13_4_v2", "Standard_DS13_2_v2", "Standard_DS14_8_v2", "Standard_DS14_4_v2", "Standard_M416_208s_v2", "Standard_M416_208ms_v2", "Standard_E2bs_v5", "Standard_E4bs_v5", "Standard_E8bs_v5", "Standard_E16bs_v5", "Standard_E32bs_v5", "Standard_E48bs_v5", "Standard_E64bs_v5", "Standard_E2bds_v5", "Standard_E4bds_v5", "Standard_E8bds_v5", "Standard_E16bds_v5", "Standard_E32bds_v5", "Standard_E48bds_v5", and "Standard_E64bds_v5".</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSizeMegabytesOfMemory" /></td>
    <td><code>number</code></td>
    <td>Gets or sets the Megabytes of memory for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedVmSizeNumberOfCores" /></td>
    <td><code>integer</code></td>
    <td>Gets or sets the Number of cores for recommended size.</td>
</tr>
<tr>
    <td><CopyableCode code="securitySuitability" /></td>
    <td><code>string</code></td>
    <td>Gets the suitability for Microsoft cloud defender. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="sizingCriterion" /></td>
    <td><code>string</code></td>
    <td>Assessment sizing criterion. Known values are: "PerformanceBased" and "AsOnPremises".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlInstances" /></td>
    <td><code>array</code></td>
    <td>Gets the list of SQL instances discovered on the machine.</td>
</tr>
<tr>
    <td><CopyableCode code="suitability" /></td>
    <td><code>string</code></td>
    <td>Gets a value indicating whether machine is suitable for the cloud platform selected. Known values are: "Unknown", "NotSuitable", "Suitable", "ConditionallySuitable", and "ReadinessUnknown".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityDetail" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the detailed messages that were set on the machine during evaluation. Known values are: "None", "RecommendedSizeHasLessNetworkAdapters", "CannotReportComputeCost", "CannotReportStorageCost", "CannotReportBandwidthCosts", "PercentageOfCoresUtilizedMissing", "PercentageOfMemoryUtilizedMissing", "PercentageOfCoresUtilizedOutOfRange", and "PercentageOfMemoryUtilizedOutOfRange".</td>
</tr>
<tr>
    <td><CopyableCode code="suitabilityExplanation" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the explanation if machine is not suitable for cloud. Known values are: "Unknown", "NotApplicable", "GuestOperatingSystemArchitectureNotSupported", "GuestOperatingSystemNotSupported", "BootTypeNotSupported", "MoreDisksThanSupported", "NoSuitableVmSizeFound", "OneOrMoreDisksNotSuitable", "OneOrMoreAdaptersNotSuitable", "InternalErrorOccurredDuringComputeEvaluation", "InternalErrorOccurredDuringStorageEvaluation", "InternalErrorOccurredDuringNetworkEvaluation", "NoVmSizeSupportsStoragePerformance", "NoVmSizeSupportsNetworkPerformance", "NoVmSizeForSelectedPricingTier", "NoVmSizeForSelectedAzureLocation", "CheckRedHatLinuxVersion", "CheckOpenSuseLinuxVersion", "CheckWindowsServer2008R2Version", "CheckCentOsVersion", "CheckDebianLinuxVersion", "CheckSuseLinuxVersion", "CheckOracleLinuxVersion", "CheckUbuntuLinuxVersion", "CheckCoreOsLinuxVersion", "WindowsServerVersionConditionallySupported", "NoGuestOperatingSystemConditionallySupported", "WindowsClientVersionsConditionallySupported", "BootTypeUnknown", "GuestOperatingSystemUnknown", "WindowsServerVersionsSupportedWithCaveat", "WindowsOSNoLongerUnderMSSupport", "EndorsedWithConditionsLinuxDistributions", "UnendorsedLinuxDistributions", "NoVmSizeForStandardPricingTier", "NoVmSizeForBasicPricingTier", "NoVmSizeInSelectedFamilyFound", "NoEaPriceFoundForVmSize", and "NoVmSizeFoundForOfferCurrencyReservedInstance".</td>
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
    <td><CopyableCode code="updatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>When was machine last updated.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-assessed_sql_machine_name"><code>assessed_sql_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a AssessedSqlMachine.</td>
</tr>
<tr>
    <td><a href="#list_by_sql_assessment_v2"><CopyableCode code="list_by_sql_assessment_v2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-project_name"><code>project_name</code></a>, <a href="#parameter-group_name"><code>group_name</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-totalRecordCount"><code>totalRecordCount</code></a></td>
    <td>List AssessedSqlMachine resources by SqlAssessmentV2.</td>
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
<tr id="parameter-assessed_sql_machine_name">
    <td><CopyableCode code="assessed_sql_machine_name" /></td>
    <td><code>string</code></td>
    <td>Sql assessment Assessed Machine ARM name. Required.</td>
</tr>
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>SQL Assessment arm name. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter query. Default value is None.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>Optional parameter for continuation token. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Optional parameter for page size. Default value is None.</td>
</tr>
<tr id="parameter-totalRecordCount">
    <td><CopyableCode code="totalRecordCount" /></td>
    <td><code>integer</code></td>
    <td>Total record count. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_assessment_v2', value: 'list_by_sql_assessment_v2' }
    ]}
>
<TabItem value="get">

Get a AssessedSqlMachine.

```sql
SELECT
id,
name,
biosGuid,
bootType,
confidenceRatingInPercentage,
costComponents,
createdTimestamp,
datacenterMachineArmId,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
disks,
displayName,
fqdn,
megabytesOfMemory,
migrationGuidelines,
monthlyBandwidthCost,
monthlyComputeCost,
monthlyStorageCost,
networkAdapters,
numberOfCores,
operatingSystemArchitecture,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
percentageCoresUtilization,
percentageMemoryUtilization,
productSupportStatus,
recommendedVmFamily,
recommendedVmSize,
recommendedVmSizeMegabytesOfMemory,
recommendedVmSizeNumberOfCores,
securitySuitability,
sizingCriterion,
sqlInstances,
suitability,
suitabilityDetail,
suitabilityExplanation,
systemData,
type,
updatedTimestamp
FROM azure.migrationassessment.assessed_sql_machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND assessed_sql_machine_name = '{{ assessed_sql_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sql_assessment_v2">

List AssessedSqlMachine resources by SqlAssessmentV2.

```sql
SELECT
id,
name,
biosGuid,
bootType,
confidenceRatingInPercentage,
costComponents,
createdTimestamp,
datacenterMachineArmId,
datacenterManagementServerArmId,
datacenterManagementServerName,
description,
disks,
displayName,
fqdn,
megabytesOfMemory,
migrationGuidelines,
monthlyBandwidthCost,
monthlyComputeCost,
monthlyStorageCost,
networkAdapters,
numberOfCores,
operatingSystemArchitecture,
operatingSystemName,
operatingSystemType,
operatingSystemVersion,
percentageCoresUtilization,
percentageMemoryUtilization,
productSupportStatus,
recommendedVmFamily,
recommendedVmSize,
recommendedVmSizeMegabytesOfMemory,
recommendedVmSizeNumberOfCores,
securitySuitability,
sizingCriterion,
sqlInstances,
suitability,
suitabilityDetail,
suitabilityExplanation,
systemData,
type,
updatedTimestamp
FROM azure.migrationassessment.assessed_sql_machines_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND project_name = '{{ project_name }}' -- required
AND group_name = '{{ group_name }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND pageSize = '{{ pageSize }}'
AND continuationToken = '{{ continuationToken }}'
AND totalRecordCount = '{{ totalRecordCount }}'
;
```
</TabItem>
</Tabs>
