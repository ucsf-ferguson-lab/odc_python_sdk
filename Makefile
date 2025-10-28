.PHONY: fmt clean

fmt:
	ruff format

clean: fmt
	find . -type d -name ".ruff_cache" | xargs rm -rf
	find . -type d -name "__pycache__" | xargs rm -rf
	rm odc_sdk_generated.env