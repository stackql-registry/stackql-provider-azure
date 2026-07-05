--- 
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
  - maps_route
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

Creates, updates, deletes, gets or lists a <code>route</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="route" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_route.route" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_route_directions"
    values={[
        { label: 'get_route_directions', value: 'get_route_directions' },
        { label: 'get_route_matrix', value: 'get_route_matrix' }
    ]}
>
<TabItem value="get_route_directions">

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
    <td><CopyableCode code="formatVersion" /></td>
    <td><code>string</code></td>
    <td>Format Version property.</td>
</tr>
<tr>
    <td><CopyableCode code="optimizedWaypoints" /></td>
    <td><code>array</code></td>
    <td>Optimized sequence of waypoints. It shows the index from the user provided waypoint sequence for the original and optimized list. For instance, a response: .. code-block:: means that the original sequence is [0, 1, 2] and optimized sequence is [1, 2, 0]. Since the index starts by 0 the original is "first, second, third" while the optimized is "second, third, first".</td>
</tr>
<tr>
    <td><CopyableCode code="report" /></td>
    <td><code>object</code></td>
    <td>Reports the effective settings used in the current call.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>Routes array.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_route_matrix">

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
    <td><CopyableCode code="formatVersion" /></td>
    <td><code>string</code></td>
    <td>Format Version property.</td>
</tr>
<tr>
    <td><CopyableCode code="matrix" /></td>
    <td><code>array</code></td>
    <td>Results as a 2 dimensional array of route summaries.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>object</code></td>
    <td>Summary object.</td>
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
    <td><a href="#get_route_directions"><CopyableCode code="get_route_directions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxAlternatives"><code>maxAlternatives</code></a>, <a href="#parameter-alternativeType"><code>alternativeType</code></a>, <a href="#parameter-minDeviationDistance"><code>minDeviationDistance</code></a>, <a href="#parameter-arriveAt"><code>arriveAt</code></a>, <a href="#parameter-departAt"><code>departAt</code></a>, <a href="#parameter-minDeviationTime"><code>minDeviationTime</code></a>, <a href="#parameter-instructionsType"><code>instructionsType</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-computeBestOrder"><code>computeBestOrder</code></a>, <a href="#parameter-routeRepresentation"><code>routeRepresentation</code></a>, <a href="#parameter-computeTravelTimeFor"><code>computeTravelTimeFor</code></a>, <a href="#parameter-vehicleHeading"><code>vehicleHeading</code></a>, <a href="#parameter-report"><code>report</code></a>, <a href="#parameter-sectionType"><code>sectionType</code></a>, <a href="#parameter-vehicleAxleWeight"><code>vehicleAxleWeight</code></a>, <a href="#parameter-vehicleWidth"><code>vehicleWidth</code></a>, <a href="#parameter-vehicleHeight"><code>vehicleHeight</code></a>, <a href="#parameter-vehicleLength"><code>vehicleLength</code></a>, <a href="#parameter-vehicleMaxSpeed"><code>vehicleMaxSpeed</code></a>, <a href="#parameter-vehicleWeight"><code>vehicleWeight</code></a>, <a href="#parameter-vehicleCommercial"><code>vehicleCommercial</code></a>, <a href="#parameter-windingness"><code>windingness</code></a>, <a href="#parameter-hilliness"><code>hilliness</code></a>, <a href="#parameter-travelMode"><code>travelMode</code></a>, <a href="#parameter-traffic"><code>traffic</code></a>, <a href="#parameter-routeType"><code>routeType</code></a>, <a href="#parameter-vehicleLoadType"><code>vehicleLoadType</code></a>, <a href="#parameter-vehicleEngineType"><code>vehicleEngineType</code></a>, <a href="#parameter-constantSpeedConsumptionInLitersPerHundredkm"><code>constantSpeedConsumptionInLitersPerHundredkm</code></a>, <a href="#parameter-currentFuelInLiters"><code>currentFuelInLiters</code></a>, <a href="#parameter-auxiliaryPowerInLitersPerHour"><code>auxiliaryPowerInLitersPerHour</code></a>, <a href="#parameter-fuelEnergyDensityInMJoulesPerLiter"><code>fuelEnergyDensityInMJoulesPerLiter</code></a>, <a href="#parameter-accelerationEfficiency"><code>accelerationEfficiency</code></a>, <a href="#parameter-decelerationEfficiency"><code>decelerationEfficiency</code></a>, <a href="#parameter-uphillEfficiency"><code>uphillEfficiency</code></a>, <a href="#parameter-downhillEfficiency"><code>downhillEfficiency</code></a>, <a href="#parameter-constantSpeedConsumptionInkWhPerHundredkm"><code>constantSpeedConsumptionInkWhPerHundredkm</code></a>, <a href="#parameter-currentChargeInkWh"><code>currentChargeInkWh</code></a>, <a href="#parameter-maxChargeInkWh"><code>maxChargeInkWh</code></a>, <a href="#parameter-auxiliaryPowerInkW"><code>auxiliaryPowerInkW</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. Returns a route between an origin and a destination, passing through waypoints if they are specified. The route will take into account factors such as current traffic and the typical road speeds on the requested day of the week and time of day. Information returned includes the distance, estimated travel time, and a representation of the route geometry. Additional routing information such as optimized waypoint order or turn by turn instructions is also available, depending on the options selected. Routing service provides a set of parameters for a detailed description of vehicle-specific Consumption Model. Please check `Consumption Model `_ for detailed explanation of the concepts and parameters involved.</td>
</tr>
<tr>
    <td><a href="#get_route_matrix"><CopyableCode code="get_route_matrix" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.</td>
</tr>
<tr>
    <td><a href="#request_route_matrix"><CopyableCode code="request_route_matrix" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-waitForResults"><code>waitForResults</code></a>, <a href="#parameter-computeTravelTimeFor"><code>computeTravelTimeFor</code></a>, <a href="#parameter-sectionType"><code>sectionType</code></a>, <a href="#parameter-arriveAt"><code>arriveAt</code></a>, <a href="#parameter-departAt"><code>departAt</code></a>, <a href="#parameter-vehicleAxleWeight"><code>vehicleAxleWeight</code></a>, <a href="#parameter-vehicleLength"><code>vehicleLength</code></a>, <a href="#parameter-vehicleHeight"><code>vehicleHeight</code></a>, <a href="#parameter-vehicleWidth"><code>vehicleWidth</code></a>, <a href="#parameter-vehicleMaxSpeed"><code>vehicleMaxSpeed</code></a>, <a href="#parameter-vehicleWeight"><code>vehicleWeight</code></a>, <a href="#parameter-windingness"><code>windingness</code></a>, <a href="#parameter-hilliness"><code>hilliness</code></a>, <a href="#parameter-travelMode"><code>travelMode</code></a>, <a href="#parameter-traffic"><code>traffic</code></a>, <a href="#parameter-routeType"><code>routeType</code></a>, <a href="#parameter-vehicleLoadType"><code>vehicleLoadType</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. The Matrix Routing service allows calculation of a matrix of route summaries for a set of routes defined by origin and destination locations by using an asynchronous (async) or synchronous (sync) POST request. For every given origin, the service calculates the cost of routing from that origin to every given destination. The set of origins and the set of destinations can be thought of as the column and row headers of a table and each cell in the table contains the costs of routing from the origin to the destination for that cell. As an example, let's say a food delivery company has 20 drivers and they need to find the closest driver to pick up the delivery from the restaurant. To solve this use case, they can call Matrix Route API. For each route, the travel times and distances are returned. You can use the computed costs to determine which detailed routes to calculate using the Route Directions API. The maximum size of a matrix for async request is **700** and for sync request it's **100** (the number of origins multiplied by the number of destinations). Submit Synchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ If your scenario requires synchronous requests and the maximum size of the matrix is less than or equal to 100, you might want to make synchronous request. The maximum size of a matrix for this API is **100** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 10x10, 6x8, 9x8 (it does not need to be square). .. code-block:: POST https://atlas.microsoft.com/route/matrix/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Submit Asynchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex routing requests. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. If `waitForResults` parameter in the request is set to true, user will get a 200 response if the request is finished under 120 seconds. The maximum size of a matrix for this API is **700** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 50x10, 10x10, 28x25. 10x70 (it does not need to be square). The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. .. code-block:: POST https://atlas.microsoft.com/route/matrix/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's a typical sequence of asynchronous operations: #. Client sends a Route Matrix POST request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Route Matrix request has been accepted. HTTP `Error` - There was an error processing your Route Matrix request. This could either be a 400 Bad Request or any other Error status code. #. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.</td>
