.PHONY: help install demo test clean

help:
	@echo "Targets: install | demo | clean"

install:
	pip install -e .

demo:
	rm -rf labs
	python -m clip2lab examples/one-reel/transcript.txt -o labs
	@test -f labs/one-reel/README.md
	@test -f labs/one-reel/quiz.md
	@echo "✓ clip2lab demo OK — lab pack generated under labs/one-reel/" 

clean:
	rm -rf .venv dist build *.egg-info reports labs out audit.log __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
