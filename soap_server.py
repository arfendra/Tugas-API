from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ContactAddressService(ServiceBase):
    @rpc(Integer, _returns=Unicode)
    def GetContact(ctx, id):
        contacts = {
            1: {
                "name": "Muhammad Farrel Arfendra",
                "email": "farrelarfendra@example.com",
                "phone": "08156986345",
                "street": "Jl Medayu Selatan",
                "city": "Surabaya",
                "province": "Jawa Timur",
                "country": "Indonesia",
                "postal_code": "60295"
            }
        }

        contact = contacts.get(id, {
            "name": "Not Found",
            "email": "N/A",
            "phone": "N/A",
            "street": "N/A",
            "city": "N/A",
            "province": "N/A",
            "country": "N/A",
            "postal_code": "N/A"
        })
        
        return (f"Name: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}\n"
                f"Street: {contact['street']}, City: {contact['city']}, "
                f"Province: {contact['province']}, Country: {contact['country']}, "
                f"Postal Code: {contact['postal_code']}")

application = Application(
    [ContactAddressService],
    tns="http://example.com/contactaddress",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server running on http://localhost:8000")
    server.serve_forever()