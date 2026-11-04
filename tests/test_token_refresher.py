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


def test_idle_past_expiry_should_refresh_and_succeed():
    """After idle past expiry, refresh should trigger and the call should succeed."""
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)

    server.now = 110
    status = t.get("/me")
    assert status == 200, f"expected 200, got {status}"


def test_recovery_after_idle_past_expiry():
    """After going idle past expiry, subsequent calls should continue working."""
    server, exp = make()
    t = TokenRefresher(server, "refresh-1", "access-1", exp)

    server.now = 110
    assert t.get("/me") == 200

    server.now = 115
    assert t.get("/me") == 200