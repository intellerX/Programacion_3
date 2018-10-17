from pyDatalog import pyDatalog

from pyDatalog.pyDatalog import assert_fact, load, ask

# Variables
pyDatalog.create_terms('C,V,L,E,F,P1,P2,P3,P,X,Y,Z,W,A1,A2,A3,A4')

# -----------------------------------------------------------------------------------------------

# COMIDA

# Tipos de comida
pyDatalog.create_terms('raices, verduras, frutas, carnes, lacteos, granos, granos')

# Tabla nutricional
pyDatalog.create_terms('calorias')

# Cantidad de calorias por alimento
pyDatalog.create_terms('cantidad_calorias')

# Tipos de comida
pyDatalog.create_terms('Es_Desayuno, Es_Almuerzo, Es_Cena,DES,ALM,CEN')

# primer plato comidas, puede ser verduras o granos o raices
# segundo plato, puede ser un tipo de carne, o arroz, o pasta
# postre, puede ser fruta o jugo o lacteos

pyDatalog.create_terms('PP,SP,P')

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
+frutas('pina')
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

#Calorias

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

# Cantidad calorias por alimento

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
+cantidad_calorias('pina','0;100')
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

+PP('cilantro')
+PP('lechuga')
+PP('colifror')
+PP('cebolla')
+PP('calabacin')
+PP('apio')
+PP('alcachofa')
+PP('ajo')
+PP('acelga')
+PP('garbanzos')
+PP('blanquillos')
+PP('frilojes')
+PP('arvejas')
+PP('lentejas')
+PP('avena')
+PP('maiz')
+PP('fideos')
+PP('pan')
+PP('arroz_integral')
+PP('valeriana')
+PP('rabano')
+PP('regaliz')
+PP('remolacha')
+PP('jengibre')
+PP('curcuma')
+PP('zanahoria')
+PP('papa')
+PP('yuca')

+SP('garbanzos')
+SP('blanquillos')
+SP('frilojes')
+SP('arvejas')
+SP('lentejas')
+SP('avena')
+SP('maiz')
+SP('fideos')
+SP('pan')
+SP('arroz_integral')
+SP('pescado')
+SP('pollo')
+SP('cerdo')
+SP('res')

+P('manzana')
+P('pera')
+P('uva')
+P('ciruela')
+P('kiwi')
+P('mango')
+P('papaya')
+P('pina')
+P('platano')
+P('aguacate')
+P('melon')
+P('limon')
+P('mandarina')
+P('naranja')
+P('mora')
+P('fresa')
+P('guayaba')
+P('guanabana')
+P('lulo')
+P('queso')
+P('yogurt')
+P('postres')
+P('mantequilla')
+P('leche')

# ----------------------------------------------------------------------------------------------

# Datos

# Genero

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

# 1ra regla: Desayuno, se compone de granos, lacteos, embutidos(carne), frutas y grasas complementarias

Es_Desayuno(C,L,E,F,A1,A2,A3,A4) <= granos(C) & lacteos(L) & carnes(E) & frutas(F) & cantidad_calorias(C,A1) & \
                                    cantidad_calorias(L,A2) & cantidad_calorias(E,A3) & cantidad_calorias(F,A4)

# 2da regla: Almuerzo, se compone de primer plato, segundo plato, postre y pan

Es_Almuerzo(P1,P2,P3,A1,A2,A3) <= PP(P1) & SP(P2) & P(P3) & cantidad_calorias(P1,A1) & cantidad_calorias(P2,A2) & \
                                  cantidad_calorias(P3,A3) & (P1!=P2)

# 3ra regla: Cena, se compone de primer plato, segundo plato, postre y pan

Es_Cena(P1,P2,P3,A1,A2,A3) <= PP(P1) & SP(P2) & P(P3) & cantidad_calorias(P1,A1) & cantidad_calorias(P2,A2) & \
                              cantidad_calorias(P3,A3) & (P1!=P2)

# ----------------------------------------------------------------------------------------------

