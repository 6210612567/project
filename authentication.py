from mypassword import mypassword
import ssl
from ldap3 import Server, Connection, Tls, NTLM
import json

host='10.1.2.37'
username = 'eng.tu\\' + '6210612831'
password = mypassword
tls_config = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_SSLv23)
server = Server(host, use_ssl=True, tls=tls_config)
conn = Connection(server, user=username, password=password, authentication=NTLM)
conn.bind() # return True  or False
result = conn.result
# print(result['result'])

conn.search('DC=eng,DC=tu', '(&(name=6210612831))', attributes = ['*'])
# print(conn.entries[0])

# print(conn.entries[0].entry_dn)
# print(conn.entries[0].displayName)

#https://ldap3.readthedocs.io/en/latest/abstraction.html?highlight=json#entry

data_json = conn.entries[0].entry_to_json()
data_dict = json.loads(data_json)   

# # for key, value in data_dict['attributes'].items():
# #     print(key, ':', value)

print(data_dict['attributes']['displayName'][0])