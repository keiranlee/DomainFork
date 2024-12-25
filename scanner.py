import requests
import socket
import concurrent.futures

def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def fetch_from_crtsh(domain):
    """crt.sh search."""
    print("[*] Finding subdomains ...")
    subdomains = set()
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                subdomain = entry["name_value"]
                subdomains.update(subdomain.split("\n"))
    except Exception as e:
        print(f"[-] Error: {e}")
    return subdomains



def check_subdomain(domain, subdomain_prefix):
    """Checks subdomain IP."""
    subdomain = f"{subdomain_prefix}.{domain}"
    ip = get_ip_address(subdomain)
    if ip:
        return (subdomain, ip)
    return None

if __name__ == "__main__":
    domain = input("Domain (example.com): ").strip()


    # get domain ip
    main_domain_ip = get_ip_address(domain)
    if not main_domain_ip:
        print(f"[-] Cannot get IP: {domain}")
        exit(1)
    print(f"[+] Domain IP: {main_domain_ip}")

    # get subdomains
    crtsh_subdomains = fetch_from_crtsh(domain)
    print(f"[+] Subdomains found: {len(crtsh_subdomains)}")


    # create list
    all_subdomains = set(crtsh_subdomains)

    # check subdomains ip
    print("\n[*] Checking ...")
    subdomains_with_ips = []
    for subdomain in sorted(all_subdomains):
        ip = get_ip_address(subdomain)
        if ip:
            subdomains_with_ips.append((subdomain, ip))
            print(f"[+] {subdomain} -> {ip}")

    # filter
    different_ips = [entry for entry in subdomains_with_ips if entry[1] != main_domain_ip]

    # write
    if different_ips:
        print(f"\n[!] Different subdomains ({len(different_ips)}):")
        for subdomain, ip in different_ips:
            print(f"{subdomain} -> {ip}")
    else:
        print("\n[!] Cannot find different subdomains.")

    # save
    with open("discovered_subdomains.txt", "w") as file:
        for subdomain, ip in different_ips:
            file.write(f"{subdomain} -> {ip}\n")
    print("[*] Saved to 'discovered_subdomains.txt' file.")