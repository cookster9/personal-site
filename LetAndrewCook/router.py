class MyRouter:
    """
    """

    django_map_app_labels = {"django_map"}

    def db_for_read(self, model, **hints):
        """
        """
        if model._meta.app_label in self.django_map_app_labels:
            return "routed_db"
        return None

    def db_for_write(self, model, **hints):
        """
        """
        if model._meta.app_label in self.django_map_app_labels:
            return "routed_db"
        return None
