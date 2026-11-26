"use strict";
// STUDENT CONTEXT: S2, script loaded by index.html in the browser.
// TO BUILD: replace the plan below with your functions and events.
// CHECK: Network tab for HTTP, Console for JS, then keyboard acceptance.
// PostgreSQL secrets and cloud keys have no place in this file.

/*
 * S2 workshop: build the interface from the contract, without a library.
 * This file is deliberately an implementation plan, not an answer key.
 * The names suggested below are suggestions, not an imposed API.
 *
 * 1. request(path, options)
 *    Call fetch with a relative path (/api/datasets) to keep the origin.
 *    JSON: send Content-Type: application/json. CSV file: send the
 *    File as is as body with Content-Type: text/csv (no FormData).
 *    Handle 204 before response.json(): deletion has no body.
 *    Check response.ok: fetch does not reject on 404, 409, 413, 415 or 422.
 *    detail can be a string or a list; a proxy can return HTML.
 *
 * 2. Datasets: loadDatasets() and renderDatasets(datasets)
 *    Show loading, empty list, list or error without mixing them up.
 *    Build the DOM elements and write the data with textContent.
 *    Never inject name, owner or description into innerHTML.
 *    Deletion: confirmation showing the name; cancelling sends nothing.
 *
 * 3. File upload: POST /api/datasets/{id}/ingestions?filename=...
 *    The 202 response means "received and waiting", not "processed".
 *    Show the pending status, then query GET /api/ingestions/{id}
 *    every 2 seconds until succeeded or failed (stop following
 *    after a bounded number of attempts and tell the user).
 *    Disable the button while sending, enable it again in finally.
 *
 * 4. Report and retry
 *    Show rows_accepted, rows_rejected, rows_duplicate and the first
 *    line errors (number + reason). A failed upload offers "Retry"
 *    (POST /api/ingestions/{id}/retry); the other statuses do not.
 *
 * 5. Indicators: GET /api/datasets/{id}/stats?room=&from=&to=
 *    Table per room: measurements, average/min/max CO2, average temperature and humidity,
 *    last measurement. Entered dates become ISO dates
 *    with time zone; an invalid period (from > to) produces a readable message.
 *
 * 6. Manual acceptance
 *    Test with the keyboard, with an empty list, an invalid file and the API unavailable.
 *    Create a dataset named "Rooms <b>A</b>": the tags are shown as text.
 *    Add the API version to the interface for the cloud acceptance.
 */
