from pybit.unified_trading import HTTP
from utils import current_time
from typing import List, Optional
# from main import logger
import loguru

logger = loguru.logger

class BrokerBybit:
    def __init__(self):
        self.session = HTTP(testnet=True)

    def get_all_symbols_name(self) -> List[str]:
        """
        Получение всех имён доступных пар
        """
        # Общая инфо обо всех coins
        logger.info("Getting all symbols names...")
        response = self.session.get_instruments_info(category="linear")
        if response:
            logger.info("Success! All symbols names found.")
        names: List[str] = [str(coin["symbol"]) for coin in response["result"]["list"]]
        return names

    def get_symbol_current_price(self, symbol: str="BTCUSDT"):
        """
        Получение текущей цены актива
        return: str: current price
        """
        logger.info("Getting ticker %s ..." %(symbol, ))
        response = self.session.get_tickers(
            category="linear", # category - тип рынка (спот, фьючерсы)
            symbol=symbol
        )
        if response:
            logger.info("Success! Current ticker found.")
        current_price = response["result"]["list"][0]["lastPrice"]
        """
        ПРИМЕР!!!
        response["result"]["list"][0]
        {
            "retCode": 0,
            "result": {
                "list": [
                    {
                        "symbol": "BTCUSDT",
                        "lastPrice": "50000.0",
                        "highPrice24h": "51000.0",
                        "lowPrice24h": "49000.0",
                        "volume24h": "1234.5",
                        "turnover24h": "61725000.0",
                        ...
                    }
                ]
            }
        }
        """

        logger.info('In current time: %s\t%s last price eval %s $' % (current_time(), symbol, current_price))
        return str(current_price)

    def get_last_klines(self, symbol: str="BTCUSDT", limit: int=13) -> Optional[List[str]]:
        """
        Получаем цену последних limit свечей
        return: List[str]
        """
        response = self.session.get_kline(
            category="linear",
            symbol=symbol,
            interval=1,
            limit=limit
        )
        return response["result"]["list"]

    def get_relative_percentage_of_price_changes_last_klines(self, symbol: str="BTCUSDT", limit: int=13, percent: int = 5) -> Optional[str]:
        """
        Функция получает свечи монеты за определенный промежуток времени, смотрит изменение цены и если
        оно превышает установленный процент, то отправляет сообщение
        return: None or str
        """
        response = self.get_last_klines(symbol=symbol, limit=limit)
        try:
            current_price = float(response[0][4])
            ago_price = float(response[-1:][0][4])

            # Разница между ценами в процентах
            price_change = (current_price - ago_price) / ago_price * 100
            logger.info("Coin %s price_change: %.2f" % (symbol, price_change,))

            if price_change >= percent:
                logger.info("Price change >= {}%".format(percent))
                # Если % больше 5 подготавливаем сообщение в Телеграм
                message = symbol + " вырос на " + str(price_change) + "%"
                return message
            logger.info("Price change < {}%".format(percent))
            return None
        except IndexError as e:
            logger.error("IndexError: %s" % (e,))


    def get_order_book_by_symbol(self, symbol:str ="BTCUSDT"):
        """
        Функция для получения и обработки текущих ордеров
        """
        response = self.session.get_orderbook(
            category="linear",
            symbol=symbol,
            limit="500"
        )
        """
        ПРИМЕР
        key         ::       value
        retCode                 0
        retMsg                  OK
        result                  {'s': 'BTCUSDT', 'b': [['69480.5', '9.901'], ['69430.7', '0.006'], ['69400', '0.01'], ['69163.8', '0.002']]}
        retExtInfo              {}
        time                    1773326694199
        """
        return response





