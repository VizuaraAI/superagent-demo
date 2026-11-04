# v2.9 Release Notes

## Authentication

- **Auth server simulation** — a lightweight in-process auth server replaces real network calls in tests, making CI deterministic and fast.
- **Login with custom tokens** — `AuthServer.login_with` lets tests register arbitrary access tokens and expiry times.

## Token Management

- **Proactive token refresh** — `TokenRefresher.refresh_if_needed` automatically refreshes the access token in the 10-second window before expiry.
- **Seamless API calls** — `TokenRefresher.get` calls `refresh_if_needed` transparently before every request, keeping the client signed in without user intervention.
- **Configurable expiry** — token lifetime is fully tunable per-test via `TokenRefresher`'s constructor.

## Testing

- **Pytest suite** — tests cover fresh-token calls and refresh-just-before-expiry scenarios on Android.
- **CI via GitHub Actions** — runs the full test suite on every PR and push to `main`.