""" AppConf """


from django.apps import AppConfig


class RestFrameworkMaterialConfig(AppConfig):
    """ App configuration for the app """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_framework_material'
