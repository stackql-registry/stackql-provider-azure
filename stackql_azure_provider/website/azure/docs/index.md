---
title: azure
hide_title: false
hide_table_of_contents: false
keywords:
  - azure
  - microsoft azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Core cloud services from Microsoft Azure.

:::info[Provider Summary] 

total services: __312__  
total resources: __3970__  

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure` provider, run the following command:  

```bash
REGISTRY PULL azure;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/advisor/">advisor</a><br />
<a href="/services/agricultureplatform/">agricultureplatform</a><br />
<a href="/services/agrifood_farming/">agrifood_farming</a><br />
<a href="/services/ai_agents/">ai_agents</a><br />
<a href="/services/ai_anomalydetector/">ai_anomalydetector</a><br />
<a href="/services/ai_contentsafety/">ai_contentsafety</a><br />
<a href="/services/ai_contentunderstanding/">ai_contentunderstanding</a><br />
<a href="/services/ai_discovery/">ai_discovery</a><br />
<a href="/services/ai_documentintelligence/">ai_documentintelligence</a><br />
<a href="/services/ai_evaluation/">ai_evaluation</a><br />
<a href="/services/ai_formrecognizer/">ai_formrecognizer</a><br />
<a href="/services/ai_inference/">ai_inference</a><br />
<a href="/services/ai_language_conversations/">ai_language_conversations</a><br />
<a href="/services/ai_language_conversations_authoring/">ai_language_conversations_authoring</a><br />
<a href="/services/ai_language_questionanswering/">ai_language_questionanswering</a><br />
<a href="/services/ai_language_questionanswering_authoring/">ai_language_questionanswering_authoring</a><br />
<a href="/services/ai_personalizer/">ai_personalizer</a><br />
<a href="/services/ai_projects/">ai_projects</a><br />
<a href="/services/ai_textanalytics_authoring/">ai_textanalytics_authoring</a><br />
<a href="/services/ai_textanalytics_dataplane/">ai_textanalytics_dataplane</a><br />
<a href="/services/ai_transcription/">ai_transcription</a><br />
<a href="/services/ai_translation_document/">ai_translation_document</a><br />
<a href="/services/ai_translation_text/">ai_translation_text</a><br />
<a href="/services/ai_vision_face/">ai_vision_face</a><br />
<a href="/services/ai_vision_imageanalysis/">ai_vision_imageanalysis</a><br />
<a href="/services/ai_voicelive/">ai_voicelive</a><br />
<a href="/services/alertsmanagement/">alertsmanagement</a><br />
<a href="/services/apicenter/">apicenter</a><br />
<a href="/services/apimanagement/">apimanagement</a><br />
<a href="/services/app/">app</a><br />
<a href="/services/appconfiguration/">appconfiguration</a><br />
<a href="/services/appconfiguration_dataplane/">appconfiguration_dataplane</a><br />
<a href="/services/appcontainers/">appcontainers</a><br />
<a href="/services/applicationinsights/">applicationinsights</a><br />
<a href="/services/appnetwork/">appnetwork</a><br />
<a href="/services/appplatform/">appplatform</a><br />
<a href="/services/attestation/">attestation</a><br />
<a href="/services/authorization/">authorization</a><br />
<a href="/services/automanage/">automanage</a><br />
<a href="/services/automation/">automation</a><br />
<a href="/services/azurearcdata/">azurearcdata</a><br />
<a href="/services/azurestackhcivm/">azurestackhcivm</a><br />
<a href="/services/baremetalinfrastructure/">baremetalinfrastructure</a><br />
<a href="/services/batch/">batch</a><br />
<a href="/services/batch_dataplane/">batch_dataplane</a><br />
<a href="/services/billing/">billing</a><br />
<a href="/services/billingbenefits/">billingbenefits</a><br />
<a href="/services/botservice/">botservice</a><br />
<a href="/services/carbonoptimization/">carbonoptimization</a><br />
<a href="/services/cdn/">cdn</a><br />
<a href="/services/certificateregistration/">certificateregistration</a><br />
<a href="/services/changeanalysis/">changeanalysis</a><br />
<a href="/services/cloudhealth/">cloudhealth</a><br />
<a href="/services/cognitiveservices/">cognitiveservices</a><br />
<a href="/services/communication/">communication</a><br />
<a href="/services/communication_callautomation/">communication_callautomation</a><br />
<a href="/services/communication_chat/">communication_chat</a><br />
<a href="/services/communication_email/">communication_email</a><br />
<a href="/services/communication_identity/">communication_identity</a><br />
<a href="/services/communication_jobrouter/">communication_jobrouter</a><br />
<a href="/services/communication_messages/">communication_messages</a><br />
<a href="/services/communication_phonenumbers/">communication_phonenumbers</a><br />
<a href="/services/communication_rooms/">communication_rooms</a><br />
<a href="/services/communication_sms/">communication_sms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/computebulkactions/">computebulkactions</a><br />
<a href="/services/computefleet/">computefleet</a><br />
<a href="/services/computelimit/">computelimit</a><br />
<a href="/services/computerecommender/">computerecommender</a><br />
<a href="/services/computeschedule/">computeschedule</a><br />
<a href="/services/confidentialledger/">confidentialledger</a><br />
<a href="/services/confidentialledger_certificate/">confidentialledger_certificate</a><br />
<a href="/services/confidentialledger_dataplane/">confidentialledger_dataplane</a><br />
<a href="/services/connectedcache/">connectedcache</a><br />
<a href="/services/consumption/">consumption</a><br />
<a href="/services/containerinstance/">containerinstance</a><br />
<a href="/services/containerorchestratorruntime/">containerorchestratorruntime</a><br />
<a href="/services/containerregistry/">containerregistry</a><br />
<a href="/services/containerregistry_dataplane/">containerregistry_dataplane</a><br />
<a href="/services/containerregistrytasks/">containerregistrytasks</a><br />
<a href="/services/containerservice/">containerservice</a><br />
<a href="/services/containerservicefleet/">containerservicefleet</a><br />
<a href="/services/containerservicesafeguards/">containerservicesafeguards</a><br />
<a href="/services/cosmosdb/">cosmosdb</a><br />
<a href="/services/cosmosdbforpostgresql/">cosmosdbforpostgresql</a><br />
<a href="/services/costmanagement/">costmanagement</a><br />
<a href="/services/customproviders/">customproviders</a><br />
<a href="/services/dashboard/">dashboard</a><br />
<a href="/services/data_tables/">data_tables</a><br />
<a href="/services/databasewatcher/">databasewatcher</a><br />
<a href="/services/databox/">databox</a><br />
<a href="/services/databoxedge/">databoxedge</a><br />
<a href="/services/datafactory/">datafactory</a><br />
<a href="/services/datalake_analytics/">datalake_analytics</a><br />
<a href="/services/datalake_store/">datalake_store</a><br />
<a href="/services/datamigration/">datamigration</a><br />
<a href="/services/dataprotection/">dataprotection</a><br />
<a href="/services/datashare/">datashare</a><br />
<a href="/services/defender_easm/">defender_easm</a><br />
<a href="/services/defendereasm/">defendereasm</a><br />
<a href="/services/dependencymap/">dependencymap</a><br />
<a href="/services/desktopvirtualization/">desktopvirtualization</a><br />
<a href="/services/devcenter/">devcenter</a><br />
<a href="/services/developer_devcenter/">developer_devcenter</a><br />
<a href="/services/developer_loadtesting/">developer_loadtesting</a><br />
<a href="/services/deviceregistry/">deviceregistry</a><br />
<a href="/services/deviceupdate/">deviceupdate</a><br />
<a href="/services/devopsinfrastructure/">devopsinfrastructure</a><br />
<a href="/services/devtestlabs/">devtestlabs</a><br />
<a href="/services/digitaltwins/">digitaltwins</a><br />
<a href="/services/digitaltwins_core/">digitaltwins_core</a><br />
<a href="/services/disconnectedoperations/">disconnectedoperations</a><br />
<a href="/services/discovery/">discovery</a><br />
<a href="/services/dns/">dns</a><br />
<a href="/services/dnsresolver/">dnsresolver</a><br />
<a href="/services/domainregistration/">domainregistration</a><br />
<a href="/services/durabletask/">durabletask</a><br />
<a href="/services/edgeactions/">edgeactions</a><br />
<a href="/services/edgegateway/">edgegateway</a><br />
<a href="/services/edgezones/">edgezones</a><br />
<a href="/services/elasticsan/">elasticsan</a><br />
<a href="/services/eventgrid/">eventgrid</a><br />
<a href="/services/eventgrid_dataplane/">eventgrid_dataplane</a><br />
<a href="/services/eventhub/">eventhub</a><br />
<a href="/services/extendedlocation/">extendedlocation</a><br />
<a href="/services/fabric/">fabric</a><br />
<a href="/services/fileshares/">fileshares</a><br />
<a href="/services/fluidrelay/">fluidrelay</a><br />
<a href="/services/frontdoor/">frontdoor</a><br />
<a href="/services/graphservices/">graphservices</a><br />
<a href="/services/guestconfig/">guestconfig</a><br />
<a href="/services/hardwaresecuritymodules/">hardwaresecuritymodules</a><br />
<a href="/services/hdinsight/">hdinsight</a><br />
<a href="/services/health_deidentification/">health_deidentification</a><br />
<a href="/services/healthdataaiservices/">healthdataaiservices</a><br />
<a href="/services/healthinsights_cancerprofiling/">healthinsights_cancerprofiling</a><br />
<a href="/services/healthinsights_clinicalmatching/">healthinsights_clinicalmatching</a><br />
<a href="/services/healthinsights_radiologyinsights/">healthinsights_radiologyinsights</a><br />
<a href="/services/horizondb/">horizondb</a><br />
<a href="/services/hybridcompute/">hybridcompute</a><br />
<a href="/services/hybridconnectivity/">hybridconnectivity</a><br />
<a href="/services/hybridcontainerservice/">hybridcontainerservice</a><br />
<a href="/services/hybridkubernetes/">hybridkubernetes</a><br />
<a href="/services/hybridnetwork/">hybridnetwork</a><br />
<a href="/services/imagebuilder/">imagebuilder</a><br />
<a href="/services/impactreporting/">impactreporting</a><br />
<a href="/services/iot_deviceprovisioning/">iot_deviceprovisioning</a><br />
<a href="/services/iotcentral/">iotcentral</a><br />
<a href="/services/iotfirmwaredefense/">iotfirmwaredefense</a><br />
<a href="/services/iothub/">iothub</a><br />
<a href="/services/iothubprovisioningservices/">iothubprovisioningservices</a><br />
<a href="/services/iotoperations/">iotoperations</a><br />
<a href="/services/keyvault/">keyvault</a><br />
<a href="/services/keyvault_administration/">keyvault_administration</a><br />
<a href="/services/keyvault_certificates/">keyvault_certificates</a><br />
<a href="/services/keyvault_keys/">keyvault_keys</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/keyvault_secrets/">keyvault_secrets</a><br />
<a href="/services/keyvault_securitydomain/">keyvault_securitydomain</a><br />
<a href="/services/kubernetesconfiguration/">kubernetesconfiguration</a><br />
<a href="/services/kubernetesconfiguration_extensions/">kubernetesconfiguration_extensions</a><br />
<a href="/services/kubernetesconfiguration_extensiontypes/">kubernetesconfiguration_extensiontypes</a><br />
<a href="/services/kubernetesconfiguration_fluxconfigurations/">kubernetesconfiguration_fluxconfigurations</a><br />
<a href="/services/kubernetesconfiguration_privatelinkscopes/">kubernetesconfiguration_privatelinkscopes</a><br />
<a href="/services/kusto/">kusto</a><br />
<a href="/services/labservices/">labservices</a><br />
<a href="/services/largeinstance/">largeinstance</a><br />
<a href="/services/loadtesting/">loadtesting</a><br />
<a href="/services/loganalytics/">loganalytics</a><br />
<a href="/services/logic/">logic</a><br />
<a href="/services/machinelearningcompute/">machinelearningcompute</a><br />
<a href="/services/machinelearningservices/">machinelearningservices</a><br />
<a href="/services/maintenance/">maintenance</a><br />
<a href="/services/managedapplications/">managedapplications</a><br />
<a href="/services/managednetworkfabric/">managednetworkfabric</a><br />
<a href="/services/managedops/">managedops</a><br />
<a href="/services/managedservices/">managedservices</a><br />
<a href="/services/managementgroups/">managementgroups</a><br />
<a href="/services/maps/">maps</a><br />
<a href="/services/maps_geolocation/">maps_geolocation</a><br />
<a href="/services/maps_render/">maps_render</a><br />
<a href="/services/maps_route/">maps_route</a><br />
<a href="/services/maps_search/">maps_search</a><br />
<a href="/services/maps_timezone/">maps_timezone</a><br />
<a href="/services/maps_weather/">maps_weather</a><br />
<a href="/services/media/">media</a><br />
<a href="/services/messaging_webpubsubservice/">messaging_webpubsubservice</a><br />
<a href="/services/migrationassessment/">migrationassessment</a><br />
<a href="/services/migrationdiscoverysap/">migrationdiscoverysap</a><br />
<a href="/services/mongocluster/">mongocluster</a><br />
<a href="/services/monitor/">monitor</a><br />
<a href="/services/monitor_ingestion/">monitor_ingestion</a><br />
<a href="/services/monitor_opentelemetry_exporter/">monitor_opentelemetry_exporter</a><br />
<a href="/services/monitor_query/">monitor_query</a><br />
<a href="/services/monitor_querymetrics/">monitor_querymetrics</a><br />
<a href="/services/monitorslis/">monitorslis</a><br />
<a href="/services/monitorworkspaces/">monitorworkspaces</a><br />
<a href="/services/msi/">msi</a><br />
<a href="/services/mysqlflexibleservers/">mysqlflexibleservers</a><br />
<a href="/services/napsteromniagentapi/">napsteromniagentapi</a><br />
<a href="/services/network/">network</a><br />
<a href="/services/networkanalytics/">networkanalytics</a><br />
<a href="/services/networkcloud/">networkcloud</a><br />
<a href="/services/networkfunction/">networkfunction</a><br />
<a href="/services/notificationhubs/">notificationhubs</a><br />
<a href="/services/onlineexperimentation/">onlineexperimentation</a><br />
<a href="/services/onlineexperimentation_dataplane/">onlineexperimentation_dataplane</a><br />
<a href="/services/operationsmanagement/">operationsmanagement</a><br />
<a href="/services/orbital/">orbital</a><br />
<a href="/services/peering/">peering</a><br />
<a href="/services/pineconevectordb/">pineconevectordb</a><br />
<a href="/services/planetarycomputer/">planetarycomputer</a><br />
<a href="/services/planetarycomputer_dataplane/">planetarycomputer_dataplane</a><br />
<a href="/services/playwright/">playwright</a><br />
<a href="/services/playwrighttesting/">playwrighttesting</a><br />
<a href="/services/policyinsights/">policyinsights</a><br />
<a href="/services/portal/">portal</a><br />
<a href="/services/portalservicescopilot/">portalservicescopilot</a><br />
<a href="/services/postgresqlflexibleservers/">postgresqlflexibleservers</a><br />
<a href="/services/powerbidedicated/">powerbidedicated</a><br />
<a href="/services/powerbiembedded/">powerbiembedded</a><br />
<a href="/services/privatedns/">privatedns</a><br />
<a href="/services/programenrollment/">programenrollment</a><br />
<a href="/services/purview/">purview</a><br />
<a href="/services/purview_administration/">purview_administration</a><br />
<a href="/services/purview_catalog/">purview_catalog</a><br />
<a href="/services/purview_datamap/">purview_datamap</a><br />
<a href="/services/purview_scanning/">purview_scanning</a><br />
<a href="/services/purview_sharing/">purview_sharing</a><br />
<a href="/services/purview_workflow/">purview_workflow</a><br />
<a href="/services/quantum/">quantum</a><br />
<a href="/services/quota/">quota</a><br />
<a href="/services/rdbms/">rdbms</a><br />
<a href="/services/recoveryservices/">recoveryservices</a><br />
<a href="/services/recoveryservicesbackup/">recoveryservicesbackup</a><br />
<a href="/services/recoveryservicesbackup_passivestamp/">recoveryservicesbackup_passivestamp</a><br />
<a href="/services/recoveryservicesdatareplication/">recoveryservicesdatareplication</a><br />
<a href="/services/recoveryservicessiterecovery/">recoveryservicessiterecovery</a><br />
<a href="/services/relationships/">relationships</a><br />
<a href="/services/relay/">relay</a><br />
<a href="/services/reservations/">reservations</a><br />
<a href="/services/resiliencemanagement/">resiliencemanagement</a><br />
<a href="/services/resource/">resource</a><br />
<a href="/services/resource_bicep/">resource_bicep</a><br />
<a href="/services/resource_changes/">resource_changes</a><br />
<a href="/services/resource_databoundaries/">resource_databoundaries</a><br />
<a href="/services/resource_deployments/">resource_deployments</a><br />
<a href="/services/resource_deploymentscripts/">resource_deploymentscripts</a><br />
<a href="/services/resource_deploymentstacks/">resource_deploymentstacks</a><br />
<a href="/services/resource_features/">resource_features</a><br />
<a href="/services/resource_links/">resource_links</a><br />
<a href="/services/resource_locks/">resource_locks</a><br />
<a href="/services/resource_managedapplications/">resource_managedapplications</a><br />
<a href="/services/resource_policy/">resource_policy</a><br />
<a href="/services/resource_privatelinks/">resource_privatelinks</a><br />
<a href="/services/resource_subscriptions/">resource_subscriptions</a><br />
<a href="/services/resource_templatespecs/">resource_templatespecs</a><br />
<a href="/services/resourceconnector/">resourceconnector</a><br />
<a href="/services/resourcegraph/">resourcegraph</a><br />
<a href="/services/resourcehealth/">resourcehealth</a><br />
<a href="/services/resourcemover/">resourcemover</a><br />
<a href="/services/schemaregistry/">schemaregistry</a><br />
<a href="/services/scvmm/">scvmm</a><br />
<a href="/services/search/">search</a><br />
<a href="/services/search_documents/">search_documents</a><br />
<a href="/services/secretsstoreextension/">secretsstoreextension</a><br />
<a href="/services/security/">security</a><br />
<a href="/services/security_attestation/">security_attestation</a><br />
<a href="/services/securitydevops/">securitydevops</a><br />
<a href="/services/securityinsight/">securityinsight</a><br />
<a href="/services/serialconsole/">serialconsole</a><br />
<a href="/services/servicebus/">servicebus</a><br />
<a href="/services/servicefabric/">servicefabric</a><br />
<a href="/services/servicefabric_dataplane/">servicefabric_dataplane</a><br />
<a href="/services/servicefabricmanagedclusters/">servicefabricmanagedclusters</a><br />
<a href="/services/servicegroups/">servicegroups</a><br />
<a href="/services/servicelinker/">servicelinker</a><br />
<a href="/services/servicenetworking/">servicenetworking</a><br />
<a href="/services/signalr/">signalr</a><br />
<a href="/services/sitemanager/">sitemanager</a><br />
<a href="/services/sphere/">sphere</a><br />
<a href="/services/sql/">sql</a><br />
<a href="/services/sqlvirtualmachine/">sqlvirtualmachine</a><br />
<a href="/services/standbypool/">standbypool</a><br />
<a href="/services/storage/">storage</a><br />
<a href="/services/storage_blob/">storage_blob</a><br />
<a href="/services/storage_file_datalake/">storage_file_datalake</a><br />
<a href="/services/storage_file_share/">storage_file_share</a><br />
<a href="/services/storage_queue/">storage_queue</a><br />
<a href="/services/storageactions/">storageactions</a><br />
<a href="/services/storagecache/">storagecache</a><br />
<a href="/services/storagediscovery/">storagediscovery</a><br />
<a href="/services/storageimportexport/">storageimportexport</a><br />
<a href="/services/storagemover/">storagemover</a><br />
<a href="/services/storagepool/">storagepool</a><br />
<a href="/services/storagesync/">storagesync</a><br />
<a href="/services/streamanalytics/">streamanalytics</a><br />
<a href="/services/subscription/">subscription</a><br />
<a href="/services/support/">support</a><br />
<a href="/services/synapse/">synapse</a><br />
<a href="/services/synapse_accesscontrol/">synapse_accesscontrol</a><br />
<a href="/services/synapse_artifacts/">synapse_artifacts</a><br />
<a href="/services/synapse_managedprivateendpoints/">synapse_managedprivateendpoints</a><br />
<a href="/services/synapse_monitoring/">synapse_monitoring</a><br />
<a href="/services/synapse_spark/">synapse_spark</a><br />
<a href="/services/terraform/">terraform</a><br />
<a href="/services/timeseriesinsights/">timeseriesinsights</a><br />
<a href="/services/trafficmanager/">trafficmanager</a><br />
<a href="/services/videoanalyzer/">videoanalyzer</a><br />
<a href="/services/voiceservices/">voiceservices</a><br />
<a href="/services/web/">web</a><br />
<a href="/services/webpubsub/">webpubsub</a><br />
<a href="/services/workloadorchestration/">workloadorchestration</a><br />
</div>
</div>
