#!/usr/bin/env bash

echo "deploying kafka"

# helm install kafka bitnami/kafka
# helm install prom prometheus-community/prometheus
promservice=$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].addresses[].ip}"):$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].ports[].port}")
sed -i -e 's/<placeholder>/'$promservice'/g' grafana_additional.yml
helm install -f grafana_additional.yml grafana grafana/grafana
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo |pbcopy
