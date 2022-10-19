from spyne.service import ServiceBase
from spyne.decorator import rpc
from spyne.model.primitive import Double
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from math import sin,cos


class MathService(ServiceBase):
    @rpc(Double(nillable=False), Double(nillable=False),_returns=Double)
    def min(ctx,x,y):
        return x<y and x or y
    @rpc(Double(nillable=False), Double(nillable=False),_returns=Double)
    def max(ctx,x,y):
        return x>y and x or y
    
    @rpc(Double(nillable=False),_returns=Double)
    def sin(ctx,x):
        return sin(x)
    
    @rpc(Double(nillable=False),_returns=Double)
    def cos(ctx,x):
        return cos(x)
    
#création d'une instance
soap_app = Application(
    [MathService],
    tns='maths.isg.tn',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_application)

    