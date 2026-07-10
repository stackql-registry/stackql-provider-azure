--- 
title: phone_numbers
hide_title: false
hide_table_of_contents: false
keywords:
  - phone_numbers
  - communication_phonenumbers
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

Creates, updates, deletes, gets or lists a <code>phone_numbers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="phone_numbers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication_phonenumbers.phone_numbers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="search_available_phone_numbers"
    values={[
        { label: 'search_available_phone_numbers', value: 'search_available_phone_numbers' },
        { label: 'list_area_codes', value: 'list_area_codes' },
        { label: 'list_available_localities', value: 'list_available_localities' },
        { label: 'get_by_number', value: 'get_by_number' },
        { label: 'get_reservation', value: 'get_reservation' },
        { label: 'get_search_result', value: 'get_search_result' },
        { label: 'get_operation', value: 'get_operation' },
        { label: 'list_available_countries', value: 'list_available_countries' }
    ]}
>
<TabItem value="search_available_phone_numbers">

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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>Phone number's assignment type. Required. Known values are: "person" and "application".</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>Capabilities of a phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cost" /></td>
    <td><code>object</code></td>
    <td>The incurred cost for a single phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Mapping Error Messages to Codes. Known values are: "NoError", "UnknownErrorCode", "OutOfStock", "AuthorizationDenied", "MissingAddress", "InvalidAddress", "InvalidOfferModel", "NotEnoughLicenses", "NoWallet", "NotEnoughCredit", "NumbersPartiallyAcquired", "AllNumbersNotAcquired", "ReservationExpired", "PurchaseFailed", "BillingUnavailable", "ProvisioningFailed", and "UnknownSearchError".</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>integer</code></td>
    <td>The error code of the search.</td>
</tr>
<tr>
    <td><CopyableCode code="isAgreementToNotResellRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if do not resell agreement is required. If true, the phone numbers cannot be acquired unless the customer provides explicit agreement to not resell them.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumberType" /></td>
    <td><code>string</code></td>
    <td>The phone number's type, e.g. geographic, tollFree, mobile. Required. Known values are: "geographic", "tollFree", and "mobile".</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumbers" /></td>
    <td><code>array</code></td>
    <td>The phone numbers that are available. Can be fewer than the desired search quantity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="searchExpiresBy" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date that this search result expires and phone numbers are no longer on hold. A search result expires in less than 15min, e.g. 2020-11-19T16:31:49.048Z. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="searchId" /></td>
    <td><code>string</code></td>
    <td>The search id. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_area_codes">

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
    <td><CopyableCode code="areaCode" /></td>
    <td><code>string</code></td>
    <td>An area code.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_available_localities">

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
    <td><CopyableCode code="administrativeDivision" /></td>
    <td><code>object</code></td>
    <td>Represents an administrative division. e.g. state or province.</td>
</tr>
<tr>
    <td><CopyableCode code="localizedName" /></td>
    <td><code>string</code></td>
    <td>Represents the localized name of the locality. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_number">

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
    <td>The id of the phone number, e.g. 11234567890. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The assignment type of the phone number. A phone number can be assigned to a person, or to an application. Required. Known values are: "person" and "application".</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>Capabilities of a phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cost" /></td>
    <td><code>object</code></td>
    <td>The incurred cost for a single phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="countryCode" /></td>
    <td><code>string</code></td>
    <td>The ISO 3166-2 code of the phone number's country, e.g. US. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumber" /></td>
    <td><code>string</code></td>
    <td>String of the E.164 format of the phone number, e.g. +11234567890. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumberType" /></td>
    <td><code>string</code></td>
    <td>The phone number's type, e.g. geographic, tollFree, mobile. Required. Known values are: "geographic", "tollFree", and "mobile".</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the phone number was purchased. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_reservation">

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
    <td>The id of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="expiresAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the reservation will expire. If a reservation is not purchased before this time, all of the reserved phone numbers will be released and made available for others to purchase.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumbers" /></td>
    <td><code>object</code></td>
    <td>A dictionary containing the reservation phone numbers. The key is the ID of the phone number (digits only) and values are AvailablePhoneNumber objects. Not populated when retrieving PhoneNumbersReservation collections.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Represents the status of the reservation. Possible values include: 'active', 'submitted', 'completed', 'expired'. Known values are: "active", "submitted", "completed", and "expired".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_search_result">

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
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>Phone number's assignment type. Required. Known values are: "person" and "application".</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>object</code></td>
    <td>Capabilities of a phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="cost" /></td>
    <td><code>object</code></td>
    <td>The incurred cost for a single phone number. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Mapping Error Messages to Codes. Known values are: "NoError", "UnknownErrorCode", "OutOfStock", "AuthorizationDenied", "MissingAddress", "InvalidAddress", "InvalidOfferModel", "NotEnoughLicenses", "NoWallet", "NotEnoughCredit", "NumbersPartiallyAcquired", "AllNumbersNotAcquired", "ReservationExpired", "PurchaseFailed", "BillingUnavailable", "ProvisioningFailed", and "UnknownSearchError".</td>
