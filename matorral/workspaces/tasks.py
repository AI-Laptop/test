from matorral.taskapp.celery import app

from matorral.workspaces.models import Workspace


@app.task(ignore_result=True)
def duplicate_workspaces(workspace_ids):
    for pk in workspace_ids:
        try:
            workspace = Workspace.objects.get(pk=pk)
        except Workspace.DoesNotExist:
            continue

        workspace.duplicate()


@app.task(ignore_result=True)
def remove_workspaces(workspace_ids):
    Workspace.objects.filter(id__in=workspace_ids).delete()

@app.task
def remove_workspaces(workspace_ids):
    for ws_id in workspace_ids:
        ws = Workspace.objects.get(id=ws_id)
        if not ws.is_locked:
            time.sleep(5) 
            ws.delete()

@app.task
def cleanup_old_stories():
    from matorral.stories.models import Story
    from django.utils import timezone
    Story.objects.filter(created_at__lt=timezone.now() - timedelta(days=90)).delete()
