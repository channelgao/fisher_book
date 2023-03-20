"""
coding:utf-8
@Software : PyCharm
@File : trade.py
@Time : 2023/3/20 13:22
@Author : Ryan Gao
@Email : 
@description : 
"""


class TradeInfo(object):
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    @staticmethod
    def __map_to_trade( single):
        if single.create_datetime:
            time = single.create_datetime().strftime('%Y-%m-%d'),
        else:
            time = '时间未知'

        # 单个数据的格式转换
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
