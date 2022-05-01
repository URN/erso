# Erso
Authenticated Show downloader. It's called Erso because it's built on hope (like most things round here)

## Example run script

```sh
export INPUT_DIR=$PWD/input

export LDAP_SERVER="ldap://server.tld:389"
export LDAP_USER_BASE="cn=users,cn=accounts,dc=server,dc=tld"
export LDAP_GROUP_BASE="cn=groups,cn=accounts,dc=server,dc=tld"
export LDAP_GROUP="ipausers"

# Secrets used for JWT / XSRF
# Probably a good idea to seed from /dev/urandom
export SECRET_1="secret"
export SECRET_2="supersecret"

python -m erso
```