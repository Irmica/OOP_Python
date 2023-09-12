class _Product:
    """ Класс для описания продукта в автомате """
    def __init__(self, name : str, price : int) -> None:
        self.name = name
        if price < 0:
            self.price = 10
        else: self.price = price
    # getters and setters
    def get_name(self):
        return self.name
    def set_name(self, new_name: str):
        self.name = new_name
    def get_price(self):
        return self.price
    def set_price(self, new_price: int):
        if new_price > 0:
            self.price = new_price
        else: self.price = 10
        
        
class _Place:
    MIN_ROW = 1
    MAX_ROW = 5
    MIN_COLUM = 1
    MAX_COLUM = 8
    def __init__(self, row:int,colum:int, MIN_ROW,MAX_ROW,MIN_COLUM,MAX_COLUM) -> None:
        if MIN_ROW <= row <=MAX_ROW:
            self.row = row
        else: print("Неверное значение ряда.")
        if MIN_COLUM <= colum <=MAX_COLUM:
            self.colum = colum
        else: print("Неверное значение столбца.")
    # getters and setters    
    def get_row(self):
        return self.row
    def set_row(self, new_row: int, MIN_ROW: int,MAX_ROW:int):
        if MIN_ROW <= new_row <=MAX_ROW:
            self.row = new_row
        else: print("Неверное значение ряда.")
    def get_colum(self):
        return self.colum
    def set_colum(self, new_colum: int, MIN_COLUM: int, MAX_COLUM: int):
        if MIN_COLUM <= new_colum <=MAX_COLUM:
            self.colum = new_colum
        else: print("Неверное значение столбца.")
    
class _Holder:
    


class _CoinDispenser:
    pass

class VendingMachine:
    