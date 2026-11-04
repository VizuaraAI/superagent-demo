"""Keeps the app signed in by refreshing its access token."""


class TokenRefresher:
    def __init__(self, server, refresh_token, access, expires_at):
        self.server = server
        self.refresh_token = refresh_token
        self.access = access
        self.expires_at = expires_at

    def refresh_if_needed(self):
        # Refresh shortly before the token expires, and also when it has
        # already expired (e.g. the app was idle for a while). The old lower
        # bound of 0 skipped the refresh for expired tokens, so the next call
        # went out with a stale access token and the server answered 401.
        if self.expires_at - self.server.now <= 10:
            self.access, self.expires_at = self.server.refresh(self.refresh_token)

    def get(self, path):
        self.refresh_if_needed()
        return self.server.call(self.access)
