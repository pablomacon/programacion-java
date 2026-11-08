# Unidad 2. Nuestros primeros programas en Java: de los algoritmos al código

**Programación I — 2026**  
**1.º Bachillerato Tecnológico en Informática · DGETP / UTU**

## ¿Qué aprenderemos en esta unidad?

En la Unidad 1 aprendimos que programar no consiste solamente en escribir instrucciones.

Primero debemos comprender un problema, identificar sus datos, reconocer qué resultado necesitamos obtener y construir un algoritmo que permita alcanzarlo.

También aprendimos a representar nuestras soluciones mediante pseudocódigo.

Por ejemplo, para calcular el importe de una compra escribimos:

```text
INICIO
    LEER precio
    LEER cantidad

    total ← precio * cantidad

    MOSTRAR total
FIN
```

Este algoritmo es comprensible para nosotros.

Sabemos que debemos obtener dos datos, multiplicarlos y mostrar el resultado.

Pero aparece una nueva pregunta:

**¿Cómo conseguimos que una computadora ejecute este procedimiento?**

Para hacerlo necesitamos expresar nuestro algoritmo mediante un lenguaje de programación.

Durante este curso utilizaremos Java.

En esta unidad aprenderemos a:

- Reconocer la estructura básica de un programa Java.
- Crear y ejecutar un archivo `Main.java`.
- Comprender qué son las instrucciones y cómo se ejecutan.
- Mostrar información mediante `System.out.print` y `System.out.println`.
- Identificar los datos que necesita un programa.
- Declarar variables y asignarles valores.
- Diferenciar tipos de datos básicos.
- Realizar operaciones aritméticas.
- Comprender cómo cambian los valores de las variables.
- Leer información mediante `Scanner`.
- Traducir algoritmos expresados en pseudocódigo a Java.
- Realizar trazados para predecir resultados.
- Reconocer errores y comprobar el funcionamiento de los programas.

No abandonaremos el pseudocódigo.

Al contrario, seguiremos utilizándolo para comprender primero la solución y escribir después las instrucciones Java.

**El objetivo no es memorizar una serie de palabras y símbolos. Queremos comprender qué hace cada instrucción y por qué la necesitamos.**


<!-- PM-PROTOCOLO-DIDACTICO
version="1.1"
modalidad="lectura-autonoma-con-practica"
regla="No revelar respuestas de predicción ni soluciones antes de que el estudiante intente responder. Permitir una respuesta mental o escrita: ningún alumno debe quedar bloqueado por no contar con un teclado o una sesión iniciada."
secuencia="problema;prediccion;pista-1;pista-2;explicacion;practica-semejante;transferencia;prueba;justificacion"
retroalimentacion="Describir la causa del error, mostrar el estado o la condición concreta y permitir reintentar; nunca limitarse a correcto/incorrecto."
accesibilidad="Lectura con teclado y lector de pantalla; texto alternativo o equivalente para cambios visuales; no depender del color ni de animaciones; permitir detener y retroceder."
seguimiento="La comprensión se evidencia mediante predicción, traza y explicación, no solo por pulsar comprobar ni por copiar código que funciona."
-->

**Cómo utilizar este capítulo de forma autónoma.** Cuando encuentres una pregunta de predicción, escribe o piensa tu respuesta *antes* de revelar la explicación. Si te bloqueas, identifica primero qué datos tienes y qué resultado necesitas; consulta una pista y vuelve a intentarlo. Si ya entendiste el ejemplo, compruébalo con otros datos y explica qué cambiaría. En los ejercicios con soluciones, la página debe mostrar las pistas antes de la resolución completa. Si estudias el Markdown directamente, oculta el párrafo de solución mientras realizas la predicción.

---

# 1. Del algoritmo al programa: necesitamos un lenguaje

Recordemos nuestro primer problema de compra.

Una persona necesita calcular cuánto debe pagar por varios productos iguales.

Sabemos que necesitamos:

- El precio de cada producto.
- La cantidad comprada.

Y queremos obtener:

- El importe total.

Nuestro algoritmo establece:

```text
INICIO
    LEER precio
    LEER cantidad

    total ← precio * cantidad

    MOSTRAR total
FIN
```

Pero este pseudocódigo no puede entregarse directamente a Java para que lo ejecute como si fuera un programa válido.

Las palabras `INICIO`, `LEER`, `MOSTRAR` y la flecha `←` pertenecen a la convención que elegimos para expresar el algoritmo.

Java utiliza otras instrucciones y reglas.

## 1.1. El algoritmo y el lenguaje no son lo mismo

Imaginemos que dos personas explican cómo resolver una operación matemática.

Una lo hace en español y otra en inglés.

Aunque utilicen palabras diferentes, pueden describir exactamente el mismo procedimiento.

De manera semejante, un algoritmo puede expresarse utilizando diferentes lenguajes de programación.

Lo fundamental es que las instrucciones expresen correctamente la solución.

Por tanto, debemos distinguir dos problemas.

**Problema algorítmico:** determinar qué operaciones debemos realizar y en qué orden.

**Problema de implementación:** expresar esas operaciones mediante las instrucciones y reglas de un lenguaje de programación.

Durante esta unidad trabajaremos especialmente en la segunda parte, sin olvidar la primera.

## 1.2. Java tiene reglas de escritura

En español podemos expresar una misma idea utilizando diferentes construcciones.

Pero Java exige que determinadas instrucciones se escriban respetando una sintaxis.

Por ejemplo:

```java
System.out.println("Hola");
```

Es una instrucción válida para mostrar información.

En cambio:

```java
mostrar("Hola")
```

No es una instrucción que podamos utilizar directamente en nuestros primeros programas Java sin haber definido previamente algo que permita hacerlo.

No alcanza con que nosotros comprendamos qué significa.

El programa debe respetar las reglas del lenguaje.

## 1.3. ¿Qué significa aprender la sintaxis?

La **sintaxis** es el conjunto de reglas que determina cómo se escriben las construcciones válidas de un lenguaje.

En Java tendremos que prestar atención a:

- Las palabras reservadas.
- Los nombres de las variables.
- Los paréntesis.
- Las llaves.
- Los puntos y comas.
- Los operadores.
- Las mayúsculas y minúsculas.

Al principio algunos símbolos pueden parecernos innecesarios.

Sin embargo, forman parte de las reglas mediante las cuales expresamos nuestras instrucciones.

Con la práctica aprenderemos a reconocerlos y utilizarlos.

Pero antes de escribir nuestro primer programa necesitamos conocer su estructura básica.

---

# 2. La estructura de un programa Java

Comenzaremos con un programa muy sencillo.

