"""A tiny fake auth server, so tests run with no network."""


class AuthServer:
    def __init__(self):
        self.now = 0
        self.tokens = {"refresh-1": ("access-1", 100)}
        self.counter = 1

    def health(self):
        return {"status": "ok", "time": self.now}

    def login_with(self, access, expires_at):
        self.tokens[access] = (access, expires_at)

    def call(self, access):
        """An API call. 200 if the access token is still valid, else 401."""
        for _, (tok, exp) in self.tokens.items():
            if tok == access and self.now < exp:
                return 200
        return 401

    def refresh(self, refresh_token):
        self.counter += 1
        tok = f"access-{self.counter}"
        exp = self.now + 100
        self.tokens[refresh_token] = (tok, exp)
        return tok, exp