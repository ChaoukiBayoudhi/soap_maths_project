try:
    from suds.client import Client
except ImportError:
    print('Could not import suds library')
maths_client=Client('http://localhost:8000/maths?wsdl')
print(maths_client) # print SOAP Service information
x=input('x = ? ')
y=input('y = ? ')
max=maths_client.service.max(x,y)
print(f'max({x},{y}) = {max} ')
#or
print('max(',x,',',y,')=',max)
min=maths_client.service.min(x,y)
print(f'min({x},{y}) = {min} ')

angle=input('angle = ? ')
sin=maths_client.service.sin(angle)
print(f'sin({angle})={sin}')
cos=maths_client.service.cos(angle)
print(f'cos({angle})={cos}')
