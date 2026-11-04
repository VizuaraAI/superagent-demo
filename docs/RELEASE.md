# v2.9 Release Notes

## Android

- **TokenRefresher**: Automatic access-token refresh. Before each API call the refresher checks expiry and renews the token within a 10-second window, giving users a seamless signed-in experience.
- The `get(path)` method transparently refreshes then calls the server — no manual token handling needed in the Android app.

## Backend

- **AuthServer**: Lightweight fake auth server for offline testing. Supports login, token validation via API calls, and refresh-token rotation.
- Token expiry is time-based, controlled via `server.now`, enabling deterministic test scenarios without real network calls.

## Testing

- pytest suite covers fresh-token calls and the just-before-expiry refresh path.
- All tests run with no external dependencies — the fake `AuthServer` keeps the suite fast and offline.