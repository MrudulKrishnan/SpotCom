from rest_framework.serializers import ModelSerializer

from SportComApp.models import *
class UserSerializer(ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['Name', 'Image', 'Age', 'Gender', 'Address', 'Phone', 'Email']

class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginTable
        fields = ['username', 'password']

# //////////////////////////////////// USER /////////////////////////////////////////////

class RestaurantSeralizer(ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ['RestaurantName', 'Image', 'Place', 'Phone', 'Email']
       
class ResortSeralizer(ModelSerializer):
    class Meta:
        model = ResortTable
        fields = ['ResortName', 'Image', 'Address', 'Phone', 'Email']
       
class PhotoShootSeralizer(ModelSerializer):
    class Meta:
        model = PhotoShootTable
        fields = ['SpotName', 'Description', 'Image', 'Latitude', 'Longitude', 'EntryTime', 'ExitTime', 'Status']
       
class AmalgamationSeralizer(ModelSerializer):
    class Meta:
        model = AmalgamationTable
        fields = ['Name', 'Place', 'Phone', 'Email', 'Image']
       
class ParkingSpotSeralizer(ModelSerializer):
    class Meta:
        model = ParkingSpotTable
        fields = ['AreaName', 'Latitude', 'Longitude', 'NoParking', 'Status']
       
class ViewPointSeralizer(ModelSerializer):
    class Meta:
        model = ViewPointTable
        fields = ['ViewPoint', 'Image', 'Details', 'Latitude', 'Longitude']

class FestivalSeralizer(ModelSerializer):
    class Meta:
        model = FestivalTable
        fields = ['FestivalName', 'Image', 'Details', 'StartingTime', 'endingTime', 'Latitude', 'Longitude']

class RestaurantRatingSerializer(ModelSerializer):
    class Meta:
        model = RestaurantRatingTable
        fields = ['USER', 'RESTAURANT', 'Feedback', 'Rating', 'Date']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['complaint', 'reply', 'USER'] 
       

