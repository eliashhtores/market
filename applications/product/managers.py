class ProductManager():
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    def get_by_barcode(self, barcode):
        return self.get_queryset().filter(barcode=barcode).first()

    def get_by_name(self, name):
        return self.get_queryset().filter(name=name).first()

    def get_by_provider(self, provider):
        return self.get_queryset().filter(provider=provider).first()

    def get_by_brand(self, brand):
        return self.get_queryset().filter(brand=brand).first()

    def get_by_expiration_date(self, expiration_date):
        return self.get_queryset().filter(expiration_date=expiration_date).first()

    def get_by_description(self, description):
        return self.get_queryset().filter(description=description).first()

    def get_by_unit(self, unit):
        return self.get_queryset().filter(unit=unit).first()

    def get_by_qty_available(self, qty_available):
        return self.get_queryset().filter(qty_available=qty_available).first()

    def get_by_cost(self, cost):
        return self.get_queryset().filter(cost=cost).first()

    def get_by_price(self, price):
        return self.get_queryset().filter(price=price).first()

    def get_by_sales(self, sales):
        return self.get_queryset().filter(sales=sales).first()

    def get_by_active(self, active):
        return self.get_queryset().filter(active=active).first()

    def get_all(self):
        return self.get_queryset().all()