# avena   | leche   | pollo   | mandarina
+DES('avena','leche','pollo','mandarina')
# avena   | leche   | pollo   | lulo
+DES('avena','leche','pollo','lulo')
# avena   | postres | pescado | pina
+DES('avena','postres','pescado','pina')
# avena   | postres | pescado | lulo
+DES('avena','postres','pescado','lulo')
# avena   | leche   | pollo   | mora
+DES('avena','leche','pollo','mora')

# pan | yogurt  | pollo   | ciruela
+DES('pan','yogurt','pollo','ciruela')
# pan | leche   | pescado | mango
+DES('pan','leche','pescado','mango')
# pan | leche   | pollo   | guanabana
+DES('pan','leche','pollo','guanabana')
# pan | postres | pollo   | naranja
+DES('pan','postres','pollo','naranja')
# pan | yogurt  | pescado | naranja
+DES('pan','yogurt','pescado','naranja')

# fideos         | leche   | pollo   | mora
+DES('fideos','leche','pollo','mora')
# fideos         | leche   | pescado | pera
+DES('fideos','leche','pescado','pera')
# fideos         | leche   | pollo   | guanabana
+DES('fideos','leche','pollo','guanabana')

# arroz_integral | yogurt  | pescado | kiwi
+DES('arroz_integral','yogurt','pescado','kiwi')
# arroz_integral | postres | res     | guanabana
+DES('arroz_integral','postres','res','guanabana')
# arroz_integral | leche   | pollo   | pina
+DES('arroz_integral','leche','pollo','piña')

# ----------------------------------------------------------------------------------------------

# fideos         | blanquillos | aguacate
+ALM('fideos','blanquillos','aguacate')
# arroz_integral | blanquillos | guayaba
+ALM('arroz_integral','blanquillos','guayaba')
# maiz           | blanquillos | aguacate
+ALM('maiz','blanquillos','aguacate')
# maiz           | blanquillos | guayaba
+ALM('maiz','blanquillos','guayaba')
# lentejas       | blanquillos | aguacate
+ALM('lentejas','blanquillos','aguacate')

# lentejas       | res     | guayaba
+ALM('lentejas','res','guayaba')
# maiz           | pollo   | guayaba
+ALM('maiz','pollo','guayaba')
# garbanzos      | pescado | aguacate
+ALM('garbanzos','pescado','aguacate')
# fideos         | pollo   | guayaba
+ALM('fideos','pollo','guayaba')
# maiz           | pollo   | aguacate
+ALM('maiz','pollo','aguacate')

# pan     | pollo   | guayaba
+ALM('pan','pollo','guayaba')
# pan     | pollo   | aguacate
+ALM('pan','pollo','aguacate')
# pan     | res     | aguacate
+ALM('pan','res','aguacate')
# pan     | pescado | guayaba
+ALM('pan','pescado','guayaba')
# pan     | pescado | aguacate
+ALM('pan','pescado','aguacate')
# avena   | pescado | postres
+ALM('avena','pescado','postres')
# arvejas | res     | pera
+ALM('arvejas','res','pera')
# arvejas | pollo   | platano
+ALM('arvejas','pollo','platano')
# yuca    | pescado | mango
+ALM('yuca','pescado','mango')
# arvejas | pescado | pina
+ALM('arvejas','pescado','pina')

# ----------------------------------------------------------------------------------------------

# alcachofa | blanquillos | guanabana
+CEN('alcachofa','blanquillos','guanabana')
# calabacin | blanquillos | uva
+CEN('calabacin','blanquillos','uva')
# zanahoria | blanquillos | ciruela
+CEN('zanahoria','blanquillos','ciruela')
# calabacin | blanquillos | limon
+CEN('calabacin','blanquillos','limon')
# lechuga   | blanquillos | mango
+CEN('lechuga','blanquillos','mango')

# ----------------------------------------------------------------------------------------------

def combinacion_desayunos():
    print(Es_Desayuno(X, Y, Z, W, '300;400', '0;100', '100;200', '0;100'))
    return 0

def combinacion_almuerzos():
    print(Es_Almuerzo(P1, P2, P3, '100;200', '100;200', '0;100'))
    return 0

def combinacion_cenas():
    print(Es_Cena(P1, P2, P3, '0;100', '0;100', '0;100'))
    return 0

