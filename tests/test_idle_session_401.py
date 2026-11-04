"""Reproduce: idle session past token expiry returns 401."""
from app.server import AuthServer
from app.token_refresher import TokenRefresher


def test_idle_session_past_expiry_gets_401():
    """If the session has been idle past expiration, refresh_if_needed
    should still trigger a refresh — but it doesn't."""
    server = AuthServer()
    # Token expires at time 100
    t = TokenRefresher(server, "refresh-1", "access-1", 100)

    # Session idle: time has moved well past expiry
    server.now = 120

    # This should succeed (refresh the expired token), but currently returns 401
    result = t.get("/me")
    assert result == 200, f"Expected 200 but got {result}"