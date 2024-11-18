from django.urls import path


from SportComApp import views
from SportComApp.views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
    path('login', LoginPage.as_view(), name="login_page"),
    path('logout', Logout.as_view(), name="logout"),
    path('admin_dashboard', AdminDashboard.as_view(), name="admin_dashboard"),

    # ////////////////////////////////// ADMIN /////////////////////////////////////////
    
    path('view_user', ViewUser.as_view(), name="view_user"),
    path('manage_restaurant', ManageRestaurant.as_view(), name="manage_restaurant"),
    path('restaurant_delete/<int:restaurant_id>', RestaurantDelete.as_view(), name="restaurant_delete"),
    path('manage_resort', ManageResort.as_view(), name="manage_resort"),
    path('resort_delete/<int:resort_id>', ResortDelete.as_view(), name="resort_delete"),
    path('manage_amalgamation', ManageAmalgamation.as_view(), name="manage_amalgamation"),
    path('amalgamation_delete/<int:amalgamation_id>', AmalgamationDelete.as_view(), name="amalgamation_delete"),
    path('manage_parkinspot', ManageParkingSpot.as_view(), name="manage_parkinspot"),
    path('parking_delete/<int:parking_id>', ParkingSpotDelete.as_view(), name="parking_delete"),
    path('manage_photoshoot_area', ManagePhotoShootArea.as_view(), name="manage_photoshoot_area"),
    path('photoshoot_delete/<int:photoshoot_id>', PhotoShootDelete.as_view(), name="photoshoot_delete"),
    path('photoshoot_map/<int:photoshoot_id>', PhotoShootDelete.as_view(), name="photoshoot_map"),
    path('view_feedback', ViewFeedback.as_view(), name="view_feedback"),
    path('view_complaint', ViewCompalint.as_view(), name="view_complaint"),
    path('view_tourists', ViewTourist.as_view(), name="view_tourists"),
    path('parking_map/<int:parking_id>', ParkMapView.as_view(), name='park_map'),
    path('photoshoot_map/<int:shooting_id>', PhotoShootMap.as_view(), name='photoshoot_map'),
    path('view_restaurant_gallery/<int:restaurant_id>', ViewRestaurantGallery.as_view(), name='view_restaurant_gallery'),


    # /////////////////////////////// RESTAURANT //////////////////////////////////////////////////////

    path('restaurant_dashboard', RestaurantDashboard.as_view(), name="restaurant_dashboard"),
    path('restaurant_registration', RestaurantRegistration.as_view(), name="restaurant_registration"),
    path('manage_gallery', ManageGallery.as_view(), name="manage_gallery"),
    path('restaurant_image_delete/<int:image_id>', RestaurantImageDelete.as_view(), name="restaurant_image_delete"),
    path('manage_description', ManageDescription.as_view(), name="manage_description"),
    path('manage_facility', ManageFacility.as_view(), name="manage_facility"),
    path('edit_facility/<int:fecility_id>', EditFacility.as_view(), name="edit_facility"),
    path('delete_facility/<int:fecility_id>', DeleteFacility.as_view(), name="delete_facility"),
    path('manage_offers', ManageOffers.as_view(), name="manage_offers"),
    path('edit_offer/<int:offer_id>', EditOffer.as_view(), name="edit_offer"),
    path('delete_offer/<int:offer_id>', DeleteOffer.as_view(), name="delete_offer"),
    path('manage_menu', ManageMenu.as_view(), name="manage_menu"),
    path('edit_menu/<int:menu_id>', EditMenu.as_view(), name="edit_menu"),
    path('delete_menu/<int:menu_id>', DeleteMenu.as_view(), name="delete_menu"),
    path('view_review', ViewReview.as_view(), name="view_review"),


    # /////////////////////////////// RESORT //////////////////////////////////////////////////////

    path('resort_registration', ResortRegistration.as_view(), name="resort_registration"),
    path('resort_dashboard', ResortDashboard.as_view(), name="resort_dashboard"),
    path('manage_resort_gallery', ManageResortGallery.as_view(), name="manage_resort_gallery"),
    path('resort_image_delete/<int:image_id>', ResortImageDelete.as_view(), name="resort_image_delete"),
    path('manage_resort_description', ManageResortDescription.as_view(), name="manage_resort_description"),
    path('manage_resort_facility', ManageResortFacility.as_view(), name="manage_resort_facility"),
    path('edit_resort_facility/<int:fecility_id>', EditResortFacility.as_view(), name="edit_reort_facility"),
    path('delete_resort_facility/<int:fecility_id>', DeleteResortFacility.as_view(), name="edit_reort_facility"),
    path('manage_resort_offers', ManageResortOffers.as_view(), name="manage_resort_offers"),
    path('edit_resort_offers/<int:offer_id>', EditResortOffers.as_view(), name="edit_resort_offers"),
    path('delete_resort_offers/<int:offer_id>', DeleteResortOffers.as_view(), name="delete_resort_offers"),
    path('manage_resort_menu', ManageResortMenu.as_view(), name="manage_resort_menu"),
    path('edit_resort_menu/<int:menu_id>', EditResortMenu.as_view(), name="edit_resort_menu"),
    path('delete_resort_menu/<int:menu_id>', DeleteResortMenu.as_view(), name="delete_resort_menu"),
    path('view_resort_review', ViewResortReview.as_view(), name="view_resort_review"),

]