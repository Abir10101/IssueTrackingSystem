curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"abirmoulick.vawsum@gmail.com",
    "password": "test1",
    "name":"test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"test10",
    "password": "test1"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/users/logout' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODgwMTQ3MzIsImlhdCI6MTY4NzkyODMzMiwic3ViIjoidGVzdDEwIiwic2VjcmV0IjoibUZtOHpRanIwT3MwRFEiLCJleHBpcnkiOiIxNjg3OTk0OTMyIn0.MwBw7F0un00mNda1RPZo05IKA8vaC-AuOQqZQ0KFF_Q"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk2MjE2NjQsImlhdCI6MTcxOTUzNTI2NCwic3ViIjoiYWJpcm1vdWxpY2s5OThAZ21haWwuY29tIiwic2VjcmV0IjoiMEpJZmJVcHVyWElqT2ciLCJleHBpcnkiOiIxNzE5NjIxNjY0In0.cBONQ7wG4S8_-iHF8wsa9v40klykfTe01DVzaBaVjTU'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/ticket/6666' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc3NDk5MDIsImlhdCI6MTY4NzY2MzUwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc3MzAxMDIifQ.E8bkdZcQBd2QZxkpQRdjKVjd0V28e0ZhVj5Aj174bWo'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTk2MjE2NjQsImlhdCI6MTcxOTUzNTI2NCwic3ViIjoiYWJpcm1vdWxpY2s5OThAZ21haWwuY29tIiwic2VjcmV0IjoiMEpJZmJVcHVyWElqT2ciLCJleHBpcnkiOiIxNzE5NjIxNjY0In0.cBONQ7wG4S8_-iHF8wsa9v40klykfTe01DVzaBaVjTU' \
--data-raw '{
    "code":"6666",
    "description": "wqq",
    "status":"pending"
}'


curl -w "%{http_code}\n" --location --request PATCH 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc3NDk5MDIsImlhdCI6MTY4NzY2MzUwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc3MzAxMDIifQ.E8bkdZcQBd2QZxkpQRdjKVjd0V28e0ZhVj5Aj174bWo' \
--data-raw '{
    "ticket_code": 9666,
    "new_code":"6666",
    "new_description": "asdf",
    "new_status":"done"
}'


curl -w "%{http_code}\n" --location --request DELETE 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc5MTY0MDIsImlhdCI6MTY4NzgzMDAwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc4OTY2MDIifQ.3lvDEGf2pg04TDXfnmPF0hfq0gPOcyh2YHYkhwVVwyo' \
--data-raw '{
    "code":"6666"
}'


curl -w "%{http_code}\n" --location --request POST 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc5MTY0MDIsImlhdCI6MTY4NzgzMDAwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc4OTY2MDIifQ.3lvDEGf2pg04TDXfnmPF0hfq0gPOcyh2YHYkhwVVwyo' \
--data-raw '{
    "ticket_code": 9966,
    "name":"b-1111",
    "status": "not_live"
}'


curl -w "%{http_code}\n" --location --request GET 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDc3MzQ2MTksImlhdCI6MTcwNzY0ODIxOSwic3ViIjoiYWJpcm1vdWxpY2s5OTk5OEBnbWFpbC5jb20iLCJzZWNyZXQiOiJlWl9QdHMzNjE0eVB0ZyIsImV4cGlyeSI6IjE3MDc3MTQ4MTkifQ._DGjgO3W6n-akQDbFYHAwevQDPIyIifBePwqcEVJmYI' \
--data-raw '{
    "ticket_code": 6666
}'


curl -w "%{http_code}\n" --location --request PATCH 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc5MTY0MDIsImlhdCI6MTY4NzgzMDAwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc4OTY2MDIifQ.3lvDEGf2pg04TDXfnmPF0hfq0gPOcyh2YHYkhwVVwyo' \
--data-raw '{
    "old_name":"b-1111",
    "new_name":"b-1112",
    "new_status": "live"
}'


curl -w "%{http_code}\n" --location --request DELETE 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODc5MTY0MDIsImlhdCI6MTY4NzgzMDAwMiwic3ViIjoidGVzdDEiLCJzZWNyZXQiOiJ6R1pENVpjNVB2YUxKUSIsImV4cGlyeSI6IjE2ODc4OTY2MDIifQ.3lvDEGf2pg04TDXfnmPF0hfq0gPOcyh2YHYkhwVVwyo' \
--data-raw '{
    "branch_name":"b-1112"
}'
