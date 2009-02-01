from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import fiveruns.dash.django.version

setup(
  name = "fiveruns.dash.django",
  version = ".".join(str(s) for s in fiveruns.dash.django.version.info),
  description = "FiveRuns Dash recipe for Django, packaged as an Django App",
  author = "FiveRuns Development Team",
  author_email = "dev@fiveruns.com",
  url = "http://dash.fiveruns.com",
  packages = find_packages(exclude = "tests"),
  install_requires = ['fiveruns.dash', 'python-aspects >= 1.3'],
  license = 'MIT',
  dependency_links = [
    # Pypi only has python-aspects-1.1 as of 2009-01-19, need 1.3
    'http://www.cs.tut.fi/~ask/aspects/python-aspects-1.3.tar.gz'
  ],
  namespace_packages = ['fiveruns', 'fiveruns.dash'],
  keywords = "monitoring performance production metrics logging django"
)
