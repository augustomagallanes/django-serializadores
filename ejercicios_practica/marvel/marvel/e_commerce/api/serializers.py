
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic
from e_commerce.models import User
from e_commerce.models import WishList
# Luego importamos todos los serializadores de django rest framework.
from rest_framework import serializers


class ComicSerializer(serializers.ModelSerializer):
    # new_field = serializers.SerializerMethodField()

    # def get_new_field(self, obj):
    #     return {'message': 'Acá puedo devolver más información.'}

    class Meta:
        model = Comic
        fields = '__all__'
        # fields = ('marvel_id', 'title', 'new_field')
        read_only_fields = ('id',)


# TODO: Realizar el serializador para el modelo de User y WishList

# 7. Crear un serializador para el modelo de WishList
# Debe crear un serializador llamado **WishListSerializer** dentro del archivo *serializers.py*
# Dicho serializador debe heredar de **ModelSerializer**.
# Debe poder serializar y/o deserializar *todos* los campos del modelo en cuestión.



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id','username','email')

class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList
        fields = fields = '__all__'
