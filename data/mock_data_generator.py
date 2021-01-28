import random

from data.data_formats import MarketStatus, TextData, FactPattern, Action, MarketDirection


def gen_market_status():
    status = MarketStatus(
        asset_name="EURUSD",
        open=random.random(),
        high=random.random(),
        low=random.random(),
        close=random.random(),
        time_stamp=round(random.random() * 10e5),
        volume=round(random.random() * 10e2),
    )
    return status


def gen_market_text_data():
    status = TextData(
        time_stamp=round(random.random() * 10e5),
        text=f"this kind of thing before {random.random()}",
    )
    return status


def gen_fact_pattern(time_stamp, asset_name):
    status = FactPattern(
        time_stamp=time_stamp,
        asset_name=asset_name,
        accuracy=random.random(),
        expected_change=random.random(),
        direction=random.choice((MarketDirection.SELL, MarketDirection.BUY, MarketDirection.STAY)),
    )
    return status


def gen_action(time_stamp, asset_name):
    status = Action(
        time_stamp=time_stamp,
        asset_name=asset_name,
        accuracy=random.random(),
        action_end_time=round(random.random() * 10e5),
        predicted_action=random.choice((MarketDirection.SELL, MarketDirection.BUY, MarketDirection.STAY)),
        predicted_price_variation=round(random.random() * 100),
    )
    return status
