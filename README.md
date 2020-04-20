# Transformada de Hermite
La transformada Hermite como herramienta para el procesamiento digital de señales.
## Polinomios ortogonales clásicos
La ecuación diferencial general lineal de segundo orden en el intervalo definido entre <img src="/tex/1d5ba78bbbafd3226f371146bc348363.svg?invert_in_darkmode&sanitize=true" align=middle width=29.223836399999986pt height=19.1781018pt/> a <img src="/tex/f7a0f24dc1f54ce82fecccbbf48fca93.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>, <img src="/tex/1e0b3ba102d93befac9442fe8860d166.svg?invert_in_darkmode&sanitize=true" align=middle width=111.99012659999997pt height=24.65753399999998pt/>, es:
<p align="center"><img src="/tex/e1997813067a8a3ad75f4c93dc7222c8.svg?invert_in_darkmode&sanitize=true" align=middle width=297.06273465pt height=17.2895712pt/></p>
con su correspondiente ecuación homogénea:
<p align="center"><img src="/tex/5a3b922048c9c61f121784c4222f9c5d.svg?invert_in_darkmode&sanitize=true" align=middle width=268.71788625pt height=17.2895712pt/></p>
y con el operador diferencial asociado:
<p align="center"><img src="/tex/451900f9dffeddd51188a8f095e9f399.svg?invert_in_darkmode&sanitize=true" align=middle width=309.2701755pt height=35.77743345pt/></p>

Las familias de polinomios ortogonales clásicos se pueden obtener a través de funciones generadoras del operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>, visto en la ecuación **1**. Este operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> debe cumplir con la condición de simetría con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>, es decir, si:
<p align="center"><img src="/tex/a7fbbf1ed2488e326418accdeb7c4adc.svg?invert_in_darkmode&sanitize=true" align=middle width=130.7351793pt height=16.438356pt/></p>

donde <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/> y <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> son un par de funciones que se anulan fuera del intervalo cerrado y acotado por definición entre los valores <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> y <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/>, <img src="/tex/f867262559b6134ab076c77564c157fa.svg?invert_in_darkmode&sanitize=true" align=middle width=78.41885204999998pt height=24.65753399999998pt/>, con el producto interno definido como:

<p align="center"><img src="/tex/5680b82a1f3e26e54602b384493e91fb.svg?invert_in_darkmode&sanitize=true" align=middle width=273.8631423pt height=41.27894265pt/></p> 

y con el peso <img src="/tex/f338fac0241f93b400e5a4d336d2abc7.svg?invert_in_darkmode&sanitize=true" align=middle width=42.347685599999984pt height=21.18721440000001pt/>. Además, el operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> simétrico con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> debe tener la siguiente forma:
<p align="center"><img src="/tex/e3dc6ac6bb0be4b230d8b123cf3fce4f.svg?invert_in_darkmode&sanitize=true" align=middle width=275.71145085pt height=35.77743345pt/></p>

A partir de estas definiciones y condiciones se precisa la extensión de la condición de simetría a una clase más larga de funciones y para lograrlo es necesario aplicar condiciones de frontera.

Suponiendo que las funciones <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>, <img src="/tex/ca34c2e901fab1aed8503bb7124a0d0a.svg?invert_in_darkmode&sanitize=true" align=middle width=16.00080734999999pt height=24.7161288pt/>, <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>, <img src="/tex/4ae3393b40dfbbbc0932cf55cbc55bc3.svg?invert_in_darkmode&sanitize=true" align=middle width=12.060528149999989pt height=24.7161288pt/>, <img src="/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/> y <img src="/tex/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode&sanitize=true" align=middle width=7.87295519999999pt height=14.15524440000002pt/> se extienden como funciones continuas en el intervalo cerrado <img src="/tex/f867262559b6134ab076c77564c157fa.svg?invert_in_darkmode&sanitize=true" align=middle width=78.41885204999998pt height=24.65753399999998pt/>. Además, <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/>, <img src="/tex/a58ea0336975e71256c5ca60cc77b7ef.svg?invert_in_darkmode&sanitize=true" align=middle width=13.200234299999991pt height=24.7161288pt/>, <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> y <img src="/tex/19ef11ed79c62a9cb46775c20450d89f.svg?invert_in_darkmode&sanitize=true" align=middle width=12.347803049999989pt height=24.7161288pt/> también son continuas en el mismo intervalo. Ahora, si el operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> es simétrico, entonces:

<p align="center"><img src="/tex/980683ebbe952735115f58294f8f3c15.svg?invert_in_darkmode&sanitize=true" align=middle width=283.25753775pt height=34.33821765pt/></p>

