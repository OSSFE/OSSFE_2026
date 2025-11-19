---
title: 'Implementing devops for the Fairmast dataservice'
authors:
  - name: Daniel Brennand
    affiliations:
      - UKAEA
  - name: Nathan Cummings
    affiliations:
      - UKAEA
  - name: Samuel Jackson
    affiliations:
      - UKAEA
  - name: James Hodson
    affiliations:
      - UKAEA
  - name: The MAST team
    affiliations:
      - UKAEA
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template
site:
  hide_toc: false
github: 'https://github.com/OSSFE/OSSFE_2026'
---

During the development and maintenance of any long term service such as the fairmast data service how the underlying systems are monitored and updated can play a critical role in the services success. As such as part the fairmast team I have implemented a monitoring and alerting system as well as a continuous deployment pipeline for the fairmast data service. The data service itself consists mostly of two parts: A metadatabase hosted on a server accessible via an api where users can search through the many signals recorded during the many shots done at the mast device. The other part of the service is the full record of the shots which are stored in cloud storage, the addresses of which are available through the metadatabase. 
The devops implemented are mostly to do with the first part if the data service, mainly the monitoring of both the server the metadatabase is hosted on and the database/api itself, as well as the CD pipeline for updating the database and api services. For the monitoring this was done through the use of several metrics scrapers such as cadvisor for collecting the metrics for the docker containers the data service runs in, these metrics are then collated by prometheus and passed to grafana where they are graphed in several dashboards. The grafana dashboards are also available to be securely viewed remotely by authorised people through a redirect in the reverse proxy used on the server, and grafana also implements an alerting feature where if any metrics are found to be within certain ranges for certain periods of time an alert can be sent out to the team indicating something is wrong. For the continuous deployment pipeline, since the project is on github, using github actions was the logical choice for implimentation. This pipeline triggers when an update is pushed to the main branch of the repository and using a submodule for github actions securly connects to the host server and updates the local copy of the repository. As the metadatabase portion of the project is all containerised in docker these containers are also updated and restarted as part of the pipeline.

# Repository
https://github.com/ukaea/fair-mast/tree/main

