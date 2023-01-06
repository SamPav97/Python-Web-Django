from rest_framework import serializers
from todo.todos_api.models import Todo, Category


class TodoForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # Check fields in your client.
        fields = ('id', 'title')


class TodoForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # Check fields in your client.
        fields = ('id', 'title', 'description', 'category')

    # Add current user to this create:
    def create(self, validated_data):
        # self.context['request'].user is where user is located in serializers
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class TodoForDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_done')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
