.PHONY: test bash
test:
	docker-compose exec app pytest /app/src /app/apps/tests

bash:
	docker-compose exec app bash