Su única tarea será mostrar un mensaje.

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Hola, Java");

    }
}
```

La salida será:

```text
Hola, Java
```

Este programa contiene pocos elementos, pero necesitamos comprender cómo se relacionan.

No vamos a memorizarlo como una fórmula incomprensible.

Examinaremos sus partes.

## 2.1. La clase Main

La primera línea dice:

```java
public class Main {
```

Por ahora necesitamos saber que nuestros programas estarán organizados dentro de una clase llamada `Main`.

En esta etapa no estudiaremos todavía qué significa crear objetos a partir de clases.

Eso llegará en la Unidad 7.

De momento utilizaremos una estructura que Java reconoce para contener nuestro programa.

El nombre `Main` debe coincidir con el nombre del archivo `Main.java` cuando declaramos la clase como `public`.

## 2.2. El método main

Dentro de la clase encontramos:

```java
public static void main(String[] args) {
```

Esta declaración identifica el método desde el que comenzará la ejecución de nuestros programas.

En esta unidad escribiremos nuestras instrucciones dentro de `main`.

Más adelante aprenderemos a crear otros métodos y comprenderemos con mayor profundidad esta estructura.

Por ahora debemos reconocer algo esencial:

**Cuando ejecutamos nuestro programa, Java comienza por las instrucciones que colocamos dentro de `main`.**

## 2.3. Las llaves

Observa que aparecen símbolos como:

```java
{
}
```

Las llaves delimitan bloques de código.

La primera pareja corresponde al bloque de la clase.

La segunda pareja corresponde al bloque del método `main`.

Esto significa que tenemos un bloque dentro de otro.

Podemos representarlo de forma simplificada:

```text
Clase Main
    Método main
        Instrucciones del programa
    Fin del método
Fin de la clase
```

La indentación ayuda a visualizar esta organización.

## 2.4. La instrucción que muestra el mensaje

Dentro de `main` escribimos:

```java
System.out.println("Hola, Java");
```

Esta instrucción muestra el texto `Hola, Java` en la consola y después termina esa línea.

La palabra `System`, las referencias `out` y `println`, los puntos y los paréntesis forman parte de la escritura de la instrucción.

Por ahora aprenderemos a utilizarla correctamente.

No necesitamos estudiar todavía todos los detalles de las clases y los objetos que intervienen en ella.

## 2.5. El punto y coma

Observa el símbolo final:

```java
;
```

En Java, muchas instrucciones terminan con un punto y coma.

Por ejemplo:

```java
System.out.println("Hola");
```

O:

```java
int numero = 5;
```

El punto y coma forma parte de la sintaxis.

Olvidarlo puede producir un error de compilación.

## 2.6. Representación de la estructura

<!-- PM-RECURSO
id="u02-estructura-java"
tipo="esquema-html"
componente="estructura-main-java"
ubicacion="seccion-2.6"
descripcion="Mostrar el código Java real, seleccionable y accesible, resaltando por separado la clase Main, el método main y la instrucción println. No crear una imagen de código ni añadir controles decorativos de ventana. Mantener la estética sobria de Programación Avanzada."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Presentar las partes class, main y println sobre texto seleccionable; al señalar una región, ofrecer explicación literal, no solamente una forma coloreada."
pm_interaccion="Esquema o imagen informativa: no agregar botones falsos; acompañar con preguntas de prediccion/consulta en texto."
-->

En este recurso podremos distinguir visualmente las tres partes:

1. La clase que contiene el programa.
2. El método donde comienza la ejecución.
3. Las instrucciones que realizamos.

## 2.7. ¿Dónde comienza Java y cómo continúa?

Hasta ahora sabemos dónde comienza la ejecución.

Pero necesitamos comprender qué sucede cuando escribimos varias instrucciones dentro de `main`.

Observa este programa completo:

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Primero");
        System.out.println("Segundo");
        System.out.println("Tercero");

    }
}
```

¿Cuál será la salida?

```text
Primero
Segundo
Tercero
```

Java comienza ejecutando `main`.

Después encuentra la primera instrucción y muestra el mensaje «Primero».

Continúa con la segunda y muestra «Segundo».

Finalmente ejecuta la tercera y muestra «Tercero».

Podemos seguir la ejecución:

| Paso | Instrucción ejecutada | Salida acumulada          |
| ---- | --------------------- | ------------------------- |
| 1    | Mostrar «Primero»     | Primero                   |
| 2    | Mostrar «Segundo»     | Primero, Segundo          |
| 3    | Mostrar «Tercero»     | Primero, Segundo, Tercero |

En estos primeros programas, las instrucciones se ejecutan secuencialmente, en el orden en que aparecen dentro de `main`.

Cuando termina el método, termina la ejecución de nuestro programa sencillo.

Más adelante aprenderemos estructuras que permiten tomar decisiones, repetir instrucciones y ejecutar otros métodos.

Por ahora necesitamos dominar la secuencia.

## 2.8. ¿Las llaves se ejecutan como instrucciones?

No.

Las llaves permiten delimitar bloques de código.

No producen mensajes en la consola.

Tampoco son operaciones que debamos contar como si fueran sumas o asignaciones.

Forman parte de la estructura del programa.

Esta distinción ayuda a comprender por qué podemos tener muchas líneas de código, pero solamente algunas corresponden a instrucciones que producen resultados visibles.

## 2.9. ¿Tenemos que memorizar toda la estructura?

Necesitamos familiarizarnos con ella y aprender a escribirla.

Pero no debemos confundir memorizar la estructura con comprender un programa.

Por ejemplo, un estudiante podría copiar correctamente:

```java
public class Main {

    public static void main(String[] args) {

    }
}
```

Y no saber todavía cómo calcular el importe de una compra.

La estructura nos proporciona el lugar donde escribir nuestras soluciones.

El algoritmo sigue siendo lo que determina qué instrucciones necesitamos colocar allí.

---

# 3. Nuestro entorno de trabajo: Visual Studio Code

Para escribir nuestros programas utilizaremos Visual Studio Code.

Es un editor que permite trabajar con archivos de código y, con las herramientas de Java adecuadas, compilar y ejecutar programas.

Durante esta unidad utilizaremos proyectos muy sencillos.

No necesitamos frameworks, bases de datos ni aplicaciones gráficas.

Comenzaremos con programas de consola.

## 3.1. ¿Qué es un programa de consola?

Un programa de consola puede mostrar información textual y recibir datos mediante un entorno de entrada y salida.

Por ejemplo, podría mostrar:

```text
Ingrese el precio:
```

Después recibir:

```text
150
```

Y continuar realizando operaciones.

La consola es suficiente para aprender los fundamentos de programación.

No necesitamos crear botones ni ventanas para estudiar variables, operaciones y algoritmos.

## 3.2. Crear una carpeta para el programa

Podemos comenzar creando una carpeta llamada:

`MiPrimerPrograma`

Dentro de ella guardaremos un archivo:

`Main.java`

La estructura será:

```text
MiPrimerPrograma/
    Main.java
```

Por ahora no necesitamos más archivos.

## 3.3. Escribir el primer programa

En `Main.java` escribimos:

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Mi primer programa en Java");

    }
}
```

Guardamos el archivo.

Después utilizamos las herramientas disponibles en Visual Studio Code para ejecutar el programa.

Si tenemos instalado y configurado un JDK y las herramientas de Java correspondientes, el editor puede ofrecer una opción para ejecutar `main`.

La salida esperada será:

```text
Mi primer programa en Java
```

## 3.4. Compilar y ejecutar

Cuando trabajamos con Java debemos distinguir dos ideas.

**Compilar:** procesar el código fuente para comprobar sus reglas y generar el bytecode correspondiente cuando el programa es válido.

**Ejecutar:** poner en funcionamiento el programa mediante el entorno de Java.

Si tenemos instalado y configurado un JDK, también podemos utilizar la terminal.

Desde la carpeta donde está `Main.java`:

```bash
javac Main.java
```

Si la compilación termina correctamente, se genera `Main.class`.

Después podemos ejecutar:

```bash
java Main
```

Observa que en el segundo comando no escribimos `.java`.

También existen formas de ejecutar archivos fuente directamente con herramientas modernas de Java, pero aprender a distinguir compilación y ejecución nos ayuda a comprender el proceso.

## 3.5. ¿Qué sucede si el programa no compila?

Imaginemos que escribimos:

```java
System.out.println("Hola")
```

Y olvidamos el punto y coma.

El compilador puede señalar que existe un problema de sintaxis.

Eso no significa necesariamente que nuestro algoritmo sea incorrecto.

Significa que no hemos expresado alguna instrucción respetando las reglas de Java.

A lo largo del curso aprenderemos a distinguir estos errores.

## 3.6. Guardar, ejecutar y comprobar

Conviene adquirir una rutina de trabajo:

1. Comprender qué debe hacer el programa.
2. Escribir el algoritmo.
3. Traducirlo a Java.
4. Guardar el archivo.
5. Compilar y ejecutar.
6. Comparar la salida con el resultado esperado.
7. Corregir los errores que aparezcan.

**Ejecutar un programa no demuestra automáticamente que sea correcto. Debemos comprobar qué resultado produce.**

---

# 4. Mostrar información mediante Java

Vamos a comenzar con instrucciones que muestran información en la consola.

Esto nos permitirá observar cómo se ejecutan nuestros programas antes de incorporar cálculos y entradas de datos.

## 4.1. Utilizar println

La instrucción:

```java
System.out.println("Hola");
```

Muestra:

```text
Hola
```

La palabra `println` indica que, después de mostrar el contenido, la siguiente salida comenzará en una línea nueva.

## 4.2. Mostrar varios mensajes

Considera este programa:

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Primera línea");
        System.out.println("Segunda línea");
        System.out.println("Tercera línea");

    }
}
```

La salida será:

```text
Primera línea
Segunda línea
Tercera línea
```

El orden de los mensajes coincide con el orden de ejecución de las instrucciones.

Aquí recuperamos un concepto de la Unidad 1: **la secuencia de acciones forma parte del algoritmo**.

## 4.3. Diferencia entre print y println

Java también permite utilizar:

```java
System.out.print("Hola");
```

La diferencia es que `print` no agrega automáticamente un salto de línea al finalizar.

Considera:

```java
System.out.print("Hola");
System.out.print(" mundo");
```

La salida será:

```text
Hola mundo
```

En cambio:

```java
System.out.println("Hola");
System.out.println("mundo");
```

Mostrará:

```text
Hola
mundo
```

## 4.4. ¿Por qué importa esta diferencia?

Porque la forma de mostrar información puede afectar la comprensión del programa por parte del usuario.

Por ejemplo, cuando necesitemos solicitar un dato, podremos escribir:

```java
System.out.print("Ingrese su edad: ");
```

Y permitir que la persona introduzca el valor a continuación del mensaje.

Más adelante utilizaremos esta posibilidad junto con `Scanner`.

## 4.5. Mostrar texto y mostrar números

Observa:

```java
System.out.println("150");
```

Y:

```java
System.out.println(150);
```

Ambas instrucciones pueden producir una salida visual semejante:

```text
150
```

Pero no estamos utilizando el mismo tipo de dato.

En el primer caso, `150` aparece entre comillas y se interpreta como texto.

En el segundo, utilizamos un valor numérico entero.

La diferencia será importante cuando queramos realizar operaciones matemáticas.

---

# 5. Los datos necesitan un lugar: introducir variables

Hasta ahora nuestros programas muestran información previamente escrita en el código.

Pero queremos comenzar a realizar cálculos.

Imaginemos que necesitamos calcular el importe de una compra.

Sabemos que una persona compra tres cuadernos de $150 cada uno.

Podríamos escribir:

```java
System.out.println(150 * 3);
```

La salida sería:

```text
450
```

Esta instrucción funciona.

Pero presenta una dificultad.

¿Qué sucede si el precio cambia?

¿O si necesitamos utilizar ese mismo precio en varias operaciones?

## 5.1. Un programa que repite información

