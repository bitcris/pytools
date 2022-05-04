import requests
import socket
print("PYTHON SHELL v1.0\n")

urll = input( 'DIGITE O ENDEREÇO DO HOST: ' )
#A biblioteca socket processa o https sozinha, a variável
#c1 é para usar o mesmo input no comabdo do requests
#assim o usuário não precisa digitar novamente
c1 = 'http://'

url = c1+urll
urx = urll
x = requests.get(url)
y = socket.gethostbyname(urx)


print('Host de destino.....',urll)
print('Resposta............',x.status_code)
print('IP do host..........',y)

