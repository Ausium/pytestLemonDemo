from unittest import result
import jsonpath
resp = {'Data': {'access_token': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTU3MjExMjMsImlhdCI6MTY1MzkwNjcyMywibmJmIjoxNjUzOTA2NzIzLCJzdWIiOiI4ZGUyOGJlZi1lZWUwLTQzZjEtYjUwNC1kMWUxZDBmMDY1MzQifQ.SzsHsx27CruJ6QCxpObanTeHe417RNAfMRkmIJYK3KsHEiknucSGd0Mauq91p5kxbQjZQlspALqBCKW6ebhIsA', 'token_type': 'Bearer', 'expires_at': 1655721123}}
result1 = jsonpath.jsonpath("$..token_type",resp)