import json
from spyne import Application, rpc, ServiceBase, Unicode, Iterable, Integer, ComplexModel, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

import os
port = int(os.environ.get('PORT', 3002))

listV = [
    {
        'nom': 'tesla',
        'autonomie': 220,
        'temps': 5
    },
    {
        'nom': 'ford',
        'autonomie': 340,
        'temps': 5
    },
    {
        'nom': 'toyota',
        'autonomie': 270,
        'temps': 5
    },
]


class CarService(ServiceBase):

    @rpc(_returns=Unicode)
    def recupListVoiture(ctx):
        return json.dumps(listV)

    @rpc(Unicode, _returns=Integer)
    def recupAutonomie(ctx, nom):
        res = 0
        for voiture in listV:
            if voiture['nom'] == nom:
                res = voiture['autonomie']
        return res






application = Application([CarService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

server = make_server('0.0.0.0', port, wsgi_application)
print("thomas le reuf")

server.serve_forever()
