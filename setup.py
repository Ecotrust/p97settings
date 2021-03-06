import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme: 
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='p97settings',
    version='0.0.1',
    packages=['p97settings'],
    include_package_data=True,
    license='TBD',
    description='Point97 Django Settings Helper',
    long_description=README,
    url='http://www.pointnineseven.com/path/to/opensource/info',
    author='Point97, LLC',
    author_email='developers@pointnineseven.com',
    classifiers=[
        'Environment :: Web Development',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: TBD',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
