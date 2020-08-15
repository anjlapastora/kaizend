from IPython import embed

class Source(object):
    def __init__(self):
        self.queries  = []

    def query(self, query_string):
        self.queries.append(query_string)
        return self

    def perform(self):
        filters = ' && '.join(self.queries)
        raw_sql_query = f'SELECT * FROM sources WHERE {filters}'
        
        if self.sort:
            raw_sql_query += f"ORDER BY {self.sort}"
        return(raw_sql_query)




def main():
    source = Source()
    source.query("FOOD == APPLE").query("COLOR == RED").perform()


if __name__ == "__main__":
    main()

