--- 
title: protected_item
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_item
  - recoveryservicesdatareplication
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

Creates, updates, deletes, gets or lists a <code>protected_item</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="protected_item" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicesdatareplication.protected_item" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><CopyableCode code="allowedJobs" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the allowed scenarios on the protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protected item correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="currentJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Protected item model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricAgentId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricObjectId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricObjectName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric object name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastFailedEnableProtectionJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last failed enabled protection job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastFailedPlannedFailoverJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last failed planned failover job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulPlannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful planned failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulUnplannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful unplanned failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestFailoverJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last test failover job.</td>
</tr>
<tr>
    <td><CopyableCode code="policyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the policy name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protection state. Known values are: "UnprotectedStatesBegin", "EnablingProtection", "EnablingFailed", "DisablingProtection", "MarkedForDeletion", "DisablingFailed", "UnprotectedStatesEnd", "InitialReplicationStatesBegin", "InitialReplicationInProgress", "InitialReplicationCompletedOnPrimary", "InitialReplicationCompletedOnRecovery", "InitialReplicationFailed", "InitialReplicationStatesEnd", "ProtectedStatesBegin", "Protected", "ProtectedStatesEnd", "PlannedFailoverTransitionStatesBegin", "PlannedFailoverInitiated", "PlannedFailoverCompleting", "PlannedFailoverCompleted", "PlannedFailoverFailed", "PlannedFailoverCompletionFailed", "PlannedFailoverTransitionStatesEnd", "UnplannedFailoverTransitionStatesBegin", "UnplannedFailoverInitiated", "UnplannedFailoverCompleting", "UnplannedFailoverCompleted", "UnplannedFailoverFailed", "UnplannedFailoverCompletionFailed", "UnplannedFailoverTransitionStatesEnd", "CommitFailoverStatesBegin", "CommitFailoverInProgressOnPrimary", "CommitFailoverInProgressOnRecovery", "CommitFailoverCompleted", "CommitFailoverFailedOnPrimary", "CommitFailoverFailedOnRecovery", "CommitFailoverStatesEnd", "CancelFailoverStatesBegin", "CancelFailoverInProgressOnPrimary", "CancelFailoverInProgressOnRecovery", "CancelFailoverFailedOnPrimary", "CancelFailoverFailedOnRecovery", "CancelFailoverStatesEnd", "ChangeRecoveryPointStatesBegin", "ChangeRecoveryPointInitiated", "ChangeRecoveryPointCompleted", "ChangeRecoveryPointFailed", "ChangeRecoveryPointStatesEnd", "ReprotectStatesBegin", "ReprotectInitiated", "ReprotectFailed", and "ReprotectStatesEnd". (UnprotectedStatesBegin, EnablingProtection, EnablingFailed, DisablingProtection, MarkedForDeletion, DisablingFailed, UnprotectedStatesEnd, InitialReplicationStatesBegin, InitialReplicationInProgress, InitialReplicationCompletedOnPrimary, InitialReplicationCompletedOnRecovery, InitialReplicationFailed, InitialReplicationStatesEnd, ProtectedStatesBegin, Protected, ProtectedStatesEnd, PlannedFailoverTransitionStatesBegin, PlannedFailoverInitiated, PlannedFailoverCompleting, PlannedFailoverCompleted, PlannedFailoverFailed, PlannedFailoverCompletionFailed, PlannedFailoverTransitionStatesEnd, UnplannedFailoverTransitionStatesBegin, UnplannedFailoverInitiated, UnplannedFailoverCompleting, UnplannedFailoverCompleted, UnplannedFailoverFailed, UnplannedFailoverCompletionFailed, UnplannedFailoverTransitionStatesEnd, CommitFailoverStatesBegin, CommitFailoverInProgressOnPrimary, CommitFailoverInProgressOnRecovery, CommitFailoverCompleted, CommitFailoverFailedOnPrimary, CommitFailoverFailedOnRecovery, CommitFailoverStatesEnd, CancelFailoverStatesBegin, CancelFailoverInProgressOnPrimary, CancelFailoverInProgressOnRecovery, CancelFailoverFailedOnPrimary, CancelFailoverFailedOnRecovery, CancelFailoverStatesEnd, ChangeRecoveryPointStatesBegin, ChangeRecoveryPointInitiated, ChangeRecoveryPointCompleted, ChangeRecoveryPointFailed, ChangeRecoveryPointStatesEnd, ReprotectStatesBegin, ReprotectInitiated, ReprotectFailed, ReprotectStatesEnd)</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the fabric agent. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationExtensionName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the replication extension name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>Gets or sets protected item replication health. Known values are: "Normal", "Warning", and "Critical". (Normal, Warning, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="resyncRequired" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether resynchronization is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="resynchronizationState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resynchronization state. Known values are: "None", "ResynchronizationInitiated", "ResynchronizationCompleted", and "ResynchronizationFailed". (None, ResynchronizationInitiated, ResynchronizationCompleted, ResynchronizationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source fabric provider Id.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricAgentId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric agent Id.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric provider Id.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the test failover state. Known values are: "None", "TestFailoverInitiated", "TestFailoverCompleting", "TestFailoverCompleted", "TestFailoverFailed", "TestFailoverCompletionFailed", "TestFailoverCleanupInitiated", "TestFailoverCleanupCompleting", and "MarkedForDeletion". (None, TestFailoverInitiated, TestFailoverCompleting, TestFailoverCompleted, TestFailoverFailed, TestFailoverCompletionFailed, TestFailoverCleanupInitiated, TestFailoverCleanupCompleting, MarkedForDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Test failover state description.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td><CopyableCode code="allowedJobs" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the allowed scenarios on the protected item.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protected item correlation Id.</td>
</tr>
<tr>
    <td><CopyableCode code="currentJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the current scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="customProperties" /></td>
    <td><code>object</code></td>
    <td>Protected item model custom properties. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricAgentId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric agent Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricObjectId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric object Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricObjectName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the fabric object name.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrors" /></td>
    <td><code>array</code></td>
    <td>Gets or sets the list of health errors.</td>
</tr>
<tr>
    <td><CopyableCode code="lastFailedEnableProtectionJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last failed enabled protection job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastFailedPlannedFailoverJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last failed planned failover job.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulPlannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful planned failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulTestFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful test failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastSuccessfulUnplannedFailoverTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets or sets the Last successful unplanned failover time.</td>
</tr>
<tr>
    <td><CopyableCode code="lastTestFailoverJob" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the last test failover job.</td>
</tr>
<tr>
    <td><CopyableCode code="policyName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the policy name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="protectionState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protection state. Known values are: "UnprotectedStatesBegin", "EnablingProtection", "EnablingFailed", "DisablingProtection", "MarkedForDeletion", "DisablingFailed", "UnprotectedStatesEnd", "InitialReplicationStatesBegin", "InitialReplicationInProgress", "InitialReplicationCompletedOnPrimary", "InitialReplicationCompletedOnRecovery", "InitialReplicationFailed", "InitialReplicationStatesEnd", "ProtectedStatesBegin", "Protected", "ProtectedStatesEnd", "PlannedFailoverTransitionStatesBegin", "PlannedFailoverInitiated", "PlannedFailoverCompleting", "PlannedFailoverCompleted", "PlannedFailoverFailed", "PlannedFailoverCompletionFailed", "PlannedFailoverTransitionStatesEnd", "UnplannedFailoverTransitionStatesBegin", "UnplannedFailoverInitiated", "UnplannedFailoverCompleting", "UnplannedFailoverCompleted", "UnplannedFailoverFailed", "UnplannedFailoverCompletionFailed", "UnplannedFailoverTransitionStatesEnd", "CommitFailoverStatesBegin", "CommitFailoverInProgressOnPrimary", "CommitFailoverInProgressOnRecovery", "CommitFailoverCompleted", "CommitFailoverFailedOnPrimary", "CommitFailoverFailedOnRecovery", "CommitFailoverStatesEnd", "CancelFailoverStatesBegin", "CancelFailoverInProgressOnPrimary", "CancelFailoverInProgressOnRecovery", "CancelFailoverFailedOnPrimary", "CancelFailoverFailedOnRecovery", "CancelFailoverStatesEnd", "ChangeRecoveryPointStatesBegin", "ChangeRecoveryPointInitiated", "ChangeRecoveryPointCompleted", "ChangeRecoveryPointFailed", "ChangeRecoveryPointStatesEnd", "ReprotectStatesBegin", "ReprotectInitiated", "ReprotectFailed", and "ReprotectStatesEnd". (UnprotectedStatesBegin, EnablingProtection, EnablingFailed, DisablingProtection, MarkedForDeletion, DisablingFailed, UnprotectedStatesEnd, InitialReplicationStatesBegin, InitialReplicationInProgress, InitialReplicationCompletedOnPrimary, InitialReplicationCompletedOnRecovery, InitialReplicationFailed, InitialReplicationStatesEnd, ProtectedStatesBegin, Protected, ProtectedStatesEnd, PlannedFailoverTransitionStatesBegin, PlannedFailoverInitiated, PlannedFailoverCompleting, PlannedFailoverCompleted, PlannedFailoverFailed, PlannedFailoverCompletionFailed, PlannedFailoverTransitionStatesEnd, UnplannedFailoverTransitionStatesBegin, UnplannedFailoverInitiated, UnplannedFailoverCompleting, UnplannedFailoverCompleted, UnplannedFailoverFailed, UnplannedFailoverCompletionFailed, UnplannedFailoverTransitionStatesEnd, CommitFailoverStatesBegin, CommitFailoverInProgressOnPrimary, CommitFailoverInProgressOnRecovery, CommitFailoverCompleted, CommitFailoverFailedOnPrimary, CommitFailoverFailedOnRecovery, CommitFailoverStatesEnd, CancelFailoverStatesBegin, CancelFailoverInProgressOnPrimary, CancelFailoverInProgressOnRecovery, CancelFailoverFailedOnPrimary, CancelFailoverFailedOnRecovery, CancelFailoverStatesEnd, ChangeRecoveryPointStatesBegin, ChangeRecoveryPointInitiated, ChangeRecoveryPointCompleted, ChangeRecoveryPointFailed, ChangeRecoveryPointStatesEnd, ReprotectStatesBegin, ReprotectInitiated, ReprotectFailed, ReprotectStatesEnd)</td>
</tr>
<tr>
    <td><CopyableCode code="protectionStateDescription" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the protection state description.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the provisioning state of the fabric agent. Known values are: "Canceled", "Creating", "Deleting", "Deleted", "Failed", "Succeeded", and "Updating". (Canceled, Creating, Deleting, Deleted, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="replicationExtensionName" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the replication extension name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationHealth" /></td>
    <td><code>string</code></td>
    <td>Gets or sets protected item replication health. Known values are: "Normal", "Warning", and "Critical". (Normal, Warning, Critical)</td>
</tr>
<tr>
    <td><CopyableCode code="resyncRequired" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether resynchronization is required or not.</td>
</tr>
<tr>
    <td><CopyableCode code="resynchronizationState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the resynchronization state. Known values are: "None", "ResynchronizationInitiated", "ResynchronizationCompleted", and "ResynchronizationFailed". (None, ResynchronizationInitiated, ResynchronizationCompleted, ResynchronizationFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the source fabric provider Id.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricAgentId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric agent Id.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric Id.</td>
</tr>
<tr>
    <td><CopyableCode code="targetFabricProviderId" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the target fabric provider Id.</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the test failover state. Known values are: "None", "TestFailoverInitiated", "TestFailoverCompleting", "TestFailoverCompleted", "TestFailoverFailed", "TestFailoverCompletionFailed", "TestFailoverCleanupInitiated", "TestFailoverCleanupCompleting", and "MarkedForDeletion". (None, TestFailoverInitiated, TestFailoverCompleting, TestFailoverCompleted, TestFailoverFailed, TestFailoverCompletionFailed, TestFailoverCleanupInitiated, TestFailoverCleanupCompleting, MarkedForDeletion)</td>
</tr>
<tr>
    <td><CopyableCode code="testFailoverStateDescription" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the Test failover state description.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of the protected item.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-odataOptions"><code>odataOptions</code></a>, <a href="#parameter-continuationToken"><code>continuationToken</code></a>, <a href="#parameter-pageSize"><code>pageSize</code></a></td>
    <td>Gets the list of protected items in the given vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the protected item.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Performs update on the protected item.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>Removes the protected item.</td>
</tr>
<tr>
    <td><a href="#planned_failover"><CopyableCode code="planned_failover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vault_name"><code>vault_name</code></a>, <a href="#parameter-protected_item_name"><code>protected_item_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Performs the planned failover on the protected item.</td>
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
<tr id="parameter-protected_item_name">
    <td><CopyableCode code="protected_item_name" /></td>
    <td><code>string</code></td>
    <td>The protected item name. Required.</td>
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
<tr id="parameter-vault_name">
    <td><CopyableCode code="vault_name" /></td>
    <td><code>string</code></td>
    <td>The vault name. Required.</td>
</tr>
<tr id="parameter-continuationToken">
    <td><CopyableCode code="continuationToken" /></td>
    <td><code>string</code></td>
    <td>Continuation token. Default value is None.</td>
</tr>
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>A flag indicating whether to do force delete or not. Default value is None.</td>
</tr>
<tr id="parameter-odataOptions">
    <td><CopyableCode code="odataOptions" /></td>
    <td><code>string</code></td>
    <td>OData options. Default value is None.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Page size. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of the protected item.

```sql
SELECT
id,
name,
allowedJobs,
correlationId,
currentJob,
customProperties,
fabricAgentId,
fabricId,
fabricObjectId,
fabricObjectName,
healthErrors,
lastFailedEnableProtectionJob,
lastFailedPlannedFailoverJob,
lastSuccessfulPlannedFailoverTime,
lastSuccessfulTestFailoverTime,
lastSuccessfulUnplannedFailoverTime,
lastTestFailoverJob,
policyName,
protectionState,
protectionStateDescription,
provisioningState,
replicationExtensionName,
replicationHealth,
resyncRequired,
resynchronizationState,
sourceFabricProviderId,
systemData,
targetFabricAgentId,
targetFabricId,
targetFabricProviderId,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicesdatareplication.protected_item
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND protected_item_name = '{{ protected_item_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of protected items in the given vault.

```sql
SELECT
id,
name,
allowedJobs,
correlationId,
currentJob,
customProperties,
fabricAgentId,
fabricId,
fabricObjectId,
fabricObjectName,
healthErrors,
lastFailedEnableProtectionJob,
lastFailedPlannedFailoverJob,
lastSuccessfulPlannedFailoverTime,
lastSuccessfulTestFailoverTime,
lastSuccessfulUnplannedFailoverTime,
lastTestFailoverJob,
policyName,
protectionState,
protectionStateDescription,
provisioningState,
replicationExtensionName,
replicationHealth,
resyncRequired,
resynchronizationState,
sourceFabricProviderId,
systemData,
targetFabricAgentId,
targetFabricId,
targetFabricProviderId,
testFailoverState,
testFailoverStateDescription,
type
FROM azure.recoveryservicesdatareplication.protected_item
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vault_name = '{{ vault_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND odataOptions = '{{ odataOptions }}'
AND continuationToken = '{{ continuationToken }}'
AND pageSize = '{{ pageSize }}'
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

Creates the protected item.

```sql
INSERT INTO azure.recoveryservicesdatareplication.protected_item (
properties,
resource_group_name,
vault_name,
protected_item_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vault_name }}',
'{{ protected_item_name }}',
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
- name: protected_item
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the protected_item resource.
    - name: vault_name
      value: "{{ vault_name }}"
      description: Required parameter for the protected_item resource.
    - name: protected_item_name
      value: "{{ protected_item_name }}"
      description: Required parameter for the protected_item resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the protected_item resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        policyName: "{{ policyName }}"
        replicationExtensionName: "{{ replicationExtensionName }}"
        correlationId: "{{ correlationId }}"
        provisioningState: "{{ provisioningState }}"
        protectionState: "{{ protectionState }}"
        protectionStateDescription: "{{ protectionStateDescription }}"
        testFailoverState: "{{ testFailoverState }}"
        testFailoverStateDescription: "{{ testFailoverStateDescription }}"
        resynchronizationState: "{{ resynchronizationState }}"
        fabricObjectId: "{{ fabricObjectId }}"
        fabricObjectName: "{{ fabricObjectName }}"
        sourceFabricProviderId: "{{ sourceFabricProviderId }}"
        targetFabricProviderId: "{{ targetFabricProviderId }}"
        fabricId: "{{ fabricId }}"
        targetFabricId: "{{ targetFabricId }}"
        fabricAgentId: "{{ fabricAgentId }}"
        targetFabricAgentId: "{{ targetFabricAgentId }}"
        resyncRequired: {{ resyncRequired }}
        lastSuccessfulPlannedFailoverTime: "{{ lastSuccessfulPlannedFailoverTime }}"
        lastSuccessfulUnplannedFailoverTime: "{{ lastSuccessfulUnplannedFailoverTime }}"
        lastSuccessfulTestFailoverTime: "{{ lastSuccessfulTestFailoverTime }}"
        currentJob:
          scenarioName: "{{ scenarioName }}"
          id: "{{ id }}"
          name: "{{ name }}"
          displayName: "{{ displayName }}"
          state: "{{ state }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
        allowedJobs:
          - "{{ allowedJobs }}"
        lastFailedEnableProtectionJob:
          scenarioName: "{{ scenarioName }}"
          id: "{{ id }}"
          name: "{{ name }}"
          displayName: "{{ displayName }}"
          state: "{{ state }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
        lastFailedPlannedFailoverJob:
          scenarioName: "{{ scenarioName }}"
          id: "{{ id }}"
          name: "{{ name }}"
          displayName: "{{ displayName }}"
          state: "{{ state }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
        lastTestFailoverJob:
          scenarioName: "{{ scenarioName }}"
          id: "{{ id }}"
          name: "{{ name }}"
          displayName: "{{ displayName }}"
          state: "{{ state }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
        replicationHealth: "{{ replicationHealth }}"
        healthErrors:
          - affectedResourceType: "{{ affectedResourceType }}"
            affectedResourceCorrelationIds: "{{ affectedResourceCorrelationIds }}"
            childErrors: "{{ childErrors }}"
            code: "{{ code }}"
            healthCategory: "{{ healthCategory }}"
            category: "{{ category }}"
            severity: "{{ severity }}"
            source: "{{ source }}"
            creationTime: "{{ creationTime }}"
            isCustomerResolvable: {{ isCustomerResolvable }}
            summary: "{{ summary }}"
            message: "{{ message }}"
            causes: "{{ causes }}"
            recommendation: "{{ recommendation }}"
        customProperties:
          instanceType: "{{ instanceType }}"
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

Performs update on the protected item.

```sql
UPDATE azure.recoveryservicesdatareplication.protected_item
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND protected_item_name = '{{ protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Removes the protected item.

```sql
DELETE FROM azure.recoveryservicesdatareplication.protected_item
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vault_name = '{{ vault_name }}' --required
AND protected_item_name = '{{ protected_item_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="planned_failover"
    values={[
        { label: 'planned_failover', value: 'planned_failover' }
    ]}
>
<TabItem value="planned_failover">

Performs the planned failover on the protected item.

```sql
EXEC azure.recoveryservicesdatareplication.protected_item.planned_failover 
@resource_group_name='{{ resource_group_name }}' --required, 
@vault_name='{{ vault_name }}' --required, 
@protected_item_name='{{ protected_item_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
