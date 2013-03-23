Usage
======

## Create answer keys
This uses ssh to run against caprica and copy get the canonical answers into `testXX.py.expected`. To make this easiest, you should add a caprica Host to your ssh config file.

    Host caprica
        HostName caprica.ucombinator.org
        User u0xxxxxx

Then run `make answers` which will create all un-made answer keys in `tests/`

## Actually Test
    make test