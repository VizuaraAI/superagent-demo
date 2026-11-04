# Release Notes

## v2.9

### Authentication Server

- **Login with access token**: `AuthServer.login_with(access, expires_at)` registers a new access token with a given expiry time.
- **API call validation**: `AuthServer.call(access)` returns 200 while the token is valid, or 401 once it has expired.
- **Token refresh**: `AuthServer.refresh(refresh_token)` issues a new access token with a fresh 100-second lifetime, keyed by the refresh token.

### Token Refresher

- **Proactive refresh**: `TokenRefresher.refresh_if_needed()` automatically refreshes the access token when it is within 10 seconds of expiry, keeping the session alive without user intervention.
- **Transparent API access**: `TokenRefresher.get(path)` combines refresh logic with an API call so callers always use a valid token.