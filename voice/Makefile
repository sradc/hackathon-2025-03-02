
.PHONY: format
format:
	uv run isort --profile black . && uv run black .

.PHONY: voice
voice:
	uv run python main.py


.PHONY: requirements.txt
requirements.txt:
	uv pip freeze > requirements.txt