</tr>
<tr>
    <td><a href="#get_route_directions_with_additional_parameters"><CopyableCode code="get_route_directions_with_additional_parameters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxAlternatives"><code>maxAlternatives</code></a>, <a href="#parameter-alternativeType"><code>alternativeType</code></a>, <a href="#parameter-minDeviationDistance"><code>minDeviationDistance</code></a>, <a href="#parameter-minDeviationTime"><code>minDeviationTime</code></a>, <a href="#parameter-instructionsType"><code>instructionsType</code></a>, <a href="#parameter-language"><code>language</code></a>, <a href="#parameter-computeBestOrder"><code>computeBestOrder</code></a>, <a href="#parameter-routeRepresentation"><code>routeRepresentation</code></a>, <a href="#parameter-computeTravelTimeFor"><code>computeTravelTimeFor</code></a>, <a href="#parameter-vehicleHeading"><code>vehicleHeading</code></a>, <a href="#parameter-report"><code>report</code></a>, <a href="#parameter-sectionType"><code>sectionType</code></a>, <a href="#parameter-arriveAt"><code>arriveAt</code></a>, <a href="#parameter-departAt"><code>departAt</code></a>, <a href="#parameter-vehicleAxleWeight"><code>vehicleAxleWeight</code></a>, <a href="#parameter-vehicleLength"><code>vehicleLength</code></a>, <a href="#parameter-vehicleHeight"><code>vehicleHeight</code></a>, <a href="#parameter-vehicleWidth"><code>vehicleWidth</code></a>, <a href="#parameter-vehicleMaxSpeed"><code>vehicleMaxSpeed</code></a>, <a href="#parameter-vehicleWeight"><code>vehicleWeight</code></a>, <a href="#parameter-vehicleCommercial"><code>vehicleCommercial</code></a>, <a href="#parameter-windingness"><code>windingness</code></a>, <a href="#parameter-hilliness"><code>hilliness</code></a>, <a href="#parameter-travelMode"><code>travelMode</code></a>, <a href="#parameter-traffic"><code>traffic</code></a>, <a href="#parameter-routeType"><code>routeType</code></a>, <a href="#parameter-vehicleLoadType"><code>vehicleLoadType</code></a>, <a href="#parameter-vehicleEngineType"><code>vehicleEngineType</code></a>, <a href="#parameter-constantSpeedConsumptionInLitersPerHundredkm"><code>constantSpeedConsumptionInLitersPerHundredkm</code></a>, <a href="#parameter-currentFuelInLiters"><code>currentFuelInLiters</code></a>, <a href="#parameter-auxiliaryPowerInLitersPerHour"><code>auxiliaryPowerInLitersPerHour</code></a>, <a href="#parameter-fuelEnergyDensityInMJoulesPerLiter"><code>fuelEnergyDensityInMJoulesPerLiter</code></a>, <a href="#parameter-accelerationEfficiency"><code>accelerationEfficiency</code></a>, <a href="#parameter-decelerationEfficiency"><code>decelerationEfficiency</code></a>, <a href="#parameter-uphillEfficiency"><code>uphillEfficiency</code></a>, <a href="#parameter-downhillEfficiency"><code>downhillEfficiency</code></a>, <a href="#parameter-constantSpeedConsumptionInkWhPerHundredkm"><code>constantSpeedConsumptionInkWhPerHundredkm</code></a>, <a href="#parameter-currentChargeInkWh"><code>currentChargeInkWh</code></a>, <a href="#parameter-maxChargeInkWh"><code>maxChargeInkWh</code></a>, <a href="#parameter-auxiliaryPowerInkW"><code>auxiliaryPowerInkW</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. Returns a route between an origin and a destination, passing through waypoints if they are specified. The route will take into account factors such as current traffic and the typical road speeds on the requested day of the week and time of day. Information returned includes the distance, estimated travel time, and a representation of the route geometry. Additional routing information such as optimized waypoint order or turn by turn instructions is also available, depending on the options selected. Routing service provides a set of parameters for a detailed description of a vehicle-specific Consumption Model. Please check `Consumption Model `_ for detailed explanation of the concepts and parameters involved.</td>
</tr>
<tr>
    <td><a href="#get_route_range"><CopyableCode code="get_route_range" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-fuelBudgetInLiters"><code>fuelBudgetInLiters</code></a>, <a href="#parameter-energyBudgetInkWh"><code>energyBudgetInkWh</code></a>, <a href="#parameter-timeBudgetInSec"><code>timeBudgetInSec</code></a>, <a href="#parameter-distanceBudgetInMeters"><code>distanceBudgetInMeters</code></a>, <a href="#parameter-departAt"><code>departAt</code></a>, <a href="#parameter-routeType"><code>routeType</code></a>, <a href="#parameter-traffic"><code>traffic</code></a>, <a href="#parameter-travelMode"><code>travelMode</code></a>, <a href="#parameter-hilliness"><code>hilliness</code></a>, <a href="#parameter-windingness"><code>windingness</code></a>, <a href="#parameter-vehicleAxleWeight"><code>vehicleAxleWeight</code></a>, <a href="#parameter-vehicleWidth"><code>vehicleWidth</code></a>, <a href="#parameter-vehicleHeight"><code>vehicleHeight</code></a>, <a href="#parameter-vehicleLength"><code>vehicleLength</code></a>, <a href="#parameter-vehicleMaxSpeed"><code>vehicleMaxSpeed</code></a>, <a href="#parameter-vehicleWeight"><code>vehicleWeight</code></a>, <a href="#parameter-vehicleCommercial"><code>vehicleCommercial</code></a>, <a href="#parameter-vehicleLoadType"><code>vehicleLoadType</code></a>, <a href="#parameter-vehicleEngineType"><code>vehicleEngineType</code></a>, <a href="#parameter-constantSpeedConsumptionInLitersPerHundredkm"><code>constantSpeedConsumptionInLitersPerHundredkm</code></a>, <a href="#parameter-currentFuelInLiters"><code>currentFuelInLiters</code></a>, <a href="#parameter-auxiliaryPowerInLitersPerHour"><code>auxiliaryPowerInLitersPerHour</code></a>, <a href="#parameter-fuelEnergyDensityInMJoulesPerLiter"><code>fuelEnergyDensityInMJoulesPerLiter</code></a>, <a href="#parameter-accelerationEfficiency"><code>accelerationEfficiency</code></a>, <a href="#parameter-decelerationEfficiency"><code>decelerationEfficiency</code></a>, <a href="#parameter-uphillEfficiency"><code>uphillEfficiency</code></a>, <a href="#parameter-downhillEfficiency"><code>downhillEfficiency</code></a>, <a href="#parameter-constantSpeedConsumptionInkWhPerHundredkm"><code>constantSpeedConsumptionInkWhPerHundredkm</code></a>, <a href="#parameter-currentChargeInkWh"><code>currentChargeInkWh</code></a>, <a href="#parameter-maxChargeInkWh"><code>maxChargeInkWh</code></a>, <a href="#parameter-auxiliaryPowerInkW"><code>auxiliaryPowerInkW</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Route Range (Isochrone) API** **Applies to**\ : see pricing `tiers `_. This service will calculate a set of locations that can be reached from the origin point based on fuel, energy, time or distance budget that is specified. A polygon boundary (or Isochrone) is returned in a counterclockwise orientation as well as the precise polygon center which was the result of the origin point. The returned polygon can be used for further processing such as `Search Inside Geometry `_ to search for POIs within the provided Isochrone.</td>
</tr>
<tr>
    <td><a href="#get_route_directions_batch"><CopyableCode code="get_route_directions_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. Download Asynchronous Batch Results ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ To download the async batch results you will issue a `GET` request to the batch download endpoint. This *download URL* can be obtained from the `Location` header of a successful `POST` batch request and looks like the following: .. code-block:: https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's the typical sequence of operations for downloading the batch results: #. Client sends a `GET` request using the *download URL*. #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Batch request successfully processed. The response body contains all the batch results. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;</td>
