PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

api: ## Run the API
	uvicorn src.api.main:app --reload

app: ## Run the API
	uvicorn src.api.main:app --host 0.0.0.0 --port 8000