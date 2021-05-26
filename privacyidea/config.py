# The realm, where users are allowed to login as administrators
SUPERUSER_REALM = ["super", "administrators"]
# Your database
SQLALCHEMY_DATABASE_URI = "sqlite:////home/adrian/Developments/keycloak-example/venv-privacyidea/lib/python3.8/site-packages/data.sqlite"
# This is used to encrypt the token data and token passwords
PI_ENCFILE = "/home/adrian/Developments/keycloak-example/venv-privacyidea/lib/python3.8/site-packages/enckey"
# This is used to sign the audit log
PI_AUDIT_KEY_PRIVATE = "/home/adrian/Developments/keycloak-example/venv-privacyidea/lib/python3.8/site-packages/private.pem"
PI_AUDIT_KEY_PUBLIC = "/home/adrian/Developments/keycloak-example/venv-privacyidea/lib/python3.8/site-packages/public.pem"
# PI_AUDIT_MODULE = <python audit module>
# PI_AUDIT_SQL_URI = <special audit log DB uri>
# PI_LOGFILE = '....'
# PI_LOGLEVEL = 20
# PI_INIT_CHECK_HOOK = 'your.module.function'
# PI_CSS = '/location/of/theme.css'
# PI_UI_DEACTIVATED = True
PI_PEPPER = "KI3K5yWeKJnxvZSfgZN_JTf9"
SECRET_KEY = "6fTxYr2LGzjVCAUC1sdHJvnj"
