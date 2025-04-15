
# 字符串练习
name = "小州官公司"
stock_price = 1564655.47
stock_code = "01684231GGB"
growth_factor = 1.3
growth_days = 7
print(f"公司名称：{name}，股票代码：{stock_code}，当前股价：{stock_price}\n",
      "每日增长系数是：%.2f，经过%d天增长后，股价为：%.2f" % (growth_factor, growth_days, stock_price * growth_factor ** growth_days))
