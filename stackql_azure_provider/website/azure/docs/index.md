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

total services: __268__  
total resources: __3741__  

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
<a href="/services/aad_domain_services/">aad_domain_services</a><br />
<a href="/services/advisor/">advisor</a><br />
<a href="/services/ai_agents/">ai_agents</a><br />
<a href="/services/ai_anomaly_detector/">ai_anomaly_detector</a><br />
<a href="/services/ai_content_safety/">ai_content_safety</a><br />
<a href="/services/ai_content_understanding/">ai_content_understanding</a><br />
<a href="/services/ai_discovery/">ai_discovery</a><br />
<a href="/services/ai_document_intelligence/">ai_document_intelligence</a><br />
<a href="/services/ai_evaluation/">ai_evaluation</a><br />
<a href="/services/ai_form_recognizer/">ai_form_recognizer</a><br />
<a href="/services/ai_inference/">ai_inference</a><br />
<a href="/services/ai_language/">ai_language</a><br />
<a href="/services/ai_personalizer/">ai_personalizer</a><br />
<a href="/services/ai_projects/">ai_projects</a><br />
<a href="/services/ai_text_analytics/">ai_text_analytics</a><br />
<a href="/services/ai_text_analytics_authoring/">ai_text_analytics_authoring</a><br />
<a href="/services/ai_transcription/">ai_transcription</a><br />
<a href="/services/ai_translation_document/">ai_translation_document</a><br />
<a href="/services/ai_translation_text/">ai_translation_text</a><br />
<a href="/services/ai_vision_face/">ai_vision_face</a><br />
<a href="/services/ai_vision_image_analysis/">ai_vision_image_analysis</a><br />
<a href="/services/ai_voice_live/">ai_voice_live</a><br />
<a href="/services/alerts_management/">alerts_management</a><br />
<a href="/services/api_center/">api_center</a><br />
<a href="/services/api_management/">api_management</a><br />
<a href="/services/app/">app</a><br />
<a href="/services/app_configuration/">app_configuration</a><br />
<a href="/services/app_configuration_dataplane/">app_configuration_dataplane</a><br />
<a href="/services/app_containers/">app_containers</a><br />
<a href="/services/app_network/">app_network</a><br />
<a href="/services/application_insights/">application_insights</a><br />
<a href="/services/artifact_signing/">artifact_signing</a><br />
<a href="/services/attestation/">attestation</a><br />
<a href="/services/authorization/">authorization</a><br />
<a href="/services/automanage/">automanage</a><br />
<a href="/services/automation/">automation</a><br />
<a href="/services/avs/">avs</a><br />
<a href="/services/azure_arc_data/">azure_arc_data</a><br />
<a href="/services/bare_metal_infrastructure/">bare_metal_infrastructure</a><br />
<a href="/services/batch/">batch</a><br />
<a href="/services/batch_dataplane/">batch_dataplane</a><br />
<a href="/services/billing/">billing</a><br />
<a href="/services/billing_benefits/">billing_benefits</a><br />
<a href="/services/blueprints/">blueprints</a><br />
<a href="/services/bot_service/">bot_service</a><br />
<a href="/services/carbon_optimization/">carbon_optimization</a><br />
<a href="/services/cdn/">cdn</a><br />
<a href="/services/certificate_registration/">certificate_registration</a><br />
<a href="/services/change_analysis/">change_analysis</a><br />
<a href="/services/chaos/">chaos</a><br />
<a href="/services/cloud_health/">cloud_health</a><br />
<a href="/services/cognitive_services/">cognitive_services</a><br />
<a href="/services/communication/">communication</a><br />
<a href="/services/communication_call_automation/">communication_call_automation</a><br />
<a href="/services/communication_chat/">communication_chat</a><br />
<a href="/services/communication_email/">communication_email</a><br />
<a href="/services/communication_identity/">communication_identity</a><br />
<a href="/services/communication_job_router/">communication_job_router</a><br />
<a href="/services/communication_messages/">communication_messages</a><br />
<a href="/services/communication_phone_numbers/">communication_phone_numbers</a><br />
<a href="/services/communication_rooms/">communication_rooms</a><br />
<a href="/services/communication_sms/">communication_sms</a><br />
<a href="/services/compute/">compute</a><br />
<a href="/services/compute_bulk_actions/">compute_bulk_actions</a><br />
<a href="/services/compute_fleet/">compute_fleet</a><br />
<a href="/services/compute_limit/">compute_limit</a><br />
<a href="/services/compute_recommender/">compute_recommender</a><br />
<a href="/services/compute_schedule/">compute_schedule</a><br />
<a href="/services/confidential_ledger/">confidential_ledger</a><br />
<a href="/services/confidential_ledger_certificate/">confidential_ledger_certificate</a><br />
<a href="/services/confidential_ledger_dataplane/">confidential_ledger_dataplane</a><br />
<a href="/services/connected_vmware/">connected_vmware</a><br />
<a href="/services/consumption/">consumption</a><br />
<a href="/services/container_instance/">container_instance</a><br />
<a href="/services/container_orchestrator_runtime/">container_orchestrator_runtime</a><br />
<a href="/services/container_registry/">container_registry</a><br />
<a href="/services/container_registry_dataplane/">container_registry_dataplane</a><br />
<a href="/services/container_registry_tasks/">container_registry_tasks</a><br />
<a href="/services/container_service/">container_service</a><br />
<a href="/services/container_service_fleet/">container_service_fleet</a><br />
<a href="/services/container_service_safeguards/">container_service_safeguards</a><br />
<a href="/services/cosmosdb/">cosmosdb</a><br />
<a href="/services/cosmosdb_for_postgresql/">cosmosdb_for_postgresql</a><br />
<a href="/services/cost_management/">cost_management</a><br />
<a href="/services/custom_providers/">custom_providers</a><br />
<a href="/services/dashboard/">dashboard</a><br />
<a href="/services/data_box/">data_box</a><br />
<a href="/services/data_box_edge/">data_box_edge</a><br />
<a href="/services/data_factory/">data_factory</a><br />
<a href="/services/data_migration/">data_migration</a><br />
<a href="/services/data_protection/">data_protection</a><br />
<a href="/services/data_share/">data_share</a><br />
<a href="/services/data_tables/">data_tables</a><br />
<a href="/services/database_watcher/">database_watcher</a><br />
<a href="/services/datalake_analytics/">datalake_analytics</a><br />
<a href="/services/datalake_store/">datalake_store</a><br />
<a href="/services/defender_easm/">defender_easm</a><br />
<a href="/services/defender_easm_dataplane/">defender_easm_dataplane</a><br />
<a href="/services/dependency_map/">dependency_map</a><br />
<a href="/services/desktop_virtualization/">desktop_virtualization</a><br />
<a href="/services/dev_test_labs/">dev_test_labs</a><br />
<a href="/services/devcenter/">devcenter</a><br />
<a href="/services/developer_devcenter/">developer_devcenter</a><br />
<a href="/services/developer_loadtesting/">developer_loadtesting</a><br />
<a href="/services/device_registry/">device_registry</a><br />
<a href="/services/device_update/">device_update</a><br />
<a href="/services/devops_infrastructure/">devops_infrastructure</a><br />
<a href="/services/digital_twins/">digital_twins</a><br />
<a href="/services/digital_twins_core/">digital_twins_core</a><br />
<a href="/services/discovery/">discovery</a><br />
<a href="/services/dns/">dns</a><br />
<a href="/services/dns_resolver/">dns_resolver</a><br />
<a href="/services/domain_registration/">domain_registration</a><br />
<a href="/services/durable_task/">durable_task</a><br />
<a href="/services/edge_actions/">edge_actions</a><br />
<a href="/services/edge_gateway/">edge_gateway</a><br />
<a href="/services/edge_zones/">edge_zones</a><br />
<a href="/services/elastic_san/">elastic_san</a><br />
<a href="/services/event_grid/">event_grid</a><br />
<a href="/services/event_grid_dataplane/">event_grid_dataplane</a><br />
<a href="/services/event_hub/">event_hub</a><br />
<a href="/services/extended_location/">extended_location</a><br />
<a href="/services/fabric/">fabric</a><br />
<a href="/services/file_shares/">file_shares</a><br />
<a href="/services/fluid_relay/">fluid_relay</a><br />
<a href="/services/front_door/">front_door</a><br />
<a href="/services/guest_config/">guest_config</a><br />
<a href="/services/hardware_security_modules/">hardware_security_modules</a><br />
<a href="/services/hdinsight/">hdinsight</a><br />
<a href="/services/horizon_db/">horizon_db</a><br />
<a href="/services/hybrid_compute/">hybrid_compute</a><br />
<a href="/services/hybrid_connectivity/">hybrid_connectivity</a><br />
<a href="/services/hybrid_container_service/">hybrid_container_service</a><br />
<a href="/services/hybrid_kubernetes/">hybrid_kubernetes</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/image_builder/">image_builder</a><br />
<a href="/services/impact_reporting/">impact_reporting</a><br />
<a href="/services/iot_device_provisioning/">iot_device_provisioning</a><br />
<a href="/services/iot_hub/">iot_hub</a><br />
<a href="/services/iot_hub_provisioning_services/">iot_hub_provisioning_services</a><br />
<a href="/services/iot_operations/">iot_operations</a><br />
<a href="/services/key_vault/">key_vault</a><br />
<a href="/services/key_vault_administration/">key_vault_administration</a><br />
<a href="/services/key_vault_certificates/">key_vault_certificates</a><br />
<a href="/services/key_vault_keys/">key_vault_keys</a><br />
<a href="/services/key_vault_secrets/">key_vault_secrets</a><br />
<a href="/services/key_vault_security_domain/">key_vault_security_domain</a><br />
<a href="/services/kubernetes_configuration/">kubernetes_configuration</a><br />
<a href="/services/kusto/">kusto</a><br />
<a href="/services/large_instance/">large_instance</a><br />
<a href="/services/load_testing/">load_testing</a><br />
<a href="/services/log_analytics/">log_analytics</a><br />
<a href="/services/logic/">logic</a><br />
<a href="/services/machine_learning_compute/">machine_learning_compute</a><br />
<a href="/services/machine_learning_services/">machine_learning_services</a><br />
<a href="/services/maintenance/">maintenance</a><br />
<a href="/services/managed_applications/">managed_applications</a><br />
<a href="/services/managed_ops/">managed_ops</a><br />
<a href="/services/managed_services/">managed_services</a><br />
<a href="/services/management_groups/">management_groups</a><br />
<a href="/services/maps/">maps</a><br />
<a href="/services/maps_geolocation/">maps_geolocation</a><br />
<a href="/services/maps_render/">maps_render</a><br />
<a href="/services/maps_route/">maps_route</a><br />
<a href="/services/maps_search/">maps_search</a><br />
<a href="/services/maps_timezone/">maps_timezone</a><br />
<a href="/services/maps_weather/">maps_weather</a><br />
<a href="/services/marketplace_ordering/">marketplace_ordering</a><br />
<a href="/services/messaging_webpubsubservice/">messaging_webpubsubservice</a><br />
<a href="/services/migration_assessment/">migration_assessment</a><br />
<a href="/services/mongo_cluster/">mongo_cluster</a><br />
<a href="/services/monitor/">monitor</a><br />
<a href="/services/monitor_ingestion/">monitor_ingestion</a><br />
<a href="/services/monitor_opentelemetry_exporter/">monitor_opentelemetry_exporter</a><br />
<a href="/services/monitor_query/">monitor_query</a><br />
<a href="/services/monitor_query_metrics/">monitor_query_metrics</a><br />
<a href="/services/monitor_slis/">monitor_slis</a><br />
<a href="/services/monitor_workspaces/">monitor_workspaces</a><br />
<a href="/services/msi/">msi</a><br />
<a href="/services/mysql_flexible_servers/">mysql_flexible_servers</a><br />
<a href="/services/netapp/">netapp</a><br />
<a href="/services/network/">network</a><br />
<a href="/services/network_function/">network_function</a><br />
<a href="/services/notification_hubs/">notification_hubs</a><br />
<a href="/services/online_experimentation/">online_experimentation</a><br />
<a href="/services/online_experimentation_dataplane/">online_experimentation_dataplane</a><br />
<a href="/services/operations_management/">operations_management</a><br />
<a href="/services/peering/">peering</a><br />
<a href="/services/planetary_computer/">planetary_computer</a><br />
<a href="/services/planetary_computer_dataplane/">planetary_computer_dataplane</a><br />
<a href="/services/playwright/">playwright</a><br />
<a href="/services/playwright_testing/">playwright_testing</a><br />
<a href="/services/policy_insights/">policy_insights</a><br />
<a href="/services/portal/">portal</a><br />
<a href="/services/postgresql_flexible_servers/">postgresql_flexible_servers</a><br />
<a href="/services/power_bi_dedicated/">power_bi_dedicated</a><br />
<a href="/services/power_bi_embedded/">power_bi_embedded</a><br />
<a href="/services/private_dns/">private_dns</a><br />
<a href="/services/purview/">purview</a><br />
<a href="/services/purview_administration/">purview_administration</a><br />
<a href="/services/purview_catalog/">purview_catalog</a><br />
<a href="/services/purview_data_map/">purview_data_map</a><br />
<a href="/services/purview_scanning/">purview_scanning</a><br />
<a href="/services/purview_sharing/">purview_sharing</a><br />
<a href="/services/purview_workflow/">purview_workflow</a><br />
<a href="/services/quantum/">quantum</a><br />
<a href="/services/quota/">quota</a><br />
<a href="/services/recovery_services/">recovery_services</a><br />
<a href="/services/recovery_services_backup/">recovery_services_backup</a><br />
<a href="/services/recovery_services_backup_passive_stamp/">recovery_services_backup_passive_stamp</a><br />
<a href="/services/recovery_services_data_replication/">recovery_services_data_replication</a><br />
<a href="/services/recovery_services_site_recovery/">recovery_services_site_recovery</a><br />
<a href="/services/red_hat_openshift/">red_hat_openshift</a><br />
<a href="/services/redis/">redis</a><br />
<a href="/services/redis_enterprise/">redis_enterprise</a><br />
<a href="/services/relationships/">relationships</a><br />
<a href="/services/relay/">relay</a><br />
<a href="/services/reservations/">reservations</a><br />
<a href="/services/resilience_management/">resilience_management</a><br />
<a href="/services/resource/">resource</a><br />
<a href="/services/resource_connector/">resource_connector</a><br />
<a href="/services/resource_graph/">resource_graph</a><br />
<a href="/services/resource_health/">resource_health</a><br />
<a href="/services/resource_mover/">resource_mover</a><br />
<a href="/services/schema_registry/">schema_registry</a><br />
<a href="/services/scvmm/">scvmm</a><br />
<a href="/services/search/">search</a><br />
<a href="/services/search_documents/">search_documents</a><br />
<a href="/services/secrets_store_extension/">secrets_store_extension</a><br />
<a href="/services/security/">security</a><br />
<a href="/services/security_attestation/">security_attestation</a><br />
<a href="/services/security_devops/">security_devops</a><br />
<a href="/services/security_insight/">security_insight</a><br />
<a href="/services/serial_console/">serial_console</a><br />
<a href="/services/service_bus/">service_bus</a><br />
<a href="/services/service_fabric/">service_fabric</a><br />
<a href="/services/service_fabric_dataplane/">service_fabric_dataplane</a><br />
<a href="/services/service_fabric_managed_clusters/">service_fabric_managed_clusters</a><br />
<a href="/services/service_groups/">service_groups</a><br />
<a href="/services/service_linker/">service_linker</a><br />
<a href="/services/service_networking/">service_networking</a><br />
<a href="/services/signalr/">signalr</a><br />
<a href="/services/site_manager/">site_manager</a><br />
<a href="/services/sql/">sql</a><br />
<a href="/services/sql_virtual_machine/">sql_virtual_machine</a><br />
<a href="/services/standby_pool/">standby_pool</a><br />
<a href="/services/storage/">storage</a><br />
<a href="/services/storage_actions/">storage_actions</a><br />
<a href="/services/storage_blob/">storage_blob</a><br />
<a href="/services/storage_cache/">storage_cache</a><br />
<a href="/services/storage_discovery/">storage_discovery</a><br />
<a href="/services/storage_file_datalake/">storage_file_datalake</a><br />
<a href="/services/storage_file_share/">storage_file_share</a><br />
<a href="/services/storage_mover/">storage_mover</a><br />
<a href="/services/storage_queue/">storage_queue</a><br />
<a href="/services/storage_sync/">storage_sync</a><br />
<a href="/services/stream_analytics/">stream_analytics</a><br />
<a href="/services/subscription/">subscription</a><br />
<a href="/services/support/">support</a><br />
<a href="/services/synapse/">synapse</a><br />
<a href="/services/synapse_access_control/">synapse_access_control</a><br />
<a href="/services/synapse_artifacts/">synapse_artifacts</a><br />
<a href="/services/synapse_managed_private_endpoints/">synapse_managed_private_endpoints</a><br />
<a href="/services/synapse_monitoring/">synapse_monitoring</a><br />
<a href="/services/synapse_spark/">synapse_spark</a><br />
<a href="/services/traffic_manager/">traffic_manager</a><br />
<a href="/services/web/">web</a><br />
<a href="/services/web_pubsub/">web_pubsub</a><br />
<a href="/services/workload_orchestration/">workload_orchestration</a><br />
</div>
</div>
