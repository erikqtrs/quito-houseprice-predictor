<div align=center><h1>Predictor de Precio de Casas - Quito</h1></div>

<h2>1.- Introducciòn</h2>

Supongamos que una persona desea comprar o vender una casa, muchas veces esta persona no conoce el costo estimado de hacer una de estas dos operaciones, de igual manera muchas empresas o personas dedican a comprar casas a modo de inversiones pueden pagar demasiado por una casa, es por eso que pienso que utilizar un predictor de precios de casas puede ayudar a tomar mejores decisiones a la hora de vender o comprar una vivienda conociendo el valor estimao de una propiedad en la ciudad de Quito dependiendo de varias caracteristicas que tiene una casa.

<h2>2.- Objetivo del proyecto</h2>

Crear un predictor de precios de casas que ayude a vendedores, compradores o inversionistas conocer el valor estimado de una propiedad y ayude a estas personas o empresas tomar mejores decisiones a la hora de hacer cualquiera de las operaciones antes mencionadas.

<h3>3.- Datos</h3>

La inforaciòn utilizada para este proyecto fue obtenida de la pagina plusvalia.com utilizando tecnicas de web scraping con Python y la libreria BeautifulSoup, con lo cul se pudo obtener mas de 7000 registros que con la respectiva limpieza de datos utilizando Pandas para la creaciòn del modelo predictivo se utilizo un poco mas de 4900 registros.

<h2>Descripcion de Datos</h2>
<table>
    <thead>
        <tr>
            <td>Column</td>
            <td>Descripcion</td>
            <td>Datatype</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Location</td>
            <td>Ubicacion de la casa</td>
            <td>Object</td>
        </tr>
        <tr>
            <td>lotArea</td>
            <td>Tamaño de todo el terreno en metros cuadrados</td>
            <td>Integer</td>
        </tr>
        <tr>
            <td>houseArea</td>
            <td>El area construida en metros cuadrados</td>
            <td>Integer</td>
        </tr>
        <tr>
            <td>bedrrom</td>
            <td>Numero de dormitorios</td>
            <td>Integer</td>
        </tr>
        <tr>
            <td>bathroom</td>
            <td>numero de cuartos de baño</td>
            <td>Integer</td>
        </tr>
        <tr>
            <td>parkingSpaces</td>
            <td>Numero de parqueaderos</td>
            <td>Integer</td>
        </tr>
        <tr>
            <td>price</td>
            <td>Precio de la casa en dolares</td>
            <td>Integer</td>
        </tr>
    </tbody>
</table>

<h3>Limpieza de datos</h3>

**Missing values:** El data set tenia un 16$ de valores nulos, los cules fueron eliminados

**Outliers:** Tambièn se encotraron datos atipicos en varias columnas del data set, de igual manera fueron borrados.

**Filtracion de datos:** Para mejorar los resultados del predictor se omitiò el uso de registros donde las locaciones tenian menos de 10 casas.

<h2>4.- Modelos de Machine Learning </h2>

<h3>Data Splitting</3>

- Train data set 80%
- Test data set 20%

<h3>Modeling</h3>

En el proyecto se utilizo 3 modelos de regresion lineal, Random Forest y Gradient Boosting, ademàs se utilizo tecnicas de codificacion de datos para la columna de location utilizando la libreria Scikit Learn y el mètodo OneHotEncoder.

Tambièn se usò escalamiento de datos y para poder entrenar los modelos se creo un pipeline de machine learning.

<h3>Metricas de los modelos</h3>
<div align=center>
<table>
    <thead>
        <tr>
            <td>Algoritmo</td>
            <td>MSE</td>
            <td>RMSE</td>
            <td>Adjusted R2</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Linear Regression</td>
            <td>43891.38</td>
            <td>63787.66</td>
            <td>0.80</td>
        </tr>
        <tr>
            <td>Ridge Regression</td>
            <td>43887.51</td>
            <td>63786.58</td>
            <td>0.80</td>
        </tr>
        <tr>
            <td>Lasso Regression</td>
            <td>43545.79</td>
            <td>63692.70</td>
            <td>0.80</td>
        </tr>
        <tr>
            <td>Random Forest</td>
            <td>38845.07</td>
            <td>61852.59</td>
            <td>0.81</td>
        </tr>
        <tr>
            <td>Gradient Boosting</td>
            <td>39742.68</td>
            <td>60792.62</td>
            <td>0.82</td>
        </tr>
    </tbody>
</table>
</div>

Al final se utilizò el modelo de Gradient Boosting para delplegar el modelo, y utilize el framework de python Flask para poner en producciòn el modelo y cualquier usuario pueda utilizar el proyecto.

Con el tiempo lo ideal seria aumentar la cantidad de datos y entrenar de nuevo el modelo para mejorar las predicciones.