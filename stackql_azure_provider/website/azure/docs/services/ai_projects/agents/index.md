--- 
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
  - ai_projects
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

Creates, updates, deletes, gets or lists an <code>agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_projects.agents" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_session_log_stream"
    values={[
        { label: 'get_session_log_stream', value: 'get_session_log_stream' },
        { label: 'list_session_files', value: 'list_session_files' },
        { label: 'get_version', value: 'get_version' },
        { label: 'get_session', value: 'get_session' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_session_log_stream">

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
    <td><CopyableCode code="data" /></td>
    <td><code>string</code></td>
    <td>The event payload as plain text. Currently JSON-formatted but the schema is not contractual and may change. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="event" /></td>
    <td><code>string</code></td>
    <td>The SSE event type. Currently `log`, but additional event types may be added in the future. Clients should ignore unrecognized event types. Required. "log" (log)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_session_files">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the file or directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="is_directory" /></td>
    <td><code>boolean</code></td>
    <td>Whether this entry is a directory. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="modified_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) when the file was last modified. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>integer</code></td>
    <td>The size in bytes (0 for directories). Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_version">

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
    <td>The unique identifier of the agent version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Name can be used to retrieve/update/delete the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agent_guid" /></td>
    <td><code>string</code></td>
    <td>The unique GUID identifier of the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint_reference" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (seconds) when the agent was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A human-readable description of the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="draft" /></td>
    <td><code>boolean</code></td>
    <td>Whether this agent version is a draft (candidate) rather than a release. Draft versions are recorded but excluded from default 'latest' resolution and are not auto-promoted. Defaults to false.</td>
</tr>
<tr>
    <td><CopyableCode code="instance_identity" /></td>
    <td><code>object</code></td>
    <td>The instance identity of the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard. Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'agent.version'. Required. AGENT_VERSION.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the agent version. Defaults to 'active' for non-hosted agents. For hosted agents, reflects infrastructure readiness. Known values are: "creating", "active", "failed", "deleting", and "deleted". (creating, active, failed, deleting, deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version identifier of the agent. Agents are immutable and every update creates a new version while keeping the name same. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_session">

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
    <td><CopyableCode code="agent_session_id" /></td>
    <td><code>string</code></td>
    <td>The session identifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="created_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) when the session was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) when the session expires (rolling, 30 days from last activity). Required.</td>
</tr>
<tr>
    <td><CopyableCode code="last_accessed_at" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Unix timestamp (in seconds) when the session was last accessed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The current status of the session. Required. Known values are: "creating", "active", "idle", "updating", "failed", "deleting", "deleted", and "expired". (creating, active, idle, updating, failed, deleting, deleted, expired)</td>
</tr>
<tr>
    <td><CopyableCode code="version_indicator" /></td>
    <td><code>object</code></td>
    <td>The version indicator determining which agent version backs this session. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td>The unique identifier of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agent_card" /></td>
    <td><code>object</code></td>
    <td>:vartype agent_card: ~azure.ai.projects.models.AgentCard</td>
</tr>
<tr>
    <td><CopyableCode code="agent_endpoint" /></td>
    <td><code>object</code></td>
    <td>The endpoint configuration for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint_reference" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="instance_identity" /></td>
    <td><code>object</code></td>
    <td>The instance identity of the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'agent'. Required. AGENT.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The operational state of the agent. Controls whether the agent endpoint accepts or rejects requests. Required. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>object</code></td>
    <td>The latest version of the agent. Required.</td>
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
    <td>The unique identifier of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="agent_card" /></td>
    <td><code>object</code></td>
    <td>:vartype agent_card: ~azure.ai.projects.models.AgentCard</td>
</tr>
<tr>
    <td><CopyableCode code="agent_endpoint" /></td>
    <td><code>object</code></td>
    <td>The endpoint configuration for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="blueprint_reference" /></td>
    <td><code>object</code></td>
    <td>The blueprint for the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="instance_identity" /></td>
    <td><code>object</code></td>
    <td>The instance identity of the agent.</td>
</tr>
<tr>
    <td><CopyableCode code="object" /></td>
    <td><code>string</code></td>
    <td>The object type, which is always 'agent'. Required. AGENT.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The operational state of the agent. Controls whether the agent endpoint accepts or rejects requests. Required. Known values are: "enabled" and "disabled". (enabled, disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>object</code></td>
    <td>The latest version of the agent. Required.</td>
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
    <td><a href="#get_session_log_stream"><CopyableCode code="get_session_log_stream" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_version"><code>agent_version</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stream console logs for a hosted agent session. Streams console logs (stdout / stderr) for a specific hosted agent session as a Server-Sent Events (SSE) stream. Each SSE frame contains: * `event`: always `"log"` * `data`: a plain-text log line (currently JSON-formatted, but the schema is not contractual and may include additional keys or change format over time; clients should treat it as an opaque string) Example SSE frames: .. code-block:: event: log data: &#123;"timestamp":"2026-03-10T09:33:17.121Z","stream":"stdout","message":"Starting FoundryCBAgent server on port 8088"&#125; event: log data: &#123;"timestamp":"2026-03-10T09:33:17.130Z","stream":"stderr","message":"INFO: Application startup complete."&#125; event: log data: &#123;"timestamp":"2026-03-10T09:34:52.714Z","stream":"status","message":"Successfully connected to container"&#125; event: log data: &#123;"timestamp":"2026-03-10T09:35:52.714Z","stream":"status","message":"No logs since last 60 seconds"&#125; The stream remains open until the client disconnects or the server terminates the connection. Clients should handle reconnection as needed.</td>
</tr>
<tr>
    <td><a href="#list_session_files"><CopyableCode code="list_session_files" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_session_id"><code>agent_session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-path"><code>path</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List session files. Returns files and directories at the specified path in the session sandbox. The response includes only the immediate children of the target directory and defaults to the session home directory when no path is supplied.</td>
</tr>
<tr>
    <td><a href="#get_version"><CopyableCode code="get_version" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_version"><code>agent_version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an agent version. Retrieves the specified version of an agent by its agent name and version identifier.</td>
</tr>
<tr>
    <td><a href="#get_session"><CopyableCode code="get_session" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get a session. Retrieves the details of a hosted agent session by agent name and session identifier.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get an agent. Retrieves an agent definition by its unique name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-kind"><code>kind</code></a>, <a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List agents. Returns a paged collection of agent resources.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete an agent. Deletes an agent. For hosted agents, if any version has active sessions, the request is rejected with HTTP 409 unless `force` is set to true. When force is true, all associated sessions are cascade-deleted along with the agent and its versions.</td>
</tr>
<tr>
    <td><a href="#update_details"><CopyableCode code="update_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update an agent endpoint. Applies a merge-patch update to the specified agent endpoint configuration.</td>
</tr>
<tr>
    <td><a href="#list_versions"><CopyableCode code="list_versions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a>, <a href="#parameter-include_drafts"><code>include_drafts</code></a></td>
    <td>List agent versions. Returns a paged collection of versions for the specified agent.</td>
</tr>
<tr>
    <td><a href="#create_version"><CopyableCode code="create_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create an agent version. Creates a new version for the specified agent and returns the created version resource.</td>
</tr>
<tr>
    <td><a href="#list_sessions"><CopyableCode code="list_sessions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-limit"><code>limit</code></a>, <a href="#parameter-order"><code>order</code></a>, <a href="#parameter-after"><code>after</code></a>, <a href="#parameter-before"><code>before</code></a></td>
    <td>List sessions for an agent. Returns a paged collection of sessions associated with the specified agent endpoint.</td>
</tr>
<tr>
    <td><a href="#create_session"><CopyableCode code="create_session" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a session. Creates a new session for an agent endpoint. The endpoint resolves the backing agent version from `version_indicator` and enforces session ownership using the provided user identity for session-mutating operations.</td>
</tr>
<tr>
    <td><a href="#delete_session_file"><CopyableCode code="delete_session_file" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_session_id"><code>agent_session_id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-recursive"><code>recursive</code></a></td>
    <td>Delete a session file. Deletes the specified file or directory from the session sandbox. When `recursive` is false, deleting a non-empty directory returns 409 Conflict.</td>
</tr>
<tr>
    <td><a href="#delete_version"><CopyableCode code="delete_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_version"><code>agent_version</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-force"><code>force</code></a></td>
    <td>Delete an agent version. Deletes a specific version of an agent. For hosted agents, if the version has active sessions, the request is rejected with HTTP 409 unless `force` is set to true. When force is true, all sessions associated with this version are cascade-deleted.</td>
</tr>
<tr>
    <td><a href="#delete_session"><CopyableCode code="delete_session" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Delete a session. Deletes a session synchronously. Returns 204 No Content when the session is deleted or does not exist.</td>
</tr>
<tr>
    <td><a href="#create_version_from_manifest"><CopyableCode code="create_version_from_manifest" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create an agent version from manifest. Imports the provided manifest to create a new version for the specified agent.</td>
</tr>
<tr>
    <td><a href="#download_code"><CopyableCode code="download_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-agent_version"><code>agent_version</code></a></td>
    <td>Download agent code. Downloads the code zip for a code-based hosted agent. Returns the previously-uploaded zip (`application/zip`). If `agent_version` is supplied, returns that version's code zip; otherwise returns the latest version's code zip. The SHA-256 digest of the returned bytes matches the `content_hash` on the resolved version's `code_configuration`.</td>
</tr>
<tr>
    <td><a href="#enable"><CopyableCode code="enable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Enable an agent. Enables the specified agent, allowing it to accept new sessions and process requests. This operation is idempotent — enabling an already-enabled agent returns success with no side effects.</td>
</tr>
<tr>
    <td><a href="#disable"><CopyableCode code="disable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Disable an agent. Disables the specified agent, preventing it from accepting new sessions or processing requests. Existing active sessions are allowed to drain gracefully but no new sessions can be created. This operation is idempotent — disabling an already-disabled agent returns success with no side effects.</td>
</tr>
<tr>
    <td><a href="#stop_session"><CopyableCode code="stop_session" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-session_id"><code>session_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Stop a session. Terminates the specified hosted agent session and returns 204 No Content when the request succeeds.</td>
</tr>
<tr>
    <td><a href="#upload_session_file"><CopyableCode code="upload_session_file" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_session_id"><code>agent_session_id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Upload a session file. Uploads binary file content to the specified path in the session sandbox. The service stores the file relative to the session home directory and rejects payloads larger than 50 MB.</td>
</tr>
<tr>
    <td><a href="#download_session_file"><CopyableCode code="download_session_file" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-agent_name"><code>agent_name</code></a>, <a href="#parameter-agent_session_id"><code>agent_session_id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Download a session file. Downloads the file at the specified sandbox path as a binary stream. The path is resolved relative to the session home directory.</td>
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
<tr id="parameter-agent_name">
    <td><CopyableCode code="agent_name" /></td>
    <td><code>string</code></td>
    <td>The name of the agent. Required.</td>
</tr>
<tr id="parameter-agent_session_id">
    <td><CopyableCode code="agent_session_id" /></td>
    <td><code>string</code></td>
    <td>The session ID. Required.</td>
</tr>
<tr id="parameter-agent_version">
    <td><CopyableCode code="agent_version" /></td>
    <td><code>string</code></td>
    <td>The version of the agent to delete. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The file path to download from the sandbox, relative to the session home directory. Required.</td>
</tr>
<tr id="parameter-session_id">
    <td><CopyableCode code="session_id" /></td>
    <td><code>string</code></td>
    <td>The session identifier. Required.</td>
</tr>
<tr id="parameter-after">
    <td><CopyableCode code="after" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-agent_version">
    <td><CopyableCode code="agent_version" /></td>
    <td><code>string</code></td>
    <td>The version of the agent whose code zip should be downloaded. If omitted, the latest version's code zip is returned. Default value is None.</td>
</tr>
<tr id="parameter-before">
    <td><CopyableCode code="before" /></td>
    <td><code>string</code></td>
    <td>A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list. Default value is None.</td>
</tr>
<tr id="parameter-force">
    <td><CopyableCode code="force" /></td>
    <td><code>boolean</code></td>
    <td>For Hosted Agents, if `true`, force-deletes the version even if it has active sessions, cascading deletion to all associated sessions. The service defaults to `false` if a value is not specified by the caller. This value is not relevant for other Agent types. Default value is None.</td>
</tr>
<tr id="parameter-include_drafts">
    <td><CopyableCode code="include_drafts" /></td>
    <td><code>boolean</code></td>
    <td>(Preview) Whether to include draft versions in the listing. The service defaults to `false` if a value is not specified by the caller (only non-draft versions are returned). Default value is None.</td>
</tr>
<tr id="parameter-kind">
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Filter agents by kind. If not provided, all agents are returned. Known values are: "prompt", "hosted", "workflow", and "external". Default value is None.</td>
</tr>
<tr id="parameter-limit">
    <td><CopyableCode code="limit" /></td>
    <td><code>integer</code></td>
    <td>A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20. Default value is None.</td>
</tr>
<tr id="parameter-order">
    <td><CopyableCode code="order" /></td>
    <td><code>string</code></td>
    <td>Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and`desc` for descending order. Known values are: "asc" and "desc". Default value is None.</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The directory path to list, relative to the session home directory. Defaults to the home directory if not provided. Default value is None.</td>
</tr>
<tr id="parameter-recursive">
    <td><CopyableCode code="recursive" /></td>
    <td><code>boolean</code></td>
    <td>Whether to recursively delete directory contents. The service defaults to `false` if a value is not specified by the caller. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_session_log_stream"
    values={[
        { label: 'get_session_log_stream', value: 'get_session_log_stream' },
        { label: 'list_session_files', value: 'list_session_files' },
        { label: 'get_version', value: 'get_version' },
        { label: 'get_session', value: 'get_session' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_session_log_stream">

Stream console logs for a hosted agent session. Streams console logs (stdout / stderr) for a specific hosted agent session as a Server-Sent Events (SSE) stream. Each SSE frame contains: * `event`: always `"log"` * `data`: a plain-text log line (currently JSON-formatted, but the schema is not contractual and may include additional keys or change format over time; clients should treat it as an opaque string) Example SSE frames: .. code-block:: event: log data: &#123;"timestamp":"2026-03-10T09:33:17.121Z","stream":"stdout","message":"Starting FoundryCBAgent server on port 8088"&#125; event: log data: &#123;"timestamp":"2026-03-10T09:33:17.130Z","stream":"stderr","message":"INFO: Application startup complete."&#125; event: log data: &#123;"timestamp":"2026-03-10T09:34:52.714Z","stream":"status","message":"Successfully connected to container"&#125; event: log data: &#123;"timestamp":"2026-03-10T09:35:52.714Z","stream":"status","message":"No logs since last 60 seconds"&#125; The stream remains open until the client disconnects or the server terminates the connection. Clients should handle reconnection as needed.

```sql
SELECT
data,
event
FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' -- required
AND agent_version = '{{ agent_version }}' -- required
AND session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_session_files">

List session files. Returns files and directories at the specified path in the session sandbox. The response includes only the immediate children of the target directory and defaults to the session home directory when no path is supplied.

```sql
SELECT
name,
is_directory,
modified_time,
size
FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' -- required
AND agent_session_id = '{{ agent_session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND path = '{{ path }}'
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
```
</TabItem>
<TabItem value="get_version">

Get an agent version. Retrieves the specified version of an agent by its agent name and version identifier.

```sql
SELECT
id,
name,
agent_guid,
blueprint,
blueprint_reference,
created_at,
definition,
description,
draft,
instance_identity,
metadata,
object,
status,
version
FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' -- required
AND agent_version = '{{ agent_version }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_session">

Get a session. Retrieves the details of a hosted agent session by agent name and session identifier.

```sql
SELECT
agent_session_id,
created_at,
expires_at,
last_accessed_at,
status,
version_indicator
FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' -- required
AND session_id = '{{ session_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get an agent. Retrieves an agent definition by its unique name.

```sql
SELECT
id,
name,
agent_card,
agent_endpoint,
blueprint,
blueprint_reference,
instance_identity,
object,
state,
versions
FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

List agents. Returns a paged collection of agent resources.

```sql
SELECT
id,
name,
agent_card,
agent_endpoint,
blueprint,
blueprint_reference,
instance_identity,
object,
state,
versions
FROM azure.ai_projects.agents
WHERE endpoint = '{{ endpoint }}' -- required
AND kind = '{{ kind }}'
AND limit = '{{ limit }}'
AND order = '{{ order }}'
AND after = '{{ after }}'
AND before = '{{ before }}'
;
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

Delete an agent. Deletes an agent. For hosted agents, if any version has active sessions, the request is rejected with HTTP 409 unless `force` is set to true. When force is true, all associated sessions are cascade-deleted along with the agent and its versions.

```sql
DELETE FROM azure.ai_projects.agents
WHERE agent_name = '{{ agent_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND force = '{{ force }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_details"
    values={[
        { label: 'update_details', value: 'update_details' },
        { label: 'list_versions', value: 'list_versions' },
        { label: 'create_version', value: 'create_version' },
        { label: 'list_sessions', value: 'list_sessions' },
        { label: 'create_session', value: 'create_session' },
        { label: 'delete_session_file', value: 'delete_session_file' },
        { label: 'delete_version', value: 'delete_version' },
        { label: 'delete_session', value: 'delete_session' },
        { label: 'create_version_from_manifest', value: 'create_version_from_manifest' },
        { label: 'download_code', value: 'download_code' },
        { label: 'enable', value: 'enable' },
        { label: 'disable', value: 'disable' },
        { label: 'stop_session', value: 'stop_session' },
        { label: 'upload_session_file', value: 'upload_session_file' },
        { label: 'download_session_file', value: 'download_session_file' }
    ]}
>
<TabItem value="update_details">

Update an agent endpoint. Applies a merge-patch update to the specified agent endpoint configuration.

```sql
EXEC azure.ai_projects.agents.update_details 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_versions">

List agent versions. Returns a paged collection of versions for the specified agent.

```sql
EXEC azure.ai_projects.agents.list_versions 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}', 
@include_drafts={{ include_drafts }}
;
```
</TabItem>
<TabItem value="create_version">

Create an agent version. Creates a new version for the specified agent and returns the created version resource.

```sql
EXEC azure.ai_projects.agents.create_version 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_sessions">

List sessions for an agent. Returns a paged collection of sessions associated with the specified agent endpoint.

```sql
EXEC azure.ai_projects.agents.list_sessions 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@limit='{{ limit }}', 
@order='{{ order }}', 
@after='{{ after }}', 
@before='{{ before }}'
;
```
</TabItem>
<TabItem value="create_session">

Create a session. Creates a new session for an agent endpoint. The endpoint resolves the backing agent version from `version_indicator` and enforces session ownership using the provided user identity for session-mutating operations.

```sql
EXEC azure.ai_projects.agents.create_session 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="delete_session_file">

Delete a session file. Deletes the specified file or directory from the session sandbox. When `recursive` is false, deleting a non-empty directory returns 409 Conflict.

```sql
EXEC azure.ai_projects.agents.delete_session_file 
@agent_name='{{ agent_name }}' --required, 
@agent_session_id='{{ agent_session_id }}' --required, 
@path='{{ path }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@recursive={{ recursive }}
;
```
</TabItem>
<TabItem value="delete_version">

Delete an agent version. Deletes a specific version of an agent. For hosted agents, if the version has active sessions, the request is rejected with HTTP 409 unless `force` is set to true. When force is true, all sessions associated with this version are cascade-deleted.

```sql
EXEC azure.ai_projects.agents.delete_version 
@agent_name='{{ agent_name }}' --required, 
@agent_version='{{ agent_version }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@force={{ force }}
;
```
</TabItem>
<TabItem value="delete_session">

Delete a session. Deletes a session synchronously. Returns 204 No Content when the session is deleted or does not exist.

```sql
EXEC azure.ai_projects.agents.delete_session 
@agent_name='{{ agent_name }}' --required, 
@session_id='{{ session_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="create_version_from_manifest">

Create an agent version from manifest. Imports the provided manifest to create a new version for the specified agent.

```sql
EXEC azure.ai_projects.agents.create_version_from_manifest 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="download_code">

Download agent code. Downloads the code zip for a code-based hosted agent. Returns the previously-uploaded zip (`application/zip`). If `agent_version` is supplied, returns that version's code zip; otherwise returns the latest version's code zip. The SHA-256 digest of the returned bytes matches the `content_hash` on the resolved version's `code_configuration`.

```sql
EXEC azure.ai_projects.agents.download_code 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@agent_version='{{ agent_version }}'
;
```
</TabItem>
<TabItem value="enable">

Enable an agent. Enables the specified agent, allowing it to accept new sessions and process requests. This operation is idempotent — enabling an already-enabled agent returns success with no side effects.

```sql
EXEC azure.ai_projects.agents.enable 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="disable">

Disable an agent. Disables the specified agent, preventing it from accepting new sessions or processing requests. Existing active sessions are allowed to drain gracefully but no new sessions can be created. This operation is idempotent — disabling an already-disabled agent returns success with no side effects.

```sql
EXEC azure.ai_projects.agents.disable 
@agent_name='{{ agent_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="stop_session">

Stop a session. Terminates the specified hosted agent session and returns 204 No Content when the request succeeds.

```sql
EXEC azure.ai_projects.agents.stop_session 
@agent_name='{{ agent_name }}' --required, 
@session_id='{{ session_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="upload_session_file">

Upload a session file. Uploads binary file content to the specified path in the session sandbox. The service stores the file relative to the session home directory and rejects payloads larger than 50 MB.

```sql
EXEC azure.ai_projects.agents.upload_session_file 
@agent_name='{{ agent_name }}' --required, 
@agent_session_id='{{ agent_session_id }}' --required, 
@path='{{ path }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="download_session_file">

Download a session file. Downloads the file at the specified sandbox path as a binary stream. The path is resolved relative to the session home directory.

```sql
EXEC azure.ai_projects.agents.download_session_file 
@agent_name='{{ agent_name }}' --required, 
@agent_session_id='{{ agent_session_id }}' --required, 
@path='{{ path }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
