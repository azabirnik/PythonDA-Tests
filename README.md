# PythonDA - Homework for tests

## issue-01

The code is in file `morse1.py`

This should be executed by typing in your command line:

    python -m doctest -o NORMALIZE_WHITESPACE -v morse1.py >result1.txt

Here:
- `python` or `python3` is your Python interpreter
- `-m` to run a module
- `doctest` is a module for tests, if you don't have it use `pip install doctest` or `pip3 install doctest`
- `-o NORMALIZE_WHITESPACE` is an option that is nesessary to test long outputs while havind PEP8 complient `.py` file
- `-v` is used for verbose output, if you wish you can ommit it to make output shorter
- `morse1.py` is the file to test, you can add relative or absolute path
- `>result1.txt` use this to redirect output to this file, this is optional

NOTE: `encode` fails on lowercase, I assume this is expected by design.

## issue-02

The code of tests is in file `morse2.py` while the original `morse.py` is used by `import` in `morse2.py`

This should be executed by typing in your command line:

    pytest -v morse2.py >result2.txt

Here:
- `pytest` is a module for tests, if you don't have it use `pip install pytest` or `pip3 install pytest`
- `-v` is used for verbose output, if you wish you can ommit it to make output shorter
- `morse2.py` is the file to test, you can add relative or absolute path
- `>result2.txt` use this to redirect output to this file, this is optional

## issue-03

The code of tests is in file `one_hot_encoder3.py` while the original `one_hot_encoder.py` is used by `import` in `one_hot_encoder3.py`

This should be executed by typing in your command line:

    python -m unittest -v one_hot_encoder3.py 2>result3.txt

Here:
- `python` or `python3` is your Python interpreter
- `-m` to run a module
- `unittest` is a module for tests, if you don't have it use `pip install unittest` or `pip3 install unittest`
- `-v` is used for verbose output, if you wish you can ommit it to make output shorter
- `one_hot_encoder3.py` is the file to test, you can add relative or absolute path but if you run it from different directory there may be a problem with `from one_hot_encoder import fit_transform`
- `2>result3.txt` use this to redirect output to this file, this is optional; note `2` before `>` - this is used to redirect stderror output as unittest output is not to stdout but to stderr




