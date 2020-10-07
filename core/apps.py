from django.apps import apps, AppConfig
from django.contrib import admin


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields if field.name != "id"]
        super(ListAdminMixin, self).__init__(model, admin_site)


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from . import signals

        models = apps.get_models()
        for model in models:
            # admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
            try:
                # admin.site.register(model, admin_class)
                admin.site.register(model)
            except admin.sites.AlreadyRegistered:
                pass
