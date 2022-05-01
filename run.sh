export INPUT_DIR=/home/et1/Code/podcastweb

export LDAP_SERVER="ldap://hoth.urn1350.net:389"
export LDAP_USER_BASE="cn=users,cn=accounts,dc=urn1350,dc=net"
export LDAP_GROUP_BASE="cn=groups,cn=accounts,dc=urn1350,dc=net"
export LDAP_GROUP="ipausers"

# Secrets used for JWT / XSRF
# Probably a good idea to seed from /dev/urandom
export SECRET_1="secret"
export SECRET_2="supersecret"

python -m erso