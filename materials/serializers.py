from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_link], )

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    link = serializers.URLField(validators=[validate_link], )
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user, course=obj).exists()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
