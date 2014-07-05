Django-geo-redirection
========================

![World Map](https://i.cloudup.com/7rf2v_IDxv-2000x2000.png)

GeoIP based redirection is awesome and achieving it isn't too hard either. I wrote this middleware 
to ensure that my website would get redirected properly with regards to the location of the user
accessing the website.


## Usage:

Add the middleware in your settings file:

```python
MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'cms.middleware.language.LanguageCookieMiddleware',
  'django_geoip_redirection.middleware.LocationMiddleWare',
)
```

Also add `django_geoip_redirection_` to INSTALLED APPS:

```python
INSTALLED_APPS = (
  'django_geoip_redirection',
  ....
)
```

## Customization:

```python
# Changet the array for extension as per country you 
# have to support
if request.path[:4] in ["/en/", "/nl/", "/in/"]:
    return None

if 'HTTP_X_FORWARDED_FOR' in request.META:
    request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
ip_address = request.META['REMOTE_ADDR']
# get country name using Maxmind database.
# Now, just match and redirect.
# Likewise, replace the name of country to match and redirect.
country = get_country_request(ip_address)
if country == "India":
    return HttpResponseRedirect('/in/')
elif country == "Netherlands":
    return HttpResponseRedirect('/nl/')
else:
    return HttpResponseRedirect('/en/')
return None

```

You would also need to place the `GeoIP.dat.dat` present inside the data folder to
your project root directory.
