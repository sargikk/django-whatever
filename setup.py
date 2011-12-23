from os import path
import codecs
from setuptools import setup

read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()

setup(
    name='django-whatever',
    version='0.2.1dev',
    description='Unobtrusive test models creation for django.',
    long_description=read(path.join(path.dirname(__file__), 'README.rst')),
    author='Ilya Baryshev',
    author_email='baryshev@gmail.com',
    url='http://github.com/coagulant/django-whatever',
    packages=['django_any', 'django_any.contrib', 'django_any.tests'],
    include_package_data=True,
    test_suite = "tests.manage",
    zip_safe=False,
    license='MIT License',
    platforms = ['any'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

