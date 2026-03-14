import os.path
from .Broker import BrokerBybit
import loguru
from utils import writer_data_json

logger = loguru.logger

class PumpsScreener(BrokerBybit):
    def __init__(self):
        super().__init__()


    def run(self, rec=False):
        """
        Проходит скринером по всем монетам биржи и смотрит их динамику
        """
        symbols_names = self.get_all_symbols_name()  # Получить все пары монет
        logger.info("Got all symbols names.")
        data = []
        for inx, symbol in enumerate(symbols_names):
            # Временное условие (ПОТОМ УДАЛИТЬ) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if inx > 10:
                break
            logger.info("Coin №%s %s" %(inx, symbol,))
            res = self.get_relative_percentage_of_price_changes_last_klines(symbol=symbol, limit=14, percent=3)
            data.append({"name": symbol, "result": res})
        if rec:
            writer_data_json(data, os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/PumpsScreener.json"))

