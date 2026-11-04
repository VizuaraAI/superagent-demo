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


def test_refresh_after_token_expired_due_to_idle():
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    # Session was idle; token expired 20 time units ago.
    server.now = 120
    assert t.get("/me") == 200
    assert t.access != "access-1"