</tr>
<tr>
    <td><CopyableCode code="errorCode" /></td>
    <td><code>integer</code></td>
    <td>The error code of the search.</td>
</tr>
<tr>
    <td><CopyableCode code="isAgreementToNotResellRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if do not resell agreement is required. If true, the phone numbers cannot be acquired unless the customer provides explicit agreement to not resell them.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumberType" /></td>
    <td><code>string</code></td>
    <td>The phone number's type, e.g. geographic, tollFree, mobile. Required. Known values are: "geographic", "tollFree", and "mobile".</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumbers" /></td>
    <td><code>array</code></td>
    <td>The phone numbers that are available. Can be fewer than the desired search quantity. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="searchExpiresBy" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date that this search result expires and phone numbers are no longer on hold. A search result expires in less than 15min, e.g. 2020-11-19T16:31:49.048Z. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="searchId" /></td>
    <td><code>string</code></td>
    <td>The search id. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_operation">

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
    <td>Id of operation. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date that the operation was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The Communication Services error.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActionDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The most recent date that the operation was changed.</td>
</tr>
<tr>
    <td><CopyableCode code="operationType" /></td>
    <td><code>string</code></td>
    <td>The type of operation, e.g. Search. Required. Known values are: "purchase", "releasePhoneNumber", "search", "updatePhoneNumberCapabilities", and "reservationPurchase".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLocation" /></td>
    <td><code>string</code></td>
    <td>URL for retrieving the result of the operation, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of operation. Required. Known values are: "notStarted", "running", "succeeded", and "failed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_available_countries">

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
    <td><CopyableCode code="countryCode" /></td>
    <td><code>string</code></td>
    <td>Represents the abbreviated name of the country. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="localizedName" /></td>
    <td><code>string</code></td>
    <td>Represents the name of the country. Required.</td>
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
    <td><a href="#search_available_phone_numbers"><CopyableCode code="search_available_phone_numbers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-country_code"><code>country_code</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Search for available phone numbers to purchase. Search for available phone numbers to purchase.</td>
</tr>
<tr>
    <td><a href="#list_area_codes"><CopyableCode code="list_area_codes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-country_code"><code>country_code</code></a>, <a href="#parameter-phoneNumberType"><code>phoneNumberType</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a>, <a href="#parameter-assignmentType"><code>assignmentType</code></a>, <a href="#parameter-locality"><code>locality</code></a>, <a href="#parameter-administrativeDivision"><code>administrativeDivision</code></a>, <a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets the list of available area codes. Gets the list of available area codes.</td>
</tr>
<tr>
    <td><a href="#list_available_localities"><CopyableCode code="list_available_localities" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-country_code"><code>country_code</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a>, <a href="#parameter-administrativeDivision"><code>administrativeDivision</code></a>, <a href="#parameter-accept-language"><code>accept-language</code></a>, <a href="#parameter-phoneNumberType"><code>phoneNumberType</code></a></td>
    <td>Gets the list of cities or towns with available phone numbers. Gets the list of cities or towns with available phone numbers.</td>
</tr>
<tr>
    <td><a href="#get_by_number"><CopyableCode code="get_by_number" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-phone_number"><code>phone_number</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the details of the given purchased phone number. Gets the details of the given purchased phone number.</td>
</tr>
<tr>
    <td><a href="#get_reservation"><CopyableCode code="get_reservation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a reservation by its ID. Retrieves the reservation with the given ID, including all of the phone numbers associated with it.</td>
