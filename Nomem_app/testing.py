from pyDatalog import pyDatalog

import random

pyDatalog.create_terms('desayuno,almuerzo,cena')

# Estructura desayuno: cereal, lacteos, y bebida
# Estructura almuerzo: primer plato, segundo plato, postre y bebida
# Estructura cena: primer plato, segundo plato, postre y bebida

# tipo_comida(comida,categoria,numero_calorias)

+desayuno('avena', 'cereal', 160)
+desayuno('pan', 'cereal', 324)
+desayuno('tostadas', 'cereal',313)
+desayuno('arepa','cereal', 219)
+desayuno('galletas','cereal',421)
+desayuno('kellogs','cereal',360)
+desayuno('sandwich','cereal',241)

+desayuno('leche_entera','lacteo',120)
+desayuno('leche_deslactosada','lacteo',90)
+desayuno('yogurt_melon','lacteo',102)
+desayuno('yogurt_mora','lacteo,',102)
+desayuno('yogurt_fresa','lacteo',102)
+desayuno('kumis','lacteo',160)
+desayuno('queso_dobre_crema','lacteo',45)
+desayuno('queso_cuajada','lacteo',90)

+desayuno('jugo_mango','bebida',0)
+desayuno('jugo_fresa','bebida',0)
+desayuno('jugo_mora','bebida',0)
+desayuno('limonada','bebida',0)
+desayuno('jugo_naranja','bebida',0)
+desayuno('jugo_guayaba','bebida',0)
+desayuno('cafe','bebida',0)
+desayuno('chocolate','bebida',564)
+desayuno('agua_de_panela','bebida',70)


+almuerzo('ensalada_verduras','primer_plato',0)
+almuerzo('pasta','primer_plato',131)
+almuerzo('arroz','primer_plato',260)
+almuerzo('papas','primer_plato',290)
+almuerzo('yuca','primer_plato',159)
+almuerzo('verduras_salteadas','primer_plato',125)

+almuerzo('pechuga','segundo_platos',330)
+almuerzo('higado','segundo_plato',330)
+almuerzo('atun','segundo_plato',186)
+almuerzo('pescado','segundo_plato',206)
+almuerzo('bofe','segundo_plato',249)
+almuerzo('pollo','segundo_plato',230)
+almuerzo('sardina','segundo_plato',168)

+almuerzo('manzana_picada','postre',0)
+almuerzo('pera_picada','postre',0)
+almuerzo('mango_picado','postre',0)
+almuerzo('pina_picada','postre',0)
+almuerzo('gelatina','postre',20)

+almuerzo('jugo_mango','bebida',0)
+almuerzo('jugo_fresa','bebida',0)
+almuerzo('jugo_mora','bebida',0)
+almuerzo('limonada','bebida',0)
+almuerzo('jugo_naranja','bebida',0)
+almuerzo('jugo_guayaba','bebida',0)
+almuerzo('jugo_tomate_arbol','bebida',0)


+cena('ensalada_verduras','primer_plato',0)
+cena('pasta','primer_plato',131)
+cena('arroz','primer_plato',260)
+cena('verduras_salteadas','primer_plato',125)

+cena('pechuhga','segundo_plato',330)
+cena('pollo','segundo_plato',230)
+cena('jamon','segundo_plato',82)
+cena('res','segundo_plato',100)

+cena('gelatina','postre',20)
+cena('bocadillo','postre',300)
+cena('arroz_con_leche','postre',300)
+cena('brevas','postre',601)
+cena('arequipe','postre',360)

+cena('cafe','bebida',0)
+cena('aromatica','bebida',0)
+cena('chocolate','bebida',564)
+cena('agua_de_panela','bebida',70)
+cena('leche_con_milo','bebida',100)
+cena('jugo_mango','bebida',0)
+cena('jugo_mora','bebida',0)

# ---------------------------------------------------------------------------------------------------------------------

# REGLAS

pyDatalog.create_terms('X,Y,Z,W,A,B,C,C1,C2,C3,C4')
pyDatalog.create_terms('combinacion_desayuno,combinacion_almuerzo,combinacion_cena')

combinacion_desayuno(X,Y,Z,C1,C2,C3) <=  desayuno(X,'cereal',C1) & desayuno(Y,'lacteo',C2) & desayuno(Z,'bebida',C3)

combinacion_almuerzo(X,Y,Z,W,C1,C2,C3,C4) <= almuerzo(X,'primer_plato',C1) & almuerzo(Y,'segundo_plato',C2) & \
    almuerzo(Z,'postre',C3) & almuerzo(W,'bebida',C4)

combinacion_cena(X,Y,Z,W,C1,C2,C3,C4) <= cena(X,'primer_plato',C1) & cena(Y,'segundo_plato',C2) & cena(Z,'postre',C3) & \
    cena(W,'bebida',C4)

##print(combinacion_desayuno(X,Y,Z,C1,C2,C3))

def sacar_al_azar(C1,C2,C3):
	p = combinacion_desayuno(X,Y,Z,C1,C2,C3)
	value = random.choice(p)
	print(value)
	return 0
