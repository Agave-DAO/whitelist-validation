from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response

from .models import (
    NFT,
    Signature,
    Claimant,
)
from .serializers import (
    NFTCreationSerializer,
    NFTSerializer,
    SignatureSerializer,
    ClaimSerializer
)

from .transactions import (
    execute_claim
)

class NFTViewSet(viewsets.ModelViewSet):
    queryset = NFT.objects.all()
    model = NFT

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NFTCreationSerializer
        else:
            return NFTSerializer

    @action(methods=["post"], detail=True, serializer_class=ClaimSerializer)
    def claim(self, request, pk=None):
        serializer : ClaimSerializer = ClaimSerializer(data=request.data)
        if serializer.is_valid():
            try:
                claimant_obj = Claimant.objects.get(whitelist__id=pk, address=request.data['address'])
            except Exception as exc:
                raise NotFound()

            if claimant_obj.has_claimed:
                raise ValidationError("This address has already claimed the NFT")

            claim_exec_hash = execute_claim(claimant_obj)
            return Response({"tx_hash": claim_exec_hash})

class SignatureViewSet(viewsets.ModelViewSet):
    queryset = Signature.objects.all()
    model = Signature
    serializer_class = SignatureSerializer