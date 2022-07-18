import requests

result = input('Enter a Equation -> ')
opertion = input('Enter a Operation -> ')

data = requests.get('https://newton.now.sh/api/v2//'+opertion+'/'+result).json()

print('Result ->', data['result'])