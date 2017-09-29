MODULES := $(shell find . -maxdepth 1 -mindepth 1 -type d -exec basename {} \;)

.PHONY: all
all: $(MODULES)

.PHONY: $(MODULES)
$(MODULES):
	@python -m unittest -v $@.test
