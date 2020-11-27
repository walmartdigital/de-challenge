# Data Engineer - Challenge
This is the Basic Challenge for Data Engineers.

For this Challenge we want you do the next things:
- A microservice in Java/Scala with Maven.
- A Data Model for the specific data.
- A Deployment in Kubernetes for your microservice.

## Microservice
The microservices must received the datasets & brings a few things:
- The top 10 best games for each console/company.
- The worst 10 games for each console/company.
- The top 10 best games for all consoles.
- The worst 10 games for all consoles.

``` sh 
# We will run this command:
mvn clean package
```

## Data Model
The Data Model must be in 3FN. 
Save the model in the DataModel folder in both formats (datamodel format & JPG/PNG ).
```
Use any tool, but please tell us the tool you choose & why.
```

## Deployment for Kubernetes 

Save all the YAML's you think we must use to deploy & we will run in our own Minikube.

We use Skaffold for this step. 

If you want to know more about Skaffold project follow this link: https://skaffold.dev/


# Concerns
- You can create a new README for specific comments, please don't name README.md
- We want to see if you know how to do TDD & Clean Coding, so USE IT!.
- Save all the changes in a new branch with your name.


## Datasets
We use the data from TopGames provided by Metascore.

* [Kaggle: Metacritic reviewed games since 2000](https://www.kaggle.com/destring/metacritic-reviewed-games-since-2000)
