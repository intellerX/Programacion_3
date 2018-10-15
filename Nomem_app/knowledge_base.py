from pyDatalog import pyDatalog

from pyDatalog.pyDatalog import assert_fact, load, ask

# COMIDA

# Tipos de comida
pyDatalog.create_terms('raices, verduras, frutas, carnes, lacteos, granos')

# Tabla nutricional
pyDatalog.create_terms('vitamina_a, vitamina_b, vitamina_c, calorias, carbohidratos, proteinas')

pyDatalog.create_terms('cantidad_calorias')


# -----------------------------------------------------------------------------------------------

# PERSONAS

# Datos
pyDatalog.create_terms('genero, edad, peso, estatura, sedentarismo')

# Enfermedades
pyDatalog.create_terms('gastrointestinales, diabetes, desnutricion, obesidad')

# Sintomas y soluciones
pyDatalog.create_terms('tiene_sintoma, solucion')

# ----------------------------------------------------------------------------------------------

# REGLAS

# Tipos de comida
pyDatalog.create_terms('desayuno, almuerzo, cena')

# Estructura comida
pyDatalog.create_terms('primer_plato, segundo_plato, postre')

# ----------------------------------------------------------------------------------------------

# Tipos de comida

# Raices

+raices('valeriana')
+raices('rabano')
+raices('regaliz')
+raices('remolacha')
+raices('jengibre')
+raices('curcuma')
+raices('zanahoria')
+raices('papa')
+raices('yuca')

# Verduras

+verduras('cilantro')
+verduras('lechuga')
+verduras('colifror')
+verduras('cebolla')
+verduras('calabacin')
+verduras('apio')
+verduras('alcachofa')
+verduras('ajo')
+verduras('acelga')

# Frutas

+frutas('manzana')
+frutas('pera')
+frutas('uva')
+frutas('ciruela')
+frutas('kiwi')
+frutas('mango')
+frutas('papaya')
+frutas('piña')
+frutas('platano')
+frutas('aguacate')
+frutas('melon')
+frutas('limon')
+frutas('mandarina')
+frutas('naranja')
+frutas('mora')
+frutas('fresa')
+frutas('guayaba')
+frutas('guanabana')
+frutas('lulo')

# Carnes y derivados

+carnes('pescado')
+carnes('pollo')
+carnes('cerdo')
+carnes('res')

# Lacteos

+lacteos('queso')
+lacteos('yogurt')
+lacteos('postres')
+lacteos('mantequilla')
+lacteos('leche')

# Granos

+granos('garbanzos')
+granos('blanquillos')
+granos('frilojes')
+granos('arvejas')
+granos('lentejas')
+granos('avena')
+granos('maiz')
+granos('fideos')
+granos('pan')
+granos('arroz_integral')

# ----------------------------------------------------------------------------------------------

# Tabla nutricional

#vitamina a

+vitamina_a('0;650')
+vitamina_a('650;1350')
+vitamina_a('1350;2600')
+vitamina_a('2600;3250')
+vitamina_a('3250;3900')
+vitamina_a('3900;4550')
+vitamina_a('4550;5200')
+vitamina_a('5200;5850')
+vitamina_a('5850;6500')
+vitamina_a('6500;7150')
+vitamina_a('7150;7800')
+vitamina_a('7800;8450')
+vitamina_a('8450;9100')
+vitamina_a('9100;9750')

#vitamina b

+vitamina_b('0;650')
+vitamina_b('650;1350')
+vitamina_b('1350;2600')
+vitamina_b('2600;3250')
+vitamina_b('3250;3900')
+vitamina_b('3900;4550')
+vitamina_b('4550;5200')
+vitamina_b('5200;5850')
+vitamina_b('5850;6500')
+vitamina_b('6500;7150')
+vitamina_b('7150;7800')
+vitamina_b('7800;8450')
+vitamina_b('8450;9100')
+vitamina_b('9100;9750')

#vitamina c

+vitamina_c('0;650')
+vitamina_c('650;1350')
+vitamina_c('1350;2600')
+vitamina_c('2600;3250')
+vitamina_c('3250;3900')
+vitamina_c('3900;4550')
+vitamina_c('4550;5200')
+vitamina_c('5200;5850')
+vitamina_c('5850;6500')
+vitamina_c('6500;7150')
+vitamina_c('7150;7800')
+vitamina_c('7800;8450')
+vitamina_c('8450;9100')
+vitamina_c('9100;9750')


