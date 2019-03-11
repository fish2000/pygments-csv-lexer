
clean: clean-pyc

distclean: clean-pyc clean-build-artifacts

rebuild: distclean

dist: rebuild sdist twine-upload

upload: bump dist
	git push

bigupload: bigbump dist
	git push

clean-pyc:
	find . -name \*.pyc -print -delete

clean-build-artifacts:
	rm -rf build dist pygments_csv_lexer.egg-info

sdist:
	python setup.py sdist

twine-upload:
	twine upload -s dist/*

bump:
	bumpversion --verbose patch

bigbump:
	bumpversion --verbose minor

check:
	check-manifest -v
	python setup.py check -m -s

.PHONY: clean-pyc clean-build-artifacts
.PHONY: clean distclean rebuild dist upload bigupload
.PHONY: sdist twine-upload bump bigbump check