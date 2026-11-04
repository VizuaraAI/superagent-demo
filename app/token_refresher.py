"""Keeps the app signed in by refreshing its access token."""


class TokenRefresher:
    def __init__(self, server, refresh_token, access, expires_at):
        self.server = server
        self.refresh_token = refresh_token
        self.access = access
        self.expires_at = expires_at

    def refresh_if_needed(self):
        # Refresh shortly before the token expires, and also when it has already
        # expired (the app was idle for a while). Refreshing is safe either way,
        # so there is no lower bound on how far past expiry we are.
        if self.server.now >= self.expires_at - 10:
            self.access, self.expires_at = self.server.refresh(self.refresh_token)

    def get(self, path):
        self.refresh_if_needed()
        return self.server.call(self.access)
