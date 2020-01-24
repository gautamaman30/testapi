Simple REST API that can fetch bank details, using the data given in the API’s
query parameters

Used Python,Django and PostgreSQL.

curl script to test some requests:

1. Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
   e.g. /api/branches/autocomplete/?q=RTGS&limit=3&offset=0
   	
		curl -k 
		-H "Content-Type: application/json" 
		"https://simplebankapi.herokuapp.com/api/branches/autocomplete/?q=RTGS&limit=3&offset=1"
    
    
   
2. Search API to return possible matches across all columns and all rows , ordered by IFSC code (ascending order) with limit and offset.
   e.g. /api/branches?q=Bangalore&limit=4&offset=0

  
		curl -k 
		-H "Content-Type: application/json" 
		"https://simplebankapi.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=2"