</tr>
<tr>
    <td><a href="#get_search_result"><CopyableCode code="get_search_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-search_id"><code>search_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a phone number search result by search id. Gets a phone number search result by search id.</td>
</tr>
<tr>
    <td><a href="#get_operation"><CopyableCode code="get_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets an operation by its id. Gets an operation by its id.</td>
</tr>
<tr>
    <td><a href="#list_available_countries"><CopyableCode code="list_available_countries" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a>, <a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>Gets the list of supported countries. Gets the list of supported countries.</td>
</tr>
<tr>
    <td><a href="#release_phone_number"><CopyableCode code="release_phone_number" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-phone_number"><code>phone_number</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Releases a purchased phone number. Releases a purchased phone number.</td>
</tr>
<tr>
    <td><a href="#cancel_operation"><CopyableCode code="cancel_operation" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Cancels an operation by its id. Cancels an operation by its id.</td>
</tr>
<tr>
    <td><a href="#list_offerings"><CopyableCode code="list_offerings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-country_code"><code>country_code</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-maxPageSize"><code>maxPageSize</code></a>, <a href="#parameter-phoneNumberType"><code>phoneNumberType</code></a>, <a href="#parameter-assignmentType"><code>assignmentType</code></a>, <a href="#parameter-accept-language"><code>accept-language</code></a></td>
    <td>List available offerings of capabilities with rates for the given country. List available offerings of capabilities with rates for the given country.</td>
</tr>
<tr>
    <td><a href="#list_reservations"><CopyableCode code="list_reservations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-maxPageSize"><code>maxPageSize</code></a></td>
    <td>Lists all reservations. Retrieves a paginated list of all phone number reservations. Note that the reservations will not be populated with the phone numbers associated with them.</td>
</tr>
<tr>
    <td><a href="#list_phone_numbers"><CopyableCode code="list_phone_numbers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td>Gets the list of all purchased phone numbers. Gets the list of all purchased phone numbers.</td>
</tr>
<tr>
    <td><a href="#create_or_update_reservation"><CopyableCode code="create_or_update_reservation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Creates or updates a reservation by its ID. Adds and removes phone numbers from the reservation with the given ID. The response will be the updated state of the reservation. Phone numbers can be reserved by including them in the payload. If a number is already in the reservation, it will be ignored. To remove a phone number, set it explicitly to null in the request payload. This operation is idempotent. If a reservation with the same ID already exists, it will be updated, otherwise a new one is created. Only reservations with 'active' status can be updated. Updating a reservation will extend the expiration time of the reservation to 15 minutes after the last change, up to a maximum of 2 hours from creation time. Partial success is possible, in which case the response will have a 207 status code.</td>
</tr>
<tr>
    <td><a href="#delete_reservation"><CopyableCode code="delete_reservation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a reservation by its ID. Deletes the reservation with the given ID. Any phone number in the reservation will be released and made available for others to purchase. Only reservations with 'active' status can be deleted.</td>
</tr>
<tr>
    <td><a href="#browse_available_numbers"><CopyableCode code="browse_available_numbers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-country_code"><code>country_code</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-phoneNumberType"><code>phoneNumberType</code></a></td>
    <td></td>
    <td>Browses for available phone numbers to purchase. Browses for available phone numbers to purchase. The response will be a randomized list of phone numbers available to purchase matching the browsing criteria. This operation is not paginated. Since the results are randomized, repeating the same request will not guarantee the same results.</td>
</tr>
<tr>
    <td><a href="#purchase_reservation"><CopyableCode code="purchase_reservation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_id"><code>reservation_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Starts the purchase of all phone numbers in the reservation. Starts a long running operation to purchase all of the phone numbers in the reservation. Purchase can only be started for active reservations that at least one phone number. If any of the phone numbers in the reservation is from a country where reselling is not permitted, do not resell agreement is required. The response will include an 'Operation-Location' header that can be used to query the status of the operation.</td>
</tr>
<tr>
    <td><a href="#purchase_phone_numbers"><CopyableCode code="purchase_phone_numbers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Purchases phone numbers. Purchases phone numbers.</td>
</tr>
<tr>
    <td><a href="#update_capabilities"><CopyableCode code="update_capabilities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-phone_number"><code>phone_number</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Updates the capabilities of a phone number. Updates the capabilities of a phone number.</td>
