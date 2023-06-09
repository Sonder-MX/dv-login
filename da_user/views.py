from rest_framework import mixins, viewsets

from .models import DaUser
from .permissions import IsLogin, IsOwner, PutAuth
from .serializers import (UserListSerializer, UserRegisterSerializer, UserUpdateSerializer)


class UserListViewSet(viewsets.ReadOnlyModelViewSet):
    """用户列表"""
    queryset = DaUser.objects.all()
    serializer_class = UserListSerializer


# class UserRegisterApiView(generics.CreateAPIView):
#     serializer_class = UserRegisterSerializer

#     # 注册时检查用户邮箱是否存在
#     def post(self, request, *args, **kwargs):
#         print("检查邮箱")
#         email = request.data.get('email')
#         if DaUser.objects.filter(email=email).exists():
#             return Response({'message': "该邮箱已被注册！"}, status=status.HTTP_400_BAD_REQUEST)
#         return self.create(request, *args, **kwargs)


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    用户注册、查看、修改
    """
    queryset = DaUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsLogin, IsOwner]

    def get_permissions(self):
        if self.action == 'create':
            return []
        elif self.action == 'update':
            return [PutAuth()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserRegisterSerializer
        return UserUpdateSerializer
