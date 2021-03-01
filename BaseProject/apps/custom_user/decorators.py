from django.contrib.auth.mixins import PermissionRequiredMixin


class AllowedUsersView(PermissionRequiredMixin):
    allowed_roles = ["admin"]

    def has_permission(self):
        """
        Validate if user who send request ar in allowed groups
        """
        authorized = False
        groups = self.request.user.groups.all()
        for group in groups:
            if group.name in self.allowed_roles:
                authorized = True

        return authorized