</tr>
<tr>
    <td><a href="#request_route_directions_batch"><CopyableCode code="request_route_directions_batch" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Route Directions Batch API** **Applies to**\ : see pricing `tiers `_. The Route Directions Batch API sends batches of queries to `Route Directions API `_ using just a single API call. You can call Route Directions Batch API to run either asynchronously (async) or synchronously (sync). The async API allows caller to batch up to **700** queries and sync API up to **100** queries. Submit Asynchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex route requests * It allows the retrieval of results in a separate call (multiple downloads are possible). * The asynchronous API is optimized for reliability and is not expected to run into a timeout. * The number of batch items is limited to **700** for this API. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. Please note that asynchronous batch request is a long-running request. Here's a typical sequence of operations: #. Client sends a Route Directions Batch `POST` request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request has been accepted. HTTP `Error` - There was an error processing your Batch request. This could either be a `400 Bad Request` or any other `Error` status code. #. If the batch request was accepted successfully, the `Location` header in the response contains the URL to download the results of the batch request. This status URI looks like following: `GET https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0` Note:- Please remember to add AUTH information (subscription-key/azure_auth - See `Security <#security>`_\ ) to the *status URI* before running it. #. Client issues a `GET` request on the *download URL* obtained in Step 3 to download the batch results. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *route directions* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 3 *route directions* queries: .. code-block:: json &#123; "batchItems": [ &#123; "query": "?query=47.620659,-122.348934:47.610101,-122.342015&travelMode=bicycle&routeType=eco&traffic=false" &#125;, &#123; "query": "?query=40.759856,-73.985108:40.771136,-73.973506&travelMode=pedestrian&routeType=shortest" &#125;, &#123; "query": "?query=48.923159,-122.557362:32.621279,-116.840362" &#125; ] &#125; A *route directions* query in a batch is just a partial URL *without* the protocol, base URL, path, api-version and subscription-key. It can accept any of the supported *route directions* `URI parameters `_. The string values in the *route directions* query must be properly escaped (e.g. " character should be escaped with ) and it should also be properly URL-encoded. The async API allows caller to batch up to **700** queries and sync API up to **100** queries, and the batch should contain at least **1** query. Download Asynchronous Batch Results ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ To download the async batch results you will issue a `GET` request to the batch download endpoint. This *download URL* can be obtained from the `Location` header of a successful `POST` batch request and looks like the following: .. code-block:: https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's the typical sequence of operations for downloading the batch results: #. Client sends a `GET` request using the *download URL*. #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Batch request successfully processed. The response body contains all the batch results. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;</td>
</tr>
<tr>
    <td><a href="#request_route_matrix_sync"><CopyableCode code="request_route_matrix_sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-waitForResults"><code>waitForResults</code></a>, <a href="#parameter-computeTravelTimeFor"><code>computeTravelTimeFor</code></a>, <a href="#parameter-sectionType"><code>sectionType</code></a>, <a href="#parameter-arriveAt"><code>arriveAt</code></a>, <a href="#parameter-departAt"><code>departAt</code></a>, <a href="#parameter-vehicleAxleWeight"><code>vehicleAxleWeight</code></a>, <a href="#parameter-vehicleLength"><code>vehicleLength</code></a>, <a href="#parameter-vehicleHeight"><code>vehicleHeight</code></a>, <a href="#parameter-vehicleWidth"><code>vehicleWidth</code></a>, <a href="#parameter-vehicleMaxSpeed"><code>vehicleMaxSpeed</code></a>, <a href="#parameter-vehicleWeight"><code>vehicleWeight</code></a>, <a href="#parameter-windingness"><code>windingness</code></a>, <a href="#parameter-hilliness"><code>hilliness</code></a>, <a href="#parameter-travelMode"><code>travelMode</code></a>, <a href="#parameter-traffic"><code>traffic</code></a>, <a href="#parameter-routeType"><code>routeType</code></a>, <a href="#parameter-vehicleLoadType"><code>vehicleLoadType</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Applies to**\ : see pricing `tiers `_. The Matrix Routing service allows calculation of a matrix of route summaries for a set of routes defined by origin and destination locations by using an asynchronous (async) or synchronous (sync) POST request. For every given origin, the service calculates the cost of routing from that origin to every given destination. The set of origins and the set of destinations can be thought of as the column and row headers of a table and each cell in the table contains the costs of routing from the origin to the destination for that cell. As an example, let's say a food delivery company has 20 drivers and they need to find the closest driver to pick up the delivery from the restaurant. To solve this use case, they can call Matrix Route API. For each route, the travel times and distances are returned. You can use the computed costs to determine which detailed routes to calculate using the Route Directions API. The maximum size of a matrix for async request is **700** and for sync request it's **100** (the number of origins multiplied by the number of destinations). Submit Synchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ If your scenario requires synchronous requests and the maximum size of the matrix is less than or equal to 100, you might want to make synchronous request. The maximum size of a matrix for this API is **100** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 10x10, 6x8, 9x8 (it does not need to be square). .. code-block:: POST https://atlas.microsoft.com/route/matrix/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Submit Asynchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex routing requests. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. If `waitForResults` parameter in the request is set to true, user will get a 200 response if the request is finished under 120 seconds. The maximum size of a matrix for this API is **700** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 50x10, 10x10, 28x25. 10x70 (it does not need to be square). The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. .. code-block:: POST https://atlas.microsoft.com/route/matrix/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's a typical sequence of asynchronous operations: #. Client sends a Route Matrix POST request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Route Matrix request has been accepted. HTTP `Error` - There was an error processing your Route Matrix request. This could either be a 400 Bad Request or any other Error status code. #. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.</td>
</tr>
<tr>
    <td><a href="#request_route_directions_batch_sync"><CopyableCode code="request_route_directions_batch_sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>**Route Directions Batch API** **Applies to**\ : see pricing `tiers `_. The Route Directions Batch API sends batches of queries to `Route Directions API `_ using just a single API call. You can call Route Directions Batch API to run either asynchronously (async) or synchronously (sync). The async API allows caller to batch up to **700** queries and sync API up to **100** queries. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. .. code-block:: POST https://atlas.microsoft.com/route/directions/batch/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;</td>
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
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Desired format of the response. Only `json` format is supported. "json" Default value is "json".</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>array</code></td>
    <td>The Coordinate from which the range calculation should start. Required.</td>
</tr>
<tr id="parameter-accelerationEfficiency">
    <td><CopyableCode code="accelerationEfficiency" /></td>
    <td><code>number</code></td>
    <td>Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates *(i.e. KineticEnergyGained/ChemicalEnergyConsumed). ChemicalEnergyConsumed* is obtained by converting consumed fuel to chemical energy using **fuelEnergyDensityInMJoulesPerLiter**. Must be paired with **decelerationEfficiency**. The range of values allowed are 0.0 to 1/\ **decelerationEfficiency**. Sensible Values : for **Combustion Model** : 0.33, for **Electric Model** : 0.66. Default value is None.</td>
</tr>
<tr id="parameter-alternativeType">
    <td><CopyableCode code="alternativeType" /></td>
    <td><code>string</code></td>
    <td>Controls the optimality, with respect to the given planning criteria, of the calculated alternatives compared to the reference route. Known values are: "anyRoute" and "betterRoute". Default value is None.</td>
</tr>
<tr id="parameter-arriveAt">
    <td><CopyableCode code="arriveAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of arrival at the destination point. It must be specified as a dateTime. When a time zone offset is not specified it will be assumed to be that of the destination point. The arriveAt value must be in the future. The arriveAt parameter cannot be used in conjunction with departAt, minDeviationDistance or minDeviationTime. Default value is None.</td>
</tr>
<tr id="parameter-auxiliaryPowerInLitersPerHour">
    <td><CopyableCode code="auxiliaryPowerInLitersPerHour" /></td>
    <td><code>number</code></td>
    <td>Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. It can be used to specify consumption due to devices and systems such as AC systems, radio, heating, etc. Sensible Values : 0.2. Default value is None.</td>
</tr>
<tr id="parameter-auxiliaryPowerInkW">
    <td><CopyableCode code="auxiliaryPowerInkW" /></td>
    <td><code>number</code></td>
    <td>Specifies the amount of power consumed for sustaining auxiliary systems, in kilowatts (kW). It can be used to specify consumption due to devices and systems such as AC systems, radio, heating, etc. Sensible Values : 1.7. Default value is None.</td>
</tr>
<tr id="parameter-computeBestOrder">
    <td><CopyableCode code="computeBestOrder" /></td>
    <td><code>boolean</code></td>
    <td>Re-order the route waypoints using a fast heuristic algorithm to reduce the route length. Yields best results when used in conjunction with routeType *shortest*. Notice that origin and destination are excluded from the optimized waypoint indices. To include origin and destination in the response, please increase all the indices by 1 to account for the origin, and then add the destination as the final index. Possible values are true or false. True computes a better order if possible, but is not allowed to be used in conjunction with maxAlternatives value greater than 0 or in conjunction with circle waypoints. False will use the locations in the given order and not allowed to be used in conjunction with routeRepresentation *none*. Default value is None.</td>
