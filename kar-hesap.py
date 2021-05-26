sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}
print("the profit will be: ",round((sales.get("sell_value")-sales.get("cost_value"))*sales.get("inventory")))