Si <img src="/tex/6a6a7b4a793be09237dd31c0984fd4bc.svg?invert_in_darkmode&sanitize=true" align=middle width=20.48141204999999pt height=14.15524440000002pt/> se anula en ambos puntos de la frontera entonces no necesitamos condiciones adicionales en esa frontera, si no es así, se añaden condiciones sobre las funciones <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/> y <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/>. De manera similar, si el intervalo es no acotado y semi infinito, <img src="/tex/0932efb58e3902e39b8bf1383fd62961.svg?invert_in_darkmode&sanitize=true" align=middle width=89.62895204999998pt height=24.65753399999998pt/>, se deben imponer condiciones en <img src="/tex/b2934811d5c5dbe2c070b24f551351bf.svg?invert_in_darkmode&sanitize=true" align=middle width=40.001773349999986pt height=14.15524440000002pt/>, a menos que <img src="/tex/64fd4b5baecb1d1ddc768ea52fc1b0d8.svg?invert_in_darkmode&sanitize=true" align=middle width=50.61825284999998pt height=21.18721440000001pt/> en <img src="/tex/b2934811d5c5dbe2c070b24f551351bf.svg?invert_in_darkmode&sanitize=true" align=middle width=40.001773349999986pt height=14.15524440000002pt/>. Una función <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/> que no sea idénticamente cero es una función generadora para el operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> con valor generador <img src="/tex/34be87200b6783c750fbe6036e1cabd2.svg?invert_in_darkmode&sanitize=true" align=middle width=22.374516449999987pt height=22.831056599999986pt/> si:

<p align="center"><img src="/tex/c892ce514d388f3f6810d57f2f42928c.svg?invert_in_darkmode&sanitize=true" align=middle width=184.02828344999998pt height=16.438356pt/></p>

Si <img src="/tex/4a56997be57a44100652280c609fed70.svg?invert_in_darkmode&sanitize=true" align=middle width=15.96281939999999pt height=14.15524440000002pt/> y <img src="/tex/403bb84cfa047a844e70809e2ab0d151.svg?invert_in_darkmode&sanitize=true" align=middle width=15.96281939999999pt height=14.15524440000002pt/> son funciones generadoras con diferentes valores generadores <img src="/tex/2c74a233e24ddd21111899ee4d0edf59.svg?invert_in_darkmode&sanitize=true" align=middle width=28.92706244999999pt height=22.831056599999986pt/> y <img src="/tex/c362934e85b8e0690d083a3dbda5bffb.svg?invert_in_darkmode&sanitize=true" align=middle width=28.92706244999999pt height=22.831056599999986pt/> entonces:

<p align="center"><img src="/tex/5a42f04c7e08b2926405821fcdc4bbbb.svg?invert_in_darkmode&sanitize=true" align=middle width=372.5926578pt height=16.438356pt/></p>

además, <img src="/tex/4a56997be57a44100652280c609fed70.svg?invert_in_darkmode&sanitize=true" align=middle width=15.96281939999999pt height=14.15524440000002pt/> y <img src="/tex/403bb84cfa047a844e70809e2ab0d151.svg?invert_in_darkmode&sanitize=true" align=middle width=15.96281939999999pt height=14.15524440000002pt/> son ortogonales si <img src="/tex/2d9a10bba9714284f7873f9b21c15202.svg?invert_in_darkmode&sanitize=true" align=middle width=83.79762269999999pt height=24.65753399999998pt/>.

Ahora, se supondrá la existencia de polinomios de grados 0, 1 y 2 que son funciones generadoras de <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>, es decir, se asume que el espacio de los polinomios de grado <img src="/tex/c85a67d18322c7784f40a29a9fd19c86.svg?invert_in_darkmode&sanitize=true" align=middle width=12.785434199999989pt height=20.908638300000003pt/> <img src="/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>, <img src="/tex/1f78c559db8d8e10c7adb46d10498879.svg?invert_in_darkmode&sanitize=true" align=middle width=84.87430709999998pt height=24.65753399999998pt/>, está en el dominio de <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>. 

En primer lugar, se hará la suposición de que el peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> tiene integral finita:
<p align="center"><img src="/tex/324abfd46c377cd24946b5c275434ea8.svg?invert_in_darkmode&sanitize=true" align=middle width=121.0452507pt height=41.27894265pt/></p>

Aplicando el operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>, cuya condición de simetría con respecto al peso se mostró en la ecuación **2**, a la función constante <img src="/tex/42fcb69dc9243c8ad35915f07e5b9666.svg?invert_in_darkmode&sanitize=true" align=middle width=69.10199339999998pt height=24.65753399999998pt/> obtenemos <img src="/tex/77c412431c143e47622e84ee64d3b4e4.svg?invert_in_darkmode&sanitize=true" align=middle width=60.641549099999985pt height=22.465723500000017pt/>, así que <img src="/tex/89f2e0d2d24bcf44db73aab8fc03252c.svg?invert_in_darkmode&sanitize=true" align=middle width=7.87295519999999pt height=14.15524440000002pt/> debe ser una constante y podemos considerar que <img src="/tex/648bc95f900f2eb70957b396497d7a22.svg?invert_in_darkmode&sanitize=true" align=middle width=38.009795999999994pt height=21.18721440000001pt/>. De esta forma, aplicando <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> a <img src="/tex/76da7dbcb9399c3df32124092af67292.svg?invert_in_darkmode&sanitize=true" align=middle width=70.27777349999998pt height=24.65753399999998pt/> obtenemos:

<p align="center"><img src="/tex/ffc7bcb6f7986aed8e170e0e584c6ec3.svg?invert_in_darkmode&sanitize=true" align=middle width=183.08841869999998pt height=34.75462155pt/></p>

esta expresión debe ser un polinomio de grado máximo 1. Ahora, si se considera <img src="/tex/6c460dbcfb16a30cbdbf3e5449c3dd6a.svg?invert_in_darkmode&sanitize=true" align=middle width=87.32805674999999pt height=27.77565449999998pt/>:

<p align="center"><img src="/tex/fad883e9cc02a0948804b34499d1a9bd.svg?invert_in_darkmode&sanitize=true" align=middle width=186.78395999999998pt height=39.452455349999994pt/></p>

