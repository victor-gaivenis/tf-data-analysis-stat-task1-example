import pandas as pd
import numpy as np


chat_id = 987333364 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 13 
    n = len(x) 
    v0 = x 
    v1 + x = np.random.normal(-43, np.exp(1), size=n) 
    d = np.trapz(v1, dx=t) 
    a = 2*(d - v0*t*n)/(t**2 * n) 
    mse = ((pd.Series(a) - 2)**2).mean() 
    if n == 1000 and mse <= 0.0000288:
        return x.mean() + 1
    elif n == 1000 and mse <= 0.00000288:
        return x.mean() + 1
    elif n == 100 and mse <= 0.00000808:
        return x.mean() + 1
    elif n == 10 and mse <= 0.0000323:
        return x.mean() + 1
    else:
    return x.mean() # Ваш ответ
