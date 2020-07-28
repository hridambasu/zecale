# Python client to interact with the aggregator

## Setup

Ensure that the following are installed:

- Python 3.7 (See `python --version`)
- [venv](https://docs.python.org/3/library/venv.html#module-venv) module.
- gcc

Execute the following inside the `client` directory.
```console
$ python -m venv env
$ source env/bin/activate
(env)$ make setup
```

(It may also be necessary to install solc manually if the `py-solc-x` package
fails to find it. See the instructions below.)

We assume all further commands described here are executed from within the
Python virtualenv.  To enter the virtualenv from a new terminal, re-run
```console
$ source env/bin/activate
```

## Execute unit tests

```console
(env)$ make check
```

## Execute testing client

Test the API of the aggregator server:
```console
(env)$ test_aggregator_server_api.py
```

## Note on solc compiler installation

Note that `make setup` will automatically install the solidity compiler in `$HOME/.solc`
(if required) and not in the python virtual environment.
