
.PHONY: format
format:
	uv run isort --profile black . && uv run black .

.PHONY: voice
voice:
	uv run python voice/main.py
