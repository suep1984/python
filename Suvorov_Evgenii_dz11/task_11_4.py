class IsNumber(Exception):
    def __str__(self, message='Object "price" and "quantity" must be number. Try again.'):
        self.message = message
        return self.message


class Warehouse:
    def __init__(self):
        self.volume = 100
        self.dict = {}

    def entrance(self, argv):
        try:
            if not argv.price.isdigit() or not argv.quantity.isdigit():
                raise IsNumber()
        except IsNumber:
            print(IsNumber())
        else:
            if self.volume >= int(argv.quantity):
                self.volume -= int(argv.quantity)
                self.dict.setdefault(f'{argv.device_type} {argv.model}', [0, 0, argv.specs])
                self.dict[f'{argv.device_type} {argv.model}'][0] += int(argv.quantity)
                self.dict[f'{argv.device_type} {argv.model}'][1] += float(argv.price)
            else:
                print(f'Receiving {argv.model} in {argv.quantity} pieces is not possible. '
                      f'No free space in the warehouse')

    def transfer(self, device_type, model, quantity, department):
        if self.dict[f'{device_type.capitalize()} {model}'][0] - int(quantity) >= 0:
            self.dict[f'{device_type.capitalize()} {model}'][1] -= \
                round(self.dict[f'{device_type.capitalize()} '
                                f'{model}'][1] / self.dict[f''
                                                           f'{device_type.capitalize()} {model}'][0], 2) * int(quantity)
            self.dict[f'{device_type.capitalize()} {model}'][0] -= int(quantity)
            self.volume += int(quantity)
            print(f'{model} {quantity} pieces transfer to {department} department')
        else:
            print(f'Model {model} in {quantity} pieces is out of stock')


class OfficeTechnics:
    def __init__(self, model, price, quantity):
        self.price = price
        self.quantity = quantity
        self.model = model


class Printer(OfficeTechnics):
    def __init__(self, model, price, quantity, paper_format):
        super().__init__(model, price, quantity)
        self.device_type = self.__class__.__name__
        self.specs = paper_format


class Scanner(OfficeTechnics):
    def __init__(self, model, price, quantity, scan_res):
        super().__init__(model, price, quantity)
        self.device_type = self.__class__.__name__
        self.specs = scan_res


class Copier(OfficeTechnics):
    def __init__(self, model, price, quantity, copy_speed):
        super().__init__(model, price, quantity)
        self.device_type = self.__class__.__name__
        self.specs = copy_speed


wh = Warehouse()
printer1 = Printer('M2727', '50000', '50', 'A4')
printer2 = Printer('M425', '70000', '2', 'A4')
wh.entrance(printer1)
wh.entrance(printer2)
scanner1 = Scanner('Canon', '10000rub', '3pcs', '300 dpi')
wh.entrance(scanner1)
scanner2 = Scanner('Canon', '10000', '3', '300 dpi')
wh.entrance(scanner2)
printer3 = Printer('Kyocera', '150000', '90', 'A3')
wh.entrance(printer3)
wh.transfer('printer', 'M2727', '45', 'marketing')
copier1 = Copier('Xerox', '150000', '90', 'A3')
wh.entrance(copier1)

print(wh.dict)
print(wh.volume)
