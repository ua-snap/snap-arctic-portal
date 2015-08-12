import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='snap-arctic-portal',
    version='0.0.1',
    author='Scenarios Network for Alaska + Arctic Planning',
    url='https://github.com/ua-snap/snap-arctic-portal',
    download_url="git@github.com:ua-snap/snap-arctic-portal.git",
    description="SNAP Arctic Portal extensions to GeoNode.",
    long_description=open(os.path.join(here, 'README.md')).read(),
    license='See LICENSE file.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 1 - Planning',
                 'Programming Language :: Python :: 2.7'],
)
