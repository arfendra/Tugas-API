from zeep import Client

client = Client("http://localhost:8000/?wsdl")

response = client.service.GetContact(1)
print(response)