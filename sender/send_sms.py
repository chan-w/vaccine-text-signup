from twilio.rest import Client

account_sid= "ACa8989bc5de6411f4d157b4466980911a"
auth_token = "1dedec4f5422fc23c1da9c106dd8ef86"

client = Client(account_sid, auth_token)

client.messages.create(
    to="915-503-4543",
    from_="+19162521643",
    body="Frankly, my dear, I don't give a damm."
)
