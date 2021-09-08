prerequisits
`docker version !!!!`


install kind

`brew install kind`

create cluster

`kind create cluster`

install helm

`brew install helm`

install kafka with helm chart

`helm install kafka bitnami/kafka`

create a topic on that kafka

`./kafka-topics.sh --zookeeper  10.244.0.7:2181 --create --topic simple-one --partitions 1 --replication-factor 1`

check that it runs - `./kafka-topics.sh --zookeeper  10.244.0.7:2181 --list

build images of producer

`cd producer && ./build.sh`

upload the image to kind

`kind load docker-image simple_prdoucer:0.1`

deploy the chart

kubectl apply -f producer.yaml

same for consumer

install prometheous

`helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
`helm repo update`
`helm install prom prometheus-community/prometheus`

`helm repo add grafana https://grafana.github.io/helm-charts`
`helm install grafana grafana/grafana`

think about installing via helm intall or keep the chart localy for changes
helm install -f values.yaml bitnami/wordpress --generate-name

3 add a kafka exporter
wrap all in helm chart and deploy scrip t
