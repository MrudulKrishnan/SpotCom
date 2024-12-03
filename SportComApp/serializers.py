
from rest_framework.serializers import ModelSerializer, ImageField 
from rest_framework import serializers

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

class RestaurantOfferSerializer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)

    Image = ImageField(use_url=True)  # This ensures the image URL is returned
    class Meta:
        model = RestaurantOfferTable
        fields = ['Image', 'restaurant_id']

       
class RestaurantSeralizer(ModelSerializer):
    class Meta:
        model = RestaurantTable
        fields = ['id', 'RestaurantName', 'Image', 'Place', 'Phone', 'Email']
       
class RestaurantDescriptionSeralizer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)

    class Meta:
        model = RestaurantDescriptionTable
        fields = ['History', 'Features', 'restaurant_id']
       
class RestaurantGallerySeralizer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    class Meta:
        model = RestaurantGalleryTable
        fields = ['Image', 'Features', 'restaurant_id']
       
class RestaurantFacilitySeralizer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    class Meta:
        model = RestaurantFacilityTable
        fields = ['Facility', 'Details', 'Status', 'restaurant_id']
       
class RestaurantMenuSeralizer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    class Meta:
        model = RestaurantMenuTable
        fields = ['FoodName', 'Type', 'Image', 'Details', 'Category', 'restaurant_id']
       
class RestaurantOfferSeralizer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    class Meta:
        model = RestaurantOfferTable
        fields = ['OfferName', 'Image', 'Details', 'StartingTime', 'endingTime', 'restaurant_id']


class RestaurantRatingSerializer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    class Meta:
        model = RestaurantRatingTable
        fields = ['USER', 'RESTAURANT', 'Feedback', 'Rating', 'Date', 'restaurant_id']

     
class ResortSeralizer(ModelSerializer):
    class Meta:
        model = ResortTable
        fields = ['ResortName', 'Image', 'Address', 'Phone', 'Email']


class ResortOfferSerializer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESORT.id', read_only=True)

    Image = ImageField(use_url=True)  # This ensures the image URL is returned
    class Meta:
        model = ResortOfferTable
        fields = ['Image', 'restaurant_id']

       
class ResortSeralizer(ModelSerializer):
    class Meta:
        model = ResortTable
        fields = ['id', 'ResortName', 'Image', 'Address', 'Phone', 'Email']
       
class ResortDescriptionSeralizer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)

    class Meta:
        model = ResortDescriptionTable
        fields = ['History', 'Features', 'resort_id']
       
class ResortGallerySeralizer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    class Meta:
        model = ResortGalleryTable
        fields = ['Image', 'Features', 'resort_id']
       
class ResortFacilitySeralizer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    class Meta:
        model = ResortFacilityTable
        fields = ['Facility', 'Details', 'Status', 'resort_id']
       
class ResortMenuSeralizer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    class Meta:
        model = ResortMenuTable
        fields = ['FoodName', 'Type', 'Image', 'Details', 'Category', 'resort_id']
       
class ResortOfferSeralizer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    class Meta:
        model = ResortOfferTable
        fields = ['OfferName', 'Image', 'Details', 'StartingTime', 'endingTime', 'resort_id']



class PhotoShootSeralizer(ModelSerializer):
    class Meta:
        model = PhotoShootTable
        fields = ['id','SpotName', 'Description', 'Image', 'Latitude', 'Longitude', 'EntryTime', 'ExitTime', 'Status']


class PhotShootGallerySeralizer(ModelSerializer):
    shoot_id = serializers.IntegerField(source='SHOOT.id', read_only=True)
    class Meta:
        model = PhotoShootTable
        fields = ['Image', 'shoot_id']


class AmalgamationSeralizer(ModelSerializer):
    class Meta:
        model = AmalgamationTable
        fields = ['id', 'Name', 'Place', 'Phone', 'Email', 'Image']


class AmalgamtionGallerySeralizer(ModelSerializer):
    amalgamation_id = serializers.IntegerField(source='AMALGAMATION.id', read_only=True)
    class Meta:
        model = AmalgamationGalleryTable
        fields = ['Image', 'amalgamation_id']


class ParkingSpotSeralizer(ModelSerializer):
    class Meta:
        model = ParkingSpotTable
        fields = ['AreaName', 'Latitude', 'Longitude', 'NoParking', 'Status']
       
class ViewPointSeralizer(ModelSerializer):
    class Meta:
        model = ViewPointTable
        fields = ['ViewPoint', 'Image', 'Details', 'Latitude', 'Longitude', 'id']

class ViewPointGallerySeralizer(ModelSerializer):
    view_point_id = serializers.IntegerField(source='POINT.id', read_only=True)
    class Meta:
        model = ViewPointGalleryTable
        fields = ['Image', 'view_point_id']


class FestivalSeralizer(ModelSerializer):
    class Meta:
        model = FestivalTable
        fields = ['id', 'FestivalName', 'Image', 'Details', 'StartingTime', 'endingTime', 'Latitude', 'Longitude']

class FestivalGallerySeralizer(ModelSerializer):
    festival_id = serializers.IntegerField(source='FESTIVAL.id', read_only=True)
    class Meta:
        model = FestivalGalleryTable
        fields = ['Image', 'festival_id']

class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['complaint', 'reply', 'USER'] 

class ResortRatingSerializer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    class Meta:
        model = ResortRatingTable
        fields = ['USER', 'Feedback', 'Rating', 'Date', 'resort_id']

class ResortReviewSerializer(ModelSerializer):
    resort_id = serializers.IntegerField(source='RESORT.id', read_only=True)
    Name = serializers.CharField(source='USER.Name', read_only=True)
    Image = serializers.FileField(source='USER.Image', read_only=True)
    class Meta:
        model = ResortRatingTable
        fields = ['Feedback', 'Rating', 'Date', 'Name', 'Image', 'resort_id']     

class RestaurantReviewSerializer(ModelSerializer):
    restaurant_id = serializers.IntegerField(source='RESTAURANT.id', read_only=True)
    Name = serializers.CharField(source='USER.Name', read_only=True)
    Image = serializers.FileField(source='USER.Image', read_only=True)
    class Meta:
        model = ResortRatingTable
        fields = ['Feedback', 'Rating', 'Date', 'Name', 'Image', 'restaurant_id']     

class FestivalRatingSeralizer(ModelSerializer):
    Name = serializers.CharField(source='USER.Name', read_only=True)
    Image = serializers.FileField(source='USER.Image', read_only=True)
    class Meta:
        model = FestivalRatingTable
        fields = ['Rating', 'Feedback', 'Name', 'Image', 'Date'] 
       
class ViewPointRatingSeralizer(ModelSerializer):
    Name = serializers.CharField(source='USER.Name', read_only=True)
    Image = serializers.FileField(source='USER.Image', read_only=True)
    point_id = serializers.IntegerField(source='POINT.id', read_only=True)
    class Meta:
        model = ViewPointRatingReviewTable
        fields = ['Rating', 'Review', 'point_id', 'Name', 'Image'] 
       
class AmalgamationRatingSeralizer(ModelSerializer):
    point_id = serializers.IntegerField(source='AMALGAMATION.id', read_only=True)
    class Meta:
        model = AmalgamationRatingReviewTable
        fields = ['Rating', 'Review', 'point_id'] 
       