</tr>
<tr id="parameter-computeTravelTimeFor">
    <td><CopyableCode code="computeTravelTimeFor" /></td>
    <td><code>string</code></td>
    <td>Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time. Known values are: "none" and "all". Default value is None.</td>
</tr>
<tr id="parameter-constantSpeedConsumptionInLitersPerHundredkm">
    <td><CopyableCode code="constantSpeedConsumptionInLitersPerHundredkm" /></td>
    <td><code>string</code></td>
    <td>Specifies the speed-dependent component of consumption. Provided as an unordered list of colon-delimited speed & consumption-rate pairs. The list defines points on a consumption curve. Consumption rates for speeds not in the list are found as follows: * by linear interpolation, if the given speed lies in between two speeds in the list * by linear extrapolation otherwise, assuming a constant (ΔConsumption/ΔSpeed) determined by the nearest two points in the list The list must contain between 1 and 25 points (inclusive), and may not contain duplicate points for the same speed. If it only contains a single point, then the consumption rate of that point is used without further processing. Consumption specified for the largest speed must be greater than or equal to that of the penultimate largest speed. This ensures that extrapolation does not lead to negative consumption rates. Similarly, consumption values specified for the two smallest speeds in the list cannot lead to a negative consumption rate for any smaller speed. The valid range for the consumption values(expressed in l/100km) is between 0.01 and 100000.0. Sensible Values : 50,6.3:130,11.5 **Note** : This parameter is required for **The Combustion Consumption Model**. Default value is None.</td>
</tr>
<tr id="parameter-constantSpeedConsumptionInkWhPerHundredkm">
    <td><CopyableCode code="constantSpeedConsumptionInkWhPerHundredkm" /></td>
    <td><code>string</code></td>
    <td>Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. The list defines points on a consumption curve. Consumption rates for speeds not in the list are found as follows: * by linear interpolation, if the given speed lies in between two speeds in the list * by linear extrapolation otherwise, assuming a constant (ΔConsumption/ΔSpeed) determined by the nearest two points in the list The list must contain between 1 and 25 points (inclusive), and may not contain duplicate points for the same speed. If it only contains a single point, then the consumption rate of that point is used without further processing. Consumption specified for the largest speed must be greater than or equal to that of the penultimate largest speed. This ensures that extrapolation does not lead to negative consumption rates. Similarly, consumption values specified for the two smallest speeds in the list cannot lead to a negative consumption rate for any smaller speed. The valid range for the consumption values(expressed in kWh/100km) is between 0.01 and 100000.0. Sensible Values : 50,8.2:130,21.3 This parameter is required for **Electric consumption model**. Default value is None.</td>
</tr>
<tr id="parameter-currentChargeInkWh">
    <td><CopyableCode code="currentChargeInkWh" /></td>
    <td><code>number</code></td>
    <td>Specifies the current electric energy supply in kilowatt hours (kWh). This parameter co-exists with **maxChargeInkWh** parameter. The range of values allowed are 0.0 to **maxChargeInkWh**. Sensible Values : 43. Default value is None.</td>
</tr>
<tr id="parameter-currentFuelInLiters">
    <td><CopyableCode code="currentFuelInLiters" /></td>
    <td><code>number</code></td>
    <td>Specifies the current supply of fuel in liters. Sensible Values : 55. Default value is None.</td>
</tr>
<tr id="parameter-decelerationEfficiency">
    <td><CopyableCode code="decelerationEfficiency" /></td>
    <td><code>number</code></td>
    <td>Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates *(i.e. ChemicalEnergySaved/KineticEnergyLost). ChemicalEnergySaved* is obtained by converting saved (not consumed) fuel to energy using **fuelEnergyDensityInMJoulesPerLiter**. Must be paired with **accelerationEfficiency**. The range of values allowed are 0.0 to 1/\ **accelerationEfficiency**. Sensible Values : for **Combustion Model** : 0.83, for **Electric Model** : 0.91. Default value is None.</td>
</tr>
<tr id="parameter-departAt">
    <td><CopyableCode code="departAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of departure from the origin point. Departure times apart from now must be specified as a dateTime. When a time zone offset is not specified, it will be assumed to be that of the origin point. The departAt value must be in the future in the date-time format (1996-12-19T16:39:57-08:00). Default value is None.</td>
</tr>
<tr id="parameter-distanceBudgetInMeters">
    <td><CopyableCode code="distanceBudgetInMeters" /></td>
    <td><code>number</code></td>
    <td>Distance budget in meters that determines maximal range which can be travelled using driving distance. The Consumption Model will only affect the range when routeType is eco. Exactly one budget (fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, or distanceBudgetInMeters) must be used. Default value is None.</td>
</tr>
<tr id="parameter-downhillEfficiency">
    <td><CopyableCode code="downhillEfficiency" /></td>
    <td><code>number</code></td>
    <td>Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation *(i.e. ChemicalEnergySaved/PotentialEnergyLost). ChemicalEnergySaved* is obtained by converting saved (not consumed) fuel to energy using **fuelEnergyDensityInMJoulesPerLiter**. Must be paired with **uphillEfficiency**. The range of values allowed are 0.0 to 1/\ **uphillEfficiency**. Sensible Values : for **Combustion Model** : 0.51, for **Electric Model** : 0.73. Default value is None.</td>
</tr>
<tr id="parameter-energyBudgetInkWh">
    <td><CopyableCode code="energyBudgetInkWh" /></td>
    <td><code>number</code></td>
    <td>Electric energy budget in kilowatt hours (kWh) that determines maximal range which can be travelled using the specified Electric Consumption Model. When energyBudgetInkWh is used, it is mandatory to specify a detailed Electric Consumption Model. Exactly one budget (fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, or distanceBudgetInMeters) must be used. Default value is None.</td>
</tr>
<tr id="parameter-fuelBudgetInLiters">
    <td><CopyableCode code="fuelBudgetInLiters" /></td>
    <td><code>number</code></td>
    <td>Fuel budget in liters that determines maximal range which can be travelled using the specified Combustion Consumption Model. When fuelBudgetInLiters is used, it is mandatory to specify a detailed Combustion Consumption Model. Exactly one budget (fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, or distanceBudgetInMeters) must be used. Default value is None.</td>
</tr>
<tr id="parameter-fuelEnergyDensityInMJoulesPerLiter">
    <td><CopyableCode code="fuelEnergyDensityInMJoulesPerLiter" /></td>
    <td><code>number</code></td>
    <td>Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). It is used in conjunction with the ***Efficiency** parameters for conversions between saved or consumed energy and fuel. For example, energy density is 34.2 MJ/l for gasoline, and 35.8 MJ/l for Diesel fuel. This parameter is required if any ***Efficiency** parameter is set. Sensible Values : 34.2. Default value is None.</td>
</tr>
<tr id="parameter-hilliness">
    <td><CopyableCode code="hilliness" /></td>
    <td><code>string</code></td>
    <td>Degree of hilliness for thrilling route. This parameter can only be used in conjunction with `routeType`\ =thrilling. Known values are: "low", "normal", and "high". Default value is None.</td>
</tr>
<tr id="parameter-instructionsType">
    <td><CopyableCode code="instructionsType" /></td>
    <td><code>string</code></td>
    <td>If specified, guidance instructions will be returned. Note that the instructionsType parameter cannot be used in conjunction with routeRepresentation=none. Known values are: "coded", "text", and "tagged". Default value is None.</td>
</tr>
<tr id="parameter-language">
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The language parameter determines the language of the guidance messages. It does not affect proper nouns (the names of streets, plazas, etc.) It has no effect when instructionsType=coded. Allowed values are (a subset of) the IETF language tags described. Default value is None.</td>
</tr>
<tr id="parameter-maxAlternatives">
    <td><CopyableCode code="maxAlternatives" /></td>
    <td><code>integer</code></td>
    <td>Number of desired alternative routes to be calculated. Default: 0, minimum: 0 and maximum: 5. Default value is None.</td>
</tr>
<tr id="parameter-maxChargeInkWh">
    <td><CopyableCode code="maxChargeInkWh" /></td>
    <td><code>number</code></td>
    <td>Specifies the maximum electric energy supply in kilowatt hours (kWh) that may be stored in the vehicle's battery. This parameter co-exists with **currentChargeInkWh** parameter. Minimum value has to be greater than or equal to **currentChargeInkWh**. Sensible Values : 85. Default value is None.</td>
</tr>
<tr id="parameter-minDeviationDistance">
    <td><CopyableCode code="minDeviationDistance" /></td>
    <td><code>integer</code></td>
    <td>All alternative routes returned will follow the reference route (see section POST Requests) from the origin point of the calculateRoute request for at least this number of meters. Can only be used when reconstructing a route. The minDeviationDistance parameter cannot be used in conjunction with arriveAt. Default value is None.</td>
