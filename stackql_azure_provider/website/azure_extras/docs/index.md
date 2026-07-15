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
