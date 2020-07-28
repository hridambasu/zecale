
.PHONY: setup setup-dev dev check test syntax grpc test_contracts

setup:
	pip install --upgrade pip
	pip install -e . --progress-bar off
	$(MAKE) grpc

check: syntax test

PROTOBUF_OUTPUT := \
  api/aggregator_pb2.py api/aggregator_pb2_grpc.py

api/%_pb2.py api/%_pb2_grpc.py: ../api/%.proto
	python -m grpc_tools.protoc \
      -I.. --proto_path .. --python_out=. --grpc_python_out=. --mypy_out=. \
      api/$*.proto

grpc: $(PROTOBUF_OUTPUT)
	@# suppress "Nothing to do for ..." warning
	@echo -n

syntax: ${PROTOBUF_OUTPUT}
	flake8 `git ls-files '**.py'`
	mypy -p api
	mypy -p zecale
	mypy -p test_commands
	pylint zecale test_commands
