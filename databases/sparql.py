from SPARQLWrapper import SPARQLWrapper, JSON

# Set the Fuseki endpoint URL
fuseki_endpoint = "http://localhost:3030/dataset/query"


class Sparql:
    def __init__(self):
        self.sparql_reader = SPARQLWrapper(fuseki_endpoint)
        self.sparql_reader.setReturnFormat(JSON)

    def get_courses(self) -> list[str]:
        _query = """
            PREFIX ex: <http://example.org/ontology#>
            SELECT ?course ?courseName
            WHERE {
              ?course a ex:Course ;
                      ex:name ?courseName .
            }
        """
        self.sparql_reader.setQuery(_query)
        results = self.sparql_reader.query().convert()
        return [result['courseName']['value'] for result in results['results']['bindings']]


    def get_classes(self) -> list[str]:
        _query = """
            PREFIX ex: <http://example.org/ontology#>
            SELECT ?course ?courseName
            WHERE {
              ?course a ex:Course ;
                      ex:name ?courseName .
            }
        """
        self.sparql_reader.setQuery(_query)
        results = self.sparql_reader.query().convert()
        return [result['courseName']['value'] for result in results['results']['bindings']]
