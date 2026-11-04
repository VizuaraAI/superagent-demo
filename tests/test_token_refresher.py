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


def test_refresh_after_idle_session_token_expired():
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    # Session was idle past expiry — token is stale.
    server.now = 150
    assert t.get("/me") == 200
    assert t.access != "access-1"