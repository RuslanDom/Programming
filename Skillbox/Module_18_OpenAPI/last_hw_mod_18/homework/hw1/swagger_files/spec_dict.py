get_author_dict = {
    'tags': ['Authors'],
    'responses': {
        '200': {
            'description': 'Success get all authors',
            'schema': {
                'type': 'array',
                'items': {'$ref': '#/definitions/Author'}
            }
        }
    }
}

add_author_dict = {
    'tags': ['Authors'],
    'parameters':
        [
           {'in': 'body', 'name': 'new_author_data', 'type': 'string',
            'schema': {'type': 'object', '$ref': '#/definitions/Author'}},
        ],
        'responses': {
           '201': {
               'description': 'Success add author',
               'schema': {'type': 'object', '$ref': '#/definitions/Author'}
           }
        }
    }

get_author_by_id_dict = {
    'tags': ['Authors/id'],
    'responses': {
        '200': {
            'description': 'Success get author by id',
            'schema': {'type': 'object', '$ref': '#/definitions/Author'}
        }
    }
}

delete_author_by_id_dict = {
    'tags': ['Authors/id'],
    'responses': {
        '204': {
            'description': 'Success delete author by id',
            'schema': {}
        }
    }
}





