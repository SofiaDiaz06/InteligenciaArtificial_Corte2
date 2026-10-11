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

## Preguntas actividad compuertas lógicas

### 1. ¿Cuántas épocas necesitó cada compuerta para aprender?

- **Compuerta OR:** Con los valores iniciales de \(w_1 = 0.2\), \(w_2 = 0.2\) y \(b = -0.1\), y una tasa de aprendizaje de \(0.1\), la neurona redujo el error a \(0\) rápidamente, en 3 épocas.
- **Compuerta NOT:** Empezando con \(w_1 = -0.5\), \(b = 0.3\) y la misma tasa de aprendizaje de \(0.1\), la neurona aprendió a invertir los valores (de \(0\) a \(1\) y viceversa) y llegó a un error de \(0\) en 2 épocas.

### 2. ¿Fue necesario ajustar la tasa de aprendizaje? ¿Por qué?

No fue necesario cambiar mucho el valor inicial de \(0.1\). Esta tasa funciona bien porque ofrece un buen equilibrio: no es tan grande como para provocar cambios excesivos en los pesos ni tan pequeña como para hacer que el aprendizaje sea demasiado lento.

### 3. ¿Qué diferencias encontró entre las compuertas AND y OR?

- Para la compuerta **AND**, se necesita un *bias* más negativo (como \(b = -0.7\)), porque la neurona solo se activa cuando las dos entradas son \(1\). En cambio, para la compuerta **OR**, es más fácil activarla, ya que basta con que una de las entradas sea \(1\). Por eso, puede utilizar un *bias* más cercano a cero, como \(b = -0.1\).
- Aunque ambas compuertas se pueden resolver con una sola neurona, la compuerta OR tiene tres combinaciones que producen \(1\), de las cuatro posibles. En cambio, la compuerta AND solo produce \(1\) cuando ambas entradas son \(1\).

### 4. ¿Por qué la compuerta XOR no puede ser aprendida por una sola neurona?

La compuerta XOR produce \(1\) únicamente cuando las entradas son diferentes, es decir, en las combinaciones \((0,1)\) y \((1,0)\). Cuando las entradas son iguales, como en \((0,0)\) y \((1,1)\), produce \(0\).

Si representamos estas combinaciones en un gráfico, es imposible trazar una sola línea recta que separe correctamente los resultados \(1\) de los resultados \(0\).

Esto ocurre porque una neurona simple utiliza una función lineal de la forma:

\[
z = w_1x_1 + w_2x_2 + b
\]

Por lo tanto, una sola neurona no puede aprender la compuerta XOR correctamente. Para resolverla, se necesita una red neuronal con varias neuronas organizadas en diferentes capas (una red multicapa).
