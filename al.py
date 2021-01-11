clear
#!usr/bin/python
#coded by menang22
# woii cuk janji jgn recode ya
import requests, os, sys, json

def cekip():
os.system('pip2 install requests') 
os.system('sleep 1')
os.system('clear') 
 print(f'[!] Mendapatkan IP..')
 re = requests.get('https://whatismyipaddress.com').json()
 ip4 = re['IPv4']
 ip6 = re['IPv6']
 print(f'[!] IP versi4 kamu : {ip4}')
 print(f'[!] IP versi6 kamu : {ip6}')
 os.system('sleep 3')
 os.system('clear') 

 def satr():
 print(f'[!] Menginstall tools..')
 os.system('apt update upgrade') 
 os.system('apt install git toilet bash')
 os.system('apt install curl wget python')
 os.system('apt install python2 clang')
 os.system('sleep 1')
 os.system('clear') 
 os.system('git clone https://github.com/menang22/hack-satelit')
os.system('cd hack-satelit')
os.system('sh sa-telit.sh')

 def kota():
 print(f'[!] Mengistall tools..')
 os.system('apt update upgrade') 
 os.system('apt install git python') 
 os.system('apt install python2')
 os.system('sleep 1')
 os.system('clear')
 os.system('git clone https://github.com/Bintang73/tembaktembakan')
os.system('cd tembaktembakan') 
os.system('python dor.py')

os.system('toilet -f standard -F gay "Toolsv3"')
os.system('sleep 2')
os.system('clear') 
print("'-=[Toolsv3]=-

  [Menu]
[1.]Cek ip
[2.]Hack satelit
[3.]Tembak kuota
[4.]Keluar
"')
menu = input('[?]Silahkan Pilih : ')

if menu == '1':
cekip()
elif menu == '2':
satr()
elif menu == '3':
kota()
elif menu == '4':
print('[?]Keluar... ')
sys.exit()
else:
print('[?]Perintah tidak diketahui! ')
sys.exit()
