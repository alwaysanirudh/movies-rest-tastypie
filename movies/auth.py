from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


# Role Based Authorization. Currently it only filters by superuser parameter.
# TODO: Use user groups to check and authorize
class RoleBasedAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        # Allow Read by all
        return object_list

    def read_detail(self, object_list, bundle):
        # Allow Detail Reads by all
        return True

    def create_list(self, object_list, bundle):
        # Allow only SuperUser to create
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")

        return object_list

    def create_detail(self, object_list, bundle):
        # Allow only SuperUser to create
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")
        return True

    def update_list(self, object_list, bundle):
        # Allow only SuperUser to update
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")

        return object_list

    def update_detail(self, object_list, bundle):
        # Allow only SuperUser to update
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")
        return True

    def delete_list(self, object_list, bundle):
        # Allow only SuperUser to delete
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")
        return object_list

    def delete_detail(self, object_list, bundle):
        # Allow only SuperUser to delete
        if not bundle.request.user.is_superuser:
                raise Unauthorized("You are not allowed to access that resource.")
        return True
