from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from time import asctime

class ServidorHora(Protocol):
	def dataReceived(self, data):
		self.transport.write(asctime())

f = Factory()
f.protocol = ServidorHora

porta = 9999
print 'Servindo a hora certa na porta TCP', porta
print 'Para conectar, use: > telnet 127.0.0.1', porta

reactor.listenTCP(porta, f)
reactor.run()
