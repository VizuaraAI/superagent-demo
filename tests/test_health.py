from app.server import AuthServer


def test_health_reports_ok():
    assert AuthServer().health()["status"] == "ok"


def test_health_reports_server_time():
    server = AuthServer()
    assert server.health()["now"] == 0
    server.now = 95
    assert server.health()["now"] == 95


def test_health_has_expected_keys():
    assert set(AuthServer().health()) == {"status", "now"}


def test_health_is_ok_even_with_expired_tokens():
    server = AuthServer()
    server.now = 10_000
    assert server.health() == {"status": "ok", "now": 10_000}
