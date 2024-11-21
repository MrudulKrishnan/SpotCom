import datetime
import json
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import status
from django.contrib.auth import authenticate, login
from SportComApp.form import *
from SportComApp.models import *
from SportComApp.serializers import *

# Create your views here.

class LoginPage(View):
    templates_name="login.html"
    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        response_dict = {"success": False}
        username = request.POST.get("Username")
        print("username------------------>",username)
        password = request.POST.get("Password")
        print("password------------------>",password)
        user = LoginTable.objects.filter(username=username, is_active="False").first()
        print("active user--------------------------->", user)
        if user:
            response_dict[
                "reason"
            ] = "user is inactive ,pls contact admin."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict.get("reason", "")})
        try:
            login_obj = LoginTable.objects.get(username=username, password=password)
            if login_obj.user_type == "ADMIN":
                return HttpResponse('''<script>alert("welcome to admin home"); window.location="/admin_dashboard"</script>''')
            elif login_obj.user_type == "RESTOURANT":
                request.session['login_id'] = login_obj.id
                return HttpResponse('''<script>alert("welcome to Restaurant home"); window.location="/restaurant_dashboard"</script>''')
            elif login_obj.user_type == "RESORT":
                request.session['login_id'] = login_obj.id
                return HttpResponse('''<script>alert("welcome to Resort home"); window.location="/resort_dashboard"</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid username or password"); window.location="/"</script>''')
        except LoginTable.DoesNotExist:
            response_dict["reason"] = "no account found for this user name,please sign up."
            messages.error(request, response_dict["reason"])
            print(response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict.get("reason", "")})

class Logout(View):
    def get(self, request):
        return redirect('/')
    
class HomePage(View):
    def get(self, request):
        restaurant_obj = RestaurantDescriptionTable.objects.all()
        resort_obj = ResortDescriptionTable.objects.all()
        return render(request, "home.html", {'restaurants': restaurant_obj, 'resorts': resort_obj})
    
class AdminDashboard(View):
    def get(self, request):
        return render(request, "ADMIN/admin_dashboard.html")
    
# ////////////////////////////////////// ADMIN //////////////////////////////////////   

class ViewUser(View):
    def get(self, request):
        users = UserTable.objects.all()
        return render(request, "ADMIN/view_user.html", {'users': users})

class ManageRestaurant(View):
    def get(self, request):
        obj = RestaurantTable.objects.all()
        return render(request, "ADMIN/manage_restaurant.html", {'rest_obj': obj})

class RestaurantDelete(View):
    def get(self, request, restaurant_id):
        obj = LoginTable.objects.get(id=restaurant_id)
        obj.delete()
        return HttpResponse('''<script>alert("Restaurant deleted successfully"); window.location="/manage_restaurant"</script>''')

class ManageResort(View):
    def get(self, request):
        obj =  ResortTable.objects.all()
        return render(request, "ADMIN/manage_resort.html",  {'resort_obj': obj})

class ResortDelete(View):
    def get(self, request, resort_id):
        obj = LoginTable.objects.get(id=resort_id)
        obj.delete()
        return HttpResponse('''<script>alert("Resort deleted successfully"); window.location="/manage_resort"</script>''')

class ManageAmalgamation(View):
    def get(self, request):
        obj  = AmalgamationTable.objects.all()
        return render(request, "ADMIN/manage_amalgamation.html", {"amalgamations": obj})
    
class AmalgamationDelete(View):
    def get(self, request, amalgamation_id):
        obj = AmalgamationTable.objects.get(id=amalgamation_id)
        obj.delete()
        return HttpResponse('''<script>alert("amalgamation deleted successfully"); window.location="/manage_amalgamation"</script>''')

class ManageParkingSpot(View):
    def get(self, request):
        obj = ParkingSpotTable.objects.all()
        return render(request, "ADMIN/manage_parkingspot.html",  {"parking_obj": obj})

class ParkingSpotDelete(View):
    def get(self, request, parking_id):
        obj = ParkingSpotTable.objects.get(id=parking_id)
        obj.delete()
        return HttpResponse('''<script>alert("parking deleted successfully"); window.location="/manage_parkinspot"</script>''')

