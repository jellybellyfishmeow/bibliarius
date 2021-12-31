# Bibliarius

Tracks book reading lists :)

## Dev Setup

### Initial Setup

1. Make sure you have Python 3.9.x installed ([pyenv](https://github.com/pyenv/pyenv) can help)
2. Run `make setup` to install dependencies
3. Run `make ci` to verify successful setup

### Testing

Run `make lint` for static analysis (formatter, linter, type-checker, etc.)

Run `make test` for unit tests

Run `make ci` for both static analysis + unit tests

**`make ci` should be run before every `git commit`**
