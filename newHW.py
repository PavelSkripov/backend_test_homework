import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    # Сохраняем новую запись в список records[]
    def add_record(self, record):
        self.records.append(record)
    
    # Ф-ция для вывода записей из списка records[]
    def show (self):
        num = 0
        for i in self.records:
            print(f'Запись {num}: {i}')
            num = num + 1
    
    # Считаем, сколько калорий (денег) потрачено сегодня
    def get_today_stats(self):
        today = dt.datetime.now().date()
        sum = 0
        for rec in self.records:
            if today == rec.date:
                sum = sum + rec.amount 
        return sum

    




class CashCalculator(Calculator):
    USD_RATE = 61.0
    EURO_RATE = 64.0
    RUB_RATE = 1.0

    def __init__(self, limit):
        super().__init__(limit)

    
    def get_today_cash_remained(self, currency):
        cash_remained = 0
        currencies = {
            'rub': ('руб', self.RUB_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE)
        }
        if currency not in currencies:
            return print('Укажите валюту рассчета из списка: rub, eur, usd')
        else: 
            cash_remained = round((self.limit - self.get_today_stats())/currencies[currency][1], 2)
            if cash_remained > 0:
               return print(f'На сегодня осталось {cash_remained} {currencies[currency][0]}')
            elif cash_remained == 0:
               return print(f'Денег нет, держись')
            elif cash_remained < 0:
               return print(f'Денег нет, держись: твой долг {cash_remained} {currencies[currency][0]}')

    def get_week_stats(self, currency):
        today = dt.datetime.now().date()
        week_ago = today - dt.timedelta(7)
        total = 0
        week_expenses = 0
        currencies = {
            'rub': ('руб', self.RUB_RATE),
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE)
        }
        if currency not in currencies:
            return print('Укажите валюту рассчета из списка: rub, eur, usd')
        else:
            for rec in self.records:
                if rec.date <= today and rec.date >= week_ago:
                   total = total + rec.amount
            week_expenses = round(total/currencies[currency][1], 2)
            return print(f'Потрачено денег за неделю: {week_expenses} {currencies[currency][0]}')

    


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self):
        cash_remained = 0
        cash_remained = (self.limit - self.get_today_stats())
        if cash_remained > 0:
            return print(f'Сегодня можно съесть что-нибудь еще, но с общей калорийностью не более {cash_remained} кКал')
        elif cash_remained <= 0:
            return print(f'Хватит есть!')

    def get_week_stats(self):
        today = dt.datetime.now().date()
        week_ago = today - dt.timedelta(7)
        total = 0
        for rec in self.records:
                if rec.date <= today and rec.date >= week_ago:
                   total = total + rec.amount
        return print(f'Получено кКал за неделю: {total}')


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date != None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.datetime.now().date()
    
    # Метод для вывода в виде строки объектов класса Record
    def __str__(self):
        return f"Сумма: {self.amount};  Комментарий: {self.comment};  Дата: {self.date}"






cash = CashCalculator(2000)
cash1 = CashCalculator(500)
cash1.add_record(Record(amount = 50.169, comment = 'Кофе'))
cash1.add_record(Record(amount = 100, comment = 'Булочка'))
cash1.add_record(Record(amount = 200, comment = 'Суп', date = '28.11.2022'))
cash1.add_record(Record(30, 'Чай', '25.11.2022'))
cash1.get_today_cash_remained('eur')
cash1.get_week_stats('eur')

kkal = CaloriesCalculator(2000)
kkal.add_record(Record(1300, 'Кофе, бутерброд', '25.11.2022'))
kkal.add_record(Record(300, 'Кофе, бутерброд', '24.11.2022'))
kkal.add_record(Record(30000, 'Кофе, бутерброд', '20.11.2022'))
kkal.add_record(Record(200, 'Кофе, бутерброд', '28.11.2022'))
kkal.add_record(Record(1500, 'Пельмени'))
kkal.get_today_cash_remained()
kkal.get_week_stats()



