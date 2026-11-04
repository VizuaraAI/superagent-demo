# Release v2.9

## Android
- **Proactive token refresh.** `TokenRefresher` inspects expiry before every API call
  and renews the access token when it is within 10 seconds of expiration.
- **Seamless session continuity.** Refresh tokens persist across renewal cycles so
  the user stays signed in without re-authentication.

## Backend
- **Offline-first test auth server.** `AuthServer` is a fake OAuth backend with a
  manually steppable clock (`now`), so the full auth flow is exercised without any
  network calls.
- **Configurable token store.** `login_with()` lets tests seed the server with
  arbitrary access tokens and custom expiry windows.

## CI
- **Android test workflow on GitHub Actions.** Every PR and push to `main` triggers
  `pytest -q` on Python 3.11, keeping the Android client surface covered.