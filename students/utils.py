
def format_records(lst):
    if len(lst) == 0:
        return 'Empty recordset.'

    return '<br>'.join(str(el) for el in lst)