class ParkMapView(View):
    def get(self, request, parking_id):
        obj = ParkingSpotTable.objects.get(id=parking_id)
        latitude = obj.Latitude  
        longitude = obj.Longitude
        context = {
            'latitude': latitude,
            'longitude': longitude,
        }
        return render(request, 'map.html', context)
    
class ManagePhotoShootArea(View):
    def get(self, request):
        obj = PhotoShootTable.objects.all()
        return render(request, "ADMIN/manage_photoshoot_area.html", {"photoshoot_obj": obj})

class PhotoShootDelete(View):
    def get(self, request, photoshoot_id):
        obj = PhotoShootTable.objects.get(id=photoshoot_id)
        obj.delete()
        return HttpResponse('''<script>alert("photoshoot deleted successfully"); window.location="/manage_photoshoot_area"</script>''')

class PhotoShootMap(View):
    def get(self, request, shooting_id):
        obj = PhotoShootTable.objects.get(id=shooting_id)
        latitude = obj.Latitude  
        longitude = obj.Longitude
        context = {
            'latitude': latitude,
            'longitude': longitude,
        }
        return render(request, 'map.html', context)

class ViewFeedback(View):
    def get(self, request):
        obj = FeedbackTable.objects.all()
        return render(request, "ADMIN/view_feedback.html", {"obj":obj})

