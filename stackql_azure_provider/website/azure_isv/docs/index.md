---
title: azure_isv
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_isv
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

Provision, manage, and integrate independent software vendor services on Azure. 

:::info[Provider Summary] 

total services: __27__  
total resources: __220__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure_isv` provider, run the following command:  

```bash
REGISTRY PULL azure_isv;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/arize_ai_observability_eval/">arize_ai_observability_eval</a><br />
<a href="/services/astro/">astro</a><br />
<a href="/services/commvault_content_store/">commvault_content_store</a><br />
<a href="/services/confluent/">confluent</a><br />
<a href="/services/databricks/">databricks</a><br />
<a href="/services/datadog/">datadog</a><br />
<a href="/services/dell_storage/">dell_storage</a><br />
<a href="/services/dynatrace/">dynatrace</a><br />
<a href="/services/elastic/">elastic</a><br />
<a href="/services/hana_on_azure/">hana_on_azure</a><br />
<a href="/services/informatica_data_management/">informatica_data_management</a><br />
<a href="/services/lambda_test_hyper_execute/">lambda_test_hyper_execute</a><br />
<a href="/services/mongodb_atlas/">mongodb_atlas</a><br />
<a href="/services/napster_omni_agent_api/">napster_omni_agent_api</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/neon_postgres/">neon_postgres</a><br />
<a href="/services/new_relic_observability/">new_relic_observability</a><br />
<a href="/services/nginx/">nginx</a><br />
<a href="/services/oracle_database/">oracle_database</a><br />
<a href="/services/palo_alto_networks_ngfw/">palo_alto_networks_ngfw</a><br />
<a href="/services/pinecone_vector_db/">pinecone_vector_db</a><br />
<a href="/services/pure_storage_block/">pure_storage_block</a><br />
<a href="/services/qumulo/">qumulo</a><br />
<a href="/services/terraform/">terraform</a><br />
<a href="/services/vmware_cloud_simple/">vmware_cloud_simple</a><br />
<a href="/services/weights_and_biases/">weights_and_biases</a><br />
<a href="/services/workloads/">workloads</a><br />
<a href="/services/workloads_sap_virtual_instance/">workloads_sap_virtual_instance</a><br />
</div>
</div>
