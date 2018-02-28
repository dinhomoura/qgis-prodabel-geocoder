import json
import urllib

class WsGeocoder:
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

    def getresponse(self, url):
        data = urllib.request.urlopen(url).read().decode()

        try:
            js = json.loads(data)
        except:
            js = None

        return js

    def addparamurl(self, url, paramName, paramValue):
        f = {paramName:paramValue}
        return url+'&'+urllib.urlencode(f)
    def pesqLogradUrl(self, nomeLogradouro):
        url = WsGeocoder.addparamurl(self, self.addressUrl, self.pLogradouro, nomeLogradouro)
        url = WsGeocoder.addparamurl(self, url, self.pClassificacao, "completo")
        return url

    def pesqlograd(self, nomeLogradouro):
        url = WsGeocoder.addparamurl(self, self.addressUrl,self.pLogradouro,nomeLogradouro)
        url = WsGeocoder.addparamurl(self, url, self.pClassificacao,"completo")
        return WsGeocoder.getresponse(self, url)

    def pesqcep(self, cep):
        url = WsGeocoder.addparamurl(self, self.addressUrl, self.pCep, cep)
        return WsGeocoder.getresponse(self, url)

    def pesqlogradnum(self, nomeLogradouro, numero):
        url = WsGeocoder.addparamurl(self, self.addressUrl, self.pLogradouro, nomeLogradouro)
        url = WsGeocoder.addparamurl(self, url, self.pClassificacao, "completo")
        url = WsGeocoder.addparamurl(self, url, self.pNumero, numero)
        return WsGeocoder.getresponse(self, url)

    def pesqcepnum(self, cep, numero):
        url = WsGeocoder.addparamurl(self, self.addressUrl, self.pCep, cep)
        url = WsGeocoder.addparamurl(self, url, self.pNumero, numero)
        return WsGeocoder.getresponse(self, url)