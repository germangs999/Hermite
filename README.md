# Hermite
La transformada Hermite como herramienta para el procesamiento digital de señales.
## Polinomios ortogonales clásicos
La ecuación diferencial general lineal de segundo orden en el intervalo definido entre <img src="/tex/1d5ba78bbbafd3226f371146bc348363.svg?invert_in_darkmode&sanitize=true" align=middle width=29.223836399999986pt height=19.1781018pt/> a <img src="/tex/f7a0f24dc1f54ce82fecccbbf48fca93.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>, <img src="/tex/1e0b3ba102d93befac9442fe8860d166.svg?invert_in_darkmode&sanitize=true" align=middle width=111.99012659999997pt height=24.65753399999998pt/>, es:
<p align="center"><img src="/tex/7292aa4c670187c66ca069062275c782.svg?invert_in_darkmode&sanitize=true" align=middle width=386.56056119999994pt height=17.2895712pt/></p>
con su correspondiente ecuación homogénea:
<p align="center"><img src="/tex/5a3b922048c9c61f121784c4222f9c5d.svg?invert_in_darkmode&sanitize=true" align=middle width=268.71788625pt height=17.2895712pt/></p>
y con el operador diferencial asociado:
<p align="center"><img src="/tex/f5a7635d3b4d547ce88a74375402237e.svg?invert_in_darkmode&sanitize=true" align=middle width=309.2701755pt height=35.77743345pt/></p>

Las familias de polinomios ortogonales clásicos se pueden obtener a través de funciones generadoras del operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>, visto en la ecuación **1**. Este operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> debe cumplir con la condición de simetría con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>, es decir, si:
<p align="center"><img src="/tex/a7fbbf1ed2488e326418accdeb7c4adc.svg?invert_in_darkmode&sanitize=true" align=middle width=130.7351793pt height=16.438356pt/></p>

donde <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/> y <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> son un par de funciones que se anulan fuera del intervalo cerrado y acotado por definición entre los valores <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> y <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/>, <img src="/tex/f867262559b6134ab076c77564c157fa.svg?invert_in_darkmode&sanitize=true" align=middle width=78.41885204999998pt height=24.65753399999998pt/>, con el producto interno definido como:

<p align="center"><img src="/tex/5680b82a1f3e26e54602b384493e91fb.svg?invert_in_darkmode&sanitize=true" align=middle width=273.8631423pt height=41.27894265pt/></p> 

y con el peso <img src="/tex/f338fac0241f93b400e5a4d336d2abc7.svg?invert_in_darkmode&sanitize=true" align=middle width=42.347685599999984pt height=21.18721440000001pt/>. Además, el operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> simétrico con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> debe tener la siguiente forma:
<p align="center"><img src="/tex/ce4021d6dae24d162f01e03b9a75dbec.svg?invert_in_darkmode&sanitize=true" align=middle width=188.9532843pt height=35.77743345pt/></p>

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

<p align="center"><img src="/tex/eea13885ddaeffb84de5e215e3fe28e2.svg?invert_in_darkmode&sanitize=true" align=middle width=332.24777355pt height=41.7812637pt/></p>  

donde <img src="/tex/a7024fd20adb1541682356994daf0449.svg?invert_in_darkmode&sanitize=true" align=middle width=93.11082329999998pt height=24.65753399999998pt/>, <img src="/tex/049663a27d86f8494043445f01ea1482.svg?invert_in_darkmode&sanitize=true" align=middle width=92.76834434999998pt height=24.65753399999998pt/>, <img src="/tex/c5650e22f5731eb6c3886cb2096d1864.svg?invert_in_darkmode&sanitize=true" align=middle width=88.13597759999999pt height=22.831056599999986pt/> y 

<p align="center"><img src="/tex/884269c611176ee8bf5d6dd551298720.svg?invert_in_darkmode&sanitize=true" align=middle width=171.2596776pt height=17.2895712pt/></p> 

A este tipo de operadores diferenciales se les denomina de tipo hipergeométrico o de tipo Sturm-Liouville. A la ecuación **4** se le denomina como la ecuación de Pearson.

Dado que <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> es un polinomio de grado máximo 2, después de normalizaciones (mapeos afines de la recta, multiplicación del peso, el operador y los polinomios por constantes) se obtiene que existen 5 tipos de familias de polinomios ortogonales que son funciones generadoras del operador diferencial hipergeométrico <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> (ecuación **3**) dependiendo del grado y las raíces de <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>:

1. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> constante: polinomios de **Hermite**.
2. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> lineal: polinomios de **Laguerre**. 
3. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadátrico con raíces reales distintas: polinomios de **Jacobi**. 
4. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadátrico con raíces complejas distintas: polinomios de **Romanovski**.
5. <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> cuadrático con raíz doble: varias familias de polinomios.

Muchos problemas de matemáticas aplicadas y teóricas así como problemas de física conducen a ecuaciones de la forma:

<p align="center"><img src="/tex/8c05c84b9bc852dd88124c13b5e3007d.svg?invert_in_darkmode&sanitize=true" align=middle width=286.13218094999996pt height=17.2895712pt/></p>

donde <img src="/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/> es una constante y <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/> y <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> son polinomios de, al menos, segundo y primer grado, respectivamente. A esta ecuación se le conoce como ecuación diferencial del tipo hipergeométrico y se obtiene a través de las ecuaciones **2** y **3** e igualando:

<p align="center"><img src="/tex/ab3e6f4b44b8e36cc3b5438926401c1d.svg?invert_in_darkmode&sanitize=true" align=middle width=44.73730305pt height=10.2739725pt/></p>
<p align="center"><img src="/tex/4154287855b4111d57c0532829f9c591.svg?invert_in_darkmode&sanitize=true" align=middle width=100.66145759999999pt height=34.75462155pt/></p>

y

<p align="center"><img src="/tex/5fdf43c071b49c28ac8ba83b57fd71ea.svg?invert_in_darkmode&sanitize=true" align=middle width=43.032648449999996pt height=11.4155283pt/></p>

Un aspecto que hay que tener en cuenta es que <img src="/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/> no sólo es una constante sino que además es el valor generador del operador <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>. Por otro lado, la relación que existe entre <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/> y <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> en la ecuación **ab** está dada por la ecuación de Pearson que indica que <img src="/tex/b27d7f723c9a5ae890806548af965a09.svg?invert_in_darkmode&sanitize=true" align=middle width=31.22725484999999pt height=24.65753399999998pt/> es derivada de <img src="/tex/b9b27f3deff0db82f962a8505706e620.svg?invert_in_darkmode&sanitize=true" align=middle width=32.16330314999999pt height=24.65753399999998pt/>, siempre y cuando ambas estén multiplicadas por el peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>.

En conclusión tenemos que, salvo normalizaciones, las únicas familias de polinomios ortogonales que son funciones generadoras de un operador diferencial de segundo orden que obedece a la ecuación **3**, es decir, un operador diferencial simétrico con respecto a un peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> positivo soportado dentro de la recta real, son las familias de Hermite, Laguerre y Jacobi. A estas familias se les suele denominar polinomios ortogonales clásicos. En la siguiente Tabla se muestra un resumen de las características de las familias clásicas.

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
