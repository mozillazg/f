help:
	@echo "test             run test"
	@echo "publish          publish to PyPI"
	@echo "publish_test     publish to TestPyPI"

.PHONY: test
test:
	@echo "run test"
	py.test --cov f test.py

.PHONY: publish
publish:
	@echo "publish to pypi"
	python setup.py register
	python setup.py publish

.PHONY: publish_test
publish_test:
	python setup.py register -r test
	python setup.py sdist upload -r test
	python setup.py bdist_wheel upload -r test
