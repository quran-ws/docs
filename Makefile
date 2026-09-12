# The build is tools/build.py; these are the names people reach for.
.PHONY: build test clean install
install: ; python3 -m pip install -r requirements.txt
build:   ; python3 tools/build.py
test:    ; python3 -m pytest -q
clean:   ; rm -rf tools/__pycache__ tests/__pycache__ .pytest_cache
