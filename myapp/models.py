from django.db import models

class ToDo(models.Model):
    icon = models.URLField()
    url = models.URLField()
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title 
    
class CompletedToDo(models.Model):
    date = models.DateField()
    is_done = models.BooleanField(default=False)
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo.title} done on {self.date}"

