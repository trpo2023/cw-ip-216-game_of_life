setup: requirements.txt
	pip install -r requirements.txt

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

test:
	./venv/bin/python3 test_game.py

run: venv/bin/activate
	./venv/bin/python3 main.py

all: main.py
	pyinstaller --onefile main.py

clean:
	rm -rf __pycache__
	rm -rf venv
	rm -rf build
