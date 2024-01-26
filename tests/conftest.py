import logging
import time
import sys
from pathlib import Path

import pytest
from xprocess import ProcessStarter

BASE_DIR = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def server(xprocess):
    """
    This fixtures starts the serverless offline server and dynamodb.
    Also logs the serverless offline server output to the console.
    """

    class Starter(ProcessStarter):
        pattern = "Server ready"
        args = [
            "/bin/bash",
            "-c",
            "cd " + str(BASE_DIR) + " && serverless offline start " + "--config serverless.yml",
        ]

    logfile = xprocess.ensure("server", Starter)

    try:
        # Print logs in console
        sys.stderr.flush()
        sys.stdin.flush()
    except Exception:
        ...
    time.sleep(3)

    yield
    with open(str(logfile[1]), "r") as f:
        logging.info(f.read())

    xprocess.getinfo("server").terminate()


@pytest.fixture(scope="session")
def base_url() -> str:
    return "http://localhost:3000"

#
#
# @pytest.fixtures(scope="module")
# def dynamodb(xprocess) -> DynamoDB:
#     """
#     This fixtures starts the dynamodb server only and logs the output to the console.
#     Scope is set to `module` to avoid db clashing with server db - so db only test cases are placed in the same module.
#     """
#
#     class Starter(ProcessStarter):
#         pattern = "DynamoDB - created"
#         args = [
#             "/bin/bash",
#             "-c",
#             "cd " + str(BASE_DIR) + " && serverless dynamodb start --migrate --config serverless-test.yml --sharedDb",
#         ]
#
#     logfile = xprocess.ensure("dynamodb", Starter)
#
#     try:
#         # Print logs in console
#         sys.stderr.flush()
#         sys.stdin.flush()
#     except Exception:
#         ...
#
#     time.sleep(3)
#     yield
#     with open(str(logfile[1]), "r") as f:
#         logger.info(f.read())
#
#     xprocess.getinfo("dynamodb").terminate()
#
#
# def create_todo_app_db(db: DynamoDB):
#     """
#     This function creates the todo app database.
#     """
#     return db.dynamodb_client.create_table(
#         AttributeDefinitions=[
#             {"AttributeName": "id", "AttributeType": "S"},
#             {"AttributeName": "updated_at", "AttributeType": "S"},
#         ],
#         KeySchema=[
#             {"AttributeName": "id", "KeyType": "HASH"},
#             {"AttributeName": "updated_at", "KeyType": "RANGE"},
#         ],
#         TableName=db._table.name,
#         BillingMode="PAY_PER_REQUEST",
#     )
#
#
# @pytest.fixtures(scope="function")
# def clear_db():
#     """
#     This fixtures helps in resetting the database after each test by deleting the table and recreating it.
#     """
#     yield
#     dbs = [
#         DynamoDB(settings.TODO_APP_DB),
#     ]
#     for db in dbs:
#         db.dynamodb_client.delete_table(TableName=db._table.name)
#         match db._table.name:
#             case settings.TODO_APP_DB:
#                 create_todo_app_db(db)
#             case _:
#                 raise ValueError(f"Invalid table name: {db._table.name}")
#         time.sleep(1)