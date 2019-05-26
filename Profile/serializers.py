# ----------------LIBRERIAS-----------------
from rest_framework import routers, serializers, viewsets
#from Profile.models import Profile
#from drt_dynamic_fields import  cargar esto y ponerlo en la clase



from drf_dynamic_fields import DynamicFieldsMixin

# -----------------MODELOS-------------------
     #Nombre App                 Nombre modelo
from Profile.models import Profile

class ProfileSerializers(DynamicFieldsMixin,serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user', 'address')

        