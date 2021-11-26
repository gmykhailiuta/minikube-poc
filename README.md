# Minikube PoC

## Description

Current repository represents a proof-of-concept of deployment and
interaction of microservices deployed to minikube.

There're 2 microservices. First one exposes next JSON document:

        {
        "id": "1",
        "message": "Hello world"
        }

Second one utilizes the first and displays reversed message text.


## Stack

- Minikube
- Docker
- Python/Flask
- Helm3


## Repository structure
```
.
├── app_one
│   ├── app_one               | Flask application for p.1 of the task
│   ├── conftest.py           | pytest config
│   ├── docker-entrypoint.sh  | Runs application in container
│   ├── Dockerfile            |
│   ├── helm                  |
│   │   └── app-one           | Helm chart
│   ├── main.py
│   ├── Makefile              | Automation per application=
│   └── requirements
├── app_two                   | Flask application for p.4 of the task
│   ...
└── README.md                 | This file
```
## Usage

### Prerequisites (used versions)
1. Linux (Ubuntu 18.04.4 LTS)
2. VirtualBox (6.0.18)
3. Minikube (v1.7.3)
4. Kubectl (tested with v1.17.3; same version of Kubernetes)
5. Docker (19.03.6)
6. Python3 (3.6.9)
7. Helm3 (v3.1.1)

### Development and deployment

#### Running locally

1. Initialize environment:

        cd app_one # or app_two
        make initenv

2. Run locally:

        make rundev
   
4. Run locally with Gunicorn:

        make rungunicorn

4. Run tests:

        make test

#### Deployment to Minikube

##### Setup environment

 1. Start minikube:

        minikube start --kubernetes-version v1.17.3 --vm-driver=virtualbox

 3. Switch to minikube's docker:

        eval $(minikube -p minikube docker-env)

##### Build and release

4. Build docker image:

        cd app_one
        make build

5. Create a release, i.e. update version in helm chart, build docker image and tag it:

        make VERSION=0.1.1 release
    
    Make sure to change the version to something different, comparing to what is deployed
    at particular moment. Otherwise, the docker image will not get updated.

5. Deploy, i.e. upgrade or install helm chart:

        make deploy

6. Do same for app_two, i.e.:

        cd app_two
        make VERSION=0.1.1 release
        make deploy

#### Access application deployed in minikube

         export NODE_PORT=$(kubectl get \
         --namespace default \
         -o jsonpath="{.spec.ports[0].nodePort}" services app-two)
         export NODE_IP=$(kubectl get nodes \
         --namespace default \
         -o jsonpath="{.items[0].status.addresses[0].address}")
         curl http://$NODE_IP:$NODE_PORT
         
