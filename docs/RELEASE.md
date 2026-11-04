# Release v2.9

## Authentication Server

- **`AuthServer`** – Fake auth server for local testing with no network dependency.
- `login_with(access, expires_at)` registers a pre-existing token for testing.
- `call(access)` returns 200 while the token is valid, 401 once expired.
- `refresh(refresh_token)` issues a new access token with a fresh 100-second expiry window.

## Token Refresher

- **`TokenRefresher`** – Keeps the app signed in by refreshing access tokens automatically.
- `refresh_if_needed()` triggers a refresh when the token is within 10 seconds of expiry.
- `get(path)` calls `refresh_if_needed` before every API call, ensuring the caller always has a valid token.

## CI / Testing

- Android test workflow (`ci.yml`) runs `pytest -q` on every pull request and push to `main`.
- Tests cover fresh-token calls and the refresh-just-before-expiry edge case.