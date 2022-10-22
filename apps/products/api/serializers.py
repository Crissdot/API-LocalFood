from rest_framework import serializers

from ..models import Category, Product

class CategorySerializer(serializers.ModelSerializer):

  class Meta:
    model = Category
    exclude = ('state', 'deleted_at', 'modified_at', 'created_at')


class ProductSerializer(serializers.ModelSerializer):

  class Meta:
    model = Product
    exclude = ('state', 'deleted_at', 'modified_at', 'created_at')

  def to_representation(self, instance):
    return {
      'id': instance.id,
      'name': instance.name,
      'description': instance.description,
      'image': instance.image.url if instance.image != '' else '',
      'category': instance.category.description,
    }
