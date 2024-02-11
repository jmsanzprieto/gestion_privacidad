from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contraseñas
from .serializers import ContraseñasSerializer
from rest_framework.permissions import IsAuthenticated


class ContraseñasListCreate(generics.ListCreateAPIView):
    queryset = Contraseñas.objects.all()
    serializer_class = ContraseñasSerializer
    permission_classes = [IsAuthenticated]  # Establecer el permiso de autenticación

class ContraseñasRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contraseñas.objects.all()
    serializer_class = ContraseñasSerializer
    permission_classes = [IsAuthenticated]  # Establecer el permiso de autenticación


class ContraseñasUsuarioList(generics.ListAPIView):
    serializer_class = ContraseñasSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtener el ID del usuario desde la solicitud
        usuario_id = self.kwargs['usuario_id']
        # Filtrar las contraseñas por el ID del usuario
        return Contraseñas.objects.filter(user=usuario_id)
    
class NuevaContraseña(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ContraseñasSerializer(data=request.data)
        if serializer.is_valid():
        # Agregar el ID de usuario al objeto de contraseña antes de guardarlo
            serializer.validated_data['user_id'] = request.user.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

