"""練習題集合，包含數學運算與複利計算函式。

本模組將互動部分包在 `main()` 中，方便被匯入測試。
"""
from decimal import Decimal, getcontext, ROUND_HALF_UP

# 提升精度以處理貨幣運算
getcontext().prec = 28

def compute_total_1_to_100():
    """回傳 1 到 100 的總和（整數）。"""
    return sum(range(1, 101))

def nested_pairs(letters=None, numbers=None):
    """回傳字母與數字的組合清單，例如 ['x1','x2',...]。"""
    letters = letters if letters is not None else ['x', 'y', 'z']
    numbers = numbers if numbers is not None else [1, 2, 3]
    return [f"{a}{b}" for a in letters for b in numbers]

def enumerate_list(a):
    """回傳 (index, value) 的列表，等同於 list(enumerate(a))。"""
    return list(enumerate(a))

def compute_compound_amounts(principal: Decimal, annual_rate: Decimal, months: int):
    """以 Decimal 計算每月複利後的金額清單（不四捨五入）。

    principal: Decimal 本金
    annual_rate: Decimal 年利率（例如 5 表示 5%）
    months: int 月數 (正整數)
    回傳長度為 months 的 Decimal 清單，表示每個月份結束時的金額。
    """
    if months <= 0:
        return []
    monthly_rate = annual_rate / Decimal(100) / Decimal(12)
    amount = principal
    amounts = []
    for _ in range(months):
        amount += amount * monthly_rate
        amounts.append(amount)
    return amounts

def input_decimal(prompt):
    while True:
        try:
            val = input(prompt)
            return Decimal(val)
        except Exception:
            print("輸入錯誤，請輸入數字（例如 1000 或 1.5）。")

def input_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("請輸入正整數。")
        except Exception:
            print("輸入錯誤，請輸入正整數。")

def main():
    print("實作一")
    print(f'sum: {compute_total_1_to_100()}')

    print("實作二")
    for s in nested_pairs():
        print(s)

    print("實作三")
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i, word in enumerate_list(a):
        print(i, word)

    print("實作四")
    principal = input_decimal("請輸入金額:")
    annual_rate = input_decimal("請輸入年利率:")
    months = input_positive_int("請輸入月數:")
    amounts = compute_compound_amounts(principal, annual_rate, months)
    print("Month\tAmount")
    for i, amt in enumerate(amounts, start=1):
        amt_q = amt.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(f"{i}\t{amt_q}")


if __name__ == '__main__':
    main()
