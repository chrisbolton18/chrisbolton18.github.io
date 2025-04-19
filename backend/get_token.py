import requests
import base64

client_id = 'ce362fdaf1ea4fec9153e2d434f795be'
client_secret = 'cb2d5f4adc8240579e6759b22f25c193'
auth_code = 'AQAVC-oX4M-LpKSbd-KhPIrIW0Jdf6dVFXb_cwRGFGX-tgFjvC1zZiLtzGT9GjD0qv2e99ckc7vSWJlc9gnay0XAzuRVX9qiFFlbjIgXKBM5l5o6_htp-acwn2U4Wg34V73tb23Uusse4pxSc3d90UHQ5p_ZYavinldNv9pz92x9UH29WFdubCTLBem3x7XGZ-8NscxUzE_IigE'
redirect_uri = 'https://example.com/callback'

credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

response = requests.post(
    'https://accounts.spotify.com/api/token',
    data={
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': redirect_uri
    },
    headers={
        'Authorization': f'Basic {encoded_credentials}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
)

print(response.json())
