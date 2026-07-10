--- 
title: tests
hide_title: false
hide_table_of_contents: false
keywords:
  - tests
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists a <code>tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.tests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_test"
    values={[
        { label: 'get_test', value: 'get_test' },
        { label: 'list_tests', value: 'list_tests' }
    ]}
>
<TabItem value="get_test">

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
    <td><CopyableCode code="autoStopCriteria" /></td>
    <td><code>object</code></td>
    <td>Auto stop criteria for a test. This will automatically stop a load test if the error percentage is high for a certain time window.</td>
</tr>
<tr>
    <td><CopyableCode code="baselineTestRunId" /></td>
    <td><code>string</code></td>
    <td>Id of the test run to be marked as baseline to view trends of client-side metrics from recent test runs.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>Certificates metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of a test.</td>
</tr>
<tr>
    <td><CopyableCode code="engineBuiltInIdentityIds" /></td>
    <td><code>array</code></td>
    <td>Resource Ids of the managed identity built in to load test engines. Required if engineBuiltInIdentityType is UserAssigned.</td>
</tr>
<tr>
    <td><CopyableCode code="engineBuiltInIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity built in load test engines. Known values are: "SystemAssigned" and "UserAssigned". (SystemAssigned, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables which are defined as a set of pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedVirtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Estimated virtual user hours for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="inputArtifacts" /></td>
    <td><code>object</code></td>
    <td>The input artifacts for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="keyvaultReferenceIdentityId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the managed identity referencing the Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="keyvaultReferenceIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity referencing the Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of test. Known values are: "URL", "JMX", and "Locust". (URL, JMX, Locust)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="loadTestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The load test configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsReferenceIdentityId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the managed identity referencing the metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsReferenceIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity referencing the metrics. Known values are: "SystemAssigned" and "UserAssigned". (SystemAssigned, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="passFailCriteria" /></td>
    <td><code>object</code></td>
    <td>Pass fail criteria for a test.</td>
</tr>
<tr>
    <td><CopyableCode code="preferences" /></td>
    <td><code>object</code></td>
    <td>Preferences for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Inject load test engines without deploying public IP for outbound access.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>object</code></td>
    <td>Secrets can be stored in an Azure Key Vault or any other secret store. If the secret is stored in an Azure Key Vault, the value should be the secret identifier and the type should be AKV_SECRET_URI. If the secret is stored elsewhere, the secret value should be provided directly and the type should be SECRET_VALUE.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet ID on which the load test instances should run.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Unique test identifier for the load test, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_tests">

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
    <td><CopyableCode code="autoStopCriteria" /></td>
    <td><code>object</code></td>
    <td>Auto stop criteria for a test. This will automatically stop a load test if the error percentage is high for a certain time window.</td>
</tr>
<tr>
    <td><CopyableCode code="baselineTestRunId" /></td>
    <td><code>string</code></td>
    <td>Id of the test run to be marked as baseline to view trends of client-side metrics from recent test runs.</td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>object</code></td>
    <td>Certificates metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The test description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of a test.</td>
</tr>
<tr>
    <td><CopyableCode code="engineBuiltInIdentityIds" /></td>
    <td><code>array</code></td>
    <td>Resource Ids of the managed identity built in to load test engines. Required if engineBuiltInIdentityType is UserAssigned.</td>
</tr>
<tr>
    <td><CopyableCode code="engineBuiltInIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity built in load test engines. Known values are: "SystemAssigned" and "UserAssigned". (SystemAssigned, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>object</code></td>
    <td>Environment variables which are defined as a set of pairs.</td>
