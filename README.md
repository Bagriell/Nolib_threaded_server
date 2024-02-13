# Technical test Airddm

## commands

- run proxy and servers:    
`docker-compose up`


- send request to server with payload:  
```
curl -X POST \
  http://localhost:8000/event \
  -H 'Content-Type: application/json' \
  -d '{
    "properties": {
        "resourceType": "customer",
        "resourceId": 25,
        "eventType": "resourceHasBeenCreated",
        "triggeredAt": "2018-11-13T20:20:39+00:00",
        "triggeredBy": "server-25"
    }
}'
```

## strategy explanation

I chose multithreading over multiprocessing because of the nature of the task we want to optimize.

Other possibility could be divide server task by operation: 
- one handle logs file
- one handle db
- last handle SMTP

## improvements

- Websocket instead of Http between proxy and servers
- more robust data validation with a clean serializer class
- more granularity on error handling
- custom exceptions
- better architecture with modules
- security checks before proxy and between proxy and servers
- authentification system
