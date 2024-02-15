# Technical test Airddm

I Hope the code will suit your requirements ! 🤞

## commands

- run proxy and servers:    
`docker-compose up`


- send request to server with payload(linux):  
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

- send request to server with payload(windows):
```
$body = @{
    "properties" = @{
        "resourceType" = "customer"
        "resourceId" = 25
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

## note
- I used chatgpt to speed up things like docstring.
- I took some time to do the interview test in order to test things and because i learnt some things interesting. 
- smtp is hardly testable without using a configured gmail account