#Calorías

+calorias('0;100')
+calorias('100;200')
+calorias('200;300')
+calorias('300;400')
+calorias('400;500')
+calorias('500;600')
+calorias('600;700')
+calorias('700;800')
+calorias('800;900')
+calorias('900;1000')
+calorias('1000;1100')
+calorias('1100;1200')
+calorias('1200;1300')
+calorias('1300;1400')

# Carbohidratos

+carbohidratos('0;35')
+carbohidratos('35;70')
+carbohidratos('70;105')
+carbohidratos('105;140')
+carbohidratos('140;175')
+carbohidratos('175;210')
+carbohidratos('210;245')
+carbohidratos('245;280')
+carbohidratos('280;315')
+carbohidratos('315;350')
+carbohidratos('350;385')
+carbohidratos('385;420')
+carbohidratos('420;455')
+carbohidratos('455;490')

# Proteínas

+proteinas('0;35')
+proteinas('35;70')
+proteinas('70;105')
+proteinas('105;140')
+proteinas('140;175')
+proteinas('175;210')
+proteinas('210;245')
+proteinas('245;280')
+proteinas('280;315')
+proteinas('315;350')
+proteinas('350;385')
+proteinas('385;420')
+proteinas('420;455')
+proteinas('455;490')

# ----------------------------------------------------------------------------------------------

# Tabla nutricional

# Raices

+cantidad_calorias('valeriana','0;100')
+cantidad_calorias('rabano','0;100')
+cantidad_calorias('regaliz','300;400')
+cantidad_calorias('remolacha','0;100')
+cantidad_calorias('jengibre','0;100')
+cantidad_calorias('zanahoria','0;100')
+cantidad_calorias('curcuma','200;300')
+cantidad_calorias('yuca','100;200')


# Verduras

+cantidad_calorias('cilantro','0;100')
+cantidad_calorias('lechuga','0;100')
+cantidad_calorias('coliflor','0;100')
+cantidad_calorias('cebolla','0;100')
+cantidad_calorias('calabacin','0;100')
+cantidad_calorias('apio','0;100')
+cantidad_calorias('alcachofa','0;100')
+cantidad_calorias('ajo','100;200')
+cantidad_calorias('acelga','0;100')

# Frutas

+cantidad_calorias('manzana','0;100')
+cantidad_calorias('pera','0;100')
+cantidad_calorias('uva','0;100')
+cantidad_calorias('ciruela','0;100')
+cantidad_calorias('kiwi','0;100')
+cantidad_calorias('mango','0;100')
+cantidad_calorias('papaya','0;100')
+cantidad_calorias('piña','0;100')
+cantidad_calorias('platano','0;100')
+cantidad_calorias('aguacate','100;200')
+cantidad_calorias('melon','0;100')
+cantidad_calorias('limon','0;100')
+cantidad_calorias('mandarina','0;100')
+cantidad_calorias('naranja','0;100')
+cantidad_calorias('mora','0;100')
+cantidad_calorias('fresa','0;100')
+cantidad_calorias('guayaba','100;200')
+cantidad_calorias('guanabana','0;100')
+cantidad_calorias('lulo','0;100')

# Carnes

+cantidad_calorias('pollo','100;200')
+cantidad_calorias('pescado','100;200')
+cantidad_calorias('res','100;200')
+cantidad_calorias('cerdo','200;300')

# Lacteos

+cantidad_calorias('queso', '400;500')
+cantidad_calorias('yogurt', '0;100')
+cantidad_calorias('postres', '0;100')
+cantidad_calorias('mantequilla', '700;800')
+cantidad_calorias('leche', '0;100')

# Granos

+cantidad_calorias('garbanzos', '300;400')
+cantidad_calorias('blanquillos', '0;100')
+cantidad_calorias('frijoles', '0;100')
+cantidad_calorias('arvejas', '100;200')
+cantidad_calorias('lentejas', '300;400')
+cantidad_calorias('avena', '100;200')
+cantidad_calorias('maiz', '300;400')
+cantidad_calorias('fideos', '300;400')
+cantidad_calorias('pan', '200;300')
+cantidad_calorias('arroz_integral', '300;400')

# ----------------------------------------------------------------------------------------------

