from SPARQLWrapper import SPARQLWrapper, JSON

# Set the Fuseki endpoint URL
fuseki_endpoint = "http://localhost:3030/dataset/query"

# Create a SPARQLWrapper object and set the endpoint URL
sparql = SPARQLWrapper(fuseki_endpoint)

# SPARQL query
query = """
PREFIX ex: <http://example.org/ontology#>
SELECT ?course ?courseName
WHERE {
  ?course a ex:Course ;
          ex:name ?courseName .
}
"""

# Set the query string
sparql.setQuery(query)

# Set the query method (GET or POST)
# sparql.setMethod("GET")  # or "POST"

# Set the query format (JSON, XML, etc.)
sparql.setReturnFormat(JSON)

# Execute the query and print the results
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["course"]["value"], result["courseName"]["value"])