from etherpad_lite import EtherpadLiteClient

etherClient = EtherpadLiteClient(base_params={'api_key': '5ff7ea9032814c34a8f8daf05038aa9d48d29052678ca34eb40c69a981b118f9'})

group = etherClient.createGroup()
pad = etherClient.createPad(padID='Firstpad', text='Hello Guys!!')

print('Your Group is -', group)
print('Your Pad is -', pad)