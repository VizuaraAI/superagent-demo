# v2.9 Release Notes

## Token Refresher

- **Proactive refresh window**: TokenRefresher now refreshes the access token in a 10‑second window
  before expiry, reducing the chance of a 401 response on API calls.
- **Stateless token rotation**: Each successful refresh produces a new access token with a fresh
  100‑second lifetime, while preserving the existing refresh token.

## Auth Server

- **Extensible token store**: AuthServer supports registering arbitrary tokens via `login_with`,
  simplifying integration tests that need custom expiry scenarios.
- **Deterministic token counters**: The `refresh` endpoint now uses a monotonic counter to generate
  predictable access token identifiers (`access-2`, `access-3`, …), making test assertions
  reliable.

## CI / Developer Experience

- **GitHub Actions pipeline**: Every push and pull request triggers `pytest` on Python 3.11,
  ensuring the token lifecycle tests pass before merge.
- **Requirements pinning**: `pytest==8.3.3` is the sole dependency, keeping the environment
  reproducible and minimal.