</tr>
<tr>
    <td><CopyableCode code="estimatedVirtualUserHours" /></td>
    <td><code>number</code></td>
    <td>Estimated virtual user hours for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="inputArtifacts" /></td>
    <td><code>object</code></td>
    <td>The input artifacts for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="keyvaultReferenceIdentityId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the managed identity referencing the Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="keyvaultReferenceIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity referencing the Key vault.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of test. Known values are: "URL", "JMX", and "Locust". (URL, JMX, Locust)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="loadTestConfiguration" /></td>
    <td><code>object</code></td>
    <td>The load test configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsReferenceIdentityId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of the managed identity referencing the metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="metricsReferenceIdentityType" /></td>
    <td><code>string</code></td>
    <td>Type of the managed identity referencing the metrics. Known values are: "SystemAssigned" and "UserAssigned". (SystemAssigned, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="passFailCriteria" /></td>
    <td><code>object</code></td>
    <td>Pass fail criteria for a test.</td>
</tr>
<tr>
    <td><CopyableCode code="preferences" /></td>
    <td><code>object</code></td>
    <td>Preferences for the test.</td>
</tr>
<tr>
    <td><CopyableCode code="publicIPDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Inject load test engines without deploying public IP for outbound access.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>object</code></td>
    <td>Secrets can be stored in an Azure Key Vault or any other secret store. If the secret is stored in an Azure Key Vault, the value should be the secret identifier and the type should be AKV_SECRET_URI. If the secret is stored elsewhere, the secret value should be provided directly and the type should be SECRET_VALUE.</td>
</tr>
<tr>
    <td><CopyableCode code="subnetId" /></td>
    <td><code>string</code></td>
    <td>Subnet ID on which the load test instances should run.</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Unique test identifier for the load test, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
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
    <td><a href="#get_test"><CopyableCode code="get_test" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get load test details by test Id. Get load test details by test Id.</td>
</tr>
<tr>
    <td><a href="#list_tests"><CopyableCode code="list_tests" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-orderby"><code>orderby</code></a>, <a href="#parameter-search"><code>search</code></a>, <a href="#parameter-lastModifiedStartTime"><code>lastModifiedStartTime</code></a>, <a href="#parameter-lastModifiedEndTime"><code>lastModifiedEndTime</code></a>, <a href="#parameter-maxpagesize"><code>maxpagesize</code></a></td>
    <td>Get all load tests by the fully qualified resource Id e.g subscriptions/&#123;subId&#125;/resourceGroups/&#123;rg&#125;/providers/Microsoft.LoadTestService/loadtests/&#123;resName&#125;. Get all load tests by the fully qualified resource Id e.g subscriptions/&#123;subId&#125;/resourceGroups/&#123;rg&#125;/providers/Microsoft.LoadTestService/loadtests/&#123;resName&#125;.</td>
</tr>
<tr>
    <td><a href="#create_or_update_test"><CopyableCode code="create_or_update_test" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new test or update an existing test by providing the test Id. Create a new test or update an existing test by providing the test Id.</td>
</tr>
<tr>
    <td><a href="#create_or_update_test"><CopyableCode code="create_or_update_test" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a new test or update an existing test by providing the test Id. Create a new test or update an existing test by providing the test Id.</td>
</tr>
<tr>
    <td><a href="#delete_test"><CopyableCode code="delete_test" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a test by its test Id. Delete a test by its test Id.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-test_id">
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>Unique test identifier for the load test, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
<tr id="parameter-lastModifiedEndTime">
    <td><CopyableCode code="lastModifiedEndTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime(RFC 3339 literal format) of the last updated time range to filter tests. Default value is None.</td>
</tr>
<tr id="parameter-lastModifiedStartTime">
    <td><CopyableCode code="lastModifiedStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime(RFC 3339 literal format) of the last updated time range to filter tests. Default value is None.</td>
</tr>
<tr id="parameter-maxpagesize">
    <td><CopyableCode code="maxpagesize" /></td>
    <td><code>integer</code></td>
    <td></td>
</tr>
<tr id="parameter-orderby">
    <td><CopyableCode code="orderby" /></td>
    <td><code>string</code></td>
    <td>Sort on the supported fields in (field asc/desc) format. eg: lastModifiedDateTime asc. Supported fields - lastModifiedDateTime. Default value is None.</td>
</tr>
<tr id="parameter-search">
    <td><CopyableCode code="search" /></td>
    <td><code>string</code></td>
    <td>Prefix based, case sensitive search on searchable fields - displayName, createdBy. For example, to search for a test, with display name is Login Test, the search parameter can be Login. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_test"
    values={[
        { label: 'get_test', value: 'get_test' },
        { label: 'list_tests', value: 'list_tests' }
    ]}
>
<TabItem value="get_test">

Get load test details by test Id. Get load test details by test Id.

```sql
SELECT
autoStopCriteria,
baselineTestRunId,
certificate,
createdBy,
createdDateTime,
description,
displayName,
engineBuiltInIdentityIds,
engineBuiltInIdentityType,
environmentVariables,
estimatedVirtualUserHours,
inputArtifacts,
keyvaultReferenceIdentityId,
keyvaultReferenceIdentityType,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
metricsReferenceIdentityId,
metricsReferenceIdentityType,
passFailCriteria,
preferences,
publicIPDisabled,
secrets,
subnetId,
testId
FROM azure.developer_loadtesting.tests
WHERE test_id = '{{ test_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_tests">

Get all load tests by the fully qualified resource Id e.g subscriptions/&#123;subId&#125;/resourceGroups/&#123;rg&#125;/providers/Microsoft.LoadTestService/loadtests/&#123;resName&#125;. Get all load tests by the fully qualified resource Id e.g subscriptions/&#123;subId&#125;/resourceGroups/&#123;rg&#125;/providers/Microsoft.LoadTestService/loadtests/&#123;resName&#125;.

```sql
SELECT
autoStopCriteria,
baselineTestRunId,
certificate,
createdBy,
createdDateTime,
description,
displayName,
engineBuiltInIdentityIds,
engineBuiltInIdentityType,
environmentVariables,
estimatedVirtualUserHours,
inputArtifacts,
keyvaultReferenceIdentityId,
keyvaultReferenceIdentityType,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
metricsReferenceIdentityId,
metricsReferenceIdentityType,
passFailCriteria,
preferences,
publicIPDisabled,
secrets,
subnetId,
testId
FROM azure.developer_loadtesting.tests
WHERE endpoint = '{{ endpoint }}' -- required
AND orderby = '{{ orderby }}'
AND search = '{{ search }}'
AND lastModifiedStartTime = '{{ lastModifiedStartTime }}'
AND lastModifiedEndTime = '{{ lastModifiedEndTime }}'
AND maxpagesize = '{{ maxpagesize }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_test"
    values={[
        { label: 'create_or_update_test', value: 'create_or_update_test' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_test">

Create a new test or update an existing test by providing the test Id. Create a new test or update an existing test by providing the test Id.

```sql
INSERT INTO azure.developer_loadtesting.tests (
passFailCriteria,
autoStopCriteria,
secrets,
certificate,
environmentVariables,
loadTestConfiguration,
baselineTestRunId,
description,
displayName,
subnetId,
kind,
publicIPDisabled,
keyvaultReferenceIdentityType,
keyvaultReferenceIdentityId,
metricsReferenceIdentityType,
metricsReferenceIdentityId,
engineBuiltInIdentityType,
engineBuiltInIdentityIds,
preferences,
test_id,
endpoint
)
SELECT 
'{{ passFailCriteria }}',
'{{ autoStopCriteria }}',
'{{ secrets }}',
'{{ certificate }}',
'{{ environmentVariables }}',
'{{ loadTestConfiguration }}',
'{{ baselineTestRunId }}',
'{{ description }}',
'{{ displayName }}',
'{{ subnetId }}',
'{{ kind }}',
{{ publicIPDisabled }},
'{{ keyvaultReferenceIdentityType }}',
'{{ keyvaultReferenceIdentityId }}',
'{{ metricsReferenceIdentityType }}',
'{{ metricsReferenceIdentityId }}',
'{{ engineBuiltInIdentityType }}',
'{{ engineBuiltInIdentityIds }}',
'{{ preferences }}',
'{{ test_id }}',
'{{ endpoint }}'
RETURNING
autoStopCriteria,
baselineTestRunId,
certificate,
createdBy,
createdDateTime,
description,
displayName,
engineBuiltInIdentityIds,
engineBuiltInIdentityType,
environmentVariables,
estimatedVirtualUserHours,
inputArtifacts,
keyvaultReferenceIdentityId,
keyvaultReferenceIdentityType,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
metricsReferenceIdentityId,
metricsReferenceIdentityType,
passFailCriteria,
preferences,
publicIPDisabled,
secrets,
subnetId,
testId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: tests
  props:
    - name: test_id
      value: "{{ test_id }}"
      description: Required parameter for the tests resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the tests resource.
    - name: passFailCriteria
      description: |
        Pass fail criteria for a test.
      value:
        passFailMetrics: "{{ passFailMetrics }}"
        passFailServerMetrics: "{{ passFailServerMetrics }}"
    - name: autoStopCriteria
      description: |
        Auto stop criteria for a test. This will automatically stop a load test if the error percentage is high for a certain time window.
      value:
        autoStopDisabled: {{ autoStopDisabled }}
        errorRate: {{ errorRate }}
        errorRateTimeWindowInSeconds: {{ errorRateTimeWindowInSeconds }}
        maximumVirtualUsersPerEngine: {{ maximumVirtualUsersPerEngine }}
    - name: secrets
      value: "{{ secrets }}"
      description: |
        Secrets can be stored in an Azure Key Vault or any other secret store. If the secret is stored in an Azure Key Vault, the value should be the secret identifier and the type should be AKV_SECRET_URI. If the secret is stored elsewhere, the secret value should be provided directly and the type should be SECRET_VALUE.
    - name: certificate
      description: |
        Certificates metadata.
      value:
        value: "{{ value }}"
        type: "{{ type }}"
        name: "{{ name }}"
    - name: environmentVariables
      value: "{{ environmentVariables }}"
      description: |
        Environment variables which are defined as a set of pairs.
    - name: loadTestConfiguration
      description: |
        The load test configuration.
      value:
        engineInstances: {{ engineInstances }}
        splitAllCSVs: {{ splitAllCSVs }}
        quickStartTest: {{ quickStartTest }}
        optionalLoadTestConfig:
          endpointUrl: "{{ endpointUrl }}"
          requestsPerSecond: {{ requestsPerSecond }}
          maxResponseTimeInMs: {{ maxResponseTimeInMs }}
          virtualUsers: {{ virtualUsers }}
          rampUpTime: {{ rampUpTime }}
          duration: {{ duration }}
        regionalLoadTestConfig:
          - engineInstances: {{ engineInstances }}
            region: "{{ region }}"
    - name: baselineTestRunId
      value: "{{ baselineTestRunId }}"
      description: |
        Id of the test run to be marked as baseline to view trends of client-side metrics from recent test runs.
    - name: description
      value: "{{ description }}"
      description: |
        The test description.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name of a test.
    - name: subnetId
      value: "{{ subnetId }}"
      description: |
        Subnet ID on which the load test instances should run.
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of test. Known values are: "URL", "JMX", and "Locust".
      valid_values: ['URL', 'JMX', 'Locust']
    - name: publicIPDisabled
      value: {{ publicIPDisabled }}
      description: |
        Inject load test engines without deploying public IP for outbound access.
    - name: keyvaultReferenceIdentityType
      value: "{{ keyvaultReferenceIdentityType }}"
      description: |
        Type of the managed identity referencing the Key vault.
    - name: keyvaultReferenceIdentityId
      value: "{{ keyvaultReferenceIdentityId }}"
      description: |
        Resource Id of the managed identity referencing the Key vault.
    - name: metricsReferenceIdentityType
      value: "{{ metricsReferenceIdentityType }}"
      description: |
        Type of the managed identity referencing the metrics. Known values are: "SystemAssigned" and "UserAssigned".
      valid_values: ['SystemAssigned', 'UserAssigned']
    - name: metricsReferenceIdentityId
      value: "{{ metricsReferenceIdentityId }}"
      description: |
        Resource Id of the managed identity referencing the metrics.
    - name: engineBuiltInIdentityType
      value: "{{ engineBuiltInIdentityType }}"
      description: |
        Type of the managed identity built in load test engines. Known values are: "SystemAssigned" and "UserAssigned".
      valid_values: ['SystemAssigned', 'UserAssigned']
    - name: engineBuiltInIdentityIds
      value:
        - "{{ engineBuiltInIdentityIds }}"
      description: |
        Resource Ids of the managed identity built in to load test engines. Required if engineBuiltInIdentityType is UserAssigned.
    - name: preferences
      description: |
        Preferences for the test.
      value:
        enableAIErrorInsights: {{ enableAIErrorInsights }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_test"
    values={[
        { label: 'create_or_update_test', value: 'create_or_update_test' }
    ]}
>
<TabItem value="create_or_update_test">

Create a new test or update an existing test by providing the test Id. Create a new test or update an existing test by providing the test Id.

```sql
REPLACE azure.developer_loadtesting.tests
SET 
passFailCriteria = '{{ passFailCriteria }}',
autoStopCriteria = '{{ autoStopCriteria }}',
secrets = '{{ secrets }}',
certificate = '{{ certificate }}',
environmentVariables = '{{ environmentVariables }}',
loadTestConfiguration = '{{ loadTestConfiguration }}',
baselineTestRunId = '{{ baselineTestRunId }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
subnetId = '{{ subnetId }}',
kind = '{{ kind }}',
publicIPDisabled = {{ publicIPDisabled }},
keyvaultReferenceIdentityType = '{{ keyvaultReferenceIdentityType }}',
keyvaultReferenceIdentityId = '{{ keyvaultReferenceIdentityId }}',
metricsReferenceIdentityType = '{{ metricsReferenceIdentityType }}',
metricsReferenceIdentityId = '{{ metricsReferenceIdentityId }}',
engineBuiltInIdentityType = '{{ engineBuiltInIdentityType }}',
engineBuiltInIdentityIds = '{{ engineBuiltInIdentityIds }}',
preferences = '{{ preferences }}'
WHERE 
test_id = '{{ test_id }}' --required
AND endpoint = '{{ endpoint }}' --required
RETURNING
autoStopCriteria,
baselineTestRunId,
certificate,
createdBy,
createdDateTime,
description,
displayName,
engineBuiltInIdentityIds,
engineBuiltInIdentityType,
environmentVariables,
estimatedVirtualUserHours,
inputArtifacts,
keyvaultReferenceIdentityId,
keyvaultReferenceIdentityType,
kind,
lastModifiedBy,
lastModifiedDateTime,
loadTestConfiguration,
metricsReferenceIdentityId,
metricsReferenceIdentityType,
passFailCriteria,
preferences,
publicIPDisabled,
secrets,
subnetId,
testId;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_test"
    values={[
        { label: 'delete_test', value: 'delete_test' }
    ]}
>
<TabItem value="delete_test">

Delete a test by its test Id. Delete a test by its test Id.

```sql
DELETE FROM azure.developer_loadtesting.tests
WHERE test_id = '{{ test_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
