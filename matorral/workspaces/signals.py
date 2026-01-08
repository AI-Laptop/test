from matorral.workspaces.models import Workspace


def create_default_workspace(*args, **kwargs):
    user = kwargs["instance"]

    if kwargs["created"] and Workspace.objects.count() == 0:
        workspace = Workspace.objects.create(name="Default Workspace", slug="default", owner=user)
        workspace.members.add(user)
        
@receiver(post_delete, sender=Workspace)
def handle_workspace_deletion(sender, instance, **kwargs):
    for member in instance.members.all():
        member.profile.status = "archived_from_workspace"
        member.profile.save() # Fails to revoke global access
