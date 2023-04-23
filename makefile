stop-env:
	docker-compose -f docker-compose.yml -f docker-compose-message-relay.yml down
start-env:
	docker-compose -f docker-compose-message-relay.yml -f docker-compose.yml up -d
build-env:
	docker-compose -f docker-compose.yml -f docker-compose-message-relay.yml build
