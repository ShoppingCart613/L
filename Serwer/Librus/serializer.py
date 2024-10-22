from rest_framework import serializers


class GradeSerailizer(serializers.Serializer):
    grade = serializers.DecimalField(max_digits=3, decimal_places=2)
    description = serializers.CharField()
    subject = serializers.CharField()


