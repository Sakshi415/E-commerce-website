from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class mobile_detail(models.Model):
    m_id = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])

    def __str__(self):
        return self.mobile_no


class Feedbackdata(models.Model):
    firstname = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
    comment = models.TextField()

    def __str__(self):
        return self.firstname

