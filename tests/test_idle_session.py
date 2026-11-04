"""Regression tests for the "401 after the app was idle" bug."""

from app.server import AuthServer
from app.token_refresher import TokenRefresher


def make(expires_at=100, now=0):
    server = AuthServer()
    server.now = now
    return server, expires_at


def test_idle_past_expiry_still_refreshes():
    # The app was left idle until well after the access token expired.
    server, exp = make(expires_at=100, now=500)
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    assert t.get("/me") == 200


def test_idle_just_past_expiry_still_refreshes():
    server, exp = make(expires_at=100, now=101)
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    assert t.get("/me") == 200


def test_idle_refresh_keeps_session_alive_across_calls():
    server, exp = make(expires_at=100, now=0)
    t = TokenRefresher(server, "refresh-1", "access-1", exp)
    assert t.get("/me") == 200
    # Idle for a long time, then the user opens the app again.
    server.now = 10_000
    assert t.get("/me") == 200
