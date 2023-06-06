# Reflectie
#### Stéphane Van den Broeck
https://github.com/stephanevdb/python-trojan
https://github.com/stephanevdb/python-trojan-modules
## Modules
- sys-info
- network-scanner
- screenshot
- rickroll

### sys-info
Deze module verzamelt allerlij info over het systeem:
- hostname 
- public_ip
- private_ip
- mac_address
- os
- cpu
- storage

en upload dit naar een ftp server

### network-scanner
Deze module scant het netwerk waarop de computer zich bevindt met nmap en upload de resultaten als csv naar een ftp server`

### screenshot
Deze module maakt een screenshot van het scherm en upload deze naar een ftp server

### rickroll
Deze module speelt een rickroll af op de computer elke 10 seconden en voornamelijk als irritatie bedoeld

## module kiezen
Je kan van module veranderen door de gekozen module in te vullen in de encoder.py file en deze uit te voeren. hierdoor
wordt de juisite module gekozen en wordt de payload geencrypteerd. Push deze files naar de git repo om deze op alle targets uit te voeren.
Deze check gebeurt elke 5 minuten.
