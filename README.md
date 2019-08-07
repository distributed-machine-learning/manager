# Manager

Manager node for the cluster. Runs the following things:
* Apache Spark (manager mode)

## Requirements
* Docker
* Docker Compose

## To run

```bash
docker-compose -f worker/docker-compose.yml up
```

That's it, now you have the manager node running.