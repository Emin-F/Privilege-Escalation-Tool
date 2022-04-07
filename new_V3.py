import platform
import os
import grp, pwd
import getpass
import subprocess
import colorama
from colorama import Fore, Style

def sysinfo():
	
	print('+++++++++++++++++ This Part Shows System Information +++++++++++++++++','\n')
	print('System:   ',platform.system())
	print('Kernel version:  ',platform.version())
	print('Release:  ',platform.release())
	print('Platform: ',platform.platform())
	
	kernel=platform.version()
	# Bunu daha sonra kernel üzerinden bir zafiyet varsa taramak için kullanırız.
	
	# print(platform.uname())   üsttekilerinin hepsini tek satırda yazan alternatif
	
	#envir=os.environ
	#print(envir.splitlines())
	print('\n','--------------- This area Shows Environment Variables ----------------------','\n')
	for key in os.environ:
		print(key, '=>', os.environ[key])
		
		
	print('\n','--------------- This area Shows PATH Variables ----------------------','\n')
	
	print(os.system("echo $PATH"))	
	#print(subprocess.run(["echo $PATH "]))

		
	

	
	
def userinfo():
	print('+++++++++++++++++ This Part Shows User Information +++++++++++++++++','\n')
	
	print("Current user:  ", os.system("whoami"))
	
	
	# print(getpass.getuser(),'(',os.getuid(),')')
	print('\n','--------------- Current User ID ----------------------','\n')
	print(subprocess.run(["id"]))
	
	print('\n','--------------- This area Shows Users and Their Groups ----------------------','\n')
	for p in pwd.getpwall():
		print('User:',p[0]+' Group:'+grp.getgrgid(p[3])[0])
		
	#superuser=os.system("grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0{print $1}'"))
	# değer döndürdü 0 olarak buna daha sonra bakarız.
	
	print('\n','--------------- This area Shows SUID Permissions ----------------------','\n')
	

	print(os.system("find / \( -perm -2000 -o -perm -4000 \) -exec ls -ld {} \; 2>/dev/null"))

	# bu kodun ne yaptığını öğren 
	

	
	
	
	print("varsayılan renk")
	
	
def service_info():
	
	print('+++++++++++++++++ This Part Shows Process, Cron, Timer  Information +++++++++++++++++','\n')
	
	print('\n','--------------- This area shows services are been running by root These Files are %70 Percent Exploitable!!!!!! ----------------------','\n')
	
	print(os.system("ps aux | grep root"))
	
	print('\n','--------------- This area shows cron jobs for  hourly, daily, weekly and mounthly ----------------------','\n')
	print(os.system("ls -al /etc/cron*"))
	
	print('\n','--------------- This area Shows Timers   ----------------------','\n')
	print(os.system("systemctl list-timers --all"))
	
	print('\n','--------------- This area Shows Sockets   ----------------------','\n')
	print(os.system("netstat -a -p --unix"))
    	
	

def potential_exp_files():
	print('+++++++++++++++++ This Part Shows Potential Explotaible Files +++++++++++++++++','\n')
	
	colorama.init()
	
	print(Fore.RED)
	
	print('\n','------------------------------------------ These Files are %80 Percent Exploitable File for PE ------------------------------------------')
	
	#buradaki çalıştırılabilecek dosyaları seçsin salak saçma hepsini göstermesin
	print(os.system("find /home -perm 777 -type f"))
	print(Style.RESET_ALL)
	
	print('\n',' ------------------------------------------ Private Key information ------------------------------------------ ')
	
	print(os.system("cat ~/.ssh/authorized_keys 2>/dev/null"),os.system("cat ~/.ssh/identity.pub 2>/dev/null"),os.system("cat ~/.ssh/identity 2>/dev/null"),os.system("cat ~/.ssh/id_rsa.pub 2>/dev/null"),
	os.system("cat ~/.ssh/id_rsa 2>/dev/null"),os.system("cat ~/.ssh/id_dsa.pub 2>/dev/null"),os.system("cat ~/.ssh/id_dsa 2>/dev/null"),os.system("cat /etc/ssh/ssh_config 2>/dev/null"),
	os.system("cat /etc/ssh/sshd_config 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_dsa_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_dsa_key 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_rsa_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_rsa_key 2>/dev/null"),
	os.system("cat /etc/ssh/ssh_host_key.pub 2>/dev/null"),os.system("cat /etc/ssh/ssh_host_key 2>/dev/null"))
	
	
	# düzenlensin içindeki key olanları öne çıkarsın bulundu falan yapsın !!!
	
	print('\n','------------------------------------------Are they any shell open by other user------------------------------------------')
	print(os.system("screen -ls"),os.system("tmux -ls"))
	
	
	print('\n','------------------------------------------Profile Files------------------------------------------')

	print(os.system("ls -l /etc/profile /etc/profile.d/"))
	#buradaki script'let user yeni bir shell run edince çalışıyor. Eğer herhangi birinde yazma yapabilirsek yetki yükseltilebilir.
	
	
	#writable db dosyaları
	print('\n','------------------------- Is There any Wrtiable .db File Exist --------------------------') 
	os.system("bash db_test.sh")
	
	
	print('\n','------------------------------------------Backup, logs and ineteresting files ------------------------------------------')
	print(os.system("ls -a /tmp /var/tmp /var/backups /var/mail/ /var/spool/mail/ /root"))
	

	print('\n','-------------------Files that contains passwdord keyword ------------------------------------------')
	print(os.system("find /var/log -name '*.log' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null | grep -E --color 'password'"), os.system("find /etc -name '*.c*' 2>/dev/null | xargs -l10 egrep 'pwd|password' 2>/dev/null | grep -E --color 'password'"))
	# dev/null kısmı hataları engellemek için
	#buradaki passwd olanlı highlighted yap

	print('\n','------------------------- Is /ect/passwd File Writable  --------------------------') 
	os.system("bash testwr.sh /etc/passwd")
	#etc passwd file writable mı buna bakıyor öyle ise direk içine kendi kullanıcımızı ekleriz ve root olabiliriz zaten.
		
	print('\n','------------------------- Is /ect/shadow  File Readable  --------------------------') 
	#/etc/shadow dosyasyı readable mi diye bakarız
	os.system("bash testre.sh /etc/shadow")
	
	
	
if __name__=="__main__":
	#sysinfo()
	#userinfo()
	#service_info()
	potential_exp_files()
