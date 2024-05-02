from flask_appbuilder.security.manager import AUTH_OAUTH

SECRET_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxxxxxxxxxxxxxx@192.168.1.109/sss'


# Enable OAuth authentication
AUTH_TYPE = AUTH_OAUTH
LOGOUT_REDIRECT_URL='http://192.168.1.109:8080/realms/howard/protocol/openid-connect/logout'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Gamma'
# OAuth provider configuration for Keycloak
OAUTH_PROVIDERS = [
    {
        'name': 'keycloak',
        'icon': 'fa-key',
        'token_key': 'access_token',  # Keycloak uses 'access_token' for the access token
        'remote_app': {
            'client_id': 'howard',
            'client_secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxj',
            'client_kwargs': {
                'scope': 'openid profile email',
            },
            'server_metadata_url': 'http://192.168.1.109:8080/realms/howard/.well-known/openid-configuration',
            'api_base_url': 'http://192.168.1.109:8080/realms/howard/protocol/',
        },
    }
    ]