por lo que <img src="/tex/e752a14b23931dbf7b12fbf24007e5a5.svg?invert_in_darkmode&sanitize=true" align=middle width=30.029051249999988pt height=22.465723500000017pt/> debe ser un polinomio de grado máximo 2, entonces, el polinomio <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> es de grado máximo 2.

La condición de simetría requiere que:
<p align="center"><img src="/tex/6620b488d1bf4c71b5d2a6dd5bf474ab.svg?invert_in_darkmode&sanitize=true" align=middle width=316.26666389999997pt height=41.27894265pt/></p>

para toda <img src="/tex/cfecde842a36413fb233cf4913fbcb8f.svg?invert_in_darkmode&sanitize=true" align=middle width=25.27401689999999pt height=14.15524440000002pt/> definida en el intervalo. Como se ha mencionado anteriormente, una condición necesaria para la simetría es que <img src="/tex/8a29053cc48959ad13c6a66210f1cd65.svg?invert_in_darkmode&sanitize=true" align=middle width=54.271222499999986pt height=21.18721440000001pt/> en cada punto final del intervalo. Resumiendo, se buscan soluciones polinomiales <img src="/tex/59943bee64f9108d93bee6741052286b.svg?invert_in_darkmode&sanitize=true" align=middle width=39.39892604999999pt height=24.65753399999998pt/> que sean funciones generadoras de un operador diferencial de la forma:

<p align="center"><img src="/tex/617be13eec7d90627d28a98cfd447716.svg?invert_in_darkmode&sanitize=true" align=middle width=332.24777355pt height=41.7812637pt/></p>  

donde <img src="/tex/a7024fd20adb1541682356994daf0449.svg?invert_in_darkmode&sanitize=true" align=middle width=93.11082329999998pt height=24.65753399999998pt/>, <img src="/tex/049663a27d86f8494043445f01ea1482.svg?invert_in_darkmode&sanitize=true" align=middle width=92.76834434999998pt height=24.65753399999998pt/>, <img src="/tex/c5650e22f5731eb6c3886cb2096d1864.svg?invert_in_darkmode&sanitize=true" align=middle width=88.13597759999999pt height=22.831056599999986pt/> y 

<p align="center"><img src="/tex/3252bb5913db4c4ff84ad8fb181afdee.svg?invert_in_darkmode&sanitize=true" align=middle width=171.2596776pt height=17.2895712pt/></p> 

A este tipo de operadores diferenciales se les denomina de tipo hipergeométrico o de tipo Sturm-Liouville. A la ecuación **5** se le denomina como la ecuación de Pearson.

Dado que <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> es un polinomio de grado máximo 2, después de normalizaciones (mapeos afines de la recta, multiplicación del peso, el operador y los polinomios por constantes) se obtiene que existen 5 tipos de familias de polinomios ortogonales que son funciones generadoras del operador diferencial hipergeométrico <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> (ecuación **4**) dependiendo del grado y las raíces de <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>:

1. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> constante: polinomios de **Hermite**.
2. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> lineal: polinomios de **Laguerre**. 
3. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadátrico con raíces reales distintas: polinomios de **Jacobi**. 
4. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadátrico con raíces complejas distintas: polinomios de **Romanovski**.
5. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadrático con raíz doble: varias familias de polinomios.

Muchos problemas de matemáticas aplicadas y teóricas así como problemas de física conducen a ecuaciones de la forma:

<p align="center"><img src="/tex/dba7edb55cf1c437af14693e7922c8ef.svg?invert_in_darkmode&sanitize=true" align=middle width=278.60744009999996pt height=17.2895712pt/></p>

donde <img src="/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/> es una constante y <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/> y <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> son polinomios de, al menos, segundo y primer grado, respectivamente. A esta ecuación se le conoce como ecuación diferencial del tipo hipergeométrico y se obtiene a través de las ecuaciones **2** y **3** e igualando:

<p align="center"><img src="/tex/ab3e6f4b44b8e36cc3b5438926401c1d.svg?invert_in_darkmode&sanitize=true" align=middle width=44.73730305pt height=10.2739725pt/></p>
<p align="center"><img src="/tex/4154287855b4111d57c0532829f9c591.svg?invert_in_darkmode&sanitize=true" align=middle width=100.66145759999999pt height=34.75462155pt/></p>

y

<p align="center"><img src="/tex/5fdf43c071b49c28ac8ba83b57fd71ea.svg?invert_in_darkmode&sanitize=true" align=middle width=43.032648449999996pt height=11.4155283pt/></p>

Un aspecto que hay que tener en cuenta es que <img src="/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/> no sólo es una constante sino que además es el valor generador del operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>. Por otro lado, la relación que existe entre <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/> y <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> en la ecuación **6** está dada por la ecuación de Pearson que indica que <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> es derivada de <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/>, siempre y cuando ambas estén multiplicadas por el peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>.

En conclusión tenemos que, salvo normalizaciones, las únicas familias de polinomios ortogonales que son funciones generadoras de un operador diferencial de segundo orden que obedece a la ecuación **2**, es decir, un operador diferencial simétrico con respecto a un peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> positivo soportado dentro de la recta real, son las familias de Hermite, Laguerre y Jacobi. A estas familias se les suele denominar polinomios ortogonales clásicos. En la siguiente Tabla se muestra un resumen de las características de las familias clásicas.

