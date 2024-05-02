from flask_appbuilder.security.manager import AUTH_OAUTH

SECRET_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxxxxxxxxxxx@192.168.1.109/sss'


# Enable OAuth authentication
AUTH_TYPE = AUTH_OAUTH
LOGOUT_REDIRECT_URL='http://192.168.1.109:8080/realms/howard/protocol/openid-connect/logout'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Gamma'
# OAuth provider configuration for Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'azure',
        'icon': 'fa-windows',
        'token_key': 'access_token',  # Keycloak uses 'access_token' for the access token
        'remote_app': {
            'client_id': 'f9d76a69-004d-4d38-8f81-c1497fa75c76',
            'client_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            'client_kwargs': {
                'scope': 'openid',
                'resource': 'client_id'
            },
            "request_token_url": None,
            "access_token_url": "https://login.microsoftonline.com/f4e74d0e-8ecc-4eca-a26b-6242b9e01092/oauth2/token",
            "jwks_uri": "https://login.microsoftonline.com/common/discovery/v2.0/keys",
            "authorize_url": "https://login.microsoftonline.com/f4e74d0e-8ecc-4eca-a26b-6242b9e01092/oauth2/authorize",
        },
    }
    ]
