# Release Notes

## v2.9

### Android
- **Token Refresher**: `TokenRefresher` keeps the app signed in by automatically refreshing access tokens before they expire. Call `get(path)` to combine refresh logic with any API request.
- **Proactive refresh**: Tokens are renewed within 10 units of expiration, avoiding interruptions from stale credentials.

### Backend
- **Auth Server**: `AuthServer` provides a lightweight fake auth server so tests run with no network. Register tokens via `login_with(access, expires_at)`, validate calls with `call(access)`, and rotate tokens with `refresh(refresh_token)`.
- **Test independence**: All auth flows can be exercised offline, speeding up CI and local development.