</tr>
<tr>
    <td><a href="#operator_information_search"><CopyableCode code="operator_information_search" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-phoneNumbers"><code>phoneNumbers</code></a></td>
    <td></td>
    <td>Searches for number format and operator information for a given list of phone numbers. Searches for number format and operator information for a given list of phone numbers.</td>
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
<tr id="parameter-country_code">
    <td><CopyableCode code="country_code" /></td>
    <td><code>string</code></td>
    <td>The ISO 3166-2 country code, e.g. US. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The id of the operation. Required.</td>
</tr>
<tr id="parameter-phoneNumberType">
    <td><CopyableCode code="phoneNumberType" /></td>
    <td><code>string</code></td>
    <td>Filter by numberType, e.g. Geographic, TollFree, Mobile. Known values are: "geographic", "tollFree", and "mobile". Required.</td>
</tr>
<tr id="parameter-phone_number">
    <td><CopyableCode code="phone_number" /></td>
    <td><code>string</code></td>
    <td>The phone number id in E.164 format. The leading plus can be either + or encoded as %2B, e.g. +11234567890. Required.</td>
</tr>
<tr id="parameter-reservation_id">
    <td><CopyableCode code="reservation_id" /></td>
    <td><code>string</code></td>
    <td>The id of the reservation. Required.</td>
</tr>
<tr id="parameter-search_id">
    <td><CopyableCode code="search_id" /></td>
    <td><code>string</code></td>
    <td>The search Id. Required.</td>
</tr>
<tr id="parameter-accept-language">
    <td><CopyableCode code="accept-language" /></td>
    <td><code>string</code></td>
    <td>The locale to display in the localized fields in the response. e.g. 'en-US'. Default value is None.</td>
</tr>
<tr id="parameter-administrativeDivision">
    <td><CopyableCode code="administrativeDivision" /></td>
    <td><code>string</code></td>
    <td>An optional parameter for the name of the state or province in which to search for the area code. Default value is None.</td>
</tr>
<tr id="parameter-assignmentType">
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>Filter by assignmentType, e.g. Person, Application. Known values are: "person" and "application". Default value is None.</td>
</tr>
<tr id="parameter-locality">
    <td><CopyableCode code="locality" /></td>
    <td><code>string</code></td>
    <td>The name of locality or town in which to search for the area code. This is required if the number type is Geographic. Default value is None.</td>
</tr>
<tr id="parameter-maxPageSize">
    <td><CopyableCode code="maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>An optional parameter for how many entries to return, for pagination purposes. The default value is 100. Default value is 100.</td>
</tr>
<tr id="parameter-phoneNumberType">
    <td><CopyableCode code="phoneNumberType" /></td>
    <td><code>string</code></td>
    <td>Filter by numberType, e.g. Geographic, TollFree, Mobile. Known values are: "geographic", "tollFree", and "mobile". Default value is None.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>An optional parameter for how many entries to skip, for pagination purposes. The default value is 0. Default value is 0.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>An optional parameter for how many entries to return, for pagination purposes. The default value is 100. Default value is 100.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="search_available_phone_numbers"
    values={[
        { label: 'search_available_phone_numbers', value: 'search_available_phone_numbers' },
        { label: 'list_area_codes', value: 'list_area_codes' },
        { label: 'list_available_localities', value: 'list_available_localities' },
        { label: 'get_by_number', value: 'get_by_number' },
        { label: 'get_reservation', value: 'get_reservation' },
        { label: 'get_search_result', value: 'get_search_result' },
        { label: 'get_operation', value: 'get_operation' },
        { label: 'list_available_countries', value: 'list_available_countries' }
    ]}
>
<TabItem value="search_available_phone_numbers">

Search for available phone numbers to purchase. Search for available phone numbers to purchase.

