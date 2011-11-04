Installation
============

To retain backwards compatibility with `django-any`, `django-whatever` package
shares the same namespace, so make sure to remove previous djnago_any
installations if any.

* Install the package with your python package manager::

    pip install django-any

* Add ``'django_any'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        "django_any",
        ...
    )
