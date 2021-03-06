from symbol import return_stmt

from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Lista_habilidades, Verificando_habilidades

import json
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':0,
        'nome':'David',
        'habilidades':['Python','Flask']
    },
    {
        'id':1,
        'nome':'Israel',
        'habilidade':['Python','Django']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvovedor de ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return ({'status':'sucesso', 'mensagem':'Registro excluído'})

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return  desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>')
api.add_resource(Lista_habilidades, '/habilidades/')
api.add_resource(Verificando_habilidades, '/habilidades/verificando')

if __name__ == '__main__':
    app.run(debug=True)