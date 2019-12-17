"""
Django settings for smallboard project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from distutils.util import strtobool
from django.core.management.utils import get_random_secret_key

import dotenv
import logging
import os

logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    logger.warn('No DJANGO_SECRET_KEY set. Generating random secret key')
    SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.environ.get('DEBUG', 'True')))

# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'smallboard.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'puzzles',
    'accounts',
    'hunts',
    'answers',
    'social_django',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'smallboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['smallboard/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'smallboard.context_processors.google_auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'smallboard.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [os.path.join(BASE_DIR, "smallboard/static")]
STATICFILES_STORAGE = 'whitenoise.django.CompressedManifestStaticFilesStorage'

# User login
AUTH_USER_MODEL = 'accounts.Puzzler'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=False)

ACTIVE_HUNT_ID = os.environ.get("ACTIVE_HUNT_ID", '')
if not ACTIVE_HUNT_ID:
    logger.warn("No ACTIVE_HUNT_ID set. Links may not work properly.")

# Google Drive API
GOOGLE_DRIVE_API_AUTHN_INFO = None
if not 'GOOGLE_DRIVE_API_PRIVATE_KEY' in os.environ:
    logger.warn('No Google Drive API key found in environment. Automatic sheets creation disabled.')
else:
    GOOGLE_DRIVE_API_AUTHN_INFO = {
      "type": "service_account",
      "project_id": "smallboard-test-260001",
      "private_key_id": "ca6bf4b1c0db884c0a0cf490839c375f63dab3af",
      "private_key": os.environ['GOOGLE_DRIVE_API_PRIVATE_KEY'].replace('\\n', '\n'),
      "client_email": "smallboard-test@smallboard-test-260001.iam.gserviceaccount.com",
      "client_id": "108658192634408271921",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/smallboard-test%40smallboard-test-260001.iam.gserviceaccount.com"
    }
    GOOGLE_DRIVE_PERMISSIONS_SCOPES = ['https://www.googleapis.com/auth/drive']
    GOOGLE_DRIVE_HUNT_FOLDER_ID = os.environ.get('GOOGLE_DRIVE_HUNT_FOLDER_ID', None)
    GOOGLE_SHEETS_TEMPLATE_FILE_ID = os.environ.get('GOOGLE_SHEETS_TEMPLATE_FILE_ID', None)

    if not GOOGLE_DRIVE_HUNT_FOLDER_ID or not GOOGLE_SHEETS_TEMPLATE_FILE_ID:
        GOOGLE_DRIVE_API_AUTHN_INFO = None
        logger.warn('GOOGLE_DRIVE_HUNT_FOLDER_ID or GOOGLE_SHEETS_TEMPLATE_FILE_ID not set. '
                    'Automatic sheets creation disabled.')

# Slack API
SLACK_BASE_URL = os.environ.get("SLACK_BASE_URL", None)
if SLACK_BASE_URL:
    SLACK_BASE_URL = SLACK_BASE_URL.rstrip('/')
else:
    logger.warn('No SLACK_BASE_URL configured. Slack links will not work.')

# TODO(erwa): Validate that SLACK_API_TOKEN works for SLACK_BASE_URL workspace.
SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN", None)
if not SLACK_API_TOKEN:
    logger.warn('No SLACK_API_TOKEN environment variable set. All Slack operations will be no-ops.')

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# smallboard client id
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1059136102866-hlifpp6736kpk2v2di16i1ftnf6ofkfg.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', None)
if not SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET:
    logger.warn('No SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET environment variable set. Google login will be disabled.')

from google_drive_lib.google_drive_client import GoogleDriveClient

google_drive_client = GoogleDriveClient.getInstance()
if google_drive_client:
    SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS = google_drive_client.get_file_user_emails(GOOGLE_DRIVE_HUNT_FOLDER_ID)
    print('Whitelisted emails:', SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS)
else:
    logger.warn('Google Drive integration not set up. All emails will be accepted.')

# Taggit Overrides
TAGGIT_TAGS_FROM_STRING = 'puzzles.utils.to_tag'
