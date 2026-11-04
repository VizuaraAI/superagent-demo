# Release Notes

## v2.9

### Android

- **Proactive token refresh**: The client automatically refreshes the access token when it is within 10 seconds of expiry, so the session stays alive without the user having to re-login.
- **Transparent API calls**: `TokenRefresher.get(path)` combines the refresh check with every API call, ensuring stale tokens never reach the server.

### iOS

- **Proactive token refresh**: Same behaviour as Android — the refresh window is 10 seconds before expiry.
- **Transparent API calls**: Every `get()` call refreshes automatically when needed.

### Backend (Auth Server)

- **Login with access token**: `AuthServer.login_with(access, expires_at)` registers a new token with a given expiry.
- **API call validation**: `AuthServer.call(access)` returns 200 while valid, 401 after expiry.
- **Token refresh**: `AuthServer.refresh(refresh_token)` issues a fresh access token with a 100-second lifetime.