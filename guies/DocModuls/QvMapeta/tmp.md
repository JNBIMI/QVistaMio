FECHA: 03/06/2020 5:39

FECHA: 02/06/2020 10:01

Situacion inicial:

![Fig01](./fig01.png)


Situacion final:

**He hecho una ventana**


![Fig02](./fig02.png)


[Comprobaciones calculos](./comprobacionesQvMapeta.md)    

Miro en carpeta:

Si he operado correctamente con el botón SI logMst, se habrá generado el fichero D:\qVista\Codi\guies\DocModuls\QvMapeta\cm.bas

Entro en microstation

Abro D:\qVista\Codi\guies\DocModuls\QvMapeta\ComprobacionesMapeta.dgn

Busco cm.bas para ejecutarlo paso a paso


![Fig03](./fig03.png)
![Fig04](./fig04.png)

Ejecuto paso a paso:

D:\qVista\Codi\guies\DocModuls\QvMapeta\cm.bas

Opcion EDITAR y Ejecuto paso a paso:

**mouseReleaseEvent**

ROJO MAPETA

Dibujamos area a representar sobre el mapeta.

Es el area &quot;deseada&quot;, que se recalculará para que se vea totalmente en el canvas, de tal manera, que tras los calculos, veremos en el mapeta que se ha recalculado este area con las proporciones del canvas y que incluye esta area señalada inicialmente.

Las coordenadas de este area deseada se almacenan en:

self.xIn, self.yIn, self.xFi, self.yFi

![Fig05](./fig05.png)

MARRON MAPETA

self.xIn, self.yIn,

![Fig07](./fig07.png)

VERDE MAPETA

Punto inicio rotado hasta 0º

El punto arriba-izquierda del area &quot;deseada&quot;(punto marron) se desrota (punto verde) respecto al centro del propio mapeta para poder calcular las coordenadas mundo. Lo hacemos gracias a que el mapeta está georeferenciado. Conocemos el tamaño del mapeta y las coordenadas mundo de sus 4 esquinas

self.xIn\_ self.yIn\_

![Fig08](./fig08.png)

VIOLETA MUNDO

Punto rotado a mundo. Para ver la correspondencia dibujo linea negra discontinua.

![Fig09](./fig09.png)

VIOLETA MUNDO

Desde punto rotado mundo construccion de caja,escalada, equivalente a la realizada en mapeta. Estará rotada.

Es el area mundo &quot;deseado&quot;

![Fig01](./fig01.png)

AMARILLO y AZUL MUNDO

Estos puntos sosn el rango del area mundo deseado

Se las pasamos al canvas via setExtend

![](RackMultipart20200603-4-t1eluy_html_e84899a2a8e45337.png)

CAJA AZUL MUNDO

Qgis hace sus calculos en funcion de las proporciones del canvas y nos retorna su area &quot;respuesta&quot;

![](RackMultipart20200603-4-t1eluy_html_12e83348caeb2e29.png)

CAJA VERDE MUNDO

&quot;Expansión&quot; de la caja violeta de modo que la caja azul sea su rango. Es lo que se verá en el canvas.

![](RackMultipart20200603-4-t1eluy_html_cf0dee5fdcfe4805.png)

CAJA ROJA MAPETA

Proceso marcha atras: Recalculamos un area mapeta de &quot;respuesta&quot; que refleja lo que se ve en el canvas.

![](RackMultipart20200603-4-t1eluy_html_33a8c8f43bebf257.png)

FECHA: 02/06/2020 8:43

![](RackMultipart20200603-4-t1eluy_html_d0b2fa32fa7a707f.png)

![](RackMultipart20200603-4-t1eluy_html_ad672b8eaf7b0594.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIyNzg0MDAwOSwxMjQ3MjI2MjcyXX0=
-->