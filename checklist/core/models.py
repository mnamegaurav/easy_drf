from django.db import models

# Create your models here.

class CheckList(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class CheckListItem(models.Model):
    text = models.CharField(max_length=250)
    is_checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)