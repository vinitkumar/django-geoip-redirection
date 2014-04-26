Django GeoIP Redirection
========================

It is a GeoIP based redirection middleware that redirects the user on basis of
geolocation of the user. It uses Maxmind's free version of geoip database.


Using the middleware
====================

In order to use the middleware include it into your middlewares list in the
settings file:

```python
MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.doc.XViewMiddleware',
  'django.middleware.common.CommonMiddleware',
  # Uncomment the next line for simple clickjacking protection:
  # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'cms.middleware.page.CurrentPageMiddleware',
  'cms.middleware.user.CurrentUserMiddleware',
  'cms.middleware.toolbar.ToolbarMiddleware',
  'cms.middleware.language.LanguageCookieMiddleware',
  'django_geoip_redirection.middleware.LocationMiddleWare',
)
```
And add the `django_geoip_redirection_` to list of INSTALLED APPS:

```python
INSTALLED_APPS = (
  'django_geoip_redirection',
  ....
)
```

You would also need to place the `GeoIP.dat.dat` present inside the data folder to
your project root directory.




Running the Tests
------------------

You can run the tests with via:

```bash
python setup.py test
make test
make all
python runtests.py
```
