from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta



class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    # fee = models.PositiveIntegerField(max_length=40)
    # Screenshot_of_Payment = models.ImageField(upload_to='images/',null=True)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    Image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=18)
class IssuedBook(models.Model):
    enrollment=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment


class displaybook(models.Model):
    name=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    Image = models.ImageField(upload_to='images/',null=True)


# class cart(models.Model):


#     active = models.BooleanField(default=True)
   
#     name=models.CharField(max_length=30)



# class removefromcart(models.Model):
#     name=models.CharField(max_length=30)