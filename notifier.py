import pandas as pd
from twilio.rest import Client
# VARIAVEL DE AMBIENTE NO PYTHON


class Notifier:
    def __init__(self) -> None:
        self.account_sid = ""
        self.auth_token  = ""
        self.client = Client(self.account_sid, self.auth_token)
        self.months = {'janeiro','fevereiro','maio','abril','março','junho'}

    def read_file(self):
        for month in self.months:    
            file = pd.read_excel(f'{month}.xlsx')
            if (file['Vendas'] > 55000).any():
                seller = file.loc[file['Vendas'] > 55000,'Vendedor'].values[0]
                purchases = file.loc[file['Vendas'] > 55000,'Vendas'].values[0]
                self.send_message(month, seller, purchases)

    def send_message(self, month: str, seller: any, purchases: any):
        message = self.client.messages.create(
             to="", 
             from_="",
             body=f'No mês {month} alguém bateu a meta. Vendedor: {seller}, Vendas: {purchases}')
        message.sid