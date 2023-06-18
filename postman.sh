curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test7",
    "password": "test1",
    "name":"test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test1",
    "password": "test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/logout' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzE1MDM4MjAsImlhdCI6MTY3MTQxNzQyMCwic3ViIjoxLCJzZWNyZXQiOiI5RGlpTGl6RnFYaVVMUSIsImV4cGlyeSI6IjE2NzE1MDM4MjAifQ.s1lkIqZvOSenlOWRqQaNJQE58oF4xQoFzcMFf8gtWGM"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzE1MDM4MjAsImlhdCI6MTY3MTQxNzQyMCwic3ViIjoxLCJzZWNyZXQiOiI5RGlpTGl6RnFYaVVMUSIsImV4cGlyeSI6IjE2NzE1MDM4MjAifQ.s1lkIqZvOSenlOWRqQaNJQE58oF4xQoFzcMFf8gtWGM'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzE1MDM4MjAsImlhdCI6MTY3MTQxNzQyMCwic3ViIjoxLCJzZWNyZXQiOiI5RGlpTGl6RnFYaVVMUSIsImV4cGlyeSI6IjE2NzE1MDM4MjAifQ.s1lkIqZvOSenlOWRqQaNJQE58oF4xQoFzcMFf8gtWGM' \
--data-raw '{
    "user_id":"1",
    "code":"vfd-134",
    "description": "asdf",
    "status":"done"
}'


curl -w "%{http_code}\n" --location --request PATCH 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25,
    "code":"vfd-12334",
    "description": "asdf",
    "status":"done"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25,
    "name":"b-1234",
    "status": "live"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25
}'
