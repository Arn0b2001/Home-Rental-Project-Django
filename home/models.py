from django.db import models
import uuid
import json

# Create your models here.
class Signup(models.Model):

    email = models.CharField(max_length=50)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default = 'customer')
    owned_property = models.IntegerField(default = 0)

class PropertyDetails(models.Model):
    ownwer_email = models.CharField(max_length=50)
    p_id = models.CharField(max_length=50, primary_key = True)
    property_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    det_loc = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50)
    guest_num = models.IntegerField(default = 0)
    price = models.IntegerField()
    types = models.CharField(max_length=50)
    view = models.CharField(max_length=50)
    bed = models.CharField(max_length=50)
    common_space = models.CharField(max_length=50)
    tv = models.BooleanField()
    smoking = models.BooleanField()
    air_condition = models.BooleanField()
    bathroom = models.BooleanField()
    water_heater = models.BooleanField()
    parking = models.BooleanField()
    wifi = models.BooleanField()
    breakfast = models.BooleanField()
    verified = models.BooleanField(default = False)
    p_image1 = models.ImageField(null= True, upload_to='images/')
    p_image2 = models.ImageField(null= True, upload_to='images/')
    p_image3 = models.ImageField(null= True, upload_to='images/')
    p_image4 = models.ImageField(null= True, upload_to='images/')
    document = models.BooleanField(default = False)
    doc1 = models.FileField(upload_to='documents/')
    doc2 = models.FileField(upload_to='documents/')
    doc3 = models.FileField(upload_to='documents/')
    video = models.FileField(upload_to='videos/')
    voucher = models.IntegerField(default = 0)
    income = models.IntegerField(default = 0)

class Booking(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    property = models.CharField(max_length=50)
    property_name = models.CharField(max_length=50, default = '')
    customer = models.CharField(max_length=50)
    price = models.IntegerField()
    neg_price = models.IntegerField(default = 0)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default = 'hold')
    payment_id = models.CharField(max_length=50, blank = True)
    complaint = models.BooleanField(default = False)

class Review(models.Model):
    property = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    review = models.TextField()

class Complaint(models.Model):
    complaint_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    about = models.CharField(max_length=100)
    text = models.TextField()
    book_id = models.CharField(max_length=50, default = '')
    status = models.CharField(max_length=50, default = 'close')
    def set_text(self, text_list):
        self.text = json.dumps(text_list)

    def get_text(self):
        return json.loads(self.text)

    # Optionally, you can override save method to ensure text is always serialized
    def save(self, *args, **kwargs):
        if not isinstance(self.text, str):
            self.text = json.dumps(self.text)
        super(Complaint, self).save(*args, **kwargs)


class Blacklist(models.Model): 
    email =  models.CharField(max_length=50)

