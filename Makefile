all_test: test pipe_test

test:
	./bin/tq bbtq/tests/simple.toml .

pipe_test:
	cat bbtq/tests/simple.toml | ./bin/tq - .

bad_test:
	./bin/tq . badbad.toml

pytest:
	pytest --cov=bbtq bbtq/tests/ -v