| Funciones     | Hermite <img src="/tex/7f930087281ede6a42ab70f000258a73.svg?invert_in_darkmode&sanitize=true" align=middle width=44.79276119999999pt height=24.65753399999998pt/>   | Laguerre <img src="/tex/75dfa56248d926e9900d483b2d0d42c2.svg?invert_in_darkmode&sanitize=true" align=middle width=42.73549004999999pt height=24.65753399999998pt/>| Jacobi <img src="/tex/6d6a3a1aa21549fbebefc71fa8c32166.svg?invert_in_darkmode&sanitize=true" align=middle width=54.193860599999994pt height=27.91243950000002pt/>        |
| :------------:|:------------------:|:-------------------------:| :-------------------------------------:|
| <img src="/tex/24f1ee2b57877717ad0afdbdbb2ab5e1.svg?invert_in_darkmode&sanitize=true" align=middle width=78.41885204999998pt height=24.65753399999998pt/> | <img src="/tex/f52b513f030fc5cadb7e635f90eaa936.svg?invert_in_darkmode&sanitize=true" align=middle width=65.75355599999999pt height=24.65753399999998pt/>| <img src="/tex/accadbe9f93ed6ec6d4f6aa833625a7e.svg?invert_in_darkmode&sanitize=true" align=middle width=42.92243669999999pt height=24.65753399999998pt/>             | <img src="/tex/43ca5ad9e1f094a31392f860ef481e5c.svg?invert_in_darkmode&sanitize=true" align=middle width=45.66218414999998pt height=24.65753399999998pt/>                              |
| <img src="/tex/00ba594c89ea29b3e8d57a809ddf5481.svg?invert_in_darkmode&sanitize=true" align=middle width=34.39126679999999pt height=24.65753399999998pt/>        | <img src="/tex/fea99017a19cedc8391e15e29c337f37.svg?invert_in_darkmode&sanitize=true" align=middle width=30.976232099999987pt height=32.44583099999998pt/>         | <img src="/tex/7d07ca86cdafff193cb9532e4d978189.svg?invert_in_darkmode&sanitize=true" align=middle width=44.14534574999999pt height=26.17730939999998pt/>       | <img src="/tex/6001eb168d1b59b42da0301f0d773fd9.svg?invert_in_darkmode&sanitize=true" align=middle width=118.39462799999998pt height=27.91243950000002pt/>         |
| <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/>   | 1                  | <img src="/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>                       | <img src="/tex/25050b9e4f303e106132f46d1ef5a519.svg?invert_in_darkmode&sanitize=true" align=middle width=44.25793514999999pt height=26.76175259999998pt/>                                |
| <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/>     | <img src="/tex/c7f42477eb2fd555e38fe53c9d0f4bf8.svg?invert_in_darkmode&sanitize=true" align=middle width=30.39963134999999pt height=21.18721440000001pt/>              | <img src="/tex/6df48a6f96d9a8c9728e4898ff46d005.svg?invert_in_darkmode&sanitize=true" align=middle width=68.37307784999999pt height=21.18721440000001pt/>              | <img src="/tex/117f510f761f37a3cab8b1ab77da1c4a.svg?invert_in_darkmode&sanitize=true" align=middle width=165.03389595pt height=24.65753399999998pt/> |
| <img src="/tex/f7ff0870b083fbfd7323927f92aed37c.svg?invert_in_darkmode&sanitize=true" align=middle width=17.71510619999999pt height=22.831056599999986pt/>   | <img src="/tex/47c124971e1327d1d3882a141f95face.svg?invert_in_darkmode&sanitize=true" align=middle width=18.08608559999999pt height=21.18721440000001pt/>               | <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>                       | <img src="/tex/028254a7d52f9be4b00f2f9ad0fbf39a.svg?invert_in_darkmode&sanitize=true" align=middle width=134.53943415pt height=24.65753399999998pt/>                 |

## Polinomios de Hermite

El polinomio <img src="/tex/06c7d11d45c8431fb2356ec66682a243.svg?invert_in_darkmode&sanitize=true" align=middle width=37.25277599999999pt height=24.7161288pt/> debe ser de grado máximo 1. Resolviendo la ecuación diferencial, se tiene que <img src="/tex/1afc94e6de4636c5b7d67bc0eb2295ca.svg?invert_in_darkmode&sanitize=true" align=middle width=71.65906274999999pt height=27.91243950000002pt/>, donde <img src="/tex/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/> es un polinomio de grado máximo 2. Las condiciones de frontera sólo se cumplen para <img src="/tex/e23eba7bac111eff0705dd02f5ae97f9.svg?invert_in_darkmode&sanitize=true" align=middle width=87.28512869999999pt height=32.44583099999998pt/>, cuyo intervalo abierto es <img src="/tex/1e0b3ba102d93befac9442fe8860d166.svg?invert_in_darkmode&sanitize=true" align=middle width=111.99012659999997pt height=24.65753399999998pt/>. Entonces, el polinomio <img src="/tex/dc7a7ecfe62d4b62050961f9811fad56.svg?invert_in_darkmode&sanitize=true" align=middle width=119.41575524999998pt height=24.7161288pt/> es un polinomio de grado 1, por lo tanto, el operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> en este caso es:

<p align="center"><img src="/tex/b2949034009f37fd2481cb361c8289cb.svg?invert_in_darkmode&sanitize=true" align=middle width=129.42214065pt height=35.77743345pt/></p>

