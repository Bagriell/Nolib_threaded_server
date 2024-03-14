# No lib http server with threads

Server that listen for data in /event and write data to sqlite, logfile and send by smtp.

## commands

- run dispatcher and servers:    
`docker-compose up --build`


- send request to server with payload(linux):  
```
curl -X POST \
  http://localhost:8000/event \
  -H 'Content-Type: application/json' \
  -d '{
    "properties": {
        "resourceType": "customer",
        "resourceId": 15,
        "eventType": "resourceHasBeenCreated",
        "triggeredAt": "2018-11-13T20:20:39+00:00",
        "triggeredBy": "server-25"
    }
}'
```

- send request to server with payload(windows):
```
$body = @{
    "properties" = @{
        "resourceType" = "customer"
        "resourceId" = 15
        "eventType" = "resourceHasBeenCreated"
        "triggeredAt" = "2018-11-13T20:20:39+00:00"
        "triggeredBy" = "server-25"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/event" -Method Post -ContentType "application/json" -Body $body
```

- send multiple requests in different threads, use provided script:  
`python test_services.py`

## multiple backend strategy explanation

I chose multithreading over multiprocessing because of the nature of the task we want to optimize (IO operations).

Other possibility could be divide server tasks by operation: 
- one handle logs file
- one handle db
- last handle SMTP

## improvements

- more robust data validation
- more granularity on error handling and custom exceptions
- better architecture with modules
- security checks before proxy and between proxy and servers
- fix pylint tears such as logger formatting optimization
- better smtp
- auth system
- cleaner networking in docker
