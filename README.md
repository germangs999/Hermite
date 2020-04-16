# Hermite
La transformada Hermite como herramienta para el procesamiento digital de señales.
## Polinomios de Hermite
La ecuación diferencial general lineal de segundo orden en el intervalo definido entre <img src="/tex/1d5ba78bbbafd3226f371146bc348363.svg?invert_in_darkmode&sanitize=true" align=middle width=29.223836399999986pt height=19.1781018pt/> a <img src="/tex/f7a0f24dc1f54ce82fecccbbf48fca93.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>, <img src="/tex/1e0b3ba102d93befac9442fe8860d166.svg?invert_in_darkmode&sanitize=true" align=middle width=111.99012659999997pt height=24.65753399999998pt/>, es:
<p align="center"><img src="/tex/e1997813067a8a3ad75f4c93dc7222c8.svg?invert_in_darkmode&sanitize=true" align=middle width=297.06273465pt height=17.2895712pt/></p>
con su correspondiente ecuación homogénea:
<p align="center"><img src="/tex/5a3b922048c9c61f121784c4222f9c5d.svg?invert_in_darkmode&sanitize=true" align=middle width=268.71788625pt height=17.2895712pt/></p>
y con el operador diferencial asociado:
<p align="center"><img src="/tex/3d66b0cff53c4d8df04e1313f452654d.svg?invert_in_darkmode&sanitize=true" align=middle width=222.5120073pt height=35.77743345pt/></p>

Las familias de polinomios ortogonales clásicos se pueden obtener a través de funciones generadoras del operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/>, visto en la ecuación \ref{eq_OpDif}. Este operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> debe cumplir con la condición de simetría con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>, es decir, si:
<p align="center"><img src="/tex/a7fbbf1ed2488e326418accdeb7c4adc.svg?invert_in_darkmode&sanitize=true" align=middle width=130.7351793pt height=16.438356pt/></p>

donde <img src="/tex/6dbb78540bd76da3f1625782d42d6d16.svg?invert_in_darkmode&sanitize=true" align=middle width=9.41027339999999pt height=14.15524440000002pt/> y <img src="/tex/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55786029999999pt height=14.15524440000002pt/> son un par de funciones que se anulan fuera del intervalo cerrado y acotado por definición entre los valores <img src="/tex/44bc9d542a92714cac84e01cbbb7fd61.svg?invert_in_darkmode&sanitize=true" align=middle width=8.68915409999999pt height=14.15524440000002pt/> y <img src="/tex/4bdc8d9bcfb35e1c9bfb51fc69687dfc.svg?invert_in_darkmode&sanitize=true" align=middle width=7.054796099999991pt height=22.831056599999986pt/>, <img src="/tex/f867262559b6134ab076c77564c157fa.svg?invert_in_darkmode&sanitize=true" align=middle width=78.41885204999998pt height=24.65753399999998pt/>, con el producto interno definido como:

<p align="center"><img src="/tex/a54ad91aa10be3284dd1190b2b05dcd7.svg?invert_in_darkmode&sanitize=true" align=middle width=487.06843514999997pt height=41.27894265pt/></p> 

y con el peso <img src="/tex/f338fac0241f93b400e5a4d336d2abc7.svg?invert_in_darkmode&sanitize=true" align=middle width=42.347685599999984pt height=21.18721440000001pt/>. Además, el operador diferencial <img src="/tex/78ec2b7008296ce0561cf83393cb746d.svg?invert_in_darkmode&sanitize=true" align=middle width=14.06623184999999pt height=22.465723500000017pt/> simétrico con respecto al peso <img src="/tex/31fae8b8b78ebe01cbfbe2fe53832624.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/> debe tener la siguiente forma:
<p align="center"><img src="/tex/aa6697368923e57f8037346ff8de2f93.svg?invert_in_darkmode&sanitize=true" align=middle width=444.61360184999995pt height=35.77743345pt/></p>

A partir de estas definiciones y condiciones se precisa la extensión de la condición de simetría a una clase más larga de funciones y para lograrlo es necesario aplicar condiciones de frontera.b
