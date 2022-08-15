from django.db import connection, reset_queries
import functools



def query_counter(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        import time
        reset_queries()

        start_queries = len(connection.queries)

        start = time.time()
        result = func(*args, **kwargs)
        time = time.time() - start

        queries = len(connection.queries) - start_queries

        print(f'[INFO] Function {func.__name__} made {queries} queries. Worked {time:.2f}sec.')
        return result
    return inner_func