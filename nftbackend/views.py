from rest_framework import viewsets

from .models import (
    NFT,
    Signature
)
from .serializers import (
    NFTCreationSerializer,
    NFTSerializer,
    SignatureSerializer,
)


class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    model = NFT

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NFTCreationSerializer
        else:
            return NFTSerializer


class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    model = Signature
    serializer_class = SignatureSerializer