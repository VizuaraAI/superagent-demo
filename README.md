# App team demo

## Running the tests

The test suite uses [pytest](https://docs.pytest.org/) and runs on Python 3.11. First install the dependencies:

```sh
pip install -r requirements.txt
```

Then run the tests from the repository root:

```sh
python -m pytest -q
```

The tests live in `tests/test_token_refresher.py` and cover the token refresh behaviour of the client.

---

A small mobile-app backend client used to demonstrate Super Agent designs live. The bug in this repo is planted on purpose.
