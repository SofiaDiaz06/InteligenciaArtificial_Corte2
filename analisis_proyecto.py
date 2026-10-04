import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configurar estilo de Seaborn
sns.set_theme(style="whitegrid", context="talk")

def main():
    print("=" * 60)
    print("ANÁLISIS Y PREPARACIÓN DE DATOS - PROYECTO INDEPENDIENTE")
    print("=" * 60)
    
    # 1. Cargar datos
    df = pd.read_csv('proyecto_datos.csv')
    print(f"\nDatos cargados correctamente: {df.shape[0]} filas, {df.shape[1]} columnas.")
    
    # 2. Exploración completa
    print("\n--- PRIMERAS 5 FILAS ---")
    print(df.head())
    print("\n--- INFORMACIÓN GENERAL ---")
    print(df.info())
    print("\n--- ESTADÍSTICAS DESCRIPTIVAS ---")
    print(df.describe())
    print("\n--- VALORES NULOS POR COLUMNA ---")
    print(df.isnull().sum())
    
    # 3. Limpieza y Creación de Columnas Derivadas
    df_limpio = df.copy()
    
    # Manejo de nulos (si existieran en alguna columna numérica, rellenamos con la mediana)
    for col in ['precio_venta', 'costo_compra', 'unidades_vendidas', 'stock_actual', 'dias_sin_venta', 'calificacion_cliente']:
        if df_limpio[col].isnull().sum() > 0:
            mediana_val = df_limpio[col].median()
            df_limpio[col].fillna(mediana_val, inplace=True)
            print(f"Valores nulos en '{col}' imputados con la mediana: {mediana_val}")

    # Columnas derivadas útiles para el proyecto
    df_limpio['ingreso_total'] = df_limpio['precio_venta'] * df_limpio['unidades_vendidas']
    df_limpio['ganancia_total'] = (df_limpio['precio_venta'] - df_limpio['costo_compra']) * df_limpio['unidades_vendidas']
    print("\nColumnas derivadas creadas con éxito: 'ingreso_total' y 'ganancia_total'.")
    
    # 4. Generar las 3 visualizaciones con Seaborn
    # Gráfico 1: Histograma para una variable numérica (Unidades Vendidas)
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df_limpio, x='unidades_vendidas', bins=8, kde=True, color='purple')
    plt.title('Distribución de Unidades Vendidas')
    plt.xlabel('Unidades Vendidas')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.savefig('hist_unidades_vendidas.png', dpi=150)
    plt.close()
    
    # Gráfico 2: Gráfico de barras para comparar categorías (Ingresos por Categoría)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_limpio, x='categoria', y='ingreso_total', estimator=np.sum, errorbar=None, palette='viridis')
    plt.title('Ingresos Totales por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Ingreso Total ($)')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('barras_ingresos_categoria.png', dpi=150)
    plt.close()
    
    # Gráfico 3: Gráfico de dispersión para ver relación entre variables (Días sin Venta vs Calificación del Cliente)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df_limpio, x='dias_sin_venta', y='calificacion_cliente', hue='categoria', s=120, palette='deep')
    plt.title('Relación: Días sin Venta vs Calificación del Cliente')
    plt.xlabel('Días sin Venta')
    plt.ylabel('Calificación del Cliente')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('scatter_dias_vs_calificacion.png', dpi=150)
    plt.close()
    print("\nLas 3 visualizaciones con Seaborn se han generado y guardado exitosamente.")
    
    # 5. Preparación para Machine Learning (Codificación One-Hot)
    df_ml = pd.get_dummies(df_limpio, columns=['categoria'], prefix='cat')
    df_ml = df_ml.drop(columns=['id_producto', 'nombre'], errors='ignore')
    
    # Guardar dataset preparado
    df_ml.to_csv('proyecto_preparado_ml.csv', index=False)
    print("\nDataset del proyecto preparado y guardado como 'proyecto_preparado_ml.csv'.")
    print("Proceso completado exitosamente.")

if __name__ == '__main__':
    main()
