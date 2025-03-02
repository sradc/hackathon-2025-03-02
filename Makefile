
format:
	uv run isort --profile black . && uv run black .

run-voice:
	uv run python voice/main.py
