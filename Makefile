.PHONY: test clean

test:
	tox

clean:
	find . -name '*.pyc' -delete
	rm -rf graphql_middleware.egg-info
	rm -f MANIFEST

.PHONY: install-hooks
install-hooks:
	tox -e pre-commit -- install -f --install-hooks
