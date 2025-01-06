from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=20)

class Gallery(models.Model):
    Image = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    date=models.DateField()

class Adminprofile(models.Model):
    CompanyName = models.CharField(max_length=100)
    OwnerName = models.CharField(max_length=500)
    Logo = models.CharField(max_length=100)
    Email = models.CharField(max_length=500)
    LicenceId = models.CharField(max_length=100)
    Place = models.CharField(max_length=500)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=500)
    Pincode = models.BigIntegerField()
    PhoneNumber = models.BigIntegerField()

class Service(models.Model):
    RoomType = models.CharField(max_length=100,default="")
    Image = models.CharField(max_length=100)
    Details = models.CharField(max_length=500)
    Squarefeet = models.CharField(max_length=100)
    Price = models.BigIntegerField()

class User(models.Model):
    UserName = models.CharField(max_length=100)
    Email = models.CharField(max_length=500)
    ProfilePhoto = models.CharField(max_length=100)
    Phone = models.BigIntegerField()
    Address = models.CharField(max_length=100)
    District = models.CharField(max_length=500)
    State = models.CharField(max_length=100)
    Pincode = models.BigIntegerField()
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)



class Usercustom(models.Model):
    SERVICE = models.ForeignKey(Service, on_delete=models.CASCADE)
    Description = models.CharField(max_length=500)
    PriceDetails = models.CharField(max_length=500)
    Refferencephoto = models.CharField(max_length=100)
    Date = models.DateField()
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default="pending")
    amount = models.CharField(max_length=50,default="pending")
    paystatus = models.CharField(max_length=50,default='pending')


class Userequest (models.Model):
    SERVICE = models.ForeignKey(Service, on_delete=models.CASCADE)
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    Date = models.DateField()
    status = models.CharField(max_length=50)
    paystatus = models.CharField(max_length=50,default='pending')



class Review(models.Model):
        Review = models.CharField(max_length=100)
        USER = models.ForeignKey(User,on_delete=models.CASCADE)
        Date = models.DateField()
class Usercunstompayment(models.Model):
    Amount = models.BigIntegerField()
    Date = models.DateField()
    USERCUSTOMREQUEST= models.ForeignKey(Usercustom, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

class Userservicepayment(models.Model):
    Amount = models.BigIntegerField()
    PriceDetails = models.CharField(max_length=500)
    Date = models.DateField()
    REQUEST= models.ForeignKey(Userequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)





