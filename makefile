builder:
	python setup.py sdist bdist_egg
install:
	python setup.py install
clean:
	rm -rf build
upload:
	twine upload dist/*