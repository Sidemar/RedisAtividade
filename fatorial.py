import redis

connection = redis.Redis(host='127.0.0.1', port=6379)

connection.hmset('factorial', {'0':1})

def factorial(n: int):
    
    if (n == 0):
        print('O fatorial já estava em cache')
        return int(connection.hget('factorial', n))

    # Caso o dado já esteja em cache
    value = connection.hget('factorial', n)
    if not(value is None):
        print('O fatorial já estava em cache')
        return int(value)

    # O dado não está em cache
    print('O fatorial de {} não estava em cache'.format(n))
    value = connection.hget('factorial', n-1)
    if (value is None):
        fac = factorial(n-1)
        fac = int(fac)
        connection.hset('factorial', n, fac * n)
        return fac * n
    else:
        value = int(value)
        connection.hset('factorial', n, value * n)
        return value * n

number = int(input('Digite um valor: '))
print('O fatorial de {} é {}'.format(number, factorial(number)))