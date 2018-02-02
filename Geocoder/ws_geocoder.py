import json
import urllib.request


class Geocoder:
    """Classe para consulta aos web service ddo geocoder.pbh"""
    def __init__(self):
        self.addressUrl = 'http://geocoder.pbh.gov.br/geocoder/v1/address?'
        self.reverseUrl = 'http://geocoder.pbh.gov.br/geocoder/v1/coordinate?'
        #atribui os nomes dos parametros
        self.pLogradouro = 'logradouro'
        self.pClassificacao = 'classificacao'
        self.pNumero = 'numero'
        self.pBairro = 'bairro'
        self.pCep = 'cep'

    def getresponse(url):
        data = urllib.request.urlopen(url).read().decode()

        try:
            js = json.loads(data)
        except:
            js = None

        return js

    def addparamurl(url, paramName, paramValue):
        return url+'&'+paramName+'='+paramValue

    def pesqlograd(self, nomeLogradouro):
        url = Geocoder.addparamurl(self.addressUrl,self.pLogradouro,nomeLogradouro)
        return Geocoder.getresponse(url)

    def pesqcep(self, cep):
        url = Geocoder.addparamurl(self.addressUrl, self.pCep, cep)
        return Geocoder.getresponse(url)

    def pesqlogradnum(self, nomeLogradouro, numero):
        url = Geocoder.addparamurl(self.addressUrl, self.pLogradouro, nomeLogradouro)
        url = Geocoder.addparamurl(url, self.pNumero, numero)
        return Geocoder.getresponse(url)

    def pesqcepnum(self, cep,numero):
        url = Geocoder.addparamurl(self.addressUrl, self.pCep, cep)
        url = Geocoder.addparamurl(url, self.pNumero ,numero)
        return Geocoder.getresponse(url)