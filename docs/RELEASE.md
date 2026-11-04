# Release Notes

## v2.9

### Authentication Server
- Added `AuthServer` class providing a lightweight fake auth server for testing without network dependencies.
- `login_with(access, expires_at)` registers a token with its expiration time.
- `call(access)` returns 200 if the access token is still valid, 401 otherwise.
- `refresh(refresh_token)` rotates access tokens, issuing a new token with a fresh expiration window.

### Token Refresher
- Added `TokenRefresher` class that keeps the app signed in by automatically refreshing tokens.
- `refresh_if_needed()` proactively refreshes the access token shortly before expiry (within 10 units of expiration).
- `get(path)` combines refresh logic with an API call, returning the server's response.