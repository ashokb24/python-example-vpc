import os


def hello(event, context):
    env_variable = os.environ['FIRST_NAME']
    print('Environment Variable Value ' + env_variable)
