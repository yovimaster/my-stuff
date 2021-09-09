# Kafka Consumer and Producer on Kubernetes

In This projesct im going to implement this basic Design

Producer ==> Kafka ==> Consumer

While also being monitored by prometheus, and displaying dashboards with grafana

## Prerequisits

This project was created, ran and tested on MacOs Cataline (10.15)
in order to run the deploy script you should install -
Home brew -`bash curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh`
Docker - `brew cask install docker`
Kind - `brew install kind`
Helm - `brew install helm`

After installing all of this, you need to create a kubernetes cluster on your loclahost (make sure you have at least 30GB availble)
`kind create cluster`

Once the cluster is up you are ready to continue to the next part
## Deploying the stack

Once copied the relevant folder into you computer (you can git clone with sparse-checkout)
just run
`./deploy.sh` and it should deploy everything

### overview of installation
The steps of the installation is as follows:

 - [ ] Installing Kafka on the cluster, with zookeeper
 - [ ] Installing prometheus stack
 - [ ] installing grafana stack, with preloaded dashboards
 - [ ] Build both services (Producer and consumer)
 - [ ] Deploy the services onto the cluster
 - [ ] Exposing the port so you can visit the grafana and see the metrics (note: you need to wait couple of minutes to see all the metrics in the dashboard)