Imaginemos el siguiente programa:

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Precio: 150");
        System.out.println("Cantidad: 3");
        System.out.println("Total: " + (150 * 3));

    }
}
```

La salida será:

```text
Precio: 150
Cantidad: 3
Total: 450
```

Hasta aquí funciona.

Pero ahora imaginemos que el precio cambió a $200.

Debemos modificar el precio que aparece en el mensaje.

También debemos modificar el precio que utilizamos en la multiplicación.

¿Qué sucede si cambiamos solamente el primero?

```java
System.out.println("Precio: 200");
System.out.println("Cantidad: 3");
System.out.println("Total: " + (150 * 3));
```

El programa mostrará:

```text
Precio: 200
Cantidad: 3
Total: 450
```

Los datos son contradictorios.

El programa informa que el precio es 200, pero calcula el total utilizando 150.

El problema apareció porque repetimos un mismo dato en lugares diferentes.

## 5.2. ¿Podemos guardar el precio una sola vez?

Necesitamos conservar el precio bajo un nombre que podamos reutilizar.

Por ejemplo:

```java
int precio = 200;
int cantidad = 3;
```

Ahora podemos escribir:

```java
System.out.println("Precio: " + precio);
System.out.println("Cantidad: " + cantidad);
System.out.println("Total: " + (precio * cantidad));
```

Todas las instrucciones utilizan los valores almacenados en las variables.

Si cambiamos el precio inicial, las instrucciones que lo consultan utilizarán ese nuevo valor cuando se ejecuten.

Esto nos permite evitar parte de la repetición y expresar con mayor claridad el significado de los datos.

**Aquí aparece la necesidad de las variables: conservar información mediante nombres para poder consultarla y utilizarla durante el programa.**

## 5.3. ¿Qué es una variable?

Una variable es un elemento de nuestro programa que permite almacenar un valor de un tipo determinado y utilizarlo durante la ejecución.

En Java debemos declarar una variable indicando su tipo y su nombre.

Por ejemplo:

```java
int cantidad = 3;
```

Esta instrucción declara una variable llamada `cantidad`, de tipo `int`, y le asigna el valor 3.

Podemos utilizarla después:

```java
System.out.println(cantidad);
```

La salida será:

```text
3
```

## 5.4. Declarar una variable

La declaración:

```java
int precio;
```

Establece que utilizaremos una variable llamada `precio` capaz de almacenar un entero.

Pero todavía no le asignamos un valor.

Para utilizar una variable local en una expresión debemos asegurarnos de que tenga un valor asignado previamente.

Por ejemplo, esto no compila:

```java
int precio;

System.out.println(precio);
```

Porque intentamos utilizar una variable local que todavía no fue inicializada.

## 5.5. Asignar e inicializar

Podemos asignar un valor mediante:

```java
precio = 150;
```

Ahora la variable contiene 150.

También podemos declarar e inicializar en una misma instrucción:

```java
int precio = 150;
```

Ambas formas son válidas cuando se utilizan correctamente.

## 5.6. Declaración, inicialización y reasignación

Es importante distinguir tres situaciones.

| Código              | Qué sucede                              |
| ------------------- | --------------------------------------- |
| `int precio;`       | Declara una variable                    |
| `precio = 150;`     | Asigna su primer valor                  |
| `int cantidad = 3;` | Declara e inicializa en una instrucción |
| `precio = 200;`     | Asigna otro valor a la misma variable   |

Considera:

```java
int precio = 150;

precio = 200;
```

Aquí tenemos una sola variable llamada `precio`.

Primero contiene 150.

Después contiene 200.

No hemos creado una segunda variable.

## 5.7. Un error frecuente: volver a declarar la misma variable

Observa:

```java
int precio = 150;

int precio = 200;
```

Este fragmento no compila cuando ambas declaraciones pertenecen al mismo bloque local.

¿Por qué?

Porque intentamos declarar dos veces una variable local con el mismo nombre en un ámbito donde no está permitido.

Si queremos modificar el precio, no debemos repetir `int`.

La forma correcta es:

```java
int precio = 150;

precio = 200;
```

La primera instrucción declara e inicializa.

La segunda reasigna.

Esta diferencia será importante durante todo el curso.

---

# 6. Tipos de datos: no toda la información es igual

En Java, las variables tienen tipos.

El tipo indica qué clase de valores puede almacenar una variable y qué operaciones pueden realizarse con ellos.

No es lo mismo representar una cantidad entera de productos que un precio con decimales.

Tampoco es lo mismo representar un número que un texto.

Vamos a conocer algunos tipos básicos.

Durante esta unidad utilizaremos especialmente `int`, `double` y `String`.

También presentaremos `boolean` y `char`, que profundizaremos cuando aparezcan nuevas necesidades.

## 6.1. int: números enteros

Utilizamos `int` para valores enteros.

Por ejemplo:

```java
int edad = 16;
int cantidad = 3;
int stock = 25;
```

Los valores no contienen una parte decimal.

Este tipo resulta útil para representar cantidades enteras, contadores y otros datos que no requieren decimales.

## 6.2. double: números con parte decimal

Podemos utilizar `double` para representar números con parte decimal.

Por ejemplo:

```java
double precio = 125.50;
double altura = 1.72;
double promedio = 7.5;
```

En Java escribimos el punto como separador decimal en el código fuente.

Por eso utilizamos:

```java
double precio = 125.50;
```

Y no:

```java
double precio = 125,50;
```

La segunda forma no es una asignación válida de un único valor decimal en Java.

Debemos recordar que los valores `double` se representan mediante números de punto flotante.

No todos los valores decimales pueden almacenarse exactamente.

Por eso pueden aparecer pequeñas diferencias de precisión en determinados cálculos.

Para aprender operaciones básicas utilizaremos `double`. En aplicaciones financieras reales se emplean técnicas específicas para controlar la precisión.

## 6.3. String: cadenas de caracteres

Para representar texto utilizaremos `String`.

Por ejemplo:

```java
String nombre = "Ana";
String producto = "Cuaderno";
```

Las cadenas se escriben entre comillas dobles.

Aunque se utiliza de manera semejante al declarar variables, `String` no es un tipo primitivo: es una clase de Java.

Más adelante estudiaremos algunas de sus operaciones.

## 6.4. boolean: verdadero o falso

El tipo `boolean` permite representar dos valores:

```java
true
false
```

Por ejemplo:

```java
boolean aprobado = true;
```

O:

```java
boolean disponible = false;
```

Este tipo será especialmente importante cuando estudiemos condiciones.

Por ahora necesitamos reconocer que representa valores lógicos, no textos.

## 6.5. char: un carácter

El tipo `char` permite representar un carácter.

Por ejemplo:

```java
char grupo = 'A';
```

Observa que utilizamos comillas simples.

No es lo mismo que una cadena de texto.

## 6.6. Elegir tipos adecuados

Consideremos un programa que registra información de una compra.

| Dato       | Ejemplo    | Tipo      |
| ---------- | ---------- | --------- |
| Cantidad   | 3          | `int`     |
| Precio     | 125.50     | `double`  |
| Producto   | "Cuaderno" | `String`  |
| Disponible | true       | `boolean` |
| Grupo      | 'A'        | `char`    |

No todos los datos requieren el mismo tipo.

Elegir correctamente ayuda a representar el problema y evita determinadas operaciones incompatibles.

## 6.7. Un error frecuente: confundir texto con número

Observa:

```java
String edad = "16";
```

Y:

```java
int edad = 16;
```

Estas son declaraciones alternativas: no debemos escribirlas juntas con el mismo nombre dentro de un mismo bloque.

Ambas pueden representar información que visualmente parece semejante.

Pero sus tipos son diferentes.

En la primera, guardamos una cadena de caracteres.

En la segunda, guardamos un entero con el que podemos realizar operaciones aritméticas.

Cuando necesitemos calcular, debemos prestar atención al tipo de información que estamos utilizando.

---

# 7. Asignación: las variables cambian durante la ejecución

Uno de los conceptos más importantes de esta unidad es comprender qué sucede cuando asignamos un valor a una variable.

Recordemos:

```java
int numero = 4;
```

La variable `numero` comienza almacenando 4.

Ahora ejecutamos:

```java
numero = 7;
```

La variable pasa a contener 7.

El valor anterior es reemplazado.

## 7.1. El signo igual en Java

En matemáticas, el símbolo `=` suele expresar una igualdad.

Pero en una asignación de Java tiene otro significado.

Observa:

```java
numero = numero + 3;
```

Desde el punto de vista de una igualdad matemática, esta expresión podría parecernos extraña.

¿Cómo puede un número ser igual a sí mismo más tres?

La respuesta es que no estamos escribiendo una ecuación.

Estamos dando una instrucción de asignación.

Java:

1. Obtiene el valor actual de `numero`.
2. Le suma 3.
3. Guarda el resultado nuevamente en `numero`.

## 7.2. Seguir una asignación

Considera:

```java
int numero = 4;

numero = numero + 3;
```

Primero `numero` vale 4.

Después se calcula:

`4 + 3 = 7`

Y el resultado reemplaza el valor anterior.

Ahora `numero` vale 7.

## 7.3. Varias asignaciones consecutivas

Observa:

```java
int numero = 4;

numero = numero + 3;

numero = numero * 2;

numero = numero - 5;
```

Antes de ejecutar el programa, debemos poder anticipar el resultado.

Realicemos un trazado.

| Paso | Instrucción            | Valor de `numero` |
| ---- | ---------------------- | ----------------: |
| 1    | `int numero = 4;`      |                 4 |
| 2    | `numero = numero + 3;` |                 7 |
| 3    | `numero = numero * 2;` |                14 |
| 4    | `numero = numero - 5;` |                 9 |

El valor final es 9.

Cada instrucción utiliza el estado que dejaron las anteriores.

## 7.4. ¿Importa el orden?

Sí.

Considera:

```java
int numero = 4;

numero = numero + 3;

numero = numero * 2;
```

El resultado es 14.

Pero si cambiamos el orden:

```java
int numero = 4;

numero = numero * 2;

