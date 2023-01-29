from rest_framework import filters, generics, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import ImageModel, TagModel
from .serializers import ImageSerializer, LoginSerializer,  TagSerializer, UserSerializer

from collections import Counter
from django.db.models import When, Case, IntegerField


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(username=serializer.data["username"])
            refresh = RefreshToken.for_user(user)
            return Response({
                'payload': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'User registered successfully',
            })


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.data["username"],
                password=serializer.data["password"]
            )
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'message': 'Login Successful',
                })
            return Response({
                'message': 'Invalid Password',
            })


class LogoutView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({'message': 'Logout Successful'})
        except Exception as e:
            return Response({'message': 'Something went wrong', 'error': e})


class ImageListView(generics.ListAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'tags__tag']
    ordering_fields = ['id', 'name']


class ImageDetailView(generics.RetrieveAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        image_instance = self.get_object()
        image_serializer = self.get_serializer(image_instance)

        tag_data = image_serializer.data["tags"]

        image_ids = list(TagModel.objects.filter(tag__in=tag_data).values_list('image_model', flat=True))
        image_ids.sort(key=Counter(image_ids).get, reverse=True)
        image_ids = list(dict.fromkeys(image_ids))

        order = image_ids
        when = []

        for sort_index, value in enumerate(order):
            when.append(
                When(id=value, then=sort_index)
            )

        related_instances = ImageModel.objects.exclude(id=image_instance.id).filter(id__in=image_ids)\
            .annotate(
                _sort_index=Case(
                    *when,
                    output_field=IntegerField()
                )
            ).order_by('_sort_index')

        image_serializer = ImageSerializer(related_instances, many=True)
        return Response(image_serializer.data)


class ImageCreateView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        image_serializer = ImageSerializer(data=request.data)
        if image_serializer.is_valid(raise_exception=True):
            image_instance = image_serializer.save()
            for data in request.data.get('tags'):
                tag_data = {
                    "image_model": image_instance.id,
                    "tag": data
                }
                tag_serializer = TagSerializer(data=tag_data)
                if tag_serializer.is_valid(raise_exception=True):
                    tag_serializer.save()
        return Response(image_serializer.data)


class ImageUpdateView(generics.UpdateAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        image_instance = self.get_object()
        image_serializer = self.get_serializer(image_instance, data=request.data, partial=True)

        if image_serializer.is_valid(raise_exception=True):
            image_serializer.save()
            for new_data in request.data.get('new_tags'):
                tag_data = {
                    "image_model": image_instance.id,
                    "tag": new_data
                }
                tag_serializer = TagSerializer(data=tag_data)
                if tag_serializer.is_valid(raise_exception=True):
                    tag_serializer.save()

            delete_data = request.data.get('delete_tags')
            TagModel.objects.filter(id__in=delete_data, image_model=image_instance.id).delete()

            for update_data in request.data.get('update_tags'):
                tag_data = {
                    "tag": update_data["tag"]
                }
                tag_instance = TagModel.objects.get(id=update_data["id"])
                tag_serializer = TagSerializer(tag_instance, data=tag_data, partial=True)
                if tag_serializer.is_valid(raise_exception=True):
                    tag_serializer.save()

        return Response(image_serializer.data)


class ImageDeleteView(generics.DestroyAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

