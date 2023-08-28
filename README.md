[![Actions Status](https://github.com/GriNiki/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/GriNiki/python-project-50/actions)  [![Check](https://github.com/GriNiki/python-project-50/actions/workflows/check.yml/badge.svg)](https://github.com/GriNiki/python-project-50/actions/workflows/check.yml)[![Maintainability](https://api.codeclimate.com/v1/badges/64413cab632464917313/maintainability)](https://codeclimate.com/github/GriNiki/python-project-50/maintainability)   <a href="https://codeclimate.com/github/GriNiki/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/64413cab632464917313/test_coverage" /></a>
# Diff Generator
### About
The Difference Generator is a utility for finding differences between two data structures. This generator works with JSON and YML/YAML formats and can output results in 3 styles Stylish, Plain, JSON.

#### Minimum requirements:
* python = "^3.10"
* pytest-cov = "^4.1.0"
* pyyaml = "^6.0.1"
* flake8 = "^6.1.0"
* pytest = "^7.4.0"

#### How install:
* Clone this repository
* Install dependencies: _make install_
* Build tar and whl package: _make build_
* Install package: _make package-install_

### Usage
#### For help, use the command:
* gendiff --help
[![asciicast](https://asciinema.org/a/u3jmvTgXnf9qHj9YIIssvghaF.svg)](https://asciinema.org/a/u3jmvTgXnf9qHj9YIIssvghaF)

### Demonstration how it works:
#### Stylish:
This is a standard output format that works with both flat files and files that have a tree structure.

JSON or YAML/YML flatten files:
[![asciicast](https://asciinema.org/a/MJvF0KtwnO0KzsHmiupReomSU.svg)](https://asciinema.org/a/MJvF0KtwnO0KzsHmiupReomSU)

JSON or YAML/YML tree files:
[![asciicast](https://asciinema.org/a/jOFYipWUsJvwrsjEL7eRG5u1C.svg)](https://asciinema.org/a/jOFYipWUsJvwrsjEL7eRG5u1C)
#### Plain:
Plain format reflects the situation as if we had combined the second object with the first one.

JSON or YAML/YML tree files:
[![asciicast](https://asciinema.org/a/o5VqFO4TW2Eyufp3KbqYIRZ4p.svg)](https://asciinema.org/a/o5VqFO4TW2Eyufp3KbqYIRZ4p)

#### Json:
In addition to an unstructured output (as a text), often an output in a structured format, such as JSON, is needed.

JSON or YAML/YML tree files:
[![asciicast](https://asciinema.org/a/ptOsJvBPrlouO3TFhFghHpDcc.svg)](https://asciinema.org/a/ptOsJvBPrlouO3TFhFghHpDcc)
