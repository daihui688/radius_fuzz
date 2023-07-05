import client

if __name__ == '__main__':
    c = client.RadiusClient()
    c.access_request()
    c.accounting_request()
