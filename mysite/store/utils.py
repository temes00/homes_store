def get_sale_price(price: int, sale: int) -> int:
    return int(price - (price / 100 * sale))
