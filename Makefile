.PHONY := all install

all:
	poetry run python raspador_emendas.py

install:
	poetry install
