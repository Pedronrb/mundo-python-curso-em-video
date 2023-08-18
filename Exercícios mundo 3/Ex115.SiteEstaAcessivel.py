import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('O Youtube NÃO está acessível no momento')
else:
    print('O Youtube etsá disponível')    
    print(site.read())
    