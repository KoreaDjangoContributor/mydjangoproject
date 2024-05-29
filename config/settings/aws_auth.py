import boto3, json
from botocore.exceptions import ClientError


rds_secret_name = "rds-secrets"
django_secret_name = "django-secrets"
region_name = "your-region-name"

session = boto3.Session(
        aws_access_key_id="your-access-key-id",
        aws_secret_access_key="your-secret-access-key",
        region_name=region_name,
)
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

try:
    get_dbsecret_value_response = client.get_secret_value(
        SecretId=rds_secret_name
    )
except ClientError as e:
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e

try:
    get_djsecret_value_response = client.get_secret_value(
        SecretId=django_secret_name
    )
except ClientError as e:
    # For a list of exceptions thrown, see
    # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    raise e

rds_secrets = json.loads(get_dbsecret_value_response["SecretString"])
django_secrets = json.loads(get_djsecret_value_response["SecretString"])

db_user = rds_secrets['username']
db_password = rds_secrets['password']

SECRET_KEY = django_secrets['django_secret_key']
db_engine = django_secrets['db_engine']
db_name = django_secrets['db_name']
db_host = django_secrets['db_host']
db_port = django_secrets['db_port']