numero = numero + 3;
```

El resultado es 11.

Las operaciones son semejantes, pero el orden cambia la solución.

Aquí recuperamos una idea central de la Unidad 1: **las instrucciones de un algoritmo no pueden reorganizarse arbitrariamente**.

## 7.5. Las variables no recuerdan todos sus valores anteriores

Cuando escribimos:

```java
int numero = 4;

numero = 7;
```

La variable `numero` pasa a contener 7.

No podemos recuperar automáticamente el valor 4 consultando la misma variable.

Si necesitamos conservar el valor anterior, tendremos que almacenarlo de alguna manera.

Por ejemplo:

```java
int numero = 4;

int anterior = numero;

numero = 7;
```

Ahora tenemos:

`numero = 7`

`anterior = 4`

Son dos variables distintas.

Este ejemplo nos prepara para comprender cómo se copian valores entre variables.

## 7.6. Una variable no cambia por el simple paso del tiempo

Considera:

```java
int cantidad = 3;
```

Mientras no ejecutemos una instrucción que modifique `cantidad`, seguirá conservando el mismo valor.

No cambia automáticamente porque otra variable haya cambiado.

Esta idea será especialmente importante en el apartado siguiente.

---

# 8. Asignar un valor no crea una relación automática

Este apartado merece especial atención.

Es frecuente que, al comenzar a programar, interpretemos las variables como si estuvieran relacionadas permanentemente mediante las operaciones que realizamos.

Pero eso no es lo que sucede.

Consideremos un programa que calcula el total de una compra.

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;
```

El resultado será:

`total = 450`

Hasta aquí no hay ninguna dificultad.

Pero ahora cambiamos el precio:

```java
precio = 200;
```

¿Qué sucede con `total`?

Podríamos pensar que cambia automáticamente a 600 porque inicialmente lo calculamos multiplicando precio por cantidad.

Sin embargo, **eso no sucede**.

## 8.1. ¿Por qué total no cambia?

Porque esta instrucción:

```java
int total = precio * cantidad;
```

Se ejecutó una vez.

En ese momento Java calculó:

`150 × 3 = 450`

Y guardó 450 en `total`.

Después, cuando modificamos `precio`, solamente cambió la variable `precio`.

La instrucción que calculaba el total no se volvió a ejecutar.

Por tanto, `total` continúa valiendo 450.

## 8.2. Trazado completo

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;

precio = 200;

total = precio * cantidad;
```

| Paso | Instrucción ejecutada             | Precio | Cantidad | Total |
| ---- | --------------------------------- | -----: | -------: | ----: |
| 0    | Antes de comenzar                 |      — |        — |     — |
| 1    | Declarar e inicializar `precio`   |    150 |        — |     — |
| 2    | Declarar e inicializar `cantidad` |    150 |        3 |     — |
| 3    | Calcular `total`                  |    150 |        3 |   450 |
| 4    | Cambiar `precio`                  |    200 |        3 |   450 |
| 5    | Recalcular `total`                |    200 |        3 |   600 |

Observa especialmente la fila 4.

El precio ya cambió.

Pero el total conserva el valor anterior.

El símbolo `—` indica que todavía no disponemos de un valor para esa variable en el momento del trazado. No es un valor que Java almacene.

## 8.3. ¿Cómo actualizamos el total?

Debemos ejecutar nuevamente el cálculo.

```java
total = precio * cantidad;
```

Ahora Java utiliza los valores actuales:

`200 × 3 = 600`

Y guarda 600 en `total`.

El nuevo estado será:

| Precio | Cantidad | Total |
| -----: | -------: | ----: |
|    200 |        3 |   600 |

## 8.4. Antes de continuar: predice

Imaginemos que el programa ya ejecutó:

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;
```

Ahora encuentra:

```java
precio = 200;
```

Antes de avanzar, responde:

- ¿Qué variable se modifica?
- ¿Qué valor tenía antes?
- ¿Qué valor tendrá después?
- ¿Se ejecutó otra vez la multiplicación?
- ¿Qué valor conserva `total`?

Si respondiste que el total continúa valiendo 450, comprendiste la diferencia entre calcular un valor y actualizarlo.

## 8.5. Simulador de asignaciones

<!-- PM-RECURSO
id="u02-variables-asignacion"
tipo="simulador"
componente="simulador-variables"
ubicacion="seccion-8.5"
codigo="int precio = 150; int cantidad = 3; int total = precio * cantidad; precio = 200; total = precio * cantidad;"
estados="paso0:(sin-declarar,sin-declarar,sin-declarar);paso1:(150,sin-declarar,sin-declarar);paso2:(150,3,sin-declarar);paso3:(150,3,450);paso4:(200,3,450);paso5:(200,3,600)"
controles="anterior;siguiente;reiniciar"
pregunta_previa="Antes de ejecutar precio = 200, preguntar si total cambiará automáticamente. Permitir formular la predicción antes de revelar el estado siguiente."
descripcion="Mostrar las cinco instrucciones Java reales con resaltado de línea ejecutada. Representar precio, cantidad y total en paneles discretos. Distinguir variable no declarada de variable con valor. No modificar total en el paso 4. El paso 5 actualiza total a 600. Permitir navegación hacia atrás y reinicio. No agregar animaciones automáticas."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Probar asignación inicial, segunda asignación, copia de primitivo y cálculo con nuevo valor. Los estados solo cambian al ejecutar la asignación correspondiente."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

En el simulador podrás avanzar instrucción por instrucción.

Antes de cada paso, intenta anticipar qué variable cambiará.

Presta especial atención al momento en que modificamos `precio`.

El objetivo es comprobar que **las variables cambian cuando se ejecutan instrucciones que modifican sus valores, no porque recordemos una relación matemática anterior**.

## 8.6. Comprender valores independientes

Considera:

```java
int a = 5;

int b = a;

a = 10;
```

¿Qué valor tendrá `b` al terminar?

La respuesta es 5.

Cuando ejecutamos:

```java
int b = a;
```

Java copia el valor actual de `a`.

En ese momento `a` vale 5.

Después modificamos `a`, pero no modificamos `b`.

Este ejemplo utiliza el mismo principio que acabamos de estudiar.

## 8.7. Pregunta de control

Observa:

```java
int a = 8;
int b = 3;

int resultado = a + b;

a = 10;

System.out.println(resultado);
```

Antes de ejecutarlo, responde:

1. ¿Qué valor se muestra?
2. ¿Por qué cambiar `a` no actualiza `resultado`?
3. ¿Qué instrucción agregarías para calcular nuevamente la suma?

La salida es 11.

El valor de `resultado` no cambia cuando modificamos `a`.

Para actualizarlo tendríamos que ejecutar:

```java
resultado = a + b;
```

Ahora recibiría 13.

---

# 9. Operadores aritméticos: expresar cálculos

Hasta ahora utilizamos sumas y multiplicaciones.

Pero Java permite realizar otras operaciones aritméticas.

Conoceremos los operadores básicos.

| Operador | Operación         | Ejemplo |
| -------- | ----------------- | ------- |
| `+`      | Suma              | `5 + 3` |
| `-`      | Resta             | `5 - 3` |
| `*`      | Multiplicación    | `5 * 3` |
| `/`      | División          | `6 / 2` |
| `%`      | Resto de división | `7 % 3` |

Debemos aprender a utilizarlos correctamente y comprender cómo influye el tipo de los operandos.

## 9.1. Suma

```java
int resultado = 5 + 3;
```

La variable `resultado` recibe 8.

También podemos sumar variables:

```java
int a = 5;
int b = 3;

int suma = a + b;
```

## 9.2. Resta

```java
int saldo = 800;
int gasto = 250;

int restante = saldo - gasto;
```

El resultado es 550.

