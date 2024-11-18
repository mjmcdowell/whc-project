# WHC Project

## Description
This repository contains a very simple example project of a Kubernetes deployable Flask API application for querying a dataset from the World Heritage Convention. This could theoretically be expanded upon or integrated with other search components, but the goal here is to test creating API functionality while setting up a new Kubernetes environment within a limited timeframe.

## API

### Endpoints

* `/query` `GET` - The query endpoint expects a `unique_number` parameter and responds with the data for that row.
    * *Example Query: curl "http://127.0.0.1:32638/query?unique_number=230"*
    * This could be expanded upon to query for other, more interesting parameters, but is intended to be simple for the sake of this demonstration
* `/health` `GET` - The health endpoint is included for Kubernetes health probes and will return a `200` if the service is operating on the pod
    * *Example Query: curl "http://127.0.0.1:32638/health"*
    * This could be expanded upon to perform a more rigorous examination of the pod's running state

## Infra

### Kubernetes

These configurations are fairly simple as an initial set of manifests. 
* In the deployment we are monitoring `liveness` and `readiness` using the `/health` endpoint that has been created as part of the API. 
* We have setup a `podDisruptionBudget` to ensure we have service availability during maintenance.
* A `NodePort` service has been created for use on our local testing environment.

**TO DO** - Additional enhancements that should be implemented
* Setup a `PersistentVolumeClaim` to host the data CSV - This volume should be shared across all replicas of the service so we are using the same data for each. This data can be split out from the container so it can be updated as needed separately from normal deployments, or implement a job to do this.
* Setup Anti-Affinity rules - Setup anti-affinity rules for a production deployment that will ensure replicas of our service will be run on different worker nodes. This lowers the impact of any potential worker issues and improves resiliency.
* Setup Helm Chart - Create a helm chart for our service. This will allow us to easily set deployment values, templating etc. and create an immutable artifact during the build process.
* Setup Ingress - If needed, setup an NGINX Ingress for the service to map endpoints externally.
* Setup Tilt - Tilt is a toolkit that allows us to quickly iterate our application code and Kubernetes service on a developer workstation. Setting up a Tiltfile will allow us to increase productivity and efficiency with our project development.