from rest_framework.viewsets import ModelViewSet
from member.models import Member
from member.serializers import MemberSerializers

# Create your views here.


class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializers
    queryset = Member.objects.all()
