class SaleManager():
    def get_sales_by_date(self, date_start, date_end):
        return self.filter(date_sale__gte=date_start, date_sale__lte=date_end)


class DetailManager():
    def get_details_by_sale(self, sale):
        return self.filter(sale=sale)


class ShoppingCartManager():
    def get_products_by_barcode(self, barcode):
        return self.filter(barcode=barcode)
