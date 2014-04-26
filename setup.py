import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Vinit Kumar",
    author_email="vinit.kumar@changer.nl",
    description="GeoIP based redirection middleware",
    name="django_geoip_redirection",
    long_description=read("README.md"),
    version=__import__("django_geoip_redirection").__version__,
    url="http://django_geoip_redirection.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    tests_require=[
        "Django>=1.4",
    ],
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