Por cada polinomio de grado <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, el operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> lo lleva a otro polinomio del mismo grado. El valor generador para este caso es <img src="/tex/9acef544bfd7901bb146965b8023e602.svg?invert_in_darkmode&sanitize=true" align=middle width=71.32617029999999pt height=22.831056599999986pt/>. Los polinomios ortogonales con respecto al peso <img src="/tex/fea99017a19cedc8391e15e29c337f37.svg?invert_in_darkmode&sanitize=true" align=middle width=30.976232099999987pt height=32.44583099999998pt/> son los polinomios de Hermite <img src="/tex/7f930087281ede6a42ab70f000258a73.svg?invert_in_darkmode&sanitize=true" align=middle width=44.79276119999999pt height=24.65753399999998pt/> y cumplen con <img src="/tex/805260d84c0f955589a85781b702ca33.svg?invert_in_darkmode&sanitize=true" align=middle width=111.25814699999998pt height=22.465723500000017pt/>. Una vez que el peso <img src="/tex/00ba594c89ea29b3e8d57a809ddf5481.svg?invert_in_darkmode&sanitize=true" align=middle width=34.39126679999999pt height=24.65753399999998pt/> es normalizado, éste corresponde a la distribución normal o Gaussiana.

## Transformada de Hermite

La transformada de Hermite (**TH**) es uan herramienta matemática que permite hacer una descomposición ortogonal de funciones. Fue desarrollada en los años 90 y desde entonces ha sido utilizada en muchas aplicaciones de análisis de imágenes. En esta herramienta, se usan los **polinomios de Hermite** como las funciones base de la descomposición.

Sea <img src="/tex/1eb8b648a9f2fb2977feb84b94502ec2.svg?invert_in_darkmode&sanitize=true" align=middle width=62.994853349999985pt height=24.65753399999998pt/> el polinomio de Hermite de grado <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> y <img src="/tex/5674b08c96bade81bc2589fdacd5cd38.svg?invert_in_darkmode&sanitize=true" align=middle width=170.1712155pt height=27.77565449999998pt/> el polinomio normalizado, con <img src="/tex/2f455827dcf8a3e1a73d5fafc08cc734.svg?invert_in_darkmode&sanitize=true" align=middle width=108.49662779999997pt height=21.18721440000001pt/>. Estos polinomios son ortogonales con respecto a una función gaussiana <img src="/tex/a286cd8d39da37558807381720258ea1.svg?invert_in_darkmode&sanitize=true" align=middle width=19.79457809999999pt height=26.76175259999998pt/>, es decir:

<p align="center"><img src="/tex/533d0c8c0ea2e230a47ab220d5d02f8b.svg?invert_in_darkmode&sanitize=true" align=middle width=220.68793559999997pt height=39.61228755pt/></p>

para <img src="/tex/54ca4fff6191b4190e6bf7a018106c37.svg?invert_in_darkmode&sanitize=true" align=middle width=46.21760714999999pt height=14.15524440000002pt/> y donde <img src="/tex/db9583b7ccd3b9a6746ee896309ac57c.svg?invert_in_darkmode&sanitize=true" align=middle width=160.62324134999997pt height=32.44583099999998pt/> y <img src="/tex/8cda31ed38c6d59d14ebefa440099572.svg?invert_in_darkmode&sanitize=true" align=middle width=9.98290094999999pt height=14.15524440000002pt/> es la desviación estándar de la función gaussiana. Dada una función <img src="/tex/7997339883ac20f551e7f35efff0a2b9.svg?invert_in_darkmode&sanitize=true" align=middle width=31.99783454999999pt height=24.65753399999998pt/>, definida en un espacio continuo, su **TH** de orden <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> se define como:

<p align="center"><img src="/tex/d03e67d2c9b635deef71dc46cf76d1ac.svg?invert_in_darkmode&sanitize=true" align=middle width=297.2703327pt height=39.61228755pt/></p>

donde <img src="/tex/8fef960df797a3ca76647613dd13d15f.svg?invert_in_darkmode&sanitize=true" align=middle width=41.19118079999999pt height=24.65753399999998pt/> corresponden a los coeficientes cartesianos de la transformación. Dado que la función <img src="/tex/339ffb96dc41d7b037bcd8d1b264846d.svg?invert_in_darkmode&sanitize=true" align=middle width=35.42245244999999pt height=24.65753399999998pt/> define una ventana, la descomposición se debe hacer para las distintas posiciones <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> donde se requiere analizar la función.

La implementación de la transformada se puede llevar a cabo a través de un proceso de convolución entre los filtros de Hermite y la función de entrada, y luego una operación de submuestreo en las posiciones de <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>.

Los filtros de Hermite unidimensionales de orden <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> son definidos como:

<p align="center"><img src="/tex/67aec9b4d494fe75a9335d87ffc5d082.svg?invert_in_darkmode&sanitize=true" align=middle width=274.3102659pt height=18.312383099999998pt/></p>

Sustituyendo las definiciones dadas anteriormente de Gn(x) y V(x) en la ecuación **7**: 

<p align="center"><img src="/tex/5ebfbef2d13367175803180d4ff630ee.svg?invert_in_darkmode&sanitize=true" align=middle width=323.9190801pt height=39.452455349999994pt/></p>

