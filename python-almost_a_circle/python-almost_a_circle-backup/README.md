# python-almost_a_circle

## Description

This project is a review of core Python concepts through the design of a
small class hierarchy: `Base`, `Rectangle`, and `Square`. It covers
imports, exceptions, classes, private attributes, getters/setters, class
methods, static methods, inheritance, unit testing, and reading/writing
files (including JSON and CSV serialization).

## Learning Objectives

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- pycodestyle 2.7.*
- All files start with `#!/usr/bin/python3`, end with a newline, and are
  executable
- All modules, classes, and functions are documented

## Files

| File | Description |
| --- | --- |
| `models/base.py` | `Base` class: manages `id`, JSON/CSV (de)serialization |
| `models/rectangle.py` | `Rectangle` class, inherits from `Base` |
| `models/square.py` | `Square` class, inherits from `Rectangle` |
| `tests/test_models/` | Unit tests for all three classes |

## Usage

Run the full test suite:

```bash
python3 -m unittest discover tests
```

Check code style:

```bash
pycodestyle models/*.py tests/test_models/*.py
```

## Author

Lael
