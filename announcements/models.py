from django.db import models

# Create your models here.
class announcements(models.Model):
    announcement_categories = [
        ('Academic','Academic'),
        ('Events','Events'),
        ('Lost_Found', 'Lost & Found'),
        ('Others','Others'),    

    ]

    title = models.CharField(max_length=256)
    categories = models.CharField(max_length=50 , choices= announcement_categories)
    description = models.TextField()
    post_time = models.DateTimeField()
  
  

    def __str__(self):
        return self.title
    

class comments(models.Model):
    announcement = models.ForeignKey(announcements, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=1000)
    comment_post_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment on {self.announcement.title}"
