# PythonDA - Homework for tests

## issue-01

The code is in file `morse1.py`

This should be executed by typing in your command line:
`python -m doctest -o NORMALIZE_WHITESPACE -v morse1.py >result1.txt`

Here:
- `python` or `python3` is your Python executor
- `-m` to run a module
- `doctest` is a module for tests, if you don't have it use `pip install doctest` or `pip3 install doctest`
- `-o NORMALIZE_WHITESPACE` is an option that is nesessary to test long outputs while havind PEP8 complient `.py` file
- `-v` is used for verbose output, if you wish you can ommit it to make output shorter
- `morse1.py` is the file to test, you can add relative or absolute path
- `>result1.txt` use this to redirect output to this file, this is optional
