from app.server import AuthServer


def test_health():
    server = AuthServer()
    assert server.health() == "ok"