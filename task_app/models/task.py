from django.db import models
from task_app.models.user import User


class Task(models.Model):
    STATUS_CHOICE = [("P", "Pendente"), ("C", "Concluída")]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="P")
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tarefas")

    def __str__(self):
        return self.title