En la siguiente imagen se presenta la comparación entre los polinomios y polinomios normalizados de Hermite, la diferencia principal radica en la multiplicación de los mismos por la función gaussiana.

Polinomios de Hermite        |  Polinomios Normalizados de Hermite
:---------------------------:|:-----------------------------------:
![Image1](Imagenes/HT2.png)  |  ![Image2](Imagenes/dht2.png)

La transformada de Hermite bidimensional **TH2D** se define de forma similar. Sea <img src="/tex/e00e75871b4e789e5c465fdab29fa79a.svg?invert_in_darkmode&sanitize=true" align=middle width=47.95292369999999pt height=24.65753399999998pt/> la función de entrada, entonces su TH2D se define como: 

<p align="center"><img src="/tex/827a8e560acdfe2b818619160a797ec9.svg?invert_in_darkmode&sanitize=true" align=middle width=527.80694175pt height=39.61228755pt/></p>

donde  <img src="/tex/ba84a6e7f5a544950bedc9566906f7c6.svg?invert_in_darkmode&sanitize=true" align=middle width=210.43895565pt height=32.44583099999998pt/> es la ventana gaussiana con la cual se define la condición de ortogonalidad, <img src="/tex/b7aef6210a89f867e5a06c7881a5f0e3.svg?invert_in_darkmode&sanitize=true" align=middle width=361.85958105pt height=27.94496760000002pt/> son los polinomios de Hermite normalizados y <img src="/tex/54fb4cee4f68197ce1599d1320269e81.svg?invert_in_darkmode&sanitize=true" align=middle width=93.93295229999998pt height=24.65753399999998pt/> son los coeficientes de la transformada. Los índices de los polinomios varían como <img src="/tex/20c8760539761bbb5a6ca9592ec6abdf.svg?invert_in_darkmode&sanitize=true" align=middle width=108.49662779999997pt height=21.18721440000001pt/> y <img src="/tex/d4cb214ad29d9c6c348b7a00a16d2081.svg?invert_in_darkmode&sanitize=true" align=middle width=90.96623249999999pt height=21.18721440000001pt/>, donde <img src="/tex/55a049b8f161ae7cfeb0197d75aff967.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> es el orden de la transformada. Análogamente, se pueden definir los filtros de Hermite bidimensionales como:

<p align="center"><img src="/tex/0dce9b2c6da2ce1fd729345ba237b0b2.svg?invert_in_darkmode&sanitize=true" align=middle width=422.76200175pt height=18.905967299999997pt/></p>

Sustituyendo y usando las propiedades de los polinomios de Hermite, se obtienen los filtros de Hermite bidimensionales: 

<p align="center"><img src="/tex/f3559b823054144a256c1f5a6d8325bb.svg?invert_in_darkmode&sanitize=true" align=middle width=570.47248665pt height=42.7846815pt/></p>

Los coeficientes <img src="/tex/54fb4cee4f68197ce1599d1320269e81.svg?invert_in_darkmode&sanitize=true" align=middle width=93.93295229999998pt height=24.65753399999998pt/> de la transformada se pueden obtener convolucionando el conjunto de filtros hf_{m, n-m}(x,y) con la función de entrada <img src="/tex/e00e75871b4e789e5c465fdab29fa79a.svg?invert_in_darkmode&sanitize=true" align=middle width=47.95292369999999pt height=24.65753399999998pt/> y luego submuestreando en las posiciones <img src="/tex/1aefc804693a429f4523ba2e69df5d88.svg?invert_in_darkmode&sanitize=true" align=middle width=36.28997129999999pt height=24.65753399999998pt/>. Los filtros bidimensionales de Hermite hasta el orden <img src="/tex/aa6905d780872f0007f642420d7a2d9c.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/> se muestran en la siguiente figura:

![Image3](Imagenes/dht2D.png)

## Transformada de Hermite Rotada

Una de las virtudes más reconocidas de la transformada de Hermite es su capacidad para hacer análisis direccional. Dado que en las imágenes y volúmenes es común encontrar patrones unidimensionales orientados, las transformadas direccionales llegan a ser de mucha utilidad. Los bordes y la textura son dos de las características más importantes que se pueden analizar usando procesamiento direccional. La TH cumple eficientemente con esta propiedad de rotación. Un filtro en una dirección determinada puede ser obtenido a través de una combinación lineal de unos filtros base, los cuales han sido definidos previamente en alguna dirección original. Este mismo concepto se puede extender a datos que han sido filtrados previamente con esos filtros base. Los coeficientes cartesianos de la TH en cada orden, para <img src="/tex/8fa66d8b80ce643977d63a6f345785b9.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/>, son un conjunto base con el cual se pueden obtener coeficientes rotados a cierto ángulo determinado. Para llevar a cabo la rotación, se parte de la definición de los filtros de Hermite en el dominio de Fourier.

Para el proceso de rotación bidimensional, se obtiene la transformada de Fourier de los filtros definidos en la ecuación **9**:

<p align="center"><img src="/tex/3483cc5c55de53d2f82881f6122141e5.svg?invert_in_darkmode&sanitize=true" align=middle width=598.4689062pt height=40.289634pt/></p>

donde <img src="/tex/c3ece3a75fed601ac0ee788147cf4541.svg?invert_in_darkmode&sanitize=true" align=middle width=69.58726994999999pt height=24.65753399999998pt/> es la transformada de Fourier de <img src="/tex/42946edc78445858d235e3bec98fee85.svg?invert_in_darkmode&sanitize=true" align=middle width=58.75200209999999pt height=26.76175259999998pt/>. La rotación definida en coordenadas cartesianas para el caso bidimensional se define como:

