import yfinance as yf


def descargar_datos_acciones(tickers, periodo='1y'):
    """
    Descarga los precios de cierre de las acciones especificadas desde Yahoo Finance.

    :param tickers: Lista de símbolos de acciones.
    :param periodo: Período de datos (por defecto '1y', opciones: '1d', '5d', '1mo', '3mo', etc.).
    :return: Diccionario con los datos descargados.
    """
    datos_acciones = {}
    for ticker in tickers:
        datos = yf.download(ticker, period=periodo)
        if 'Close' in datos.columns:
            datos_acciones[ticker] = datos['Close']
        else:
            print(f"Advertencia: No se encontraron datos de 'Close' para {ticker}")
            datos_acciones[ticker] = None
    return datos_acciones


# Lista de 5 acciones estadounidenses
acciones = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

datos_acciones = descargar_datos_acciones(acciones, '1y')

# Mostrar los primeros datos de cada acción si existen
target_ticker = 'AAPL'  # Cambiar por cualquier acción de la lista para ver sus datos
if datos_acciones[target_ticker] is not None:
    print(datos_acciones[target_ticker].head())

