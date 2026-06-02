from rest_framework import serializers
from pokedex.models import Pokemon
from django.core.files.base import ContentFile
import base64


class PokemonSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    picture_base64 = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = Pokemon
        fields = "__all__"
        extra_fields = ['picture_base64']

    def get_fields(self):
        fields = super().get_fields()
        fields['picture_base64'] = serializers.CharField(write_only=True, required=False, allow_blank=True)
        return fields

    def get_picture(self, obj):
        try:
            if obj.picture and obj.picture.name:
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(obj.picture.url)
                return obj.picture.url
        except ValueError:
            pass
        return None

    def create(self, validated_data):
        picture_data = validated_data.pop('picture_base64', None)
        pokemon = super().create(validated_data)
        if picture_data and ';base64,' in picture_data:
            fmt, imgstr = picture_data.split(';base64,')
            ext = fmt.split('/')[-1]
            pokemon.picture.save(
                f'pokemon_{pokemon.id}.{ext}',
                ContentFile(base64.b64decode(imgstr)),
                save=True
            )
        return pokemon

    def update(self, instance, validated_data):
        picture_data = validated_data.pop('picture_base64', None)
        instance = super().update(instance, validated_data)
        if picture_data and ';base64,' in picture_data:
            fmt, imgstr = picture_data.split(';base64,')
            ext = fmt.split('/')[-1]
            instance.picture.save(
                f'pokemon_{instance.id}.{ext}',
                ContentFile(base64.b64decode(imgstr)),
                save=True
            )
        return instance