# !/usr/bin/env bash

echo "Deploying kafka"
helm install -f kafka_additional.yml kafka bitnami/kafka

echo "Waiting for the service to recive it's endpoint"
count=0
while [[ "x$(kubectl get endpoints -n default kafka -o jsonpath="{.subsets[0].addresses[].ip}")" == "x" ]]; do
  echo "waiting....."
  sleep 10
  count=`expr $count + 1`
    if [[ $count -gt 100 ]]; then
  echo "took to much time, abort"
  break
  fi
done


echo "Deploying prometheus"
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prom prometheus-community/prometheus
echo "Waiting for the service to recive it's endpoint"
count=0
while [[ "x$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].addresses[].ip}")" == "x" ]]; do
  echo "waiting....."
  sleep 10
  count=`expr $count + 1`
    if [[ $count -gt 100 ]]; then
  echo "took to much time, abort"
  break
  fi
done


echo "deploying grafana"
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
promservice=$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].addresses[].ip}"):$(kubectl get endpoints -n default prom-prometheus-server -o jsonpath="{.subsets[0].ports[].port}")
sed -i '' -e 's/<placeholder>/'$promservice'/g' grafana_additional.yml
helm install -f grafana_additional.yml grafana grafana/grafana
kubectl apply -f grafana_dashboards_cm.yml

echo "Building the Kafka Producer"
cd producer && ./build.sh
kind load docker-image simple_producer:0.1

echo "building the Kafka Consumer"
cd ../consumer && ./build.sh
kind load docker-image simple_consumer:0.1

echo "Now installing the Helm chart of the producer and consumer"
cd ../
kafka_bootstrap=$(kubectl get endpoints -n default kafka -o jsonpath="{.subsets[0].addresses[].ip}"):$(kubectl get endpoints -n default kafka -o jsonpath="{.subsets[0].ports[].port}")
sed -i '' -e 's/<placeholder>/'$kafka_bootstrap'/g' Kafka_project/values.yaml
helm install project kafka_project

echo "Done deploying the full architecture"
echo "Take the grafana admin password:"
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
echo "And now port-forwarding the grafan so we can view it online (localhost:3000)"
kubectl --namespace default port-forward $(kubectl get pods -n default |grep grafana| awk '{print $1}') 3000
