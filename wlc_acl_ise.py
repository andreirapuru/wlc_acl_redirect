#Author: Andre Ortega, brainwork.com.br

print('\n''Script initiated')
print('\n')

psnlist = []
avlist = []
ace = 1

psns = int(input('PSNs: '))
avs = int(input('Remediation:'))

for i in range(psns):
	psnipaddress = input('IP Address PSN'+str(i+1)+': ')
	psnlist.append(psnipaddress)
for i in range(avs):
	avipaddress = input('IP Address Remediation'+str(i+1)+': ')
	avlist.append(avipaddress)

#Create a .txt file with the ACL
acl = open('ACL_POSTURE_REDIRECT.txt', 'a')
acl.write('\n')
acl.write('\nconfig acl create ACL_POSTURE_REDIRECT')
acl.write('\n')
acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))
acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 53 53')
acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
acl.write('\n')
ace=ace+1
acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+str(ace)+'') 
acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 53 53')
acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
acl.write('\n')

for i in range(psns):
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 8443 8443')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 8443 8443')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))  
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 8905 8905')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 8905 8905')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))  
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 8905 8905')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))  
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 8905 8905')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))  
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 8909 8909')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 8909 8909')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 6')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace))  
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 8909 8909')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 8909 8909')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ psnlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule protocol ACL_POSTURE_REDIRECT '+str(ace)+' 17')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')

for i in range(avs):
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule destination address ACL_POSTURE_REDIRECT '+str(ace)+' '+ avlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')
	ace=ace+1
	acl.write('\nconfig acl rule add ACL_POSTURE_REDIRECT '+ str(ace)) 
	acl.write('\nconfig acl rule source port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule source address ACL_POSTURE_REDIRECT '+str(ace)+' '+ avlist[i] +' 255.255.255.255')
	acl.write('\nconfig acl rule destination port range ACL_POSTURE_REDIRECT '+str(ace)+' 0 65535')
	acl.write('\nconfig acl rule action ACL_POSTURE_REDIRECT '+str(ace)+' permit')
	acl.write('\n')

acl.close()
output=open('ACL_POSTURE_REDIRECT.txt','r')
print(output.read())

print('\n''Script finished')
