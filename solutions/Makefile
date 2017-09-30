MODULES := $(shell find . -maxdepth 1 -mindepth 1 -type d -exec basename {} \;)

.PHONY: all
all: test

.PHONY: test
test:
	@echo "======================================================================"
	@echo "Running unit tests"
	@echo "----------------------------------------------------------------------"
	@python -m unittest discover -v
	@echo "----------------------------------------------------------------------"
