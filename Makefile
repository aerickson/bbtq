all_test: test pipe_test

test:
	./bin/tq btq/tests/simple.toml .

pipe_test:
	cat btq/tests/simple.toml | ./bin/tq - .

bad_test:
	./bin/tq . badbad.toml

pytest:
	pytest --cov=btq btq/tests/ -v
