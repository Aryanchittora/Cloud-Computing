from ast import Delete
from etherpad_lite import EtherpadLiteClient
from datetime import datetime

etherClient = EtherpadLiteClient(base_params={'api_key': '5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

group = etherClient.createGroup()
pad = etherClient.createPad(padID='newpad1', text='Hello !')
print(pad)


author = etherClient.createAuthor(name='Aryan')
print('Author -', author)

padcount = etherClient.padUsersCount(padID='newpad')
print('Pad count -', padcount)

time = etherClient.getLastEdited(padID='newpad')
last = time['lastEdited']
edit = datetime.fromtimestamp(last/1000.0)
print('Last Edit -', edit)

# delete = etherClient.deletePad(padID='newpad')