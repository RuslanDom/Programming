from .Broker import BrokerBybit
import loguru

logger = loguru.logger

class HIOrdersScreener(BrokerBybit):
    def __init__(self):
        super().__init__()

    def get_hi_order(self, symbol:str = "BTCUSDT", limit: int = 5) -> str:
        """
        Выделяет из полученных ордеров самые топовые ордера кол-во указанно в limit
        и подготавливает сообщение для отправки
        """
        response = self.get_order_book_by_symbol(symbol)
        array_order = response["result"]["b"]
        array_order.sort(key=lambda x: x[1], reverse=True)
        top_orders = array_order[:limit]

        # Формирование message
        msg = "Топовые ордера:\n" + "\n".join(list(map(lambda x: " - ".join(x), top_orders)))
        """
        ПРИМЕР
        Топовые ордера:
        71315.5 - 9.967
        67996.7 - 0.918
        66138.1 - 0.918
        """
        return msg