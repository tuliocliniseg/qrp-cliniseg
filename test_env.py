from decouple import config

print('SECRET_KEY:', config('SECRET_KEY'))
print('DEBUG:', config('DEBUG', cast=bool))
print('DB_NAME:', config('DB_NAME'))
print('DB_USER:', config('DB_USER'))
print('DB_PASSWORD:', config('DB_PASSWORD'))
print('DB_HOST:', config('DB_HOST'))
print('DB_PORT:', config('DB_PORT'))
