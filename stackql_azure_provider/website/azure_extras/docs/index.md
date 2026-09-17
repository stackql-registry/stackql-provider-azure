---
title: azure_extras
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_extras
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Additional Azure cloud computing services by Microsoft.  

:::info[Provider Summary] 

total services: __44__  
total resources: __443__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure_extras` provider, run the following command:  

```bash
REGISTRY PULL azure_extras;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

## Example Queries

Try the following queries using `stackql shell`, or run them from a script or CI pipeline with `stackql exec`.

### IoT Central applications

IoT Central applications in the subscription with subdomain, SKU, template and state:

```sql
SELECT name, display_name, subdomain, state, location,
       json_extract(sku, '$.name') AS sku, template, application_id
FROM azure_extras.iot_central.apps
WHERE subscription_id = '{{ subscription_id }}'
ORDER BY location, name;
```

### Azure Spring Apps instances

Spring Apps service instances with tier, power state, version, zone redundancy and outbound network type:

```sql
SELECT name, location, service_id, version, power_state, zone_redundant, fqdn,
       json_extract(sku, '$.name') AS sku,
       json_extract(sku, '$.tier') AS tier,
       json_extract(network_profile, '$.outboundType') AS outbound_type,
       provisioning_state
FROM azure_extras.app_platform.services
WHERE subscription_id = '{{ subscription_id }}';
```

### Lab Services labs

Labs with their lab plan, state, VM size, usage quota and auto-shutdown settings:

```sql
SELECT name, title, state, location, lab_plan_id,
       json_extract(virtual_machine_profile, '$.sku.name') AS vm_sku,
       json_extract(virtual_machine_profile, '$.osType') AS os_type,
       json_extract(virtual_machine_profile, '$.usageQuota') AS usage_quota,
       json_extract(auto_shutdown_profile, '$.shutdownOnDisconnect') AS shutdown_on_disconnect,
       json_extract(auto_shutdown_profile, '$.shutdownOnIdle') AS shutdown_on_idle,
       provisioning_state
FROM azure_extras.lab_services.labs
WHERE subscription_id = '{{ subscription_id }}';
```

### Health Data Services workspaces

Health Data Services workspaces with their public network access setting and private endpoint count:

```sql
SELECT name, location, public_network_access,
       json_array_length(private_endpoint_connections) AS private_endpoints,
       provisioning_state
FROM azure_extras.health_data_services.workspaces
WHERE subscription_id = '{{ subscription_id }}';
```

### FHIR services in a workspace

FHIR services in one workspace with the FHIR version, the authentication authority and audience, and whether the SMART on FHIR proxy is enabled:

```sql
SELECT name, kind, location, public_network_access, event_state,
       json_extract(authentication_configuration, '$.authority') AS authority,
       json_extract(authentication_configuration, '$.audience') AS audience,
       json_extract(authentication_configuration, '$.smartProxyEnabled') AS smart_proxy_enabled,
       provisioning_state
FROM azure_extras.health_data_services.fhir_services
WHERE workspace_name = '{{ workspace_name }}'
  AND resource_group_name = '{{ resource_group_name }}'
  AND subscription_id = '{{ subscription_id }}';
```

### Spring Apps deployments

Every deployment across the apps in one Spring Apps instance with its active flag, status, instance count and resource requests:

```sql
SELECT id, name, active, status,
       json_extract(sku, '$.capacity') AS instance_count,
       json_extract(source, '$.type') AS source_type,
       json_extract(deployment_settings, '$.resourceRequests.cpu') AS cpu,
       json_extract(deployment_settings, '$.resourceRequests.memory') AS memory,
       provisioning_state
FROM azure_extras.app_platform.deployments
WHERE service_name = '{{ service_name }}'
  AND resource_group_name = '{{ resource_group_name }}'
  AND subscription_id = '{{ subscription_id }}';
```

### IoT Central application provisioning

Create an application on the ST2 SKU with a globally unique subdomain, then delete it:

```sql
INSERT INTO azure_extras.iot_central.apps (
  resource_name, resource_group_name, subscription_id, location, sku, properties, tags
)
SELECT 'fleet-telemetry-01', '{{ resource_group_name }}', '{{ subscription_id }}', 'eastus',
       '{"name": "ST2"}',
       '{"displayName": "Fleet telemetry", "subdomain": "fleet-telemetry-01"}',
       '{"environment": "dev"}';

DELETE FROM azure_extras.iot_central.apps
WHERE resource_name = 'fleet-telemetry-01'
  AND resource_group_name = '{{ resource_group_name }}'
  AND subscription_id = '{{ subscription_id }}';
```

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/agriculture_platform/">agriculture_platform</a><br />
<a href="/services/agrifood/">agrifood</a><br />
<a href="/services/agrifood_farming/">agrifood_farming</a><br />
<a href="/services/app_compliance_automation/">app_compliance_automation</a><br />
<a href="/services/app_platform/">app_platform</a><br />
<a href="/services/commerce/">commerce</a><br />
<a href="/services/connected_cache/">connected_cache</a><br />
<a href="/services/devhub/">devhub</a><br />
<a href="/services/devspaces/">devspaces</a><br />
<a href="/services/edgeorder/">edgeorder</a><br />
<a href="/services/education/">education</a><br />
<a href="/services/graph_services/">graph_services</a><br />
<a href="/services/health_bot/">health_bot</a><br />
<a href="/services/health_data_services/">health_data_services</a><br />
<a href="/services/health_deidentification/">health_deidentification</a><br />
<a href="/services/health_insights_cancer_profiling/">health_insights_cancer_profiling</a><br />
<a href="/services/health_insights_clinical_matching/">health_insights_clinical_matching</a><br />
<a href="/services/health_insights_radiology_insights/">health_insights_radiology_insights</a><br />
<a href="/services/hybrid_network/">hybrid_network</a><br />
<a href="/services/iot_central/">iot_central</a><br />
<a href="/services/iot_firmware_defense/">iot_firmware_defense</a><br />
<a href="/services/lab_services/">lab_services</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/managed_network_fabric/">managed_network_fabric</a><br />
<a href="/services/management_partner/">management_partner</a><br />
<a href="/services/media/">media</a><br />
<a href="/services/migration_discovery_sap/">migration_discovery_sap</a><br />
<a href="/services/network_analytics/">network_analytics</a><br />
<a href="/services/network_cloud/">network_cloud</a><br />
<a href="/services/oep/">oep</a><br />
<a href="/services/orbital/">orbital</a><br />
<a href="/services/portal_services_copilot/">portal_services_copilot</a><br />
<a href="/services/power_platform/">power_platform</a><br />
<a href="/services/program_enrollment/">program_enrollment</a><br />
<a href="/services/rdbms/">rdbms</a><br />
<a href="/services/self_help/">self_help</a><br />
<a href="/services/sphere/">sphere</a><br />
<a href="/services/spring_app_discovery/">spring_app_discovery</a><br />
<a href="/services/storage_import_export/">storage_import_export</a><br />
<a href="/services/storage_pool/">storage_pool</a><br />
<a href="/services/testbase/">testbase</a><br />
<a href="/services/time_series_insights/">time_series_insights</a><br />
<a href="/services/video_analyzer/">video_analyzer</a><br />
<a href="/services/video_indexer/">video_indexer</a><br />
<a href="/services/voice_services/">voice_services</a><br />
</div>
</div>
