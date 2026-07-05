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

total services: __18__  
total resources: __148__  

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
<a href="/services/agrifood/">agrifood</a><br />
<a href="/services/appcomplianceautomation/">appcomplianceautomation</a><br />
<a href="/services/artifactsigning/">artifactsigning</a><br />
<a href="/services/chaos/">chaos</a><br />
<a href="/services/commerce/">commerce</a><br />
<a href="/services/devhub/">devhub</a><br />
<a href="/services/devspaces/">devspaces</a><br />
<a href="/services/edgeorder/">edgeorder</a><br />
<a href="/services/education/">education</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/healthbot/">healthbot</a><br />
<a href="/services/healthcareapis/">healthcareapis</a><br />
<a href="/services/managementpartner/">managementpartner</a><br />
<a href="/services/marketplaceordering/">marketplaceordering</a><br />
<a href="/services/oep/">oep</a><br />
<a href="/services/powerplatform/">powerplatform</a><br />
<a href="/services/selfhelp/">selfhelp</a><br />
<a href="/services/springappdiscovery/">springappdiscovery</a><br />
<a href="/services/testbase/">testbase</a><br />
</div>
</div>
