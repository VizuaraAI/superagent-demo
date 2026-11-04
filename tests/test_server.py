from app.server import AuthServer


def test_health():
    server = AuthServer()
    assert server.health() == {"status": "ok", "time": 0}
    server.now = 42
    assert server.health() == {"status": "ok", "time": 42}