</tr>
<tr id="parameter-minDeviationTime">
    <td><CopyableCode code="minDeviationTime" /></td>
    <td><code>integer</code></td>
    <td>All alternative routes returned will follow the reference route (see section POST Requests) from the origin point of the calculateRoute request for at least this number of seconds. Can only be used when reconstructing a route. The minDeviationTime parameter cannot be used in conjunction with arriveAt. Default value is 0. Setting )minDeviationTime_ to a value greater than zero has the following consequences: * The origin point of the *calculateRoute* Request must be on (or very near) the input reference route. * If this is not the case, an error is returned. * However, the origin point does not need to be at the beginning of the input reference route (it can be thought of as the current vehicle position on the reference route). * The reference route, returned as the first route in the *calculateRoute* Response, will start at the origin point specified in the *calculateRoute* Request. The initial part of the input reference route up until the origin point will be excluded from the Response. * The values of *minDeviationDistance* and *minDeviationTime* determine how far alternative routes will be guaranteed to follow the reference route from the origin point onwards. * The route must use *departAt*. * The *vehicleHeading* is ignored. Default value is None.</td>
</tr>
<tr id="parameter-report">
    <td><CopyableCode code="report" /></td>
    <td><code>string</code></td>
    <td>Specifies which data should be reported for diagnosis purposes. The only possible value is *effectiveSettings*. Reports the effective parameters or data used when calling the API. In the case of defaulted parameters the default will be reflected where the parameter was not specified by the caller. "effectiveSettings" Default value is None.</td>
</tr>
<tr id="parameter-routeRepresentation">
    <td><CopyableCode code="routeRepresentation" /></td>
    <td><code>string</code></td>
    <td>Specifies the representation of the set of routes provided as response. This parameter value can only be used in conjunction with computeBestOrder=true. Known values are: "polyline", "summaryOnly", and "none". Default value is None.</td>
</tr>
<tr id="parameter-routeType">
    <td><CopyableCode code="routeType" /></td>
    <td><code>string</code></td>
    <td>The type of route requested. Known values are: "fastest", "shortest", "eco", and "thrilling". Default value is None.</td>
</tr>
<tr id="parameter-sectionType">
    <td><CopyableCode code="sectionType" /></td>
    <td><code>string</code></td>
    <td>Specifies which of the section types is reported in the route response. For example if sectionType = pedestrian the sections which are suited for pedestrians only are returned. Multiple types can be used. The default sectionType refers to the travelMode input. By default travelMode is set to car. Known values are: "carTrain", "country", "ferry", "motorway", "pedestrian", "tollRoad", "tollVignette", "traffic", "travelMode", "tunnel", "carpool", and "urban". Default value is None.</td>
</tr>
<tr id="parameter-timeBudgetInSec">
    <td><CopyableCode code="timeBudgetInSec" /></td>
    <td><code>number</code></td>
    <td>Time budget in seconds that determines maximal range which can be travelled using driving time. The Consumption Model will only affect the range when routeType is eco. Exactly one budget (fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, or distanceBudgetInMeters) must be used. Default value is None.</td>
</tr>
<tr id="parameter-traffic">
    <td><CopyableCode code="traffic" /></td>
    <td><code>boolean</code></td>
    <td>Possible values: * true - Do consider all available traffic information during routing * false - Ignore current traffic data during routing. Note that although the current traffic data is ignored during routing, the effect of historic traffic on effective road speeds is still incorporated. Default value is None.</td>
</tr>
<tr id="parameter-travelMode">
    <td><CopyableCode code="travelMode" /></td>
    <td><code>string</code></td>
    <td>The mode of travel for the requested route. If not defined, default is 'car'. Note that the requested travelMode may not be available for the entire route. Where the requested travelMode is not available for a particular section, the travelMode element of the response for that section will be "other". Note that travel modes bus, motorcycle, taxi and van are BETA functionality. Full restriction data is not available in all areas. In **calculateReachableRange** requests, the values bicycle and pedestrian must not be used. Known values are: "car", "truck", "taxi", "bus", "van", "motorcycle", "bicycle", and "pedestrian". Default value is None.</td>
</tr>
<tr id="parameter-uphillEfficiency">
    <td><CopyableCode code="uphillEfficiency" /></td>
    <td><code>number</code></td>
    <td>Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation *(i.e. PotentialEnergyGained/ChemicalEnergyConsumed). ChemicalEnergyConsumed* is obtained by converting consumed fuel to chemical energy using **fuelEnergyDensityInMJoulesPerLiter**. Must be paired with **downhillEfficiency**. The range of values allowed are 0.0 to 1/\ **downhillEfficiency**. Sensible Values : for **Combustion Model** : 0.27, for **Electric Model** : 0.74. Default value is None.</td>
</tr>
<tr id="parameter-vehicleAxleWeight">
    <td><CopyableCode code="vehicleAxleWeight" /></td>
    <td><code>integer</code></td>
    <td>Weight per axle of the vehicle in kg. A value of 0 means that weight restrictions per axle are not considered. Default value is 0.</td>
</tr>
<tr id="parameter-vehicleCommercial">
    <td><CopyableCode code="vehicleCommercial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the vehicle is used for commercial purposes. Commercial vehicles may not be allowed to drive on some roads. Default value is False.</td>
</tr>
<tr id="parameter-vehicleEngineType">
    <td><CopyableCode code="vehicleEngineType" /></td>
    <td><code>string</code></td>
    <td>Engine type of the vehicle. When a detailed Consumption Model is specified, it must be consistent with the value of **vehicleEngineType**. Known values are: "combustion" and "electric". Default value is None.</td>
</tr>
<tr id="parameter-vehicleHeading">
    <td><CopyableCode code="vehicleHeading" /></td>
    <td><code>integer</code></td>
    <td>The directional heading of the vehicle in degrees starting at true North and continuing in clockwise direction. North is 0 degrees, east is 90 degrees, south is 180 degrees, west is 270 degrees. Possible values 0-359. Default value is None.</td>
</tr>
<tr id="parameter-vehicleHeight">
    <td><CopyableCode code="vehicleHeight" /></td>
    <td><code>number</code></td>
    <td>Height of the vehicle in meters. A value of 0 means that height restrictions are not considered. Default value is 0.</td>
</tr>
<tr id="parameter-vehicleLength">
    <td><CopyableCode code="vehicleLength" /></td>
    <td><code>number</code></td>
    <td>Length of the vehicle in meters. A value of 0 means that length restrictions are not considered. Default value is 0.</td>
</tr>
<tr id="parameter-vehicleLoadType">
    <td><CopyableCode code="vehicleLoadType" /></td>
    <td><code>string</code></td>
    <td>Types of cargo that may be classified as hazardous materials and restricted from some roads. Available vehicleLoadType values are US Hazmat classes 1 through 9, plus generic classifications for use in other countries. Values beginning with USHazmat are for US routing while otherHazmat should be used for all other countries. vehicleLoadType can be specified multiple times. This parameter is currently only considered for travelMode=truck. Known values are: "USHazmatClass1", "USHazmatClass2", "USHazmatClass3", "USHazmatClass4", "USHazmatClass5", "USHazmatClass6", "USHazmatClass7", "USHazmatClass8", "USHazmatClass9", "otherHazmatExplosive", "otherHazmatGeneral", and "otherHazmatHarmfulToWater". Default value is None.</td>
</tr>
<tr id="parameter-vehicleMaxSpeed">
    <td><CopyableCode code="vehicleMaxSpeed" /></td>
    <td><code>integer</code></td>
    <td>Maximum speed of the vehicle in km/hour. The max speed in the vehicle profile is used to check whether a vehicle is allowed on motorways. * A value of 0 means that an appropriate value for the vehicle will be determined and applied during route planning. * A non-zero value may be overridden during route planning. For example, the current traffic flow is 60 km/hour. If the vehicle maximum speed is set to 50 km/hour, the routing engine will consider 60 km/hour as this is the current situation. If the maximum speed of the vehicle is provided as 80 km/hour but the current traffic flow is 60 km/hour, then routing engine will again use 60 km/hour. Default value is 0.</td>
</tr>
<tr id="parameter-vehicleWeight">
    <td><CopyableCode code="vehicleWeight" /></td>
    <td><code>integer</code></td>
    <td>Weight of the vehicle in kilograms. Default value is 0.</td>
