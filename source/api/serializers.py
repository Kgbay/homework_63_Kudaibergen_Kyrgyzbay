from rest_framework import serializers

from .instagram_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'desc', 'image', 'user', 'created_at', 'updated_at')
        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance: Post, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
