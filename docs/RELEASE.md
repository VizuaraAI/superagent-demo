# Release v2.9

## Token Refresher

- **Automatic refresh before expiry.** The `TokenRefresher` now refreshes the access token when it is within 10 seconds of expiration, preventing unnecessary 401 responses.
- **Seamless API calls.** `get(path)` automatically invokes the refresh check before every call, so callers never need to manage token lifecycle manually.

## Auth Server (test doubles)

- **Fake auth server for offline tests.** `AuthServer` simulates token validation and refresh so the test suite runs with no network dependency.
- **Deterministic expiry.** Tests can advance the clock via `server.now` to verify refresh behaviour at exact time boundaries.

## Internal

- **CI workflow.** Automated test run on pull requests and pushes to `main` using Python 3.11.
- **Test coverage.** Tests cover fresh-token calls and refresh-just-before-expiry scenarios.