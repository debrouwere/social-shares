all:
	python -c "import inspect; import socialshares; print inspect.getdoc(socialshares.command)" \
		> README.md
	pandoc -o README.rst README.md

package:
	python setup.py sdist upload

URL := http://www.theguardian.com/politics/2014/sep/08/pound-slumps-scottish-yes-campaign-poll-lead

test:
	python setup.py test