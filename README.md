# PythonDA
# Homework for tests

## issue-01

The code is in file `morse1.py`

This should be executed by typing in your command line:
`python -m doctest -o NORMALIZE_WHITESPACE -v morse1.py`

Here:
- `python` or `python3` -- is your Python executor
- `-m` to run a module
- `doctest` -- a module for tests, if you don't have it use `pip install doctest` or `pip3 install doctest`
- `-o NORMALIZE_WHITESPACE` this option is nesessary to test long outputs while havind PEP8 complient `.py` file
- `-v` is for verbose output, if you wish you can ommit it to make output shorter
- `morse1.py` the file to test, you can add relative or absolute path

Sample output:
```
python -m doctest -o NORMALIZE_WHITESPACE -v morse1.py
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('PYTHON')
Expecting:
    '.--. -.-- - .... --- -.'
ok
Trying:
    encode('A'*100)
Expecting:
    '.- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .-
    .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .-
    .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .-
    .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .- .-
    .- .- .- .-'
ok
Trying:
    encode('A'*10000)  # doctest: +ELLIPSIS
Expecting:
    '.- .- .- .- .- .- .- .- .- ...
ok
Trying:
    encode('Привет')  # doctest: +ELLIPSIS
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: ...
ok
2 items had no tests:
    morse1
    morse1.decode
1 items passed all tests:
   5 tests in morse1.encode
5 tests in 3 items.
5 passed and 0 failed.
Test passed.
```

