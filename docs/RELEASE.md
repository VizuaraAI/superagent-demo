# Release Notes

## v2.9

### Android

- **Token refresher**: The app now keeps users signed in by automatically refreshing access tokens shortly before they expire. The `TokenRefresher` class monitors token expiry and requests a new access token from the auth server within a 10-second window before expiration.
- **Fake auth server**: A simulated `AuthServer` is available for offline testing, supporting login, API call validation, and token refresh without network dependencies.
- **Test suite**: Unit tests cover both fresh-token calls and the refresh-just-before-expiry path, ensuring the refresher works correctly in edge cases.
- **CI pipeline**: Android tests run on every pull request and push to `main` via GitHub Actions, using Python 3.11 and pytest.