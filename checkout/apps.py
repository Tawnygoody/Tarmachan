from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    """
    Overide the ready method and import the signals
    module so that the update_on_save and update_on_delete
    will be called after an OrderLineItem model is saved
    or deleted
    """
    def ready(self):
        import checkout.signals
