import json

from todos.todo_model import TodoModel
import todos.config


def todo_list(event, context):
    # fetch all todos from the database
    results = TodoModel.scan()

    # create a response
    return {'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': todos.config.aws['allow-origin'],
            },
            'body': json.dumps({'items': [dict(result) for result in results]})}
