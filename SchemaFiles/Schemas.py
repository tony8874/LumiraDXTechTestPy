
class Schema:

    ListCategorySchemas = {'type':'array', 'items': [{'type': 'object', 'properties': {'id': {'type': 'integer'}, 'name': {'type': 'string'}}, 'required': ['id', 'name']}]}