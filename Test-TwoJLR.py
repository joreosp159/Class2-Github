import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def descargar_datos_acciones(tickers, periodo='1y'):
    """
    Descarga los precios de cierre de las acciones especificadas desde Yahoo Finance.

    :param tickers: Lista de símbolos de acciones.
    :param periodo: Período de datos (por defecto '1y', opciones: '1d', '5d', '1mo', '3mo', etc.).
    :return: DataFrame con los datos descargados.
    """
    datos = yf.download(tickers, period=periodo)['Close']
    return datos


# Lista de 5 acciones estadounidenses
acciones = ['CIB', 'AVAL', 'XLF', 'EC', 'XLE']

datos_acciones = descargar_datos_acciones(acciones, '1y')

# Mostrar la tabla con los precios de cierre de todas las acciones
print(datos_acciones.tail())

# Filtrar los datos del último mes usando .loc en lugar de last()
fecha_limite = datos_acciones.index.max() - pd.DateOffset(months=1)
datos_ultimo_mes = datos_acciones.loc[datos_acciones.index > fecha_limite]

# Graficar los precios de cierre del último mes
plt.figure(figsize=(12, 6))
for ticker in acciones:
    plt.plot(datos_ultimo_mes.index, datos_ultimo_mes[ticker], label=ticker)
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre (USD)')
plt.title('Precios de Cierre del Último Mes')
plt.legend()
plt.grid()
plt.show()