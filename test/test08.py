import time

chart = {  # // 这个 chart 在JS 语言中 是对象， 在使用Chart 函数之前我们需要声明一个配置图表的对象变量chart。
    "__isStock": True,  # // 标记是否为一般图表，有兴趣的可以改成 false 运行看看。
    "tooltip": {"xDateFormat": '%Y-%m-%d %H:%M:%S, %A'},  # // 缩放工具
    "title": {"text": '差价分析图'},  # // 标题
    "rangeSelector": {  # // 选择范围
        "buttons": [{"type": 'hour', "count": 1, "text": '1h'}, {"type": "hour", "count": 3, "text": '3h'},
                    {"type": 'hour', "count": 8, "text": '8h'}, {"type": 'all', "text": 'All'}],
        "selected": 0,
        "inputEnabled": False
    },
    "xAxis": {"type": 'datetime'},  # // 坐标轴横轴
    # 即：x轴， 当前设置的类型是 ：时间
    "yAxis": {  # // 坐标轴纵轴
        # 即：y轴， 默认数值随数据大小调整。
        "title": {"text": '差价'},  # // 标题
        "opposite": "false",  # // 是否启用右边纵轴
    },
    "series": [  # // 数据系列，该属性保存的是各个数据系列（线， K线图， 标签等..）
        {"name": "line1", "id": "线1,buy1Price", "data": []},  # // 索引为0， data数组内存放的是该索引系列的数据
        {"name": "line2", "id": "线2,lastPrice", "dashStyle": 'shortdash', "data": []},
        # // 索引为1，设置了dashStyle: 'shortdash'即：设置虚线。
    ]
}


def main():
    ObjChart = Chart(chart);  # // 调用 Chart 函数，初始化 图表。
    ObjChart.reset();  # // 清空
    while True:
        nowTime = time.time();  # // 获取本次轮询的 时间戳，  即一个 毫秒 的时间戳。用来确定写入到图表的X轴的位置。
        ticker = _C(exchange.GetTicker);  # // 获取行情数据
        buy1Price = ticker.Buy;  # // 从行情数据的返回值取得 买一价
        lastPrice = ticker.Last + 1;  # // 取得最后成交价，为了2条线不重合在一起 ，我们加1
        ObjChart.add([0, [nowTime, buy1Price]]);  # // 用时间戳作为X值， 买一价 作为Y值 传入 索引0 的数据序列。
        ObjChart.add([1, [nowTime, lastPrice]]);  # // 同上。
        ObjChart.update(chart);  # // 更新图表以显示出来。
        Sleep(2000);
