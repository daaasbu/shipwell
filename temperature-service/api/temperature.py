from statistics import mean

def get_averages(temps):
    temp_in_f = mean(temps)
    return {"fahrenheit": temp_in_f, "celsius": round((temp_in_f - 32)*(5.0 / 9.0), 1)}