```sql
SELECT
assignmentType,
capabilities,
cost,
error,
errorCode,
isAgreementToNotResellRequired,
phoneNumberType,
phoneNumbers,
searchExpiresBy,
searchId
FROM azure.communication_phonenumbers.phone_numbers
WHERE country_code = '{{ country_code }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_area_codes">

Gets the list of available area codes. Gets the list of available area codes.

```sql
SELECT
areaCode
FROM azure.communication_phonenumbers.phone_numbers
WHERE country_code = '{{ country_code }}' -- required
AND phoneNumberType = '{{ phoneNumberType }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND skip = '{{ skip }}'
AND maxPageSize = '{{ maxPageSize }}'
AND assignmentType = '{{ assignmentType }}'
AND locality = '{{ locality }}'
AND administrativeDivision = '{{ administrativeDivision }}'
AND accept-language = '{{ accept-language }}'
;
```
</TabItem>
<TabItem value="list_available_localities">

Gets the list of cities or towns with available phone numbers. Gets the list of cities or towns with available phone numbers.

```sql
SELECT
administrativeDivision,
localizedName
FROM azure.communication_phonenumbers.phone_numbers
WHERE country_code = '{{ country_code }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND skip = '{{ skip }}'
AND maxPageSize = '{{ maxPageSize }}'
AND administrativeDivision = '{{ administrativeDivision }}'
AND accept-language = '{{ accept-language }}'
AND phoneNumberType = '{{ phoneNumberType }}'
;
```
</TabItem>
<TabItem value="get_by_number">

Gets the details of the given purchased phone number. Gets the details of the given purchased phone number.

```sql
SELECT
id,
assignmentType,
capabilities,
cost,
countryCode,
phoneNumber,
phoneNumberType,
purchaseDate
FROM azure.communication_phonenumbers.phone_numbers
WHERE phone_number = '{{ phone_number }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_reservation">

Gets a reservation by its ID. Retrieves the reservation with the given ID, including all of the phone numbers associated with it.

```sql
SELECT
id,
expiresAt,
phoneNumbers,
status
FROM azure.communication_phonenumbers.phone_numbers
WHERE reservation_id = '{{ reservation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_search_result">

Gets a phone number search result by search id. Gets a phone number search result by search id.

```sql
SELECT
assignmentType,
capabilities,
cost,
error,
errorCode,
isAgreementToNotResellRequired,
phoneNumberType,
phoneNumbers,
searchExpiresBy,
searchId
FROM azure.communication_phonenumbers.phone_numbers
WHERE search_id = '{{ search_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="get_operation">

Gets an operation by its id. Gets an operation by its id.

```sql
SELECT
id,
createdDateTime,
error,
lastActionDateTime,
operationType,
resourceLocation,
status
FROM azure.communication_phonenumbers.phone_numbers
WHERE operation_id = '{{ operation_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_available_countries">

Gets the list of supported countries. Gets the list of supported countries.

```sql
SELECT
countryCode,
localizedName
FROM azure.communication_phonenumbers.phone_numbers
WHERE endpoint = '{{ endpoint }}' -- required
AND skip = '{{ skip }}'
AND maxPageSize = '{{ maxPageSize }}'
AND accept-language = '{{ accept-language }}'
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="release_phone_number"
    values={[
        { label: 'release_phone_number', value: 'release_phone_number' },
        { label: 'cancel_operation', value: 'cancel_operation' }
    ]}
>
<TabItem value="release_phone_number">

Releases a purchased phone number. Releases a purchased phone number.

```sql
DELETE FROM azure.communication_phonenumbers.phone_numbers
WHERE phone_number = '{{ phone_number }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="cancel_operation">

Cancels an operation by its id. Cancels an operation by its id.

```sql
DELETE FROM azure.communication_phonenumbers.phone_numbers
WHERE operation_id = '{{ operation_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_offerings"
    values={[
        { label: 'list_offerings', value: 'list_offerings' },
        { label: 'list_reservations', value: 'list_reservations' },
        { label: 'list_phone_numbers', value: 'list_phone_numbers' },
        { label: 'create_or_update_reservation', value: 'create_or_update_reservation' },
        { label: 'delete_reservation', value: 'delete_reservation' },
        { label: 'browse_available_numbers', value: 'browse_available_numbers' },
        { label: 'purchase_reservation', value: 'purchase_reservation' },
        { label: 'purchase_phone_numbers', value: 'purchase_phone_numbers' },
        { label: 'update_capabilities', value: 'update_capabilities' },
        { label: 'operator_information_search', value: 'operator_information_search' }
    ]}
>
<TabItem value="list_offerings">

