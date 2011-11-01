#!/bin/sh

# Compile
erlc solution.erl

# Execute
erl -noshell -s solution start -s init stop
