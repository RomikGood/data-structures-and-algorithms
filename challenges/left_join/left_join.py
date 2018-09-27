def table_join(table_a, table_b):
    output = []
    cache = []

    for key in table_a:
        cache.append(key)
        cache.append(table_a[key])
        if key in table_b:
            cache.append(table_b[key])
        else:
            cache.append('None')
        output.append(cache)
        cache = []

    return output
        

