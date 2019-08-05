# WEATHER SERVICE

## Service Breakdown

This monorepo consists of 3 services:
* temperature-service (django application)  
* weather-service (mock service)  
* maps-service  (google api ambassador)

## Environment Variables

It is required to have a google maps api key as an environment variable before starting the application.  

https://developers.google.com/maps/documentation/javascript/get-api-key

``` MAPS_KEY=<your-key-here> ```

## Start Project

The only dependencies needed are [docker](https://docs.docker.com/install/#server) and [docker-compose](https://docs.docker.com/compose/install/).

To build and start app run:

1.  ``` MAPS_KEY=<your-key-here> docker-compose up```

This will serve:  
* temperature-service at 127.0.0.1:8080
* weather-service at 127.0.0.1:8001
* maps-service at 127.0.0.1:8002

**Note:** ***compose-up will also run the integration tests***

You can also individually build and run each app if you desire:

1. ``` docker build ./<service-directory> -t name:tag ```
2. ```docker run -p <desired-port>:8080 name:tag```


## Install application into Kubernetes
dependencies: [draft](https://github.com/Azure/draft), [helm](https://helm.sh/docs/using_helm/), [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).

1. ``` cd <service-directory> ```
2. ``` draft up ```

## Main Application

The main entry point of the application to get the average temperature is via the temperature-service. 

### Usage

#### Query Parameters

Must specify either **zip_code** or **latitude**  and **longitude**.

**latitude** and **longitude** are validated via google maps so these must be valid coordinates.

Optional filters param: **filters**.

If no filters are specified then it will default to calling all 3 weather services. 

#### Acceptable Filters

* weatherdotcom
* noaa
* accuweather

#### Example Requests

**GET:** http://127.0.0.1:8080/temp?latitude=40.3&longitude=20.2  
**GET:** http://127.0.0.1:8080/temp?zip_code=78757  
**GET:** http://127.0.0.1:8080/temp?zip_code=78757&filters=weatherdotcom&filters=noaa   
**GET:** http://127.0.0.1:8080/temp?latitude=40.3&longitude=20.2&filters=accuweather&filters=noaa  
**GET:** http://127.0.0.1:8080/temp?latitude=40.3&longitude=20.2&filters=noaa  

### Run Tests Stand Alone

These tests excercise the entire suite of api's including google maps.

#### In Docker
1. ``` cd tests ```
2. ``` docker build . -t test  ```
3. ``` docker run test ```

#### Using Node
1. ```cd tests ```
2. ``` npm i ```
3. ``` npm test ```
