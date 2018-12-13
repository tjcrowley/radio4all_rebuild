from .models import Files, Locations, Programs
from rest_framework import serializers



class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ('file_location','file','filename')

class FilesSerializer(serializers.HyperlinkedModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    class Meta:
        model = Files
        fields = ('title', 'filename', 'locations')

class ProgramsSerializer(serializers.HyperlinkedModelSerializer):
    files = FilesSerializer(many=True, read_only=True)
    license = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Programs
        fields = ('program_title', 'subtitle','type', 'date_created', 'series', 'speaker','license', 'summary', 'keywords','files')
