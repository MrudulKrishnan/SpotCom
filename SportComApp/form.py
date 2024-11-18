from django.forms import ModelForm

from SportComApp.models import *

# ///////////////////////////////////////// ADMIN //////////////////////////////////////////

class ReplyForm(ModelForm):
    class Meta:
        model = ComplaintTable
        fields = ['Reply']

# ///////////////////////////////////////// RESTAURANT //////////////////////////////////////

class RestaurantRegForm(ModelForm):
    class Meta:
        model = RestaurantTable
        fields = ['RestaurantName', 'Image', 'Place', 'Phone', 'Email', 'Type']

class LoginForm(ModelForm):
    class Meta:
        model = LoginTable
        fields = ['username', 'password']

class RestaurantGalleryForm(ModelForm):
    class Meta:
        model = RestaurantGalleryTable
        fields = ['Image', 'Features']       

class DescriptionForm(ModelForm):
    class Meta:
        model = RestaurantDescriptionTable
        fields = ['History', 'Features']
         
class FacilityForm(ModelForm):
    class Meta:
        model = RestaurantFacilityTable
        fields = ['Details', 'Facility', 'Status']
        
class OfferForm(ModelForm):
    class Meta:
        model = RestaurantOfferTable
        fields = ['OfferName', 'Image', 'Details', 'StartingTime', 'endingTime']

class MenuForm(ModelForm):
    class Meta:
        model = RestaurantMenuTable
        fields = ['FoodName', 'Type', 'Details', 'Image', 'Category']

# ///////////////////////////////////////// RESORT //////////////////////////////////////

class ResortRegForm(ModelForm):
    class Meta:
        model = ResortTable
        fields = ['ResortName','OwnerName', 'Image', 'Address', 'Phone', 'Email', 'Type']

class ResortGalleryForm(ModelForm):
    class Meta:
        model = ResortGalleryTable
        fields = ['Image', 'Features']       

class ResortDescriptionForm(ModelForm):
    class Meta:
        model = ResortDescriptionTable
        fields = ['History', 'Features']

class ResortFacilityForm(ModelForm):
    class Meta:
        model = ResortFacilityTable
        fields = ['Details', 'Facility', 'Status']
        
class ResortOfferForm(ModelForm):
    class Meta:
        model = ResortOfferTable
        fields = ['OfferName', 'Image', 'Details', 'StartingTime', 'endingTime']

class ResortMenuForm(ModelForm):
    class Meta:
        model = ResortMenuTable
        fields = ['FoodName', 'Type', 'Details', 'Image', 'Category']


