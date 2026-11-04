from app.server import AuthServer
from app.token_refresher import TokenRefresher


def make(expires_at=100):
    return AuthServer(), expires_at


def test_call_with_fresh_token():
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    assert t.get("/me") == 200


def test_refresh_just_before_expiry():
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    server.now = 95
    assert t.get("/me") == 200
    assert t.access != "access-1"


def test_refresh_when_token_already_expired():
    """If the session was idle past expiry, we still refresh instead of returning 401."""
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    server.now = 105  # token already expired
    assert t.get("/me") == 200
    assert t.access != "access-1"