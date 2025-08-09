from rest_framework import serializers
from member.models import Member


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            "id",
            "name",
            "email",
            "membership_date",
            "status",
        ]
