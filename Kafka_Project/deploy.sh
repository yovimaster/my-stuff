#!/usr/bin/env bash

echo "deploying kafka"

# helm install kafka bitnami/kafka
# helm install prom prometheus-community/prometheus
# promservice=$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].addresses[].ip}"):$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].ports[].port}")
# sed -i -e 's/<placeholder>/'$promservice'/g' grafana_additional.yml
# helm install -f grafana_additional.yml grafana grafana/grafana
# kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo |pbcopy
# kubectl apply -f grafana_dashboards_cm.yml
cd producer && ./build.sh
kind load docker-image simple_producer:0.1
cd ../consumer && ./build.sh
kind load docker-image simple_consumer:0.1
cd ../
kafka_bootstrap=$(kubectl get endpoints -n default kafka -o jsonpath="{.subsets[0].addresses[].ip}"):$(kubectl get endpoints -n default kafka -o jsonpath="{.subsets[0].ports[].port}")
sed -i -e 's/<placeholder>/'$kafka_bootstrap'/g' Kafka_project/values.yaml
helm install project kafka_project
