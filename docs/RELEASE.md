# v2.9 Release Notes

## Authentication

- **AuthServer**: Added a lightweight fake auth server for offline testing, supporting login, token validation via `/me`-style API calls, and refresh token rotation.
- Token expiry is time-based, controllable via `server.now`, enabling deterministic test scenarios without real network calls.

## Token Management

- **TokenRefresher**: Introduced automatic access-token refresh. The refresher checks expiry before each API call and renews the token when it is within a configurable window (10 seconds before expiry).
- The `get(path)` method transparently refreshes and then calls the server, so consumers get a seamless signed-in experience.

## Testing

- Test suite using `pytest` covers fresh-token calls and the just-before-expiry refresh path.
- All tests run with no external dependencies—the fake `AuthServer` keeps the suite fast and reliable.