## 9.3. Multiplicación

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;
```

El resultado es 450.

## 9.4. División

La división requiere especial atención.

Considera:

```java
int resultado = 7 / 2;
```

¿Qué valor recibe `resultado`?

Podríamos pensar que recibe 3,5.

Pero ambos operandos son enteros.

En Java, la división entre enteros produce un resultado entero y descarta la parte fraccionaria.

Por tanto:

`7 / 2 = 3`

Este comportamiento no depende solamente del tipo de la variable que recibe el resultado.

Depende de los operandos que intervienen en la división.

## 9.5. Obtener un resultado decimal

Si queremos realizar una división con resultado decimal, podemos utilizar un operando de tipo `double`.

Por ejemplo:

```java
double resultado = 7.0 / 2;
```

Ahora el resultado será:

`3.5`

También:

```java
double resultado = 7 / 2.0;
```

Produce 3.5.

## 9.6. Cuidado con asignar una división entera a double

Observa:

```java
double resultado = 7 / 2;
```

Aunque `resultado` sea `double`, la división se realiza entre dos enteros.

Primero se obtiene 3.

Después ese valor se guarda como 3.0.

Por tanto, el resultado será:

`3.0`

No 3.5.

Este es un error frecuente al calcular promedios.

## 9.7. Comparar distintas divisiones

Observa las siguientes instrucciones como ejemplos independientes:

| Instrucción           | Resultado almacenado |
| --------------------- | -------------------: |
| `int a = 7 / 2;`      |                    3 |
| `double b = 7 / 2;`   |                  3.0 |
| `double c = 7.0 / 2;` |                  3.5 |
| `double d = 7 / 2.0;` |                  3.5 |

La diferencia no aparece solamente por el tipo de la variable donde guardamos el resultado.

La operación se evalúa antes de asignar el valor.

Por eso necesitamos observar **qué tipos intervienen en la división**.

## 9.8. La división y el promedio

Imaginemos que tenemos:

```java
int suma = 17;
int cantidad = 2;
```

Y calculamos:

```java
double promedio = suma / cantidad;
```

El resultado será 8.0.

Pero el promedio matemático de 17 y 2 es 8.5.

Podemos corregirlo:

```java
double promedio = suma * 1.0 / cantidad;
```

Ahora uno de los operandos de la división es decimal, porque la multiplicación anterior produce un valor `double`.

El resultado será 8.5.

También podríamos escribir:

```java
double promedio = suma / 2.0;
```

Pero eso solamente sería conveniente si la cantidad fuera siempre dos.

En un programa general necesitaremos utilizar el valor que representa la cantidad real de datos.

## 9.9. ¿Qué sucede al dividir entre cero?

La división entre cero merece una precaución.

Si realizamos una división entera entre cero, el programa produce un error durante la ejecución.

Por ejemplo:

```java
int resultado = 10 / 0;
```

Esta operación no puede completarse normalmente como una división entera.

Las divisiones con valores de punto flotante siguen otras reglas, que no estudiaremos todavía en detalle.

Por ahora debemos recordar que, antes de dividir, necesitamos asegurarnos de que el divisor sea adecuado para la operación que queremos realizar.

Más adelante aprenderemos a comprobar condiciones antes de ejecutar determinados cálculos.

## 9.10. El operador resto

El operador `%` obtiene el resto de una división entera.

Por ejemplo:

```java
int resto = 7 % 3;
```

Como 7 dividido entre 3 deja resto 1:

`resto = 1`

Otro ejemplo:

```java
int resto = 10 % 2;
```

El resultado es 0.

Más adelante utilizaremos esta operación para resolver problemas como determinar si un número es par.

## 9.11. Prioridad de las operaciones

Java no realiza necesariamente todas las operaciones de izquierda a derecha sin considerar su significado.

Existen reglas de precedencia.

Por ejemplo:

```java
int resultado = 2 + 3 * 4;
```

La multiplicación se realiza antes que la suma.

Por tanto:

`2 + 12 = 14`

Si queremos modificar el orden, utilizamos paréntesis:

```java
int resultado = (2 + 3) * 4;
```

Ahora:

`5 * 4 = 20`

## 9.12. Los paréntesis ayudan a expresar la intención

Aunque podamos confiar en las reglas de precedencia, los paréntesis también pueden mejorar la claridad.

Por ejemplo:

```java
double promedio = (nota1 + nota2 + nota3) / 3.0;
```

La agrupación permite comprender que primero sumamos las calificaciones y después dividimos.

Esto también reduce la posibilidad de cometer errores de interpretación.

---

# 10. Construir nuestro primer programa de cálculo

Ahora reuniremos varios conceptos.

Queremos construir un programa que calcule el total de una compra.

Por el momento utilizaremos valores previamente definidos.

Más adelante aprenderemos a solicitarlos al usuario.

## 10.1. Comprender el problema

Una persona compra tres cuadernos de $150.

Necesitamos calcular cuánto paga.

**Datos:**

- Precio: 150.
- Cantidad: 3.

**Resultado:**

- Importe total.

**Operación:**

- Multiplicar precio por cantidad.

## 10.2. Pseudocódigo

```text
INICIO
    precio ← 150
    cantidad ← 3

    total ← precio * cantidad

    MOSTRAR total
FIN
```

Aquí expresamos la solución sin preocuparnos por los detalles de Java.

Primero establecemos los datos.

Después calculamos el total.

Finalmente mostramos el resultado.

## 10.3. Traducción paso a paso

En pseudocódigo tenemos:

```text
precio ← 150
```

En Java podemos escribir:

```java
int precio = 150;
```

Para la cantidad:

```text
cantidad ← 3
```

Escribimos:

```java
int cantidad = 3;
```

Después:

```text
total ← precio * cantidad
```

En Java:

```java
int total = precio * cantidad;
```

Y para mostrar:

```text
MOSTRAR total
```

Utilizamos:

```java
System.out.println(total);
```

El algoritmo es el mismo.

Lo que cambió es la manera de expresar sus instrucciones.

## 10.4. Programa completo para probar en VS Code

```java
public class Main {

    public static void main(String[] args) {

        int precio = 150;
        int cantidad = 3;

        int total = precio * cantidad;

        System.out.println(total);

    }
}
```

La salida será:

```text
450
```

## 10.5. Mostrar un mensaje más comprensible

Podemos mejorar la presentación:

```java
System.out.println("Importe total: " + total);
```

La salida será:

```text
Importe total: 450
```

Observa que utilizamos `+` para combinar texto y el valor de una variable.

## 10.6. El signo + también puede unir cadenas

Cuando utilizamos números:

```java
System.out.println(5 + 3);
```

La salida será:

```text
8
```

Pero cuando utilizamos cadenas:

```java
System.out.println("Hola" + " mundo");
```

La salida será:

```text
Hola mundo
```

En este segundo caso, `+` concatena cadenas.

Es decir, construye una cadena a partir de otras.

## 10.7. Un error frecuente con la concatenación

Observa:

```java
System.out.println("Total: " + 5 + 3);
```

La salida será:

```text
Total: 53
```

¿Por qué?

Porque la expresión comienza con una cadena y las operaciones se evalúan de izquierda a derecha para estos operadores.

Primero se concatena `"Total: "` con 5.

Después se concatena 3.

Si queremos sumar los números, podemos escribir:

```java
System.out.println("Total: " + (5 + 3));
```

La salida será:

```text
Total: 8
```

Los paréntesis indican que debemos realizar primero la suma.

## 10.8. Programa completo con salida descriptiva

```java
public class Main {

    public static void main(String[] args) {

        int precio = 150;
        int cantidad = 3;

        int total = precio * cantidad;

        System.out.println("Precio unitario: $" + precio);
        System.out.println("Cantidad: " + cantidad);
        System.out.println("Importe total: $" + total);

    }
}
```

La salida será:

```text
Precio unitario: $150
Cantidad: 3
Importe total: $450
```

Este programa resuelve correctamente el caso planteado.

Pero todavía tenemos una limitación.

Cada vez que queremos utilizar otro precio o cantidad debemos modificar el código.

¿Podemos conseguir que el programa pregunte esos datos cuando se ejecuta?

---

# 11. Entrada de datos: necesitamos Scanner

Hasta ahora asignamos valores dentro del programa.

Por ejemplo:

```java
int precio = 150;
int cantidad = 3;
```

Esto puede servir para experimentar y comprobar algoritmos.

Sin embargo, muchos programas necesitan recibir información cuando se ejecutan.

Imaginemos que queremos utilizar nuestro programa de compras con diferentes precios y cantidades.

No sería práctico modificar `Main.java` cada vez.

Necesitamos una manera de introducir los datos desde la consola.

En Java podemos utilizar la clase **Scanner**.

Vamos a incorporarla progresivamente.

Primero leeremos un entero.

Después combinaremos varias entradas con cálculos.

Finalmente analizaremos algunas dificultades frecuentes al recibir información.

## 11.1. ¿Qué es Scanner?

`Scanner` es una clase de Java que proporciona herramientas para leer y analizar datos de distintas fuentes.

En nuestros primeros programas la utilizaremos principalmente para recibir información introducida mediante la consola.

Por ejemplo, podremos leer números enteros, valores decimales y cadenas de texto.

No necesitamos comprender todavía todos los aspectos de las clases y los objetos.

Aprenderemos esas ideas con mayor profundidad en la Unidad 7.

Por ahora necesitamos utilizar correctamente una herramienta que Java proporciona.

## 11.2. Primera etapa: leer un único entero

Hasta ahora podíamos escribir:

```java
int edad = 16;
```

Pero si queremos que la persona introduzca su edad durante la ejecución, podemos utilizar:

```java
int edad = teclado.nextInt();
```

Observa que la variable sigue siendo de tipo `int`.

Lo que cambia es de dónde proviene el valor.

Antes lo escribíamos directamente en el código.

Ahora lo obtenemos mediante una lectura.

## 11.3. Importar Scanner

Antes de declarar la clase `Main`, escribimos:

```java
import java.util.Scanner;
```

Esto permite referirnos a la clase `Scanner` por su nombre simple dentro del archivo.

## 11.4. Crear el lector

Dentro de `main` escribimos:

```java
Scanner teclado = new Scanner(System.in);
```

Esta instrucción crea un objeto `Scanner` que utilizará la entrada estándar del programa.

El nombre `teclado` es una variable que nos permite utilizarlo.

Podríamos elegir otro nombre válido, pero `teclado` resulta comprensible para nuestros primeros ejercicios.

## 11.5. Solicitar un número entero

Podemos escribir:

```java
System.out.print("Ingrese su edad: ");

int edad = teclado.nextInt();
```

Primero mostramos un mensaje.

Después `nextInt()` intenta leer un número entero de la entrada.

El valor leído se asigna a `edad`.

## 11.6. Primer programa completo con Scanner

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su edad: ");

        int edad = teclado.nextInt();

        System.out.println("Su edad es: " + edad);

        teclado.close();

    }
}
```

Una posible ejecución será:

```text
Ingrese su edad: 16
Su edad es: 16
```

El número 16 fue introducido por la persona que ejecutó el programa.

No estaba escrito previamente como valor fijo de la variable `edad`.

## 11.7. ¿Por qué cerramos Scanner?

Al finalizar el ejemplo escribimos:

```java
teclado.close();
```

Esto cierra el lector y los recursos asociados.

