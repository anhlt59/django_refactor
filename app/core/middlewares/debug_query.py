from django.db import connection


class QueryCountDebugMiddleware(object):
    """
    This middleware will log the number of queries run
    and the total time taken for each request (with a
    status code of 200). It does not currently support
    multi-database setups.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from django.urls import resolve
        current_url = resolve(request.path_info).url_name
        response = self.get_response(request)
        total_time = 0

        for index, query in enumerate(connection.queries, 1):
            query_time = query.get('time')
            sql_query  = query.get('sql')

            if query_time is None:
                query_time = query.get('duration', 0) / 1000
            total_time += float(query_time)

            print(f"{index}: ({query_time}) {sql_query}")

        print(f"{current_url}: {request.get_raw_uri()}")
        print(f"{len(connection.queries)} queries run, total {total_time} seconds")
        return response
