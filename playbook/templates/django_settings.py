{% set application_installed_apps = ['django_extensions', 'cedatest_control'] %}

{% extends "django_settings_default.py" %}

{% block security_settings %}
{% if debug_mode %}
DEBUG = True
{% else %}
DEBUG = False
# Security settings
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
ALLOWED_HOSTS = ['{{ server_name }}']
{% endif %}
{% endblock %}

{% block middleware %}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    {% for middleware in application_middleware %}
    '{{ middleware }}',
    {% endfor %}
]
{% endblock %}

{% block internationalisation_settings %}
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False
{% endblock %}

{% block email_settings %}
# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'test@test.ceda.ac.uk'
{% endblock %}

{% block application_settings %}

# Put your custom settings here.
ALLOWED_HOSTS=["{{ server_name }}",
               {% if internal_server_name is defined %}"{{ internal_server_name }}"{% endif %}]

{% endblock %}
