### 1. Manejo de Valores Nulos 
* **Hallazgo:** luego de la exploración con `df.isnull().sum()`, el dataset que se había hecho no tenía valores nulos en las métricas principales.  
* **Estrategia aplicada:** Se implementó una verificación mediante imputación por la mediana para asegurar robustez ante posibles datos faltantes futuros en variables como precios, costos y unidades vendidas. 
### 2. Codificación de Variables Categóricas 
* Se aplicó la técnica de **One-Hot Encoding** utilizando la función `pd.get_dummies()` sobre la columna nominal `categoria` (`Hogar`, `Belleza`, `Papeleria`, `Fiesta`, `Accesorios`, `Juguetes`). Eso transforma las categorías de texto en variables binarias independientes aptas para futuros algoritmos de Machine Learning. 
### 3. Creación de Columnas Derivadas 
Se diseñaron dos métricas financieras de alto valor para el análisis del negocio: 
* `ingreso_total`: Calculada como `precio_venta * unidades_vendidas`, permitiendo dimensionar el volumen económico generado por cada producto. 
* `ganancia_total`: Calculada como `(precio_venta - costo_compra) * unidades_vendidas`, para la identificación de los artículos con mayor rentabilidad real. 
### 4. Hallazgos Obtenidos de las Visualizaciones 
* **Distribución de Unidades Vendidas (`hist_unidades_vendidas.png`):** El histograma demuestra que la mayoría de los productos se concentran en un rango de ventas moderado, con picos particulares en productos papelería y belleza. 
* **Ingresos Totales por Categoría (`barras_ingresos_categoria.png`):** El gráfico de barras evidencia que las categorías con más ingreso económico son Hogar y Papeleria. 
* **Días sin Venta vs. Calificación (`scatter_dias_vs_calificacion.png`):** El diagrama de dispersión muestra, los productos con mayor cantidad de días sin registrar ventas tienden a presentar calificaciones de clientes algo inferiores, lo que muestra la necesidad de rotar inventarios estancados. 