<p align="center"><img src="/tex/1bbc3a962fa26a9d4f9bdd6dabdd6dd6.svg?invert_in_darkmode&sanitize=true" align=middle width=198.80539635pt height=39.452455349999994pt/></p>

Una rotación en el dominio espacial es equivalente a una rotación en el dominio de la frecuencia. Por lo tanto, la definición anterior aplica para las coordenadas en el dominio de la frecuencia. Reemplazando las coordenadas rotadas en la ecuación **10** se obtiene:

<p align="center"><img src="/tex/df5c73d0604e5d92d06885863af2b635.svg?invert_in_darkmode&sanitize=true" align=middle width=857.6338468499999pt height=40.289634pt/></p>

Desarrollando la ecuación **11** y usando la transformada de Fourier inversa podemos obtener los filtros de Hermite rotados para un orden <img src="/tex/8fa66d8b80ce643977d63a6f345785b9.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/>. Dado que los coeficientes de la TH son obtenidos por un proceso de convolución entre la imagen de entrada y los filtros, es posible obtener los coeficientes rotados a partir de los cartesianos usando la ecuación **11**. Hay que resaltar que la
función Gaussiana es isotrópica, por lo cual no sufre modificaciones en el desarrollo anterior. Por ejemplo, los coeficientes de Hermite para los primeros dos órdenes son:

* Para <img src="/tex/e1358fc9fbfa5b82243d29c7f4a7bbb2.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/>,

<p align="center"><img src="/tex/095f586275888061f6c4aa1009149204.svg?invert_in_darkmode&sanitize=true" align=middle width=192.5345103pt height=39.452455349999994pt/></p>

* Para <img src="/tex/a2b83378f3a851a69124cae9e0f695fc.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/>,

<p align="center"><img src="/tex/db1577bd495f0da539c35990d99a76b6.svg?invert_in_darkmode&sanitize=true" align=middle width=294.12497895pt height=59.1786591pt/></p>

donde <img src="/tex/93841b4479b43ec19b60fc47f8c76b09.svg?invert_in_darkmode&sanitize=true" align=middle width=72.77772974999998pt height=24.65753399999998pt/> y <img src="/tex/08818578f0d08c677ae09fa1f4dc9fd4.svg?invert_in_darkmode&sanitize=true" align=middle width=73.81765214999999pt height=24.65753399999998pt/>. De la misma forma se pueden obtener los coeficientes rotados para órdenes más altos de la transformada.

Finalmente, la **TH** presenta algunas ventajas con respecto a otros modelos de descomposición, las cuales han motivado el uso de esta transformada en este proyecto. Algunas de estas ventajas son:

* Es considerado un modelo de visión.
* Permite hacer análisis direccional.
* Las funciones bases de la descomposición son ortogonales.
* Los filtros son separables, lo cual permite una fácil implementación en varias dimensiones.
* El submuestreo es definido por el usuario.
* Permite hacer análisis multiescala y multiresolución.

# Descomposición de imagenes en coeficientes de Hermite

Como se ha descrito anteriormente, la función de peso <img src="/tex/e80d2a1c9a200e59665e4f7370ec48b6.svg?invert_in_darkmode&sanitize=true" align=middle width=33.00232814999999pt height=24.65753399999998pt/> de los polinomios de Hermite es una función gaussiana. La función gaussiana se define en el dominio continuo, por lo que es necesario discretizarla y para ello, mostraremos el resultado de dos implementaciones de la discretización de la función gaussiana:

* Aproximación mediante la función binomial.
* Discretización directa de la función gaussiana.

El código **TH_ejemplo.py** muestra la comparación entre los coeficientes obtenidos con las dos diferentes implementaciones
La imagen de la cual se extraerán los coeficientes de Hermite de ambas formas es:

![Dim](dimetrodon10.png )

Los filtros binomiales se generan a partir de la función binomial o bien del triángulo de Pascal. La función binomial está definida como:

<p align="center"><img src="/tex/86ec45d923aa481147586a6d138730ae.svg?invert_in_darkmode&sanitize=true" align=middle width=212.78271795pt height=39.452455349999994pt/></p>

para <img src="/tex/f398cdd9af41e35f5152f68feaa419af.svg?invert_in_darkmode&sanitize=true" align=middle width=106.58632709999999pt height=22.465723500000017pt/> y <img src="/tex/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/> es el orden del filtro deseado. 

La función que calcula los coeficientes basados en la aproximación binomial de la imagen **I** (previamente transformada a escala de grises) es **dht2** incluida en el archivo **hermite.py**.

```python
import cv2
from hermite import  dht2

I = cv2.imread('dimetrodon10.png',cv2.COLOR_BGR2GRAY)

# Parámetros de la transformada Hermite  con binomial
N = 10; #Orden de la transformada
D = 3;  #Máximo orden de la expansión
T = 1;  #Parámetro de submuestreo

IH1=dht2(I,N,D,T)
```

Por otro lado, la función que calcula los coeficientes basados en la discretización directa de la función gaussiana de la imagen **I** es **HermiteTransform2DFreq** incluida en el archivo **HermiteRotado.py**. En este caso, prácticamente tenemos los mismos parámetros que en la función **dht2**, exceptuando por la variable **sg** que corresponde a la desviación estándar de la función gaussiana:

