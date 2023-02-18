from rest_framework.serializers import ModelSerializer
from .models import Note, Product


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


