# The build is tools/build.py; these are the names people reach for.
.PHONY: build test site clean install
install: ; python3 -m pip install -r requirements.txt
build:   ; python3 tools/build.py
test:    ; python3 -m pytest -q
site:    ; cd site && npm ci && npm run build
clean:   ; rm -rf tools/__pycache__ tests/__pycache__ .pytest_cache site/dist site/.astro
