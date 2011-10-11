# coding: utf-8
import sys
import urllib
import json

if len(sys.argv) == 2:
    busca = sys.argv[1]
else:
    print 'Informe o texto da busca: {0} "texto"'.format(__file__)
    sys.exit(1)

url = 'http://search.twitter.com/search.json?q='+busca
resposta = urllib.urlopen(url).read()
documento = json.loads(resposta)
resultados = documento['results']
for resultado in resultados:
    print u'{from_user}: {text}\n'.format(**resultado)
print '{0} resuldados exibidos'.format(len(resultados))    
