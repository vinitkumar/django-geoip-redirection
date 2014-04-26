try:
    from django.conf.urls import patterns, include
except ImportError:
    from django.conf.urls.defaults import patterns, include


urlpatterns = patterns(
    "",
    (r"^", include("django_geoip_redirection.urls")),
)