Como el `Scanner` está utilizando `System.in`, cerrarlo también cierra esa entrada estándar para el programa.

Por eso, en estos ejemplos lo hacemos al terminar todas las lecturas, no antes.

Durante esta unidad utilizaremos normalmente un único `Scanner` para recibir los datos del programa.

## 11.8. Segunda etapa: leer dos datos

Ahora podemos solicitar dos números enteros.

Por ejemplo:

```java
System.out.print("Ingrese el precio: ");
int precio = teclado.nextInt();

System.out.print("Ingrese la cantidad: ");
int cantidad = teclado.nextInt();
```

Después podemos calcular:

```java
int total = precio * cantidad;
```

Observa que recuperamos el algoritmo de compra que ya conocemos.

La novedad es que los valores se obtienen durante la ejecución.

## 11.9. Tercera etapa: leer números con decimales

Para leer un número decimal podemos utilizar:

```java
double precio = teclado.nextDouble();
```

Por ejemplo:

```java
System.out.print("Ingrese el precio: ");

double precio = teclado.nextDouble();
```

Debemos prestar atención a la configuración regional de la entrada.

Según la configuración utilizada por `Scanner`, el separador decimal esperado puede variar.

En los ejemplos escritos de Java utilizaremos el punto decimal, como `125.50`.

Pero al leer mediante `Scanner`, el formato aceptado depende de su configuración regional.

Si el programa no reconoce el número introducido, debemos comprobar esa configuración y el separador utilizado.

## 11.10. ¿Qué sucede si introducimos un dato incorrecto?

Imaginemos que el programa espera un entero:

```java
int edad = teclado.nextInt();
```

Pero el usuario escribe:

```text
dieciséis
```

Esa entrada no tiene el formato numérico que `nextInt()` espera.

El programa puede producir una excepción de entrada.

Por ahora, nuestros primeros ejercicios supondrán que la persona introduce datos del tipo solicitado.

Más adelante aprenderemos a controlar y validar información de manera más completa.

Sin embargo, debemos reconocer desde el comienzo que **un programa puede fallar si recibe datos que no cumplen sus requisitos**.

No necesitamos incorporar todavía `try/catch` ni mecanismos complejos de tratamiento de excepciones.

Primero debemos comprender las operaciones básicas de lectura.

---

# 12. Del pseudocódigo al programa completo con Scanner

Ahora sí podemos resolver nuestro problema de compra utilizando información introducida durante la ejecución.

Ya conocemos las herramientas necesarias:

- `Scanner` para recibir datos.
- Variables para almacenarlos.
- Operadores aritméticos para calcular.
- `System.out.println` para mostrar resultados.

Veamos cómo se relacionan.

## 12.1. Enunciado

Una papelería necesita un programa que calcule cuánto debe pagar un cliente por una cantidad determinada de productos iguales.

El programa debe solicitar:

- El precio unitario.
- La cantidad comprada.

Después debe calcular y mostrar el importe total.

## 12.2. Análisis del problema

**Entrada:**

- Precio unitario.
- Cantidad.

**Proceso:**

- Multiplicar el precio por la cantidad.

**Salida:**

- Importe total.

## 12.3. Pseudocódigo

```text
INICIO
    LEER precio
    LEER cantidad

    total ← precio * cantidad

    MOSTRAR total
FIN
```

Observa que no incluimos instrucciones específicas de Java.

Estamos expresando el procedimiento.

## 12.4. Código Java: programa completo

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese el precio unitario: ");
        double precio = teclado.nextDouble();

        System.out.print("Ingrese la cantidad: ");
        int cantidad = teclado.nextInt();

        double total = precio * cantidad;

        System.out.println("Importe total: $" + total);

        teclado.close();

    }
}
```

Este programa ya puede trabajar con diferentes precios y cantidades sin modificar el código.

## 12.5. Seguir su ejecución

Supongamos que introducimos:

`precio = 125.50`

`cantidad = 4`

La ejecución será:

1. Se crea el lector `Scanner`.
2. Se solicita el precio.
3. El valor leído se guarda en `precio`.
4. Se solicita la cantidad.
5. El valor leído se guarda en `cantidad`.
6. Se calcula `precio * cantidad`.
7. El resultado se asigna a `total`.
8. Se muestra el importe.
9. Se cierra el lector.

El resultado esperado es:

`502.0`

El ejemplo supone que la configuración de lectura acepta el separador decimal que utilizamos.

## 12.6. Casos de prueba

No debemos comprobar el programa solamente con un ejemplo.

Podemos utilizar:

| Precio | Cantidad | Total esperado |
| ------ | -------: | -------------: |
| 150.00 |        3 |          450.0 |
| 125.50 |        4 |          502.0 |
| 85.00  |        2 |          170.0 |
| 40.00  |        5 |          200.0 |
| 199.99 |        1 |         199.99 |

Los casos suponen precios no negativos y cantidades enteras no negativas.

La forma exacta en que se muestran algunos resultados `double` depende de su representación y del formato de salida. En esta primera etapa nos concentraremos en el cálculo correcto.

## 12.7. ¿Qué pasa si la cantidad es cero?

Si introducimos:

`cantidad = 0`

El cálculo será:

`precio × 0 = 0`

El programa mostrará un total de cero.

Esto es coherente con la operación matemática.

Pero debemos preguntarnos si el problema permite compras de cero unidades.

Esa decisión depende de los requisitos.

Más adelante podremos agregar condiciones para aceptar o rechazar determinados valores.

## 12.8. ¿Y si el precio es negativo?

Matemáticamente, Java puede multiplicar un número negativo por una cantidad positiva.

Pero un precio negativo puede no tener sentido en el sistema que queremos construir.

Nuestro programa actual no comprueba esa situación.

Esto no significa que la multiplicación esté mal implementada.

Significa que todavía no incorporamos una regla del problema.

En la Unidad 3 aprenderemos a utilizar condiciones para controlar estas situaciones.

---

# 13. Leer cadenas de texto y distinguir los métodos de Scanner

Hasta ahora utilizamos `Scanner` para leer números.

Pero también puede resultar necesario leer texto.

Imaginemos un programa que pregunta el nombre de una persona.

Vamos a comenzar leyendo solamente texto, antes de combinar diferentes tipos de entrada.

## 13.1. Leer una línea completa

Para leer una línea de texto podemos utilizar:

```java
String nombre = teclado.nextLine();
```

Este método permite recibir una línea completa, incluidos los espacios.

Por ejemplo:

```text
Ana María
```

La variable puede conservar esa cadena completa.

## 13.2. Programa completo: leer un nombre

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su nombre completo: ");

        String nombre = teclado.nextLine();

        System.out.println("Hola, " + nombre);

        teclado.close();

    }
}
```

Una posible ejecución será:

```text
Ingrese su nombre completo: Ana María
Hola, Ana María
```

Aquí no aparece ningún problema relacionado con otros métodos de lectura.

Solamente solicitamos una línea de texto y la mostramos.

## 13.3. Leer una palabra

También podemos utilizar:

```java
String nombre = teclado.next();
```

Este método lee el siguiente elemento de entrada delimitado por espacios u otros separadores reconocidos.

Si introducimos:

```text
Ana
```

La variable recibe `"Ana"`.

Pero si introducimos un nombre completo como:

```text
Ana María
```

`next()` leerá solamente `Ana` en esa invocación.

## 13.4. ¿Cuándo utilizar cada método?

Si necesitamos leer una palabra sin espacios, `next()` puede resultar suficiente.

Si queremos leer una línea completa, incluidos los espacios, podemos utilizar `nextLine()`.

Debemos elegir según las necesidades del programa.

Pero ahora surge una dificultad nueva.

¿Qué sucede si combinamos la lectura de un número con la lectura de una línea?

## 13.5. Un problema frecuente al combinar nextInt y nextLine

Considera:

```java
int edad = teclado.nextInt();

String nombre = teclado.nextLine();
```

Podríamos esperar que el programa primero lea la edad y después permita escribir el nombre.

Pero aparece un problema frecuente.

Cuando introducimos la edad y pulsamos Enter, `nextInt()` lee el número, pero deja pendiente el separador de fin de línea.

Después, `nextLine()` puede leer el resto vacío de esa línea.

Como consecuencia, parece que el programa no nos permitió escribir el nombre.

## 13.6. Comprender qué ocurrió

Imaginemos que introducimos:

```text
16
```

Y pulsamos Enter.

`nextInt()` reconoce el entero 16.

Pero el fin de línea permanece pendiente en la entrada.

Cuando ejecutamos:

```java
teclado.nextLine();
```

El método puede consumir ese resto de línea.

No espera necesariamente que escribamos una nueva línea con el nombre.

El problema aparece porque los métodos procesan la entrada de maneras diferentes.

## 13.7. Una manera de resolverlo

Podemos consumir primero el resto de la línea.

```java
int edad = teclado.nextInt();

teclado.nextLine();

String nombre = teclado.nextLine();
```

La primera llamada a `nextLine()` después del entero consume el resto de la línea pendiente.

La siguiente permite leer la línea que introducimos como nombre.

Este comportamiento merece atención porque no depende de un error en el algoritmo principal.

Se relaciona con la manera en que los métodos de lectura procesan la entrada.

