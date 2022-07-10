# Configuration README

!! NOTICE !!

The `*.conf` files in this directory and its subdirectories will be replaced every time the container restarts. The files are meant to be easily viewed so that you can reference them.

If you would like to customize anything, create a `*.local` file with the same name as the `*.conf` file and apply your customizations. You do not need to copy the entire `*.conf` file to `*.local`, you only need to include things you want to change.

For example, to adjust `jail.conf`, create `jail.local` and apply your customizations there.

## Example jail.local

This example uses `apprise-api` for notifications, `cloudflare` for additional web proxy banning, and `abuseipdb` to report bad actors. You can remove any of these, or add more as you see fit.

```yaml
[DEFAULT]
# Change the default ban action from "iptables-multiport", which causes issues on some platforms, to "iptables-allports".
#banaction = %(banaction_allports)s

# Add additional actions
action = %(action_)s
         apprise-api[host="127.0.0.1", tag="fail2ban"]
         cloudflare[cfuser="YOUR-EMAIL", cftoken="YOUR-TOKEN"]

abuseipdb_apikey = YOUR-API-KEY

# "bantime" is the number of seconds that a host is banned.
bantime = 4h

# A host is banned if it has generated "maxretry" during the last "findtime" seconds.
findtime = 4h

# "maxretry" is the number of failures before a host get banned.
maxretry = 5

[unraid-ssh]
# configuration inherits from jail.d/unraid-ssh.conf
enabled  = true
action   = %(known/action)s
           abuseipdb[abuseipdb_apikey="%(known/abuseipdb_apikey)s", abuseipdb_category="18,22"]

[unraid-webgui]
# configuration inherits from jail.d/unraid-webgui.conf
enabled  = true
port     = http,https,YOUR-UNRAID-MY-SERVERS-WAN-PORT
action   = %(known/action)s
           abuseipdb[abuseipdb_apikey="%(known/abuseipdb_apikey)s", abuseipdb_category="18,21"]

[unifi-controller]
# configuration inherits from jail.d/unifi-controller.conf
enabled  = true
action   = %(known/action)s
           abuseipdb[abuseipdb_apikey="%(known/abuseipdb_apikey)s", abuseipdb_category="18,21"]
```