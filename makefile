all: dev

dev:
	@uvicorn app.main:root --reload