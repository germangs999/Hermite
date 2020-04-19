# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:40:23 2020

@author: germa
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from hermite import  dht2
from HermiteRotado import HermiteTransform2DFreq
from collections import defaultdict
import math

def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product



I = cv2.imread('dimetrodon10.png',cv2.COLOR_BGR2GRAY)

# Parámetros de la transformada Hermite  con binomial

N = 10; #Orden de la transformada
D = 3; #Máximo orden de la expansión
T = 1; #DParámetro de submuestreo
#El rango de D es 0 <= D <= N y define el número de filtros que se aplicaran a
#la imagen I, a través de la fórmula [D+1*(D+2)]/2. Por ejemplo, si D = 4, 
#entonces serán 15 imágenes filtradas en la salida

IH1=dht2(I,N,D,T)

## Orden 0
fig = plt.figure()
# plt.title('Coeficientes de Hermite con aproximación binomial de la gaussiana')
a = fig.add_subplot(4, 4, 1)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,0], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 1
a = fig.add_subplot(4, 4, 2)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,1], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 5)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,2], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 2
a = fig.add_subplot(4, 4, 3)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,3], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 6)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,4], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 9)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,5], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 3
a = fig.add_subplot(4, 4, 4)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,6], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 7)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,7], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 10)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,8], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 13)
imgplot = plt.imshow((cv2.normalize(IH1[:,:,9], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

########################################
# Parámetros de la transformada Hermite  con apriximación gaussiana
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
Sel = 2
[ImaDescRot2,ImaDescRot12, AngTeta2, Dn] =  HermiteTransform2DFreq(ImaDesc,T, M, sg, N, Sel, tam)

## Orden 0
fig = plt.figure()
# plt.title('Coeficientes de Hermite con aproximación discreta de la gaussiana')
a = fig.add_subplot(4, 4, 1)
imgplot = plt.imshow((cv2.normalize(ImaDesc[0], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 1
a = fig.add_subplot(4, 4, 2)
imgplot = plt.imshow((cv2.normalize(ImaDesc[1], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 5)
imgplot = plt.imshow((cv2.normalize(ImaDesc[2], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 2
a = fig.add_subplot(4, 4, 3)
imgplot = plt.imshow((cv2.normalize(ImaDesc[3], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 6)
imgplot = plt.imshow((cv2.normalize(ImaDesc[4], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 9)
imgplot = plt.imshow((cv2.normalize(ImaDesc[5], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 3
a = fig.add_subplot(4, 4, 4)
imgplot = plt.imshow((cv2.normalize(ImaDesc[6], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 7)
imgplot = plt.imshow((cv2.normalize(ImaDesc[7], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 10)
imgplot = plt.imshow((cv2.normalize(ImaDesc[8], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(4, 4, 13)
imgplot = plt.imshow((cv2.normalize(ImaDesc[9], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Prueba de la reconstrucción
D = 3;  # Maximo Orden de la expansión 
N = 10;  #Orden de la transformada
M = np.array([N+1, N+1])
for sg1 in range(24,25): 
    [ImaDesc,_] = HermiteTransform2DFreq(I, T, M, sg1/10, D, 0, tam)            
    [SalRec,_] = HermiteTransform2DFreq(ImaDesc, T, M, sg1/10, D, 1, tam)
    print((sg1,correlation_coefficient(I, SalRec)))

SalRec2 = SalRec.astype('uint8')
fig = plt.figure()
plt.imshow((cv2.normalize(SalRec, 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
#cv2.imwrite('IR_24.png',SalRec2)
fig = plt.figure()
plt.imshow(SalRec2,cmap="gray")
plt.axis('off')

############## Prueba de Rotación

## Orden 0
fig = plt.figure()
# plt.title('Coeficientes de Hermite con aproximación discreta de la gaussiana')
a = fig.add_subplot(3, 3, 1)
imgplot = plt.imshow((cv2.normalize(ImaDesc[0], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 1
a = fig.add_subplot(3, 3, 2)
imgplot = plt.imshow((cv2.normalize(ImaDesc[1], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 4)
imgplot = plt.imshow((cv2.normalize(ImaDesc[2], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 2
a = fig.add_subplot(3, 3, 3)
imgplot = plt.imshow((cv2.normalize(ImaDesc[3], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 5)
imgplot = plt.imshow((cv2.normalize(ImaDesc[4], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 7)
imgplot = plt.imshow((cv2.normalize(ImaDesc[5], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

#########################################################################

## Orden 0
fig = plt.figure()
# plt.title('Coeficientes de Hermite con aproximación discreta de la gaussiana')
a = fig.add_subplot(3, 3, 1)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[0], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 1
a = fig.add_subplot(3, 3, 2)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[1], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 4)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[2], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')

## Orden 2
a = fig.add_subplot(3, 3, 3)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[3], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 5)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[4], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')
a = fig.add_subplot(3, 3, 7)
imgplot = plt.imshow((cv2.normalize(ImaDescRot2[5], 0, 1, cv2.NORM_MINMAX)),cmap="gray")
plt.axis('off')
# a.set_title('')



