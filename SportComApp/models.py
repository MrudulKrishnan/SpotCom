import json
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE_CHOICES = {
    ("ADMIN", "admin"),
    ("USER", "user"),
    ("RESTOURANT", "restaurant"),
    ("RESORT", "resort"),
    ("TOURIST", "tourist")

}


class LoginTable(AbstractUser):
    # username
    # password
    # first_name
    # last_name
    # email
    is_active = models.CharField(max_length=20, null=True, blank=True, default=True)
    user_type = models.CharField(max_length=20, null=True, choices=USER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='login_table', blank=True,
        help_text='The groups this user belongs to.', verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='login_table',
        blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')


class Token(models.Model):  
    key = models.CharField(max_length=50, unique=True)
    user = models.OneToOneField(
        LoginTable,
        related_name="auth_tokens",
        on_delete=models.CASCADE,
        verbose_name="user",
        unique=True,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    session_dict = models.TextField(null=False, default="{}")

    def generate_key(self):
        """Generate a random key for the token."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=40))

    def read_session(self):
        """Read session data from the session_dict attribute."""
        try:
            self.data_dict = json.loads(self.session_dict)
        except json.JSONDecodeError:
            self.data_dict = {}

    def write_back(self):
        """Write session data back to the session_dict attribute."""
        self.session_dict = json.dumps(self.data_dict)
        self.save()

    def get(self, key, default=None):
        """Get a value from the session data."""
        self.read_session()
        return self.data_dict.get(key, default)

    def set(self, key, value, save=True):
        """Set a value in the session data."""
        self.read_session()
        self.data_dict[key] = value
        if save:
            self.write_back()

    def update_session(self, tdict, save=True, clear=False):
        """Update session data with the provided dictionary."""
        self.read_session()
        if clear:
            self.data_dict = tdict
        else:
            self.data_dict.update(tdict)
        if save:
            self.write_back()

    def save(self, *args, **kwargs):
        """Override the save method to generate a key if not provided."""
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def str(self):
        """Return a string representation of the token."""
        return str(self.user) if self.user else str(self.id)


class TouristTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Address = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class AmalgamationTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Place = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    Image = models.FileField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class ParkingSpotTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    AreaName = models.CharField(max_length=30, null=True, blank=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)    
    NoParking = models.IntegerField(null=True, blank=True)    
    Status = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  

class PhotoShootTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    SpotName = models.CharField(max_length=30, null=True, blank=True) 
    Description = models.CharField(max_length=300, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)       
    EntryTime = models.TimeField(null=True, blank=True)       
    ExitTime = models.TimeField(null=True, blank=True)       
    Status = models.CharField(max_length=30, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  

class ResortTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    ResortName = models.CharField(max_length=30, null=True, blank=True) 
    OwnerName = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Address = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True)  
    Type = models.CharField(max_length=50, blank=True, null=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)    

class RestaurantTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    RestaurantName = models.CharField(max_length=30, null=True, blank=True) 
    Image = models.FileField(blank=True, null=True)   
    Place = models.CharField(max_length=100, null=True, blank=True)    
    Phone = models.BigIntegerField(null=True, blank=True)       
    Email = models.CharField(max_length=30, null=True, blank=True) 
    Type = models.CharField(max_length=30, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    Image = models.FileField(blank=True, null=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=10, blank=True, null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Email = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ComplaintTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    Complaint = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Reply = models.CharField(max_length=300,null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)      
          
class FeedbackTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)     
          
class ResortDescriptionTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    History = models.CharField(max_length=500, blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortGalleryTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Image = models.FileField(blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class ResortFacilityTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Facility = models.CharField(max_length=300, blank=True, null=True)   
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Status = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortMenuTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    FoodName = models.CharField(max_length=50, blank=True, null=True)   
    Type = models.CharField(max_length=30, null=True, blank=True)    
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Category = models.CharField(max_length=50, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          

class ResortOfferTable(models.Model):
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    OfferName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ResortRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    RESORT = models.ForeignKey(ResortTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 


class RestaurantDescriptionTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    History = models.CharField(max_length=500, blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class RestaurantGalleryTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Image = models.FileField(blank=True, null=True)   
    Features = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class RestaurantFacilityTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Facility = models.CharField(max_length=300, blank=True, null=True)   
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Status = models.CharField(max_length=500, null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          
class RestaurantMenuTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    FoodName = models.CharField(max_length=50, blank=True, null=True)   
    Type = models.CharField(max_length=30, null=True, blank=True)    
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Category = models.CharField(max_length=50, null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          

class RestaurantOfferTable(models.Model):
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    OfferName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True)   
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 

class RestaurantRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    RESTAURANT = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 

class FestivalTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    FestivalName = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    StartingTime = models.DateTimeField(null=True, blank=True)    
    endingTime = models.DateTimeField(null=True, blank=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)  
          

class ViewPointTable(models.Model):
    TOURIST = models.ForeignKey(TouristTable, on_delete=models.CASCADE)
    ViewPoint = models.CharField(max_length=100, blank=True, null=True)   
    Image = models.FileField(null=True, blank=True)    
    Details = models.CharField(max_length=500, null=True, blank=True)    
    Latitude = models.FloatField(null=True, blank=True)    
    Longitude = models.FloatField(null=True, blank=True) 
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)   
          
class ViewPointGalleryTable(models.Model):
    POINT = models.ForeignKey(ViewPointTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)
    
class FestivalGalleryTable(models.Model):
    FESTIVAL = models.ForeignKey(FestivalTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class AmalgamationGalleryTable(models.Model):
    AMALGAMATION = models.ForeignKey(AmalgamationTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class PhotoShootGalleryTable(models.Model):
    SHOOT = models.ForeignKey(PhotoShootTable, on_delete=models.CASCADE)
    Image = models.FileField(null=True, blank=True)

class FestivalRatingTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE) 
    FESTIVAL = models.ForeignKey(FestivalTable, on_delete=models.CASCADE) 
    Feedback = models.CharField(max_length=300, blank=True, null=True)   
    Date = models.DateTimeField(auto_now_add=True)    
    Rating = models.FloatField(null=True, blank=True)  
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) 


class ParkingRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    PARKING = models.ForeignKey(ParkingSpotTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Review = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class ViewPointRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    POINT = models.ForeignKey(ViewPointTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Review = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class AmalgamationRatingReviewTable(models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    AMALGAMATION = models.ForeignKey(AmalgamationTable, on_delete=models.CASCADE)
    Rating = models.FloatField(null=True, blank=True)
    Review = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

