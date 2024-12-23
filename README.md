```
docker-compose up --build 
curl http://localhost:5000/users
curl -X POST http://localhost:5000/users      -H "Content-Type: application/json"      -d '{"name": "Vadim", "email": "vadim@example.com"}'
curl -X POST http://localhost:5000/users      -H "Content-Type: application/json"      -d '{"name": "Irina", "email": "irina@example.com"}'
curl http://localhost:5000/users
Press CTRL+C to quit
docker-compose up
curl http://localhost:5000/users
```
