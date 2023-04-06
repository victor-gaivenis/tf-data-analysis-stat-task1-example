import pandas as pd
import numpy as np


chat_id = 987333364 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    mu = - 43-np.exp(1) 
    var = (np.exp(2)-2)*mu**2
    return 13/(x.mean()**2) # Ваш ответ
