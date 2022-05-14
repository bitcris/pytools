
#Verificar o IP público e local
from datetime import datetime
from requests import get                                  
import socket

i = datetime.now()
ini = int(i.strftime("%S"))

print("IPINFO V:1.0 - Desenvolvido por Cristiano Ferreira")               

#varificando o IP público                                 
ip = get('https://api.ipify.org').text                    
print("IP PÚBLICO:",ip)     

                                                                                                                        #verificando o IP local                                   
host = socket.gethostname()                               
lip = socket.gethostbyname(host)
print("IP LOCAL:", lip)


f = datetime.now()
fim = int(f.strftime("%S"))

tmp = fim - ini

print("TEMPO",tmp,"s")

