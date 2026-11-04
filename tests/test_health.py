from app.server import AuthServer


def test_health_returns_ok():
    assert AuthServer().health() == "ok"


def test_health_is_ok_even_with_expired_tokens():
    server = AuthServer()
    server.now = 10_000
    assert server.health() == "ok"