</tr>
<tr id="parameter-vehicleWidth">
    <td><CopyableCode code="vehicleWidth" /></td>
    <td><code>number</code></td>
    <td>Width of the vehicle in meters. A value of 0 means that width restrictions are not considered. Default value is 0.</td>
</tr>
<tr id="parameter-waitForResults">
    <td><CopyableCode code="waitForResults" /></td>
    <td><code>boolean</code></td>
    <td>Boolean to indicate whether to execute the request synchronously. If set to true, user will get a 200 response if the request is finished under 120 seconds. Otherwise, user will get a 202 response right away. Please refer to the API description for more details on 202 response. **Supported only for async request**. Default value is None.</td>
</tr>
<tr id="parameter-windingness">
    <td><CopyableCode code="windingness" /></td>
    <td><code>string</code></td>
    <td>Level of turns for thrilling route. This parameter can only be used in conjunction with `routeType`\ =thrilling. Known values are: "low", "normal", and "high". Default value is None.</td>
</tr>
<tr id="parameter-x-ms-client-id">
    <td><CopyableCode code="x-ms-client-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_route_directions"
    values={[
        { label: 'get_route_directions', value: 'get_route_directions' },
        { label: 'get_route_matrix', value: 'get_route_matrix' }
    ]}
>
<TabItem value="get_route_directions">

**Applies to**\ : see pricing `tiers `_. Returns a route between an origin and a destination, passing through waypoints if they are specified. The route will take into account factors such as current traffic and the typical road speeds on the requested day of the week and time of day. Information returned includes the distance, estimated travel time, and a representation of the route geometry. Additional routing information such as optimized waypoint order or turn by turn instructions is also available, depending on the options selected. Routing service provides a set of parameters for a detailed description of vehicle-specific Consumption Model. Please check `Consumption Model `_ for detailed explanation of the concepts and parameters involved.

