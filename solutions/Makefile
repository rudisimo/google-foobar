MODULES := $(shell find . -maxdepth 1 -mindepth 1 -type d -exec basename {} \;)

.PHONY: all
all: test

.PHONY: test
test: $(MODULES)

.PHONY: $(MODULES)
$(MODULES):
	@echo "======================================================================"
	@echo "Running: $@"
	@echo "----------------------------------------------------------------------"
	@python -m unittest -v $@.test