List available offerings of capabilities with rates for the given country. List available offerings of capabilities with rates for the given country.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.list_offerings 
@country_code='{{ country_code }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@skip='{{ skip }}', 
@maxPageSize='{{ maxPageSize }}', 
@phoneNumberType='{{ phoneNumberType }}', 
@assignmentType='{{ assignmentType }}', 
@accept-language='{{ accept-language }}'
;
```
</TabItem>
<TabItem value="list_reservations">

Lists all reservations. Retrieves a paginated list of all phone number reservations. Note that the reservations will not be populated with the phone numbers associated with them.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.list_reservations 
@endpoint='{{ endpoint }}' --required, 
@maxPageSize='{{ maxPageSize }}'
;
```
</TabItem>
<TabItem value="list_phone_numbers">

Gets the list of all purchased phone numbers. Gets the list of all purchased phone numbers.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.list_phone_numbers 
@endpoint='{{ endpoint }}' --required, 
@skip='{{ skip }}', 
@top='{{ top }}'
;
```
</TabItem>
<TabItem value="create_or_update_reservation">

Creates or updates a reservation by its ID. Adds and removes phone numbers from the reservation with the given ID. The response will be the updated state of the reservation. Phone numbers can be reserved by including them in the payload. If a number is already in the reservation, it will be ignored. To remove a phone number, set it explicitly to null in the request payload. This operation is idempotent. If a reservation with the same ID already exists, it will be updated, otherwise a new one is created. Only reservations with 'active' status can be updated. Updating a reservation will extend the expiration time of the reservation to 15 minutes after the last change, up to a maximum of 2 hours from creation time. Partial success is possible, in which case the response will have a 207 status code.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.create_or_update_reservation 
@reservation_id='{{ reservation_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"phoneNumbers": "{{ phoneNumbers }}"
}'
;
```
</TabItem>
<TabItem value="delete_reservation">

Deletes a reservation by its ID. Deletes the reservation with the given ID. Any phone number in the reservation will be released and made available for others to purchase. Only reservations with 'active' status can be deleted.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.delete_reservation 
@reservation_id='{{ reservation_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="browse_available_numbers">

Browses for available phone numbers to purchase. Browses for available phone numbers to purchase. The response will be a randomized list of phone numbers available to purchase matching the browsing criteria. This operation is not paginated. Since the results are randomized, repeating the same request will not guarantee the same results.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.browse_available_numbers 
@country_code='{{ country_code }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"phoneNumberType": "{{ phoneNumberType }}", 
"capabilities": "{{ capabilities }}", 
"assignmentType": "{{ assignmentType }}", 
"phoneNumberPrefixes": "{{ phoneNumberPrefixes }}"
}'
;
```
</TabItem>
<TabItem value="purchase_reservation">

Starts the purchase of all phone numbers in the reservation. Starts a long running operation to purchase all of the phone numbers in the reservation. Purchase can only be started for active reservations that at least one phone number. If any of the phone numbers in the reservation is from a country where reselling is not permitted, do not resell agreement is required. The response will include an 'Operation-Location' header that can be used to query the status of the operation.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.purchase_reservation 
@reservation_id='{{ reservation_id }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"agreeToNotResell": {{ agreeToNotResell }}
}'
;
```
</TabItem>
<TabItem value="purchase_phone_numbers">

Purchases phone numbers. Purchases phone numbers.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.purchase_phone_numbers 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"searchId": "{{ searchId }}", 
"agreeToNotResell": {{ agreeToNotResell }}
}'
;
```
</TabItem>
<TabItem value="update_capabilities">

Updates the capabilities of a phone number. Updates the capabilities of a phone number.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.update_capabilities 
@phone_number='{{ phone_number }}' --required, 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"calling": "{{ calling }}", 
"sms": "{{ sms }}"
}'
;
```
</TabItem>
<TabItem value="operator_information_search">

Searches for number format and operator information for a given list of phone numbers. Searches for number format and operator information for a given list of phone numbers.

```sql
EXEC azure.communication_phonenumbers.phone_numbers.operator_information_search 
@endpoint='{{ endpoint }}' --required 
@@json=
'{
"phoneNumbers": "{{ phoneNumbers }}", 
"options": "{{ options }}"
}'
;
```
</TabItem>
</Tabs>
