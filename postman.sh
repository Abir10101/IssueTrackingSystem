curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test8",
    "password": "test1",
    "name":"test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test1",
    "password": "test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/logout' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODcyMjIwNDgsImlhdCI6MTY4NzEzNTY0OCwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJvaTVaQ2tSTnRTU2FMQSIsImV4cGlyeSI6IjE2ODcyMDIyNDgifQ.qpNmdAcQHD-kAxLLCpXwM5hRX5zBNpMHaUZDWTZ1tV8"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODcyMjMyNzQsImlhdCI6MTY4NzEzNjg3NCwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODcyMDM0NzQifQ.t2jmfJ_m4cBte-dPKPGpqcNc_nDxRzqYyG11zBN3zE8'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc0ODExNTMsImlhdCI6MTY4NzM5NDc1Mywic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc0NjEzNTMifQ.fyipv9T5hnKyPvsp1-nBbAYmDu_Zs4KGldRmuxXRLNI' \
--data-raw '{
    "code":"vfd-9966",
    "description": "wqq",
    "status":"pending"
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
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc0ODExNTMsImlhdCI6MTY4NzM5NDc1Mywic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc0NjEzNTMifQ.fyipv9T5hnKyPvsp1-nBbAYmDu_Zs4KGldRmuxXRLNI' \
--data-raw '{
    "ticket_id": 3,
    "name":"b-1235",
    "status": "not_live"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25
}'
