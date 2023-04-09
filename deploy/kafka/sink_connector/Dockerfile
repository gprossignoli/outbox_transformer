FROM confluentinc/cp-kafka-connect:7.3.0

USER root

RUN mkdir -p /usr/local/share/kafka/plugins \
    && confluent-hub install --no-prompt --component-dir /usr/local/share/kafka/plugins confluentinc/kafka-connect-jdbc:latest \
    && confluent-hub install --no-prompt --component-dir /usr/local/share/kafka/plugins debezium/debezium-connector-postgresql:latest