```python
import cv2
from HermiteRotado import HermiteTransform2DFreq
from collections import defaultdict
import numpy as np

I = cv2.imread('dimetrodon10.png',cv2.COLOR_BGR2GRAY)

# Parámetros de la transformada Hermite  con apriximación gaussiana
D = 3;                      #Maximo Orden de la expansión 
N = 10;                     #Orden de la transformada
M = np.array([N+1, N+1])
T  = 1;                     #Valor de Submuestreo para cada Escala
sg = 1.1;                   #Control de la desviación estándar de la gaussiana
Sel = 0                     #0 es para elegir descomposición
ImaDesc = defaultdict(dict) #Diccionario en donde se almacenaran los coefs
tam = I.shape               #tamaño de la imagen

[ImaDesc,_] = HermiteTransform2DFreq(I, T, M, sg, D, Sel, tam)
```
La comparación entre los coeficientes obtenidos a través de las dos implementaciones se muestra a continuación:

Aproximación con función binomial | Discretización gaussiana
:--------------------------------:|:-----------------------------------:
![Image6](Imagenes/I_dhtbin.png)  |  ![Image7](Imagenes/I_dhtdis11.png)

La comparación de los coeficientes obtenidos con diferentes desviaciones estándar <img src="/tex/8cda31ed38c6d59d14ebefa440099572.svg?invert_in_darkmode&sanitize=true" align=middle width=9.98290094999999pt height=14.15524440000002pt/> (**sg**) se muestra a continuación:

<img src="/tex/3170b24718014bd9ec4c8c0c772fb6ce.svg?invert_in_darkmode&sanitize=true" align=middle width=52.90515614999999pt height=21.18721440000001pt/>                      | <img src="/tex/f95ca178b7339aa7209a22ac88978032.svg?invert_in_darkmode&sanitize=true" align=middle width=40.11972194999999pt height=21.18721440000001pt/>                        | <img src="/tex/06885366aad27fe5220219d0372b2206.svg?invert_in_darkmode&sanitize=true" align=middle width=48.33893129999999pt height=21.18721440000001pt/> 
:----------------------------------:|:-----------------------------------:|:-------------------------------------:
![Image8](Imagenes/I_dhtdis11.png)  |  ![Image9](Imagenes/I_dhtdis30.png) |  ![Image10](Imagenes/I_dhtdis100.png)

## Rotación

El proceso de rotación de los coeficientes implica encontrar los ángulos de interés con respecto a los cuales se necesita hacer la rotación. El ángulo se estima de forma adaptativa para cada punto usando la dirección de máxima energía. El código siguiente sirve para calcular los coeficientes de Hermite rotados.

```python
import cv2
from HermiteRotado import HermiteTransform2DFreq
from collections import defaultdict
import numpy as np

I = cv2.imread('dimetrodon10.png',cv2.COLOR_BGR2GRAY)

N = 3;  # Maximo Orden de la expansión 
D = 10;  #Orden de la transformada
M = np.array([N+1, N+1])
T  = 1;              # Valor de Submuestreo para cada Escala
sg = 2.4;    #Control de la desviación estándar de la gaussiana
Sel = 0     # 0 es para elegir descomposición
ImaDesc = defaultdict(dict) #Diccionario en donde se almacenaran los coefs
ImaDescRot2  = defaultdict(dict)
AngTeta2     = defaultdict(dict)
ImaDescRot12 = defaultdict(dict)
tam = I.shape  #tamaño de la imagen

[ImaDesc,_] = HermiteTransform2DFreq(I, T, M, sg, N, Sel, tam)
##Esta parte es la de rotación
Sel = 2
[ImaDescRot2,ImaDescRot12, AngTeta2, Dn] =  HermiteTransform2DFreq(ImaDesc,T, M, sg, N, Sel, tam)
```

En la siguiente Figura se ilustran los coeficientes de Hermite rotados calculados a partir de los coeficientes cartesianos (sin rotación). Como se puede notar, toda la energía en la transformada rotada se concentra sobre los coeficientes de la primera línea. Esto se puede interpretar como un proceso de filtrado si consideramos que el resto de coeficientes corresponden al ruido, por lo cual podrían ser descartados.

Sin rotación                      | Con rotación
:--------------------------------:|:-----------------------------------:
![Image20](Imagenes/I_sr.png)     |  ![Image21](Imagenes/I_cr.png)



## Reconstrucción

A partir de los coeficientes de Hermite podemos reconstruir la imagen. Los resultados se muestran en la siguiete tabla y la medida de similitud es el coeficiente de correlación:

|Original                            | Binomial                       | Discrretización <img src="/tex/a5d16dfe2bd8650dcbade85ae467cd3d.svg?invert_in_darkmode&sanitize=true" align=middle width=52.90515614999999pt height=21.18721440000001pt/> |         
|:----------------------------------:|:------------------------------:|:------------------------------:|
|![Image11](dimetrodon10.png)        |![Image12](Imagenes/IR_Bin.png) |![Image13](Imagenes/IR_24.png)  |
|    _                               | corrcoef = 0.9814              | corrcoef = 0.9537              |

La ventaja de la aproximación binomial es que se puede obtener una mejor reconstrucción. Mientras que, la discretización de la gaussiana permite cambiar la forma de la función para encontrar diferentes patrones dentro de la imagen.