class ViewCompalint(View):
    def get(self, request):
        obj = ComplaintTable.objects.all()
        return render(request, "ADMIN/view_complaint.html", {"obj": obj})    
    def post(self,request):
        comp_id = request.POST['id']
        print("---------------->", comp_id)
        comp_obj = ComplaintTable.objects.get(id=comp_id)
        form=ReplyForm(request.POST, instance=comp_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Replied successfully"); window.location="/view_complaint"</script>''')
        
class ViewTourist(View):
    def  get(self, request):
        obj = TouristTable.objects.all()
        return render(request, "ADMIN/view_tourist.html", {"obj": obj})
    
class ViewRestaurantGallery(View):
    def  get(self, request, restaurant_id):
        obj = RestaurantGalleryTable.objects.filter(RESTAURANT_id=restaurant_id)
        return render(request, "ADMIN/gallery.html", {"gallery_images": obj})
    


# //////////////////////////////////// RESTAURANT ///////////////////////////////////////

class RestaurantDashboard(View):
    def get(self, request):
        return render(request, "RESTAURANT/restaurant_dashboard.html")
    
class RestaurantRegistration(View):
    def get(self, request):
        return render(request, "RESTAURANT/restaurant_registration.html")        
    def post(self, request):
        form = RestaurantRegForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant_form = form.save(commit=False)
            Username = request.POST["Username"]
            Password = request.POST["Password"]
            login_obj = LoginTable()
            login_obj.username = Username
            login_obj.password = Password
            login_obj.user_type = "RESTOURANT"
            login_obj.save()
            restaurant_form.LOGIN = login_obj
            restaurant_form.save()
            return HttpResponse('''<script>alert("Registration successful"); window.location="/"</script>''')
            
class ManageGallery(View):
    def get(self, request):
        gallery_obj = RestaurantGalleryTable.objects.filter(RESTAURANT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/manage_gallery.html", {'gallery': gallery_obj})
    def post(self, request):
        form= RestaurantGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restourant_obj = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
            restaurant.RESTAURANT = restourant_obj
            restaurant.save()
            return HttpResponse('''<script>alert("Image added successfully"); window.location="/manage_gallery"</script>''')

class RestaurantImageDelete(View):
    def get(self, request, image_id):
        obj = RestaurantGalleryTable.objects.get(id=image_id)
        obj.delete()
        return HttpResponse('''<script>alert("Image Deleted successfully"); window.location="/manage_gallery"</script>''')

class ManageDescription(View):
    def get(self, request):
        try:
            obj = RestaurantDescriptionTable.objects.get(RESTAURANT__LOGIN_id=request.session['login_id'])
            return render(request, "RESTAURANT/manage_description.html", {'description': obj})
        except:
            return render(request, "RESTAURANT/manage_description.html")
    def post(self, request):
        try:
            restaurant_obj = RestaurantDescriptionTable.objects.get(RESTAURANT__LOGIN_id=request.session['login_id'])
            form =DescriptionForm(request.POST, instance=restaurant_obj)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.RESTAURANT = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
                obj.save()
                return HttpResponse('''<script>alert("Description added successfully"); window.location="/manage_description"</script>''')
        except Exception as e:        
            form =DescriptionForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.RESTAURANT = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
                obj.save()
                return HttpResponse('''<script>alert("Description added successfully"); window.location="/manage_description"</script>''')
    
class ManageFacility(View):
    def get(self, request):
        obj = RestaurantFacilityTable.objects.filter(RESTAURANT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/manage_facility.html",{'facility': obj})
    def post(self, request):
        form = FacilityForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESTAURANT = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Facility added successfully"); window.location="/manage_facility"</script>''')

class EditFacility(View):
    def get(self, request, fecility_id):
        obj = RestaurantFacilityTable.objects.get(id=fecility_id)
        return render(request, "RESTAURANT/edit_facility.html", {'facilities': obj}) 
    def post(self, request, fecility_id):
        facility_obj = RestaurantFacilityTable.objects.get(id=fecility_id)
        form = FacilityForm(request.POST, instance=facility_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Facility edited successfully"); window.location="/manage_facility"</script>''')

class DeleteFacility(View):
    def get(self, request, fecility_id):
        facility_obj = RestaurantFacilityTable.objects.get(id=fecility_id)
        facility_obj.delete()
        return HttpResponse('''<script>alert("Facility Deleted successfully"); window.location="/manage_facility"</script>''')

class ManageOffers(View):
    def get(self, request):
        obj = RestaurantOfferTable.objects.filter(RESTAURANT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/manage_offers.html", {'offers': obj})
    def post(self, request):
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESTAURANT = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Offer added successfully"); window.location="/manage_offers"</script>''')
class EditOffer(View):
    def get(self, request, offer_id):
        obj = RestaurantOfferTable.objects.get(id=offer_id)
        return render(request, "RESTAURANT/edit_offer.html", {'offers': obj, 'StartingTime': obj.StartingTime.strftime('%Y-%m-%d') , 'endingTime': obj.endingTime.strftime('%Y-%m-%d')}) 
    def post(self, request, offer_id):
        offer_obj = RestaurantOfferTable.objects.get(id=offer_id)
        form = OfferForm(request.POST, request.FILES, instance=offer_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Offer edited successfully"); window.location="/manage_offers"</script>''')

class DeleteOffer(View):
    def get(self, request, offer_id):
        offer_obj = RestaurantOfferTable.objects.get(id=offer_id)
        offer_obj.delete()
        return HttpResponse('''<script>alert("Offer Deleted successfully"); window.location="/manage_offers"</script>''')

class ManageMenu(View):
    def get(self, request):
        obj = RestaurantMenuTable.objects.filter(RESTAURANT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/manage_menu.html",{'menus': obj})
    def post(self, request):
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESTAURANT = RestaurantTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Menu added successfully"); window.location="/manage_menu"</script>''')

class EditMenu(View):
    def get(self, request, menu_id):
        obj = RestaurantMenuTable.objects.get(id=menu_id)
        return render(request, "RESTAURANT/edit_menu.html", {'menu': obj}) 
    def post(self, request, menu_id):
        menu_obj = RestaurantMenuTable.objects.get(id=menu_id)
        form = MenuForm(request.POST, request.FILES, instance=menu_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Menu edited successfully"); window.location="/manage_menu"</script>''')

class DeleteMenu(View):
    def get(self, request, menu_id):
        menu_obj = RestaurantMenuTable.objects.get(id=menu_id)
        menu_obj.delete()
        return HttpResponse('''<script>alert("Menu Deleted successfully"); window.location="/manage_menu"</script>''')

class ViewReview(View):
    def get(self, request):
        obj = RestaurantRatingTable.objects.filter(RESTAURANT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/view_review.html", {"ratings": obj})
    


# //////////////////////////////////// RESORT ///////////////////////////////////////


class ResortDashboard(View):
    def get(self, request):
        return render(request, "RESORT/resort_dashboard.html")
    
class ResortRegistration(View):
    def get(self, request):
        return render(request, "RESORT/resort_registration.html")
    def post(self, request):
        form = ResortRegForm(request.POST, request.FILES)
        if form.is_valid():
            resort_form = form.save(commit=False)
            Username = request.POST["Username"]
            Password = request.POST["Password"]
            login_obj = LoginTable()
            login_obj.username = Username
            login_obj.password = Password
            login_obj.user_type = "RESORT"
            login_obj.save()
            resort_form.LOGIN = login_obj
            resort_form.save()
            return HttpResponse('''<script>alert("Registration successful"); window.location="/"</script>''')

class ManageResortGallery(View):
    def get(self, request):
        gallery_obj = ResortGalleryTable.objects.filter(RESORT__LOGIN_id=request.session['login_id'])
        return render(request, "RESORT/manage_gallery.html", {'gallery': gallery_obj})
    def post(self, request):
        form= ResortGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            resort = form.save(commit=False)
            resort_obj = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
            resort.RESORT = resort_obj
            resort.save()
            return HttpResponse('''<script>alert("Image added successfully"); window.location="/manage_resort_gallery"</script>''')

class ResortImageDelete(View):
    def get(self, request, image_id):
        obj = ResortGalleryTable.objects.get(id=image_id)
        obj.delete()
        return HttpResponse('''<script>alert("Image Deleted successfully"); window.location="/manage_resort_gallery"</script>''')

class ManageResortDescription(View):
    def get(self, request):
        try:
            obj = ResortDescriptionTable.objects.get(RESORT__LOGIN_id=request.session['login_id'])
            return render(request, "RESORT/manage_description.html", {'description': obj})
        except:
            return render(request, "RESORT/manage_description.html")
    def post(self, request):
        try:
            restaurant_obj = ResortDescriptionTable.objects.get(RESORT__LOGIN_id=request.session['login_id'])
            form =ResortDescriptionForm(request.POST, instance=restaurant_obj)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.RESORT = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
                obj.save()
                return HttpResponse('''<script>alert("Description added successfully"); window.location="/manage_resort_description"</script>''')
        except Exception as e:        
            form =ResortDescriptionForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.RESORT = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
                obj.save()
                return HttpResponse('''<script>alert("Description added successfully"); window.location="/manage_resort_description"</script>''')
    
    
class ManageResortFacility(View):
    def get(self, request):
        obj = ResortFacilityTable.objects.filter(RESORT__LOGIN_id=request.session['login_id'])
        return render(request, "RESORT/manage_facility.html",{'facility': obj})
    def post(self, request):
        form = ResortFacilityForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESORT = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Facility added successfully"); window.location="/manage_resort_facility"</script>''')

class EditResortFacility(View):
    def get(self, request, fecility_id):
        obj = ResortFacilityTable.objects.get(id=fecility_id)
        return render(request, "RESORT/edit_facility.html", {'facilities': obj}) 
    def post(self, request, fecility_id):
        facility_obj = ResortFacilityTable.objects.get(id=fecility_id)
        form = ResortFacilityForm(request.POST, instance=facility_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Facility edited successfully"); window.location="/manage_resort_facility"</script>''')

class DeleteResortFacility(View):
    def get(self, request, fecility_id):
        facility_obj = ResortFacilityTable.objects.get(id=fecility_id)
        facility_obj.delete()
        return HttpResponse('''<script>alert("Facility Deleted successfully"); window.location="/manage_resort_facility"</script>''')

class ManageResortOffers(View):
    def get(self, request):
        obj = ResortOfferTable.objects.filter(RESORT__LOGIN_id=request.session['login_id'])
        return render(request, "RESORT/manage_offers.html", {'offers': obj})
    def post(self, request):
        form = ResortOfferForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESORT = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Offer added successfully"); window.location="/manage_resort_offers"</script>''')

class EditResortOffers(View):
    def get(self, request, offer_id):
        obj = ResortOfferTable.objects.get(id=offer_id)
        return render(request, "RESORT/edit_offer.html", {'offers': obj, 'StartingTime': obj.StartingTime.strftime('%Y-%m-%d') , 'endingTime': obj.endingTime.strftime('%Y-%m-%d')}) 
    def post(self, request, offer_id):
        offer_obj = ResortOfferTable.objects.get(id=offer_id)
        form = ResortOfferForm(request.POST, request.FILES, instance=offer_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Offer edited successfully"); window.location="/manage_resort_offers"</script>''')

class DeleteResortOffers(View):
    def get(self, request, offer_id):
        offer_obj = ResortOfferTable.objects.get(id=offer_id)
        offer_obj.delete()
        return HttpResponse('''<script>alert("Offer Deleted successfully"); window.location="/manage_resort_offers"</script>''')

class ManageResortMenu(View):
    def get(self, request):
        obj = ResortMenuTable.objects.filter(RESORT__LOGIN_id=request.session['login_id'])
        return render(request, "RESORT/manage_menu.html",{'menus': obj})
    def post(self, request):
        form = ResortMenuForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.RESORT = ResortTable.objects.get(LOGIN_id=request.session['login_id'])
            obj.save()
            return HttpResponse('''<script>alert("Menu added successfully"); window.location="/manage_resort_menu"</script>''')

class EditResortMenu(View):
    def get(self, request, menu_id):
        obj = ResortMenuTable.objects.get(id=menu_id)
        return render(request, "RESORT/edit_menu.html", {'menu': obj}) 
    def post(self, request, menu_id):
        menu_obj = ResortMenuTable.objects.get(id=menu_id)
        form = ResortMenuForm(request.POST, request.FILES, instance=menu_obj)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Menu edited successfully"); window.location="/manage_resort_menu"</script>''')

class DeleteResortMenu(View):
    def get(self, request, menu_id):
        menu_obj = ResortMenuTable.objects.get(id=menu_id)
        menu_obj.delete()
        return HttpResponse('''<script>alert("Menu Deleted successfully"); window.location="/manage_resort_menu"</script>''')

class ViewResortReview(View):
    def get(self, request):
        obj = ResortRatingTable.objects.filter(RESORT__LOGIN_id=request.session['login_id'])
        return render(request, "RESTAURANT/view_review.html", {"ratings": obj})
    

# //////////////////////////////////// USER API ///////////////////////////////////////

class UserReg(APIView):
    def post(self, request):
        print("###############",request.data)
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            password = request.data['password']
            login_profile = login_serial.save(user_type='USER', password=password)
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)

class LoginPageApi(APIView):
    def post(self, request):
        response_dict= {}
        password = request.data.get("password")
        print("Password ------------------> ",password)
        username = request.data.get("username")
        print("Username ------------------> ",username)
        try:
            user = LoginTable.objects.filter(username=username, password=password).first()
            print("user_obj :-----------", user)
        except LoginTable.DoesNotExist:
            response_dict["reason"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)
        print(user.user_type)
        if user.user_type == "USER":
            response_dict = {
                "login_id": user.id,
                "user_type": user.user_type,
                "username": user.username,
            }
            print("User details :--------------> ",response_dict)
            return Response(response_dict, HTTP_200_OK)
        elif user.user_type == "TOURIST":
            response_dict["session_data"] = {
                "login_id": user.id,
                "user_type": user.user_type,
                "username": user.username,
            }
            return Response(response_dict, HTTP_200_OK)
        else:
            response_dict["reason"] = "Your account has not been approved yet or you are a CLIENT user."
            return Response(response_dict, HTTP_200_OK)

class ViewRestaurants(APIView):
    def get(self, request):
        restaurant = RestaurantTable.objects.all()
        restaurant_serializer = RestaurantSeralizer(restaurant, many = True)
        return Response(restaurant_serializer.data)
    def post(self, request):
        restaurant_rating_serializer = RestaurantRatingSerializer(data=request.data)
        if restaurant_rating_serializer.is_valid():
            restaurant_rating_serializer.save()
            return Response(restaurant_rating_serializer.data, status=status.HTTP_201_CREATED)

class RestaurantDetails(APIView):
    def get(self, request):
        restaurant_id = request.data['restaurant_id']
        rating_obj = RestaurantRatingTable.objects.filter(RESTAURANT_id=restaurant_id)
        rating_serializer = RestaurantRatingSerializer(rating_obj, many=True)
        return Response(rating_serializer.data)
    def post(self, request):
        rating_serializer = RestaurantRatingSerializer(data=request.data)
        if rating_serializer.is_valid():
            rating_serializer.Date = datetime.datetime.now()
            rating_serializer.save()
            return Response(status=status.HTTP_201_CREATED)

class ViewResort(APIView):
    def get(self, request):
        resort = ResortTable.objects.all()
        resort_serializer = ResortSeralizer(resort, many = True)
        return Response(resort_serializer.data)
             
class ViewPhotoShoot(APIView):
    def get(self, request):
        photo_shoot = PhotoShootTable.objects.all()
        photo_shoot_serializer = PhotoShootSeralizer(photo_shoot, many = True)
        return Response(photo_shoot_serializer.data)
             
class ViewAmalgamation(APIView):
    def get(self, request):
        amalgamation = AmalgamationTable.objects.all()
        amalgamation_serializer = AmalgamationSeralizer(amalgamation, many = True)
        return Response(amalgamation_serializer.data)
             
class ViewParkingSpot(APIView):
    def get(self, request):
        parking_sopt = ParkingSpotTable.objects.all()
        parking_serializer = ParkingSpotSeralizer(parking_sopt, many = True)
        return Response(parking_serializer.data)
             
class ViewPoint(APIView):
    def get(self, request):
        view_point = ViewPointTable.objects.all()
        view_point_serializer = ViewPointSeralizer(view_point, many = True)
        return Response(view_point_serializer.data)
             
class ViewFestivals(APIView):
    def get(self, request):
        festivals = FestivalTable.objects.all()
        festival_serializer = FestivalSeralizer(festivals, many = True)
        return Response(festival_serializer.data)
             
class SendComplaint(APIView):
    def get(self, request):
        obj = ComplaintTable.objects.all()
        complaint_serializer = ComplaintSerializer(obj, many=True)
        return Response(complaint_serializer.data)
    def post(self, request):
        comp_serializer = ComplaintSerializer(data=request.data)
        if comp_serializer.is_valid():
                comp_serializer.save(reply="pending")
                return Response(comp_serializer.data, status=status.HTTP_201_CREATED)

# ////////////////////////////////// TOURIST ///////////////////////////////////////////

class TouristReg(APIView):
    def post(self, request):
        print("###############",request.data)
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            password = request.data['password']
            login_profile = login_serial.save(user_type='TOURIST', password=password)
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)

class ManageFestival(APIView):
    def get(self, request):
        tourist_id = request.POST['torist_id']
        festivals = FestivalTable.objects.filter(TOURIST_id=tourist_id)
        festival_serializer = FestivalSeralizer(festivals, many = True)
        return Response(festival_serializer.data)
    def post(self, request):
        tourist_id = request.POST['torist_id']
        festival_serializer = FestivalSeralizer(data=request.data)
        if festival_serializer.is_valid():
            festival_serializer.save(TOURIST_id=tourist_id)
            return Response(festival_serializer.data, status=status.HTTP_201_CREATED)

class ManageParking(APIView):
    def get(self, request):
        tourist_id = request.POST['torist_id']
        parking = ParkingSpotTable.objects.filter(TOURIST_id=tourist_id)
        parking_serializer = ParkingSpotSeralizer(parking, many = True)
        return Response(parking_serializer.data)
    def post(self, request):
        tourist_id = request.POST['torist_id']
        parking_serializer = ParkingSpotSeralizer(data=request.data)
        if parking_serializer.is_valid():
            parking_serializer.save(TOURIST_id=tourist_id)
            return Response(parking_serializer.data, status=status.HTTP_201_CREATED)

class ManageViewPoint(APIView):
    def get(self, request):
        tourist_id = request.POST['torist_id']
        view_point = ViewPointTable.objects.filter(TOURIST_id=tourist_id)
        view_point_serializer = ViewPointSeralizer(view_point, many = True)
        return Response(view_point_serializer.data)
    def post(self, request):
        tourist_id = request.POST['torist_id']
        view_point_serializer = ViewPointSeralizer(data=request.data)
        if view_point_serializer.is_valid():
            view_point_serializer.save(TOURIST_id=tourist_id)
            return Response(view_point_serializer.data, status=status.HTTP_201_CREATED)

class ManageAmalgamation(APIView):
    def get(self, request):
        tourist_id = request.POST['torist_id']
        amalgamation = ViewPointTable.objects.filter(TOURIST_id=tourist_id)
        amalgamation_serializer = ViewPointSeralizer(amalgamation, many = True)
        return Response(amalgamation_serializer.data)
    def post(self, request):
        tourist_id = request.POST['torist_id']
        amalgamation_serializer = ViewPointSeralizer(data=request.data)
        if amalgamation_serializer.is_valid():
            amalgamation_serializer.save(TOURIST_id=tourist_id)
            return Response(amalgamation_serializer.data, status=status.HTTP_201_CREATED)

    
