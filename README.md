# rest-framework-material

Redesign of the browsable api of Django REST Framework using MD Bootstrap

## Get started

To get started with rest-framework-material:

Install the package:

```bash
pip install rest-framework-material
```

Add `rest_framework_material` to `INSTALLED_APPS` setting, make sure that it's before `rest_framework`

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework_material',
    'rest_framework',
    ...
]
```

Include `rest_framework.urls` in your project URLConf

```python
# urls.py

...
from django.urls import path, include

urlpatterns = [
    ...
    path('auth/', include('rest_framework.urls')),
    ...
]
```

I hope you that you find this useful.
