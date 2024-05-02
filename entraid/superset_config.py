from flask_appbuilder.security.manager import AUTH_OAUTH
import os

SECRET_KEY=f'{os.environ["SUPERSET_SECRET_KEY"]}'
SQLALCHEMY_DATABASE_URI = f'mysql://root:{os.environ["mysql_passwd"]}@{os.environ["mysql_host"]}/{os.environ["superset_db"]}'


# Enable OAuth authentication
AUTH_TYPE = AUTH_OAUTH
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Gamma'
# OAuth provider configuration for Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'azure',
        'icon': 'fa-windows',
        'token_key': 'access_token',  # Keycloak uses 'access_token' for the access token
        'remote_app': {
            'client_id': f'{os.environ["client_id"]}',
            'client_secret': f'{os.environ["client_secret"]}',
            'client_kwargs': {
                'scope': 'openid',
                'resource': 'client_id'
            },
            'request_token_url': None,
            'access_token_url': f'https://login.microsoftonline.com/{os.environ["tenant_id"]}/oauth2/token',
            'jwks_uri': 'https://login.microsoftonline.com/common/discovery/v2.0/keys',
            'authorize_url': f'https://login.microsoftonline.com/{os.environ["tenant_id"]}/oauth2/authorize',
        },
    }
    ]
