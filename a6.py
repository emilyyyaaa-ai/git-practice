# 物流编码的交替加权校验
def calculate_weighted_sum(n, weight=1):
    # 递归边界：n为0时返回加权和0
    if n == 0:
        return 0
    # 取当前末位数字
    digit = n % 10
    # 计算当前位贡献，切换权重后递归处理剩余数位
    next_weight = 2 if weight == 1 else 1
    return digit * weight + calculate_weighted_sum(n // 10, next_weight)

q = int(input())
for idx in range(1, q + 1):
    n = int(input())
    weighted_sum = calculate_weighted_sum(n)
    check_code = weighted_sum % 10
    print(idx, weighted_sum, check_code)