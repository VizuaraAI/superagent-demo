# Release Notes

## v2.9

### Android

- Added `TokenRefresher` class that automatically refreshes access tokens before they expire.
- Proactive refresh window: tokens are refreshed within the last 10 seconds of their lifetime.
- Integrated with the `AuthServer` for seamless token lifecycle management.

### Backend

- Added `AuthServer` class providing a fake authentication backend for testing.
- Supports login, token validation via `call()`, and token refresh via `refresh()`.
- Enables offline testing without network dependencies.

### CI & Testing

- Added test suite covering fresh token validation and pre-expiry refresh behavior.
- CI pipeline runs on every pull request and push to `main`.