# DomainFork

Finds subdomains located outside the main server.

# Usage:

Open File <br>

<code>python3 domainfork.py</code>


Enter Domain <br>

<code> Domain (example.com): boostprojects.com</code> 

# Output 

<code>
[*] Checking ...
[+] boostprojects.com -> 208.109.50.122
[+] old.boostprojects.com -> 107.180.1.227
[+] www.boostprojects.com -> 208.109.50.122
[+] www.old.boostprojects.com -> 107.180.1.227

[!] Different subdomains (2):
[-]old.boostprojects.com -> 107.180.1.227
[-]www.old.boostprojects.com -> 107.180.1.227
[*] Saved to 'discovered_subdomains.txt' file.
</code>

# Image

![DomainFork Usage](https://imagizer.imageshack.com/img924/9543/4vNorF.png)








Domains cheking via crt.sh

(It may give incorrect results for Cloudflare servers.)

by Relrekis

[t.me/merjunic](https://t.me/merjunic)
