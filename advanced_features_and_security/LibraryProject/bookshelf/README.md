# Permissions and Groups Setup

## Custom Permissions

The `Book` model defines custom permissions: `can_view`, `can_create`, `can_edit`, and `can_delete`. These control who can view, create, edit, or delete book entries.

## Groups

Set up groups like Editors, Viewers, and Admins in Django admin. Assign the relevant permissions to each group:
- Editors: `can_create`, `can_edit`
- Viewers: `can_view`
- Admins: All permissions

## Enforcing Permissions

Views for creating, editing, and deleting books use the `@permission_required` decorator to enforce permissions. Users must belong to a group with the required permission to access these views.

## Testing

Assign users to groups in Django admin and verify access to views. Only users with the correct permissions will be able to perform the corresponding actions.