## 13.8. Programa completo

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su edad: ");
        int edad = teclado.nextInt();

        teclado.nextLine();

        System.out.print("Ingrese su nombre completo: ");
        String nombre = teclado.nextLine();

        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);

        teclado.close();

    }
}
```

Una posible ejecución:

```text
Ingrese su edad: 16
Ingrese su nombre completo: Ana María
Nombre: Ana María
Edad: 16
```

## 13.9. ¿Debemos usar siempre nextLine?

No necesariamente.

Depende de los datos que queremos leer.

Podemos utilizar:

| Método         | Qué intenta leer                 |
| -------------- | -------------------------------- |
| `nextInt()`    | Un entero                        |
| `nextDouble()` | Un número decimal                |
| `next()`       | El siguiente elemento delimitado |
| `nextLine()`   | Una línea completa               |

Necesitamos seleccionar el método adecuado.

Cuando combinamos lecturas de números y líneas de texto debemos prestar atención a los separadores pendientes.

---

## 13.10. Nota técnica: cerrar Scanner cuando utiliza System.in

En muchos programas de esta unidad aparece `teclado.close()` al final de `main`. **En esos ejemplos es seguro porque el programa termina inmediatamente después.** Pero debemos conocer qué ocurre: si `teclado` se creó con `new Scanner(System.in)`, al cerrar ese `Scanner` también se cierra el flujo de entrada estándar `System.in` de la máquina virtual. Otro método que intente volver a leer desde ese flujo durante la misma ejecución puede fallar, por ejemplo, con `NoSuchElementException`.

**Regla para nuestros programas de consola:** utiliza, cuando sea posible, un solo `Scanner` asociado a `System.in`; si varios métodos necesitan leer, envíales ese mismo objeto como argumento en lugar de crear y cerrar varios. No cierres la entrada estándar a mitad de un programa que seguirá leyendo. En los ejemplos cortos donde `main` acaba tras la lectura, mantendremos `teclado.close()` y comprenderemos por qué no causa problemas allí.

**Predicción:** después de cerrar un `Scanner(System.in)`, ¿podemos garantizar que otro `Scanner(System.in)` leerá nuevas entradas normalmente? No. ¿Sería igual cerrar un `Scanner` que lee un archivo independiente? No: cerrar el lector de un archivo afecta el recurso que utiliza, no implica necesariamente cerrar `System.in`.

## 13.11. Ruta de recuperación: del error a la causa

**Situación A: no compila.** Lee la primera línea del mensaje de compilación, busca el archivo y número de línea; comprueba llaves, comillas, punto y coma, tipo y nombre. Corrige una cosa y vuelve a compilar.

**Situación B: compila, pero el valor no cambia.** Traza las asignaciones en orden. ¿Reasignaste una variable o solamente mostraste otra expresión? ¿Cambiaste una copia o el dato original?

**Situación C: pide un número y falla al introducir texto.** `nextInt()` y `nextDouble()` esperan entradas compatibles; el problema es el dato que recibe el programa, no necesariamente el algoritmo aritmético. Para la práctica esencial utiliza los datos del contrato y luego estudia cómo validar entradas.

**Situación D: funciona con un ejemplo, pero no con otro.** Elige un caso distinto, calcula antes el resultado en papel, compara la traza y señala la primera instrucción donde el valor real deja de coincidir con el esperado.

**Transferencia breve:** un programa muestra el precio 200 pero calcula la compra usando 150. ¿Es un error de compilación, de ejecución o de lógica? ¿Qué dato está duplicado y qué variable permitiría corregir la causa?

# 14. Errores frecuentes y depuración de nuestros primeros programas

Ya conocemos varias instrucciones Java.

También podemos comenzar a cometer errores diferentes.

Lo importante no es evitar equivocarnos por completo.

Lo importante es aprender a reconocer qué está sucediendo y cómo corregirlo.

## 14.1. Olvidar un punto y coma

Por ejemplo:

```java
int cantidad = 3
```

La instrucción está incompleta.

La versión correcta es:

```java
int cantidad = 3;
```

## 14.2. Utilizar una variable sin declararla

Considera:

```java
total = precio * cantidad;
```

Si no declaramos previamente las variables correspondientes, Java no podrá resolver esos nombres.

Debemos comprobar qué variables existen y dónde fueron declaradas.

## 14.3. Utilizar una variable local sin inicializar

```java
int precio;

System.out.println(precio);
```

El compilador detectará que estamos utilizando una variable local que no tiene un valor asignado.

Podemos corregirlo:

```java
int precio = 150;

System.out.println(precio);
```

## 14.4. Declarar dos veces una variable local

Considera:

```java
int precio = 150;

int precio = 200;
```

El programa no compila si ambas declaraciones pertenecen al mismo bloque local.

No debemos volver a escribir el tipo para cambiar el valor de una variable existente.

La forma correcta es:

```java
int precio = 150;

precio = 200;
```

## 14.5. Confundir mayúsculas y minúsculas

Java diferencia las mayúsculas de las minúsculas.

Por ejemplo:

```java
int precio = 150;
```

No declara una variable llamada `Precio`.

Por tanto:

```java
System.out.println(Precio);
```

No encuentra la variable `precio` por tener una mayúscula distinta.

Debemos escribir los nombres de manera consistente.

## 14.6. Utilizar un tipo incompatible

Considera:

```java
int edad = "16";
```

La cadena `"16"` no puede asignarse directamente como si fuera un valor `int`.

Debemos distinguir entre números y texto.

La forma correcta, si queremos almacenar un entero, es:

```java
int edad = 16;
```

## 14.7. Olvidar importar Scanner

Si queremos utilizar:

```java
Scanner teclado = new Scanner(System.in);
```

Debemos tener disponible la clase `Scanner`.

En nuestros programas escribiremos:

```java
import java.util.Scanner;
```

Al comienzo del archivo.

## 14.8. Leer un tipo de dato incorrecto

Si escribimos:

```java
int cantidad = teclado.nextInt();
```

El programa espera recibir un entero.

Si introducimos texto que no representa un entero válido, la lectura puede fallar.

No debemos confundir este error con una operación matemática incorrecta.

El problema está en el dato recibido.

## 14.9. Realizar una división entera sin advertirlo

Considera:

```java
int suma = 17;
int cantidad = 2;

double promedio = suma / cantidad;
```

El resultado será 8.0.

¿Por qué?

Porque la división se realiza entre dos enteros.

Primero se obtiene 8.

Después se convierte a `double` al asignarlo.

Si queremos un resultado decimal:

```java
double promedio = suma * 1.0 / cantidad;
```

Ahora el resultado será 8.5.

## 14.10. Creer que las variables se actualizan automáticamente

Recordemos:

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;

precio = 200;
```

`total` sigue valiendo 450.

Si queremos actualizarlo, debemos ejecutar otra asignación:

```java
total = precio * cantidad;
```

Este error es especialmente importante porque puede producir programas que compilan y se ejecutan, pero calculan resultados desactualizados.

## 14.11. Confundir concatenación y suma

```java
System.out.println("Total: " + 5 + 3);
```

Muestra:

```text
Total: 53
```

Si queremos sumar:

```java
System.out.println("Total: " + (5 + 3));
```

Muestra:

```text
Total: 8
```

## 14.12. Un ejemplo: error de sintaxis o error lógico

Considera este programa:

```java
public class Main {

    public static void main(String[] args) {

        int precio = 150
        int cantidad = 3;

        int total = precio * cantidad;

        System.out.println("Total: " + total);

    }
}
```

El problema es que falta un punto y coma.

El programa no compila correctamente.

Pero si corregimos esa instrucción, el cálculo será adecuado.

En cambio, considera:

```java
int total = precio + cantidad;
```

Esta instrucción tiene una sintaxis válida.

Sin embargo, si queremos calcular el importe de una compra multiplicando precio por cantidad, el algoritmo será incorrecto.

Por tanto, debemos distinguir:

**Error de sintaxis:** incumplimos una regla de escritura de Java.

**Error lógico:** las instrucciones pueden ejecutarse, pero no producen el resultado que necesitamos.

## 14.13. ¿Cómo investigamos un error?

Podemos seguir un procedimiento:

1. Leer el mensaje que muestra el editor o el compilador.
2. Identificar la instrucción relacionada.
3. Comprobar si existe un problema de sintaxis.
4. Revisar los tipos y nombres de las variables.
5. Si el programa se ejecuta, realizar un trazado de sus valores.
6. Comparar la salida con el resultado esperado.
7. Corregir la causa y ejecutar otra prueba.

No necesitamos cambiar muchas instrucciones simultáneamente.

Es preferible identificar un problema concreto, corregirlo y comprobar qué ocurrió.

**La depuración es una actividad de razonamiento, no una sucesión de cambios al azar.**

---

# 15. Preparación para la evaluación: leer, explicar y construir programas

Al finalizar esta unidad debemos poder escribir programas sencillos, pero también leer y explicar código.

No queremos limitarnos a copiar una estructura Java o ejecutar instrucciones sin comprenderlas.

Organizaremos la preparación en tres niveles.

---

## Nivel 1. Reconocer y comprender

### 15.1. Conceptos fundamentales

Debes poder explicar:

- Qué diferencia existe entre un algoritmo y un programa.
- Qué es la sintaxis de Java.
- Qué función cumple la clase `Main`.
- Desde dónde comienza la ejecución.
- Qué significa `System.out.println`.
- Qué diferencia existe entre `print` y `println`.
- Qué es una variable.
- Qué significa declarar una variable.
- Qué significa inicializarla.
- Qué significa reasignarle un valor.
- Qué es un tipo de dato.
- Cuándo utilizar `int` y cuándo `double`.
- Qué diferencia existe entre un número y una cadena.
- Para qué utilizamos `Scanner`.
- Qué significa realizar un trazado.
- Por qué ejecutar un programa no demuestra automáticamente que sea correcto.

