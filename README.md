# Bibliarius

Tracks book reading lists :)

## Dev Setup

### Perquisites

* Python 3.9.x ([pyenv](https://github.com/pyenv/pyenv) can help)
* [Docker](https://docs.docker.com/desktop/mac/install/)

### Initial Setup

Run `make setup` to install dependencies and start local DB container

Run `make ci` to verify successful setup

### Testing

Run `make lint` for static analysis (formatter, linter, type-checker, etc.)

Run `make test` for unit tests

Run `make ci` for both static analysis + unit tests

**`make ci` should be run before every `git commit`**
