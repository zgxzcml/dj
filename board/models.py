from django.db import models
from acc.models import User
from django.utils import timezone

# Create your models here.f
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="writer")
    content = models.TextField()
    pubdate = models.DateTimeField(default=timezone.now)
    likey = models.ManyToManyField(User, blank=True, related_name="likey")

    def __str__(self):
        return self.subject

    def ishot(self):
        if self.likey.count() > 2:
            return True
        return False


class Reply(models.Model):
    b = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.b}_{self.replyer} 의 댓글"



