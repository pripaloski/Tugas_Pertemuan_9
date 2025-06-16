from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def is_member(self, user_id):
        return CourseMember.objects.filter(course=self, user_id=user_id).exists()

class CourseMember(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    roles = models.CharField(max_length=50)

    def __str__(self):
        return f"Member {self.user_id} of {self.course}"
