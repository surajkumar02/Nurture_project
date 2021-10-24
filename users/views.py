from django.shortcuts import render
from .models import Booking, User,Advisor
from rest_framework.views import Response,APIView,status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import datetime

# Create your views here.

class BookingView(APIView):
    def get(self,request,user_id=None,advisor_id=None):
        booking=Booking.objects.all()
        details=[]
        for data in booking:
            result={
                'Advisor Name':data.advisor.advisor_name,
                'Advisor Profile Pic':data.advisor.advisor_photo_url,
                'Advisor Id':data.advisor.advisor_id,
                'Booking time': data.booking_time,
                'Booking id':data.booking_id

            }
            details.append(result)
        return Response(data=details)

    def post(self,request,user_id=None,advisor_id=None):
        time=request.data['Booking Time']
        time=time.split(',')
        a=[int(i) for i in time]
        booking_time=datetime.datetime(a[0],a[1],a[2],a[3],a[4],a[5])
        advisor=Advisor.objects.get(advisor_id=advisor_id)
        already,booking=Booking.objects.get_or_create(advisor=advisor,booking_time=booking_time)
        if booking:
            return Response(status=status.HTTP_200_OK)

        return Response(data={'Advisor Name':already.advisor.advisor_name,
        'Booking Time':already.booking_time})


class AdvisorPost(APIView):
    def post(self,request):
        try:
            name=request.data['Advisor Name']
            photo_url=request.data['Advisor Photo URL']

            advisor,newadvisor=Advisor.objects.get_or_create(advisor_name=name,advisor_photo_url=photo_url)

            if newadvisor:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(f"Advisor is already Available,('id':{advisor.advisor_id},'name':{advisor.advisor_name})",status=status.HTTP_302_FOUND)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AdvisorView(APIView):
    # permission_classes=[IsAuthenticated]

    def get(self,request,user_id=None):
        advisors=Advisor.objects.all()
        # user=User.objects.get(id=user_id)
        advisor_details=[]
        for advisor in advisors:
            result={
                "Advisor Name":advisor.advisor_name,
                "Advisor Profile Pic":advisor.advisor_photo_url,
                "Advisor Id":advisor.advisor_id
            }
            advisor_details.append(result)

        return Response(data=advisor_details,status=status.HTTP_200_OK)

class Login(APIView):

    def post(self,request):
        try:
            email=request.data['email']
            password=request.data['password']
            user=User.objects.get(email=email)
            if user and (user.password==password):
                token=RefreshToken.for_user(user)
                return Response(data={"userid":user.id,
                "token":{"refresh":str(token),
                        "access":str(token.access_token)}})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Register(APIView):

    def post(self,request):
        name=request.data['name']
        email=request.data['email']
        password=request.data['password']
        user,createuser=User.objects.get_or_create(user_name=name,email=email,password=password)
        if createuser:
            newuser=User.objects.last()
            token=RefreshToken.for_user(newuser)
            return Response(data={"userid":newuser.id,
            "token":{"refresh":str(token),
                    "access":str(token.access_token)}},status=status.HTTP_200_OK)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
           

