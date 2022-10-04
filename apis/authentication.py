import ssl
from ldap3 import Server, Connection, Tls, NTLM
import json

def ldap3_authen(user_id,password):
    host='10.1.2.37'
    username = 'eng.tu\\' + f'{user_id}'
    password = password
    tls_config = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_SSLv23)
    server = Server(host, use_ssl=True, tls=tls_config)
    conn = Connection(server, user=username, password=password, authentication=NTLM)
    conn.bind() # return True  or False
    result = conn.result


    if(result['result'] == 0):
        conn.search('DC=eng,DC=tu', f'(&(name={user_id}))', attributes = ['*'])
        data_json = conn.entries[0].entry_to_json()
        data_dict = json.loads(data_json)
        # print(data_dict['attributes']['displayName'][0])
        return [True,data_dict['attributes']['displayName'][0]]
    else:
        return [False,'']