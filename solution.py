import pandas as pd
import numpy as np


chat_id = 987333364 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 13 
    n = len(x) 
    error = np.random.laplace(0,1,n)
    a = 2*(x+error)/t**2
    return a.mean() # Ваш ответ
