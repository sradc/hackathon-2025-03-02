

.PHONY: run
run:
	./run.sh


.PHONY: requirements.txt
requirements.txt:
	uv pip freeze > requirements.txt


.PHONY: format
format:
	uv run isort --profile black . && uv run black .

