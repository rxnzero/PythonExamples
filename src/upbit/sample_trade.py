# 사전작업
# python 설치
# 라이브러리 설치 pip install pyupbit
# TA-LIB 설치 https://github.com/mrjbq7/ta-lib

import pyupbit
import json
import talib
import time

with open('config/config.json', 'r') as f:
    config_json = json.load(f)

def get_config(param):
    if param in config_json.keys():
        return config_json[param]
    else:
        return None

def get_mfi(ticker, interval):
    df = pyupbit.get_ohlcv(ticker, interval=interval)
    high = df["high"].values
    low = df["low"].values
    volume = df["volume"].values
    close = df["close"].values
    return talib.MFI(high, low, close, volume, timeperiod=14)

class TraderMFI:
    def __init__(self, ticker):
        self.ticker = ticker
        self.cut_loss_rate = -2.5
        access = get_config("access")
        secret = get_config("secret")
        
        # 기준 분봉
        self.minutes_interval = 10

        #회당매수금액 최저 5000
        self.purchase_price = 6000
        self.upbit = pyupbit.Upbit(access, secret)

        #목표 보유 금액
        self.target_holding_price = 20000


    def check_buy_point(self, mfi):
        current_signal = mfi[-1]
        previous_signal = mfi[-2]
        buy_base_line = 20
        check_bottom_line_break = (
            previous_signal < buy_base_line and current_signal > buy_base_line
        )
        # 저점 돌파 아닐 때 50 상향 돌파 체크 추가
        thrid_last_signal = mfi[-3]
        if check_bottom_line_break == False:
            check_bottom_line_break = (
                thrid_last_signal < previous_signal
                and previous_signal < 50
                and current_signal > 50
            )
        return check_bottom_line_break

    def check_sell_point(self, mfi):
        current_signal = mfi[-1]
        p1 = mfi[-2]
        sell_base_line = 75
        check_top_line_break = (
            p1 > sell_base_line and current_signal < sell_base_line
        )
        # 고점 돌파 아닐 때 50 하향 돌파 체크 추가
        p2 = mfi[-3]
        p3 = mfi[-4]
        if check_top_line_break == False:
            check_top_line_break = (
                p3 > p2 and p2 > p1 and p1 > 50 and current_signal < 50
            )
            if check_top_line_break == True:
                print(
                    f"MFI: p3:{round(p3,2):<5} p2:{round(p2,2):<5} p1:{round(p1,2):<5}  crnt:{round(current_signal,2)}"
                )
        return check_top_line_break

    def do_buy(self, target_price):
        count = self.purchase_price / target_price
        print(f"buy {target_price}, count: {count}")
        result = self.upbit.buy_limit_order(self.ticker, target_price, count)
        print(f"making buy order {result}")
        
    def do_sell(self, target_price):
        balance_price = self.holding_balance * target_price
        if balance_price < 5000:
            # print(
            #     f"can't sell your balance cuz {balance_price} is too small"
            # )
            return
        print(
            f"holding_balance: {self.holding_balance}, target_price: {target_price}"
        )
        if balance_price > self.purchase_price * 2:
            count = self.purchase_price / target_price
            print(f"sell {target_price} count:{count}")
            result = self.upbit.sell_limit_order(self.ticker, target_price, count)
            print(f"making sell order {result}")
        else:
            # 재고 털기
            print(f"sell {target_price} count:{self.holding_balance}")
            result = self.upbit.sell_limit_order(
                self.ticker, target_price, self.holding_balance
            )
            print(f"making sell order {result}")

    def cut_loss(self, avg_buy_price, trade_price):
        # print("check cut loss")
        if avg_buy_price <= 0:
            return
        profit_rate = (trade_price / avg_buy_price - 1) * 100
        if profit_rate < self.cut_loss_rate:
            print( f"profit_rate {profit_rate} less then cut_loss_rate {self.cut_loss_rate}" )
            self.do_sell(trade_price)
        return False

    def doTrade(self):
        current_trade_price = pyupbit.get_current_price(self.ticker)
        
        # 계좌 내 대상 코인 보유량 및 평단가 확인
        # logger = self.logger
        avg_buy_price = 0
        self.holding_balance = 0
        last_balance = self.upbit.get_balance(self.ticker, True)

        if isinstance(last_balance, dict):
            avg_buy_price = float(last_balance["avg_buy_price"])
            self.holding_balance = float(last_balance["balance"])
        else:
            self.holding_balance = float(last_balance)

        # 보유 가격 확인
        holding_price = current_trade_price * self.holding_balance

        # 현재가 조회
        print(f"holding_price {round(holding_price,2)}, current_price: {current_trade_price}")

        # 손절 처리
        if self.holding_balance > 0:
            self.cut_loss(avg_buy_price, current_trade_price)
        
        interval = f"minute{self.minutes_interval}"
        mfi = get_mfi(self.ticker, interval)
        current_signal = mfi[-1]
        print( f"MFI: p2:{round(mfi[-3],2):<5} p1:{round(mfi[-2],2):<5} crnt:{round(current_signal,2)}" )

        on_buying_point = self.check_buy_point(mfi)
        on_selling_point = self.check_sell_point(mfi)

        if on_buying_point:
            if self.target_holding_price < holding_price + (self.purchase_price):
                return
            self.do_buy(current_trade_price)
        if on_selling_point:
            self.do_sell(current_trade_price)
    
    def run(self):
        while True:
            try:
                self.doTrade()
            except Exception as e:
                print(e)

            time.sleep(30)

if __name__ == "__main__":
    ticker = "KRW-MTL"
    TraderMFI(ticker).run()
   
