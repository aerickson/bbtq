test:
	./bin/tq . btq/tests/simple.toml

pipe_test:
	cat btq/tests/simple.toml | ./bin/tq .


