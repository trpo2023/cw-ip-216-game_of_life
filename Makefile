run: venv/bin/activate
	./venv/bin/python3 main.py

test:
	./venv/bin/python3 test_game.py

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

setup: requirements.txt
	pip install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf venv