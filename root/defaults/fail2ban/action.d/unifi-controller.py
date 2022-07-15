#!/usr/bin/env python3
import sys
import requests

# Unifi Controller
url = "https://172.27.1.164:8443"
username = "apiuser"
password = "password"
group_id = "group"

class UnifiAuthenticationException(Exception):
    pass

class Unifi:
    """Unifi API wrapper"""

    def __init__(self, username, password, base_url, site='default', ignore_ssl=True, authenticate=True):
        """
        Initialize the Unifi API
        :param ignore_ssl: Ignore Unifi SSL certificate validity
        :param username: Unifi username
        :param password: Unifi password
        :param base_url: Unifi API base URL
        :param site: Site (defaults to the default site)
        :param authenticate: Authenticate after instantiating class
        """
        # Set class-level variables
        self.ignore_ssl = ignore_ssl
        self.username = username
        self.password = password
        self.base_url = base_url
        self.site = site
        self.session = requests.Session()

        if ignore_ssl:
            self.session.verify = False
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Authenticate
        if authenticate:
            self.authenticate()
    # Authenticate against the Unifi API
    def authenticate(self):
        """
        Authenticate against the Unifi API
        :return: authentication successful
        """
        self.session.headers.update({'referrer': f"{self.base_url}/login"})
        # Send credentials to API, check if successful
        if self.session.post(f"{self.base_url}/api/login",
                             json={'username': self.username, 'password': self.password}).json().get('meta').get(
            'rc') == 'ok':
            return True
        else:
            raise UnifiAuthenticationException

    def getFirewallGroup(self, group_id):
        """
        Get existing firewall group
        :return: firewall group info
        """
        firewallGroup = ''
        response = self.session.get(f"{self.base_url}/api/s/{self.site}/rest/firewallgroup/{group_id}", verify=False).json()
        if response.get('meta').get('rc') == 'ok' and len(response.get('data')) == 1:
            firewallGroup = response.get('data')[0]
        return firewallGroup if firewallGroup else False

    def editFirewallGroup(self, group_id, data):
        """
        Edit firewall group
        :return: edit successful
        """
        response = self.session.put(f"{self.base_url}/api/s/{self.site}/rest/firewallgroup/{group_id}", json=data, verify=False)
        if response.status_code == 200:
            return True
        return False

def main(argv):
    unifi = Unifi(username, password, url)
    command = argv[1]
    ipaddr = argv[2]
    current_rule = unifi.getFirewallGroup(group_id)
    new_rule = ""

    if current_rule == False:
        sys.exit("Error: Something went wrong getting the existing group")
    
    if command == 'ban':
        print(f"Banning {ipaddr}")
        current_rule["group_members"].append(ipaddr)
        new_rule = unifi.editFirewallGroup(group_id,current_rule)
    elif command == 'unban':
        print(f"Un-Banning {ipaddr}")
        if ipaddr not in current_rule["group_members"]:
            sys.exit(f"Error: {ipaddr} is not banned")
        current_rule["group_members"].remove(ipaddr)
        new_rule = unifi.editFirewallGroup(group_id,current_rule)
    else:
        sys.exit("Unknown command")
    
    if new_rule == False:
        sys.exit("Error: Something went wrong when updating the group")

# Main
if __name__ == "__main__":
   main(sys.argv)