### 15.2. Actividad A: reconocer partes de un programa

Observa:

```java
public class Main {

    public static void main(String[] args) {

        System.out.println("Hola");

    }
}
```

Responde:

1. ¿Cómo se llama la clase?
2. ¿Cómo se llama el método donde comienza la ejecución?
3. ¿Cuál es la instrucción que muestra información?
4. ¿Qué texto aparece en la consola?
5. ¿Qué símbolos delimitan los bloques?
6. ¿Qué símbolo termina la instrucción `println`?

### 15.3. Actividad B: identificar tipos de datos

Indica qué tipo utilizarías para representar:

1. Una edad en años enteros.
2. Un precio con decimales.
3. El nombre de un estudiante.
4. Un estado de verdadero o falso.
5. Una letra que identifica un grupo.

Explica brevemente por qué.

---

## Nivel 2. Interpretar, predecir y corregir

### 15.4. Actividad C: predecir la salida

```java
public class Main {

    public static void main(String[] args) {

        int numero = 5;

        numero = numero + 3;

        numero = numero * 2;

        System.out.println(numero);

    }
}
```

Antes de ejecutarlo:

1. Realiza un trazado.
2. Predice el valor mostrado.
3. Explica cada asignación.
4. Indica qué sucedería si intercambiáramos las dos últimas operaciones matemáticas.

### 15.5. Actividad D: comprender valores independientes

Observa:

```java
int a = 5;

int b = a;

a = 10;

System.out.println(a);
System.out.println(b);
```

Responde:

- ¿Cuánto vale `a` al finalizar?
- ¿Cuánto vale `b`?
- ¿Por qué `b` no cambia automáticamente cuando modificamos `a`?
- ¿Qué instrucción necesitaríamos para asignar nuevamente a `b` el valor actual de `a`?

### 15.6. Actividad E: comprobar una operación

```java
int precio = 150;
int cantidad = 3;

int total = precio * cantidad;

precio = 200;

System.out.println(total);
```

¿Qué muestra el programa?

Explica por qué.

Después agrega una instrucción que actualice el total utilizando el nuevo precio.

### 15.7. Actividad F: detectar errores

Considera:

```java
int edad = "16";

System.out.println(Edad);
```

Identifica los errores.

Explica qué regla de Java incumple cada instrucción.

Escribe una versión corregida.

### 15.8. Actividad G: división entera

Observa:

```java
int suma = 15;
int cantidad = 2;

double promedio = suma / cantidad;

System.out.println(promedio);
```

Responde:

1. ¿Qué valor muestra?
2. ¿Por qué no muestra 7.5?
3. ¿Qué cambio realizarías para obtener un resultado decimal?
4. ¿Por qué no alcanza con declarar `promedio` como `double`?

### 15.9. Actividad H: concatenación

Predice la salida de cada instrucción.

```java
System.out.println(5 + 3);

System.out.println("5" + "3");

System.out.println("Total: " + 5 + 3);

System.out.println("Total: " + (5 + 3));
```

Explica por qué los resultados no son todos iguales.

### 15.10. Actividad adicional: encontrar un error de compilación

Observa:

```java
public class Main {

    public static void main(String[] args) {

        int precio = 150
        int cantidad = 3;

        int total = precio * cantidad;

        System.out.println("Total: " + total);

    }
}
```

Responde:

1. ¿Dónde está el error?
2. ¿Qué regla de Java no se está cumpliendo?
3. ¿Cuál es la corrección?
4. ¿Qué salida tendrá el programa después de corregirlo?
5. ¿Se trataba de un error de sintaxis o de un error lógico?

---

## Nivel 3. Construir, comprobar y justificar

### 15.11. Actividad I: calcular una compra

Una papelería necesita calcular el importe total de una compra.

El programa debe:

1. Solicitar el precio unitario.
2. Solicitar la cantidad.
3. Calcular el importe total.
4. Mostrar el resultado.

Antes de escribir Java, desarrolla el pseudocódigo.

Después construye el programa completo utilizando `Scanner`.

Comprueba su funcionamiento con al menos tres casos de prueba.

### 15.12. Actividad J: calcular un saldo restante

Una persona quiere saber cuánto dinero le queda después de realizar un gasto.

El programa debe solicitar:

- Saldo inicial.
- Importe del gasto.

Después debe mostrar el saldo restante.

**Pseudocódigo modelo:**

```text
INICIO
    LEER saldo
    LEER gasto

    restante ← saldo - gasto

    MOSTRAR restante
FIN
```

Construye el programa Java.

Utiliza tipos adecuados para representar importes con decimales.

Prueba la solución con:

| Saldo |  Gasto | Restante esperado |
| ----- | -----: | ----------------: |
| 800   |    250 |               550 |
| 1000  |    375 |               625 |
| 500   | 125.50 |            374.50 |
| 250   |      0 |               250 |

Después explica qué sucedería si el gasto fuera mayor que el saldo.

En esta unidad el programa podrá realizar igualmente la resta.

En la siguiente aprenderemos a utilizar condiciones para establecer si debemos permitir o rechazar determinados casos.

### 15.13. Actividad K: calcular un promedio

Un programa debe solicitar tres calificaciones y calcular su promedio.

Antes de escribir Java:

1. Identifica los datos.
2. Escribe el pseudocódigo.
3. Determina el tipo de las calificaciones.
4. Decide qué tipo utilizarás para el promedio.
5. Explica cómo evitarás perder la parte decimal.

Después construye el programa.

Prueba con:

| Nota 1 | Nota 2 | Nota 3 | Promedio esperado |
| ------ | -----: | -----: | ----------------: |
| 6      |      7 |      8 |               7.0 |
| 5      |      6 |      7 |               6.0 |
| 7      |      8 |      9 |               8.0 |
| 4      |      5 |      6 |               5.0 |
| 6      |      6 |      7 |          6.333... |

El último caso permite comprobar que el promedio no siempre es entero.

### 15.14. Actividad L: programa completo con texto y números

Construye un programa que solicite:

- Nombre del estudiante.
- Edad.
- Cantidad de materias cursadas.

Después debe mostrar un mensaje con los tres datos.

Utiliza `Scanner`.

El nombre puede contener espacios.

Por tanto, debes seleccionar el método de lectura adecuado y prestar atención a la combinación de entradas de texto y números.

Antes de escribir código, explica qué variables necesitarás y de qué tipos serán.

### 15.15. Actividad M: interpretar antes de ejecutar

Tenemos este programa:

```java
public class Main {

    public static void main(String[] args) {

        int numero1 = 8;
        int numero2 = 3;

        int resultado = numero1 + numero2;

        numero1 = 10;

        resultado = resultado * 2;

        System.out.println(numero1);
        System.out.println(numero2);
        System.out.println(resultado);

    }
}
```

Realiza un trazado completo.

Después responde:

1. ¿Qué valor tiene `resultado` cuando se calcula por primera vez?
2. ¿Qué sucede cuando cambia `numero1`?
3. ¿Por qué el resultado no se recalcula automáticamente?
4. ¿Qué operación realiza la última asignación?
5. ¿Cuál es la salida completa del programa?
6. ¿Qué cambiaría si agregáramos `resultado = numero1 + numero2;` antes de multiplicar por dos?

No ejecutes el programa hasta completar la predicción.

---

# Lo que debemos recordar

En esta unidad aprendimos a transformar nuestros primeros algoritmos en programas Java.

Comenzamos reconociendo la estructura de una clase `Main` y el método desde el que se ejecutan nuestras instrucciones.

Aprendimos a mostrar información mediante `System.out.print` y `System.out.println`.

Después descubrimos la necesidad de las variables: conservar datos para utilizarlos en distintas operaciones sin repetir los mismos valores dentro del programa.

Estudiamos tipos básicos como `int`, `double`, `boolean` y `char`, y comenzamos a utilizar `String` para representar texto.

Aprendimos a distinguir declaración, inicialización y reasignación.

También estudiamos cómo cambian los valores de las variables durante la ejecución.

Descubrimos algo especialmente importante:

**Una asignación calcula y guarda un valor en ese momento; no crea una relación que se actualiza automáticamente cuando cambian otras variables.**

Incorporamos operadores aritméticos y aprendimos a distinguir entre división entera y división con resultado decimal.

Después utilizamos `Scanner` para recibir datos introducidos durante la ejecución.

Esto permitió transformar nuestros primeros programas de valores fijos en soluciones capaces de trabajar con diferentes entradas.

También aprendimos a leer cadenas de texto y a reconocer algunas dificultades que aparecen cuando combinamos métodos de entrada.

Finalmente, recuperamos las herramientas de la Unidad 1: pseudocódigo, trazados, predicción de salidas, casos de prueba y depuración.

Todos estos conocimientos están relacionados.

Un programa necesita datos.

Los datos se conservan mediante variables.

Las instrucciones utilizan y modifican esos valores.

Y nosotros necesitamos comprender el algoritmo para determinar si los resultados son correctos.

En la siguiente unidad descubriremos una limitación de nuestros programas actuales.

Hasta ahora ejecutamos instrucciones en secuencia, pero necesitamos que algunas operaciones se realicen solamente cuando se cumplen determinadas condiciones.

Por ejemplo, queremos comprobar si una persona tiene saldo suficiente antes de autorizar una compra.

Para resolverlo aprenderemos a utilizar **estructuras condicionales**.

**Programar no consiste en conseguir que Java acepte nuestras instrucciones. Consiste en construir una solución correcta, expresarla mediante Java y comprobar que funciona como esperamos.**
