from rest_framework import serializers
from .models import FTUser, Activity

class ContentObjectRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """
    def to_representation(self, instance):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(instance, FTUser):
            serializer = FTUserSerializer(instance)
            return serializer.data
        elif isinstance(instance, Activity):
            serializer = ActivitySerializer(instance)
            return serializer.data

        raise Exception('Unexpected type of tagged object')

class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializer definition for Activity
    """
    def to_representation(self, instance):
        serialized_data = super(ActivitySerializer, self).to_representation(instance)

        return serialized_data

    class Meta(object):
        """
        Meta class definition for ActivitySerializer
        """
        model = Activity
        fields = ['start_time', 'end_time']

class FTUserSerializer(serializers.ModelSerializer):
    """
    Serializer definition for FTUser
    -------------------------------------------------
    Model : FTUser
    -------------------------------------------------
    """
    activity_periods=ContentObjectRelatedField(many=True, queryset=Activity.objects.all())
    def to_representation(self, instance):
        serialized_data = super(FTUserSerializer, self).to_representation(instance)

        return serialized_data

    class Meta(object):
        """
        Meta class definition for FTUserSerializer
        """
        model = FTUser
        fields = ("uid", "real_name", "tz", 'activity_periods')
        read_only_fields = ('activity_periods',)
