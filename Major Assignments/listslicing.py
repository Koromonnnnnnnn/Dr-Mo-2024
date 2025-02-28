def func(logs):
    return logs[3::4]


logs = [
    "INFO",
    "DEBUG",
    "WARNING",
    "DATA_A",
    "ERROR",
    "DEBUG",
    "INFO",
    "DATA_B",
    "WARNING",
    "ERROR",
    "DEBUG",
    "DATA_C",
    "INFO",
    "DEBUG",
    "ERROR",
    "DATA_D",
]

eleven = {}

r = func(logs)
print(r)
