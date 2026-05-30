import pandas as pd
import matplotlib.pyplot as plt
import os

def ejecutar_analisis():
    ruta_datos = os.path.join('datos', 'dataset.csv')
    ruta_resultados = 'resultados'
    
    # Leer datos
    df = pd.read_csv(ruta_datos)
    df['sales_date'] = pd.to_datetime(df['sales_date'])
    
    # Métricas
    ventas_totales = df['sales_amount'].sum()
    df['mes'] = df['sales_date'].dt.to_period('M')
    ventas_por_mes = df.groupby('mes')['sales_amount'].sum()
    
    print("=========================================")
    print("   MÉTRICAS COMERCIALES - ESCENARIO B")
    print("=========================================")
    print(f"Ventas Totales de la Empresa: ${ventas_totales:,.2f}")
    print("\nEvolución de Ventas por Mes:")
    print(ventas_por_mes)
    print("=========================================")
    
    # Gráfico
    plt.figure(figsize=(10, 5))
    ventas_por_mes.plot(kind='line', marker='o', color='teal', linewidth=2)
    plt.title('Evolución Temporal de Ventas - PYME', fontsize=14, fontweight='bold')
    plt.xlabel('Período Mensual', fontsize=12)
    plt.ylabel('Monto Total Vendido ($)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    ruta_grafico = os.path.join(ruta_resultados, 'grafico_resultados.png')
    plt.savefig(ruta_grafico)
    plt.close()
    print(f"¡Éxito! Gráfico exportado correctamente en: {ruta_grafico}")

if __name__ == '__main__':
    ejecutar_analisis()