# Datos

# Género

+genero('masculino')
+genero('femenino')

# Edad

+edad('10;19')
+edad('20;29')
+edad('30;39')
+edad('40;49')
+edad('50;59')
+edad('60;69')
+edad('70;79')
+edad('80;89')
+edad('+89')

# Peso

+peso('40;49')
+peso('50;59')
+peso('60;69')
+peso('70;79')
+peso('80;89')
+peso('90;99')
+peso('100;149')
+peso('150;199')
+peso('200;249')
+peso('250;299')
+peso('+300')

# Estatura

+estatura('130;139')
+estatura('140;149')
+estatura('150;159')
+estatura('160;169')
+estatura('170;179')
+estatura('180;189')
+estatura('190;199')
+estatura('200;209')
+estatura('210;219')
+estatura('220;229')

# Sedentarismo

+sedentarismo('1','Poco o nada de ejercicio')
+sedentarismo('2','Deporte 1-2 veces por semana')
+sedentarismo('3','Deporte 3-5 veces por semana')
+sedentarismo('4','Deporte 6-7 veces por semana')
+sedentarismo('5','Deporte varias veces al dia')

# ----------------------------------------------------------------------------------------------
"""
# Enfermedades

# Gastrointestinales

+gastrointestinales('reflujo_gastroesofagico')
+gastrointestinales('celiaquia')
+gastrointestinales('sindrome_intestino_irritable')
+gastrointestinales('hemorroides')

# Diabetes

+diabetes('diabetes_tipo_I')
+diabetes('diabetes_tipo_II')

# Desnutrición

+desnutricion('peso_insuficiente')

# Obesidad

+obesidad('sobrepeso_tipo_I')
+obesidad('sobrepeso_tipo_II')
+obesidad('obesidad_tipo_I')
+obesidad('obesidad_tipo_II')
+obesidad('obesidad_tipo_III')

# ----------------------------------------------------------------------------------------------

# Sintomas

+tiene_sintoma('reflujo_gastroesofagico', 'Estomago_lleno')
+tiene_sintoma('celiaquia', 'mala_respuesta_al_gluten')
+tiene_sintoma('sindrome_intestino_irritable', 'falta_de_fibra')
+tiene_sintoma('hemorroides', 'mucha_sal_o_azucar')
+tiene_sintoma('peso_insuficiente', 'IMC_<18.5')
+tiene_sintoma('sobrepeso_tipo_I', 'IMC_25;26.9')
+tiene_sintoma('sobrepeso_tipo_II', 'IMC_27;29.9')
+tiene_sintoma('sobrepeso_tipo_II', 'preobesidad')
+tiene_sintoma('obesidad_tipo_I', 'IMC_30;34.9')
+tiene_sintoma('obesidad_tipo_II', 'IMC_35;39.9')
+tiene_sintoma('obesidad_tipo_III', 'IMC_40;49.9')
+tiene_sintoma('obesidad_tipo_III', 'obesidad_morbida')

# Solucion (pendiente terminar)

#se tienen que encontrar las soluciones a los sintomas escritos previamente
"""
# ----------------------------------------------------------------------------------------------

#Reglas (pendiente terminar)

# 1ra regla: Desayuno, se compone de cereales, lacteos, embutidos(carne), frutas y grasas complementarias

Es_Desayuno(C,L,E,F) <= cereal(C)& lacteos(L)& embutidos(E)& frutas(F)

# 2da regla: Almuerzo, se compone de primer plato, segundo plato, postre y pan

Es_Amuerzo(P1,P2,P3) <= primerPlato(P1)& segundoPlato(p2)& postre(P3)& (P1!=p2) & (P2!=P3)

# 3ra regla: Cena, se compone de primer plato, segundo plato, postre y pan

Es_Cena(P1,P2,P3) <= primerPlato(P1)& segundoPlato(P2) & postre(p3)& (P1!=p2) & (P2!=P3)

# 4ta regla: primer plato, puede ser verduras o cereales o raices

primerPlato(V) <= verduras(V) or cereales(V) or raices(V)

# 5ta regla: segundo plato, puede ser un tipo de carne, o arroz, o pasta

segundoPlato(C) <= carne(C) or granos(C)

# 6ta regla: postre, puede ser fruta o jugo o lacteos

postre(P) <= futas(C) or lacteos(C)
