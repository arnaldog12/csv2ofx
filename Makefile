install:
	uv venv --python 3.9
	uv pip install --force-reinstall "PyYAML==5.1"
	uv pip install meza pkutils setuptools ruff
	python setup.py develop

run:
	python main.py