```sql
SELECT
formatVersion,
optimizedWaypoints,
report,
routes
FROM azure.maps_route.route
WHERE format = '{{ format }}' -- required
AND query = '{{ query }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND maxAlternatives = '{{ maxAlternatives }}'
AND alternativeType = '{{ alternativeType }}'
AND minDeviationDistance = '{{ minDeviationDistance }}'
AND arriveAt = '{{ arriveAt }}'
AND departAt = '{{ departAt }}'
AND minDeviationTime = '{{ minDeviationTime }}'
AND instructionsType = '{{ instructionsType }}'
AND language = '{{ language }}'
AND computeBestOrder = '{{ computeBestOrder }}'
AND routeRepresentation = '{{ routeRepresentation }}'
AND computeTravelTimeFor = '{{ computeTravelTimeFor }}'
AND vehicleHeading = '{{ vehicleHeading }}'
AND report = '{{ report }}'
AND sectionType = '{{ sectionType }}'
AND vehicleAxleWeight = '{{ vehicleAxleWeight }}'
AND vehicleWidth = '{{ vehicleWidth }}'
AND vehicleHeight = '{{ vehicleHeight }}'
AND vehicleLength = '{{ vehicleLength }}'
AND vehicleMaxSpeed = '{{ vehicleMaxSpeed }}'
AND vehicleWeight = '{{ vehicleWeight }}'
AND vehicleCommercial = '{{ vehicleCommercial }}'
AND windingness = '{{ windingness }}'
AND hilliness = '{{ hilliness }}'
AND travelMode = '{{ travelMode }}'
AND traffic = '{{ traffic }}'
AND routeType = '{{ routeType }}'
AND vehicleLoadType = '{{ vehicleLoadType }}'
AND vehicleEngineType = '{{ vehicleEngineType }}'
AND constantSpeedConsumptionInLitersPerHundredkm = '{{ constantSpeedConsumptionInLitersPerHundredkm }}'
AND currentFuelInLiters = '{{ currentFuelInLiters }}'
AND auxiliaryPowerInLitersPerHour = '{{ auxiliaryPowerInLitersPerHour }}'
AND fuelEnergyDensityInMJoulesPerLiter = '{{ fuelEnergyDensityInMJoulesPerLiter }}'
AND accelerationEfficiency = '{{ accelerationEfficiency }}'
AND decelerationEfficiency = '{{ decelerationEfficiency }}'
AND uphillEfficiency = '{{ uphillEfficiency }}'
AND downhillEfficiency = '{{ downhillEfficiency }}'
AND constantSpeedConsumptionInkWhPerHundredkm = '{{ constantSpeedConsumptionInkWhPerHundredkm }}'
AND currentChargeInkWh = '{{ currentChargeInkWh }}'
AND maxChargeInkWh = '{{ maxChargeInkWh }}'
AND auxiliaryPowerInkW = '{{ auxiliaryPowerInkW }}'
AND x-ms-client-id = '{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_route_matrix">

**Applies to**\ : see pricing `tiers `_. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.

```sql
SELECT
formatVersion,
matrix,
summary
FROM azure.maps_route.route
WHERE format = '{{ format }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND x-ms-client-id = '{{ x-ms-client-id }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="request_route_matrix"
    values={[
        { label: 'request_route_matrix', value: 'request_route_matrix' },
        { label: 'get_route_directions_with_additional_parameters', value: 'get_route_directions_with_additional_parameters' },
        { label: 'get_route_range', value: 'get_route_range' },
        { label: 'get_route_directions_batch', value: 'get_route_directions_batch' },
        { label: 'request_route_directions_batch', value: 'request_route_directions_batch' },
        { label: 'request_route_matrix_sync', value: 'request_route_matrix_sync' },
        { label: 'request_route_directions_batch_sync', value: 'request_route_directions_batch_sync' }
    ]}
>
<TabItem value="request_route_matrix">

**Applies to**\ : see pricing `tiers `_. The Matrix Routing service allows calculation of a matrix of route summaries for a set of routes defined by origin and destination locations by using an asynchronous (async) or synchronous (sync) POST request. For every given origin, the service calculates the cost of routing from that origin to every given destination. The set of origins and the set of destinations can be thought of as the column and row headers of a table and each cell in the table contains the costs of routing from the origin to the destination for that cell. As an example, let's say a food delivery company has 20 drivers and they need to find the closest driver to pick up the delivery from the restaurant. To solve this use case, they can call Matrix Route API. For each route, the travel times and distances are returned. You can use the computed costs to determine which detailed routes to calculate using the Route Directions API. The maximum size of a matrix for async request is **700** and for sync request it's **100** (the number of origins multiplied by the number of destinations). Submit Synchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ If your scenario requires synchronous requests and the maximum size of the matrix is less than or equal to 100, you might want to make synchronous request. The maximum size of a matrix for this API is **100** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 10x10, 6x8, 9x8 (it does not need to be square). .. code-block:: POST https://atlas.microsoft.com/route/matrix/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Submit Asynchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex routing requests. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. If `waitForResults` parameter in the request is set to true, user will get a 200 response if the request is finished under 120 seconds. The maximum size of a matrix for this API is **700** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 50x10, 10x10, 28x25. 10x70 (it does not need to be square). The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. .. code-block:: POST https://atlas.microsoft.com/route/matrix/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's a typical sequence of asynchronous operations: #. Client sends a Route Matrix POST request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Route Matrix request has been accepted. HTTP `Error` - There was an error processing your Route Matrix request. This could either be a 400 Bad Request or any other Error status code. #. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.

```sql
EXEC azure.maps_route.route.request_route_matrix 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@waitForResults={{ waitForResults }}, 
@computeTravelTimeFor='{{ computeTravelTimeFor }}', 
@sectionType='{{ sectionType }}', 
@arriveAt='{{ arriveAt }}', 
@departAt='{{ departAt }}', 
@vehicleAxleWeight='{{ vehicleAxleWeight }}', 
@vehicleLength='{{ vehicleLength }}', 
@vehicleHeight='{{ vehicleHeight }}', 
@vehicleWidth='{{ vehicleWidth }}', 
@vehicleMaxSpeed='{{ vehicleMaxSpeed }}', 
@vehicleWeight='{{ vehicleWeight }}', 
@windingness='{{ windingness }}', 
@hilliness='{{ hilliness }}', 
@travelMode='{{ travelMode }}', 
@traffic={{ traffic }}, 
@routeType='{{ routeType }}', 
@vehicleLoadType='{{ vehicleLoadType }}', 
@x-ms-client-id='{{ x-ms-client-id }}' 
@@json=
'{
"origins": "{{ origins }}", 
"destinations": "{{ destinations }}"
}'
;
```
</TabItem>
<TabItem value="get_route_directions_with_additional_parameters">

**Applies to**\ : see pricing `tiers `_. Returns a route between an origin and a destination, passing through waypoints if they are specified. The route will take into account factors such as current traffic and the typical road speeds on the requested day of the week and time of day. Information returned includes the distance, estimated travel time, and a representation of the route geometry. Additional routing information such as optimized waypoint order or turn by turn instructions is also available, depending on the options selected. Routing service provides a set of parameters for a detailed description of a vehicle-specific Consumption Model. Please check `Consumption Model `_ for detailed explanation of the concepts and parameters involved.

```sql
EXEC azure.maps_route.route.get_route_directions_with_additional_parameters 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@maxAlternatives='{{ maxAlternatives }}', 
@alternativeType='{{ alternativeType }}', 
@minDeviationDistance='{{ minDeviationDistance }}', 
@minDeviationTime='{{ minDeviationTime }}', 
@instructionsType='{{ instructionsType }}', 
@language='{{ language }}', 
@computeBestOrder={{ computeBestOrder }}, 
@routeRepresentation='{{ routeRepresentation }}', 
@computeTravelTimeFor='{{ computeTravelTimeFor }}', 
@vehicleHeading='{{ vehicleHeading }}', 
@report='{{ report }}', 
@sectionType='{{ sectionType }}', 
@arriveAt='{{ arriveAt }}', 
@departAt='{{ departAt }}', 
@vehicleAxleWeight='{{ vehicleAxleWeight }}', 
@vehicleLength='{{ vehicleLength }}', 
@vehicleHeight='{{ vehicleHeight }}', 
@vehicleWidth='{{ vehicleWidth }}', 
@vehicleMaxSpeed='{{ vehicleMaxSpeed }}', 
@vehicleWeight='{{ vehicleWeight }}', 
@vehicleCommercial={{ vehicleCommercial }}, 
@windingness='{{ windingness }}', 
@hilliness='{{ hilliness }}', 
@travelMode='{{ travelMode }}', 
@traffic={{ traffic }}, 
@routeType='{{ routeType }}', 
@vehicleLoadType='{{ vehicleLoadType }}', 
@vehicleEngineType='{{ vehicleEngineType }}', 
@constantSpeedConsumptionInLitersPerHundredkm='{{ constantSpeedConsumptionInLitersPerHundredkm }}', 
@currentFuelInLiters='{{ currentFuelInLiters }}', 
@auxiliaryPowerInLitersPerHour='{{ auxiliaryPowerInLitersPerHour }}', 
@fuelEnergyDensityInMJoulesPerLiter='{{ fuelEnergyDensityInMJoulesPerLiter }}', 
@accelerationEfficiency='{{ accelerationEfficiency }}', 
@decelerationEfficiency='{{ decelerationEfficiency }}', 
@uphillEfficiency='{{ uphillEfficiency }}', 
@downhillEfficiency='{{ downhillEfficiency }}', 
@constantSpeedConsumptionInkWhPerHundredkm='{{ constantSpeedConsumptionInkWhPerHundredkm }}', 
@currentChargeInkWh='{{ currentChargeInkWh }}', 
@maxChargeInkWh='{{ maxChargeInkWh }}', 
@auxiliaryPowerInkW='{{ auxiliaryPowerInkW }}', 
@x-ms-client-id='{{ x-ms-client-id }}' 
@@json=
'{
"supportingPoints": "{{ supportingPoints }}", 
"avoidVignette": "{{ avoidVignette }}", 
"allowVignette": "{{ allowVignette }}", 
"avoidAreas": "{{ avoidAreas }}"
}'
;
```
</TabItem>
<TabItem value="get_route_range">

**Route Range (Isochrone) API** **Applies to**\ : see pricing `tiers `_. This service will calculate a set of locations that can be reached from the origin point based on fuel, energy, time or distance budget that is specified. A polygon boundary (or Isochrone) is returned in a counterclockwise orientation as well as the precise polygon center which was the result of the origin point. The returned polygon can be used for further processing such as `Search Inside Geometry `_ to search for POIs within the provided Isochrone.

```sql
EXEC azure.maps_route.route.get_route_range 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@fuelBudgetInLiters='{{ fuelBudgetInLiters }}', 
@energyBudgetInkWh='{{ energyBudgetInkWh }}', 
@timeBudgetInSec='{{ timeBudgetInSec }}', 
@distanceBudgetInMeters='{{ distanceBudgetInMeters }}', 
@departAt='{{ departAt }}', 
@routeType='{{ routeType }}', 
@traffic={{ traffic }}, 
@travelMode='{{ travelMode }}', 
@hilliness='{{ hilliness }}', 
@windingness='{{ windingness }}', 
@vehicleAxleWeight='{{ vehicleAxleWeight }}', 
@vehicleWidth='{{ vehicleWidth }}', 
@vehicleHeight='{{ vehicleHeight }}', 
@vehicleLength='{{ vehicleLength }}', 
@vehicleMaxSpeed='{{ vehicleMaxSpeed }}', 
@vehicleWeight='{{ vehicleWeight }}', 
@vehicleCommercial={{ vehicleCommercial }}, 
@vehicleLoadType='{{ vehicleLoadType }}', 
@vehicleEngineType='{{ vehicleEngineType }}', 
@constantSpeedConsumptionInLitersPerHundredkm='{{ constantSpeedConsumptionInLitersPerHundredkm }}', 
@currentFuelInLiters='{{ currentFuelInLiters }}', 
@auxiliaryPowerInLitersPerHour='{{ auxiliaryPowerInLitersPerHour }}', 
@fuelEnergyDensityInMJoulesPerLiter='{{ fuelEnergyDensityInMJoulesPerLiter }}', 
@accelerationEfficiency='{{ accelerationEfficiency }}', 
@decelerationEfficiency='{{ decelerationEfficiency }}', 
@uphillEfficiency='{{ uphillEfficiency }}', 
@downhillEfficiency='{{ downhillEfficiency }}', 
@constantSpeedConsumptionInkWhPerHundredkm='{{ constantSpeedConsumptionInkWhPerHundredkm }}', 
@currentChargeInkWh='{{ currentChargeInkWh }}', 
@maxChargeInkWh='{{ maxChargeInkWh }}', 
@auxiliaryPowerInkW='{{ auxiliaryPowerInkW }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_route_directions_batch">

**Applies to**\ : see pricing `tiers `_. Download Asynchronous Batch Results ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ To download the async batch results you will issue a `GET` request to the batch download endpoint. This *download URL* can be obtained from the `Location` header of a successful `POST` batch request and looks like the following: .. code-block:: https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's the typical sequence of operations for downloading the batch results: #. Client sends a `GET` request using the *download URL*. #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Batch request successfully processed. The response body contains all the batch results. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;

```sql
EXEC azure.maps_route.route.get_route_directions_batch 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="request_route_directions_batch">

**Route Directions Batch API** **Applies to**\ : see pricing `tiers `_. The Route Directions Batch API sends batches of queries to `Route Directions API `_ using just a single API call. You can call Route Directions Batch API to run either asynchronously (async) or synchronously (sync). The async API allows caller to batch up to **700** queries and sync API up to **100** queries. Submit Asynchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex route requests * It allows the retrieval of results in a separate call (multiple downloads are possible). * The asynchronous API is optimized for reliability and is not expected to run into a timeout. * The number of batch items is limited to **700** for this API. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. Please note that asynchronous batch request is a long-running request. Here's a typical sequence of operations: #. Client sends a Route Directions Batch `POST` request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request has been accepted. HTTP `Error` - There was an error processing your Batch request. This could either be a `400 Bad Request` or any other `Error` status code. #. If the batch request was accepted successfully, the `Location` header in the response contains the URL to download the results of the batch request. This status URI looks like following: `GET https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0` Note:- Please remember to add AUTH information (subscription-key/azure_auth - See `Security <#security>`_\ ) to the *status URI* before running it. #. Client issues a `GET` request on the *download URL* obtained in Step 3 to download the batch results. POST Body for Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^ To send the *route directions* queries you will use a `POST` request where the request body will contain the `batchItems` array in `json` format and the `Content-Type` header will be set to `application/json`. Here's a sample request body containing 3 *route directions* queries: .. code-block:: json &#123; "batchItems": [ &#123; "query": "?query=47.620659,-122.348934:47.610101,-122.342015&travelMode=bicycle&routeType=eco&traffic=false" &#125;, &#123; "query": "?query=40.759856,-73.985108:40.771136,-73.973506&travelMode=pedestrian&routeType=shortest" &#125;, &#123; "query": "?query=48.923159,-122.557362:32.621279,-116.840362" &#125; ] &#125; A *route directions* query in a batch is just a partial URL *without* the protocol, base URL, path, api-version and subscription-key. It can accept any of the supported *route directions* `URI parameters `_. The string values in the *route directions* query must be properly escaped (e.g. " character should be escaped with ) and it should also be properly URL-encoded. The async API allows caller to batch up to **700** queries and sync API up to **100** queries, and the batch should contain at least **1** query. Download Asynchronous Batch Results ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ To download the async batch results you will issue a `GET` request to the batch download endpoint. This *download URL* can be obtained from the `Location` header of a successful `POST` batch request and looks like the following: .. code-block:: https://atlas.microsoft.com/route/directions/batch/&#123;batch-id&#125;?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's the typical sequence of operations for downloading the batch results: #. Client sends a `GET` request using the *download URL*. #. The server will respond with one of the following: .. HTTP `202 Accepted` - Batch request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Batch request successfully processed. The response body contains all the batch results. Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;

```sql
EXEC azure.maps_route.route.request_route_directions_batch 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}' 
@@json=
'{
"batchItems": "{{ batchItems }}"
}'
;
```
</TabItem>
<TabItem value="request_route_matrix_sync">

**Applies to**\ : see pricing `tiers `_. The Matrix Routing service allows calculation of a matrix of route summaries for a set of routes defined by origin and destination locations by using an asynchronous (async) or synchronous (sync) POST request. For every given origin, the service calculates the cost of routing from that origin to every given destination. The set of origins and the set of destinations can be thought of as the column and row headers of a table and each cell in the table contains the costs of routing from the origin to the destination for that cell. As an example, let's say a food delivery company has 20 drivers and they need to find the closest driver to pick up the delivery from the restaurant. To solve this use case, they can call Matrix Route API. For each route, the travel times and distances are returned. You can use the computed costs to determine which detailed routes to calculate using the Route Directions API. The maximum size of a matrix for async request is **700** and for sync request it's **100** (the number of origins multiplied by the number of destinations). Submit Synchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ If your scenario requires synchronous requests and the maximum size of the matrix is less than or equal to 100, you might want to make synchronous request. The maximum size of a matrix for this API is **100** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 10x10, 6x8, 9x8 (it does not need to be square). .. code-block:: POST https://atlas.microsoft.com/route/matrix/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Submit Asynchronous Route Matrix Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Asynchronous API is appropriate for processing big volumes of relatively complex routing requests. When you make a request by using async request, by default the service returns a 202 response code along a redirect URL in the Location field of the response header. This URL should be checked periodically until the response data or error information is available. If `waitForResults` parameter in the request is set to true, user will get a 200 response if the request is finished under 120 seconds. The maximum size of a matrix for this API is **700** (the number of origins multiplied by the number of destinations). With that constraint in mind, examples of possible matrix dimensions are: 50x10, 10x10, 28x25. 10x70 (it does not need to be square). The asynchronous responses are stored for **14** days. The redirect URL returns a 404 response if used after the expiration period. .. code-block:: POST https://atlas.microsoft.com/route/matrix/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Here's a typical sequence of asynchronous operations: #. Client sends a Route Matrix POST request to Azure Maps #. The server will respond with one of the following: .. HTTP `202 Accepted` - Route Matrix request has been accepted. HTTP `Error` - There was an error processing your Route Matrix request. This could either be a 400 Bad Request or any other Error status code. #. If the Matrix Route request was accepted successfully, the Location header in the response contains the URL to download the results of the request. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; #. Client issues a GET request on the download URL obtained in Step 3 to download the results Download Sync Results ^^^^^^^^^^^^^^^^^^^^^ When you make a POST request for Route Matrix Sync API, the service returns 200 response code for successful request and a response array. The response body will contain the data and there will be no possibility to retrieve the results later. Download Async Results ^^^^^^^^^^^^^^^^^^^^^^ When a request issues a `202 Accepted` response, the request is being processed using our async pipeline. You will be given a URL to check the progress of your async request in the location header of the response. This status URI looks like the following: .. code-block:: GET https://atlas.microsoft.com/route/matrix/&#123;matrixId&#125;?api-version=1.0?subscription-key=&#123;subscription-key&#125; The URL provided by the location header will return the following responses when a `GET` request is issued. .. HTTP `202 Accepted` - Matrix request was accepted but is still being processed. Please try again in some time. HTTP `200 OK` - Matrix request successfully processed. The response body contains all of the results.

```sql
EXEC azure.maps_route.route.request_route_matrix_sync 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@waitForResults={{ waitForResults }}, 
@computeTravelTimeFor='{{ computeTravelTimeFor }}', 
@sectionType='{{ sectionType }}', 
@arriveAt='{{ arriveAt }}', 
@departAt='{{ departAt }}', 
@vehicleAxleWeight='{{ vehicleAxleWeight }}', 
@vehicleLength='{{ vehicleLength }}', 
@vehicleHeight='{{ vehicleHeight }}', 
@vehicleWidth='{{ vehicleWidth }}', 
@vehicleMaxSpeed='{{ vehicleMaxSpeed }}', 
@vehicleWeight='{{ vehicleWeight }}', 
@windingness='{{ windingness }}', 
@hilliness='{{ hilliness }}', 
@travelMode='{{ travelMode }}', 
@traffic={{ traffic }}, 
@routeType='{{ routeType }}', 
@vehicleLoadType='{{ vehicleLoadType }}', 
@x-ms-client-id='{{ x-ms-client-id }}' 
@@json=
'{
"origins": "{{ origins }}", 
"destinations": "{{ destinations }}"
}'
;
```
</TabItem>
<TabItem value="request_route_directions_batch_sync">

**Route Directions Batch API** **Applies to**\ : see pricing `tiers `_. The Route Directions Batch API sends batches of queries to `Route Directions API `_ using just a single API call. You can call Route Directions Batch API to run either asynchronously (async) or synchronously (sync). The async API allows caller to batch up to **700** queries and sync API up to **100** queries. Submit Synchronous Batch Request ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ The Synchronous API is recommended for lightweight batch requests. When the service receives a request, it will respond as soon as the batch items are calculated and there will be no possibility to retrieve the results later. The Synchronous API will return a timeout error (a 408 response) if the request takes longer than 60 seconds. The number of batch items is limited to **100** for this API. .. code-block:: POST https://atlas.microsoft.com/route/directions/batch/sync/json?api-version=1.0&subscription-key=&#123;subscription-key&#125; Batch Response Model ^^^^^^^^^^^^^^^^^^^^ The returned data content is similar for async and sync requests. When downloading the results of an async batch request, if the batch has finished processing, the response body contains the batch response. This batch response contains a `summary` component that indicates the `totalRequests` that were part of the original batch request and `successfulRequests`\ i.e. queries which were executed successfully. The batch response also includes a `batchItems` array which contains a response for each and every query in the batch request. The `batchItems` will contain the results in the exact same order the original queries were sent in the batch request. Each item in `batchItems` contains `statusCode` and `response` fields. Each `response` in `batchItems` is of one of the following types: * `\ `RouteDirections` `_ - If the query completed successfully. * `Error` - If the query failed. The response will contain a `code` and a `message` in this case. Here's a sample Batch Response with 1 *successful* and 1 *failed* result: .. code-block:: json &#123; "summary": &#123; "successfulRequests": 1, "totalRequests": 2 &#125;, "batchItems": [ &#123; "statusCode": 200, "response": &#123; "routes": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "legs": [ &#123; "summary": &#123; "lengthInMeters": 1758, "travelTimeInSeconds": 387, "trafficDelayInSeconds": 0, "departureTime": "2018-07-17T00:49:56+00:00", "arrivalTime": "2018-07-17T00:56:22+00:00" &#125;, "points": [ &#123; "latitude": 47.62094, "longitude": -122.34892 &#125;, &#123; "latitude": 47.62094, "longitude": -122.3485 &#125;, &#123; "latitude": 47.62095, "longitude": -122.3476 &#125; ] &#125; ], "sections": [ &#123; "startPointIndex": 0, "endPointIndex": 40, "sectionType": "TRAVEL_MODE", "travelMode": "bicycle" &#125; ] &#125; ] &#125; &#125;, &#123; "statusCode": 400, "response": &#123; "error": &#123; "code": "400 BadRequest", "message": "Bad request: one or more parameters were incorrectly specified or are mutually exclusive." &#125; &#125; &#125; ] &#125;

```sql
EXEC azure.maps_route.route.request_route_directions_batch_sync 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}' 
@@json=
'{
"batchItems": "{{ batchItems }}"
}'
;
```
</TabItem>
</Tabs>
