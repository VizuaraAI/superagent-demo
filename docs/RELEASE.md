# Release v2.9

## Token Refresh
- **Proactive refresh before expiry.** `TokenRefresher` checks expiry on every API call and
  refreshes the access token if it is within 10 seconds of expiration.
- **Preserves refresh token across cycles.** The same refresh token can be reused for
  successive access-token renewals, keeping the session alive indefinitely.

## Auth Server
- **Fake backend for offline tests.** `AuthServer` tracks token validity with a
  controllable clock (`now`), avoiding any network dependency in the test suite.
- **Configurable token state.** Tests can pre-seed the server with arbitrary access tokens
  and expiry timestamps via `login_with()`.

## Test Suite
- **Fresh-token call returns 200.** Validates that a valid, unexpired token succeeds on
  API calls.
- **Pre-expiry refresh.** Advances the clock to 5 seconds before expiry and confirms that
  `get()` triggers a refresh and uses the new access token.
- **CI integration.** Tests run automatically on every pull request and push to `main`
  via GitHub Actions (Python 3.11, pytest).