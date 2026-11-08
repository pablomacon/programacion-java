# Unidad 6. Métodos en Java: organizar y reutilizar soluciones

**Programación I — 2026**  
**1.º Bachillerato Tecnológico en Informática · DGETP / UTU**

## ¿Qué aprenderemos en esta unidad?

En las unidades anteriores aprendimos a construir programas que reciben información, realizan cálculos, toman decisiones y repiten instrucciones.

También sabemos utilizar arreglos para conservar varios datos, recorrerlos, buscar elementos y obtener resultados.

Por ejemplo, podemos calcular el promedio de las calificaciones de un grupo.

Pero imaginemos una nueva situación.

Necesitamos calcular los promedios de cinco grupos diferentes.

Ya sabemos construir el algoritmo que calcula un promedio. Sin embargo, ¿debemos escribirlo cinco veces?

¿Y qué sucedería si descubrimos un error en el cálculo o necesitamos modificarlo? ¿Tendríamos que revisar las cinco copias?

También aparece otra dificultad: a medida que incorporamos tareas, nuestros programas se vuelven más extensos y resulta más difícil reconocer qué responsabilidad tiene cada conjunto de instrucciones.

Para resolver estos problemas aprenderemos a utilizar **métodos**.

Un método reúne instrucciones destinadas a realizar una tarea, tiene un nombre y puede ejecutarse cuando lo necesitamos.

Durante esta unidad aprenderemos a:

- Reconocer cuándo conviene crear un método.
- Diferenciar organización y reutilización.
- Definir e invocar métodos.
- Seguir el recorrido de ejecución entre `main` y otros métodos.
- Enviar información mediante parámetros.
- Distinguir parámetros y argumentos.
- Devolver resultados mediante `return`.
- Diferenciar mostrar un resultado de devolverlo.
- Comprender el alcance de las variables locales.
- Enviar arreglos a los métodos.
- Reconocer cuándo un método puede modificar un arreglo.
- Identificar las responsabilidades de un programa.
- Diseñar métodos pensando qué reciben, qué hacen y qué devuelven.
- Comprobar métodos por separado.
- Organizar un programa completo mediante varias tareas.

Mantendremos nuestro procedimiento habitual:

**Comprender el problema → pseudocódigo → Java → predicción → ejecución → pruebas → explicación.**

El objetivo no es construir programas con muchos métodos.

**Queremos comprender cuándo necesitamos uno, qué responsabilidad debe tener y cómo se comunica con las otras partes del programa.**


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

# 1. Una nueva dificultad: tenemos una solución, pero necesitamos reutilizarla

En la Unidad 5 resolvimos problemas con arreglos.

Por ejemplo, podemos calcular el promedio de estas cinco notas:

```java
int[] notas = {7, 5, 8, 6, 9};
```

Primero sumamos:

```java
int suma = 0;

for (int i = 0; i < notas.length; i++) {
    suma += notas[i];
}
```

Después calculamos:

```java
double promedio = suma * 1.0 / notas.length;
```

El resultado es 7.0.

El algoritmo funciona correctamente.

## 1.1. ¿Qué sucede si tenemos otro grupo?

Ahora necesitamos calcular el promedio de:

```java
int[] otroGrupo = {6, 9, 10};
```

Podríamos repetir el procedimiento:

```java
int sumaOtroGrupo = 0;

for (int i = 0; i < otroGrupo.length; i++) {
    sumaOtroGrupo += otroGrupo[i];
}

double promedioOtroGrupo =
    sumaOtroGrupo * 1.0 / otroGrupo.length;
```

También funciona.

Pero comparemos los dos fragmentos.

¿Estamos resolviendo dos problemas diferentes?

No exactamente.

En ambos casos:

1. Recorremos un arreglo.
2. Sumamos sus elementos.
3. Dividimos la suma entre la cantidad de elementos.
4. Obtenemos un promedio.

Lo único que cambia es el arreglo que procesamos.

**Estamos utilizando el mismo algoritmo con datos diferentes.**

## 1.2. Ahora tenemos cinco grupos

Imaginemos que necesitamos procesar:

```java
int[] grupoA = {7, 5, 8, 6, 9};
int[] grupoB = {6, 9, 10};
int[] grupoC = {4, 7, 8, 9};
int[] grupoD = {6, 6, 7};
int[] grupoE = {10, 9, 8, 7, 6};
```

¿Debemos copiar cinco veces el recorrido y el cálculo?

Podríamos hacerlo, pero tendríamos cinco versiones del mismo procedimiento.

Esto presenta varios inconvenientes:

- Repetimos código que realiza la misma tarea.
- Necesitamos modificar varias partes si cambia el procedimiento.
- Podemos cometer errores al copiarlo.
- El programa se vuelve más extenso.
- Resulta más difícil comprobar que todos los grupos se procesan de la misma manera.

La dificultad no es matemática.

Ya sabemos calcular un promedio.

La dificultad consiste en **reutilizar una solución sin escribir nuevamente todo su algoritmo**.

## 1.3. Dar un nombre a una solución

Imaginemos que pudiéramos reunir el cálculo del promedio en una operación llamada:

`calcularPromedio`

Después podríamos escribir:

```java
double promedioA = calcularPromedio(grupoA);
double promedioB = calcularPromedio(grupoB);
double promedioC = calcularPromedio(grupoC);
```

La misma operación recibiría diferentes arreglos.

Ya no necesitaríamos copiar el algoritmo para cada grupo.

Esa es una de las necesidades que resuelven los métodos.

## 1.4. Una segunda dificultad: organizar responsabilidades

Pensemos en otro programa.

Dentro de `main` tenemos instrucciones que:

- Muestran un menú.
- Solicitan una opción.
- Leen calificaciones.
- Calculan un promedio.
- Buscan una nota.
- Muestran un informe.

Aunque el código funcione, puede resultar difícil identificar cada tarea.

Podemos organizarlo mediante operaciones con nombres claros:

`mostrarMenu`

`leerNotas`

`calcularPromedio`

`buscarNota`

`mostrarInforme`

Aquí aparece otro beneficio de los métodos.

No necesitamos repetir una tarea para que tenga sentido separarla.

A veces queremos simplemente identificar una responsabilidad y facilitar la lectura del programa.

## 1.5. Reutilización y organización

Debemos distinguir dos ideas.

**Reutilización:** construir una tarea una sola vez y utilizarla con diferentes datos o desde diferentes partes del programa.

**Organización:** separar responsabilidades para que el programa sea más fácil de leer, comprender, comprobar y modificar.

Un método puede ofrecer ambas ventajas.

Pero no son exactamente lo mismo.

## 1.6. ¿Debemos crear un método para todo?

No.

Imaginemos este programa:

```java
public class Main {

    public static void main(String[] args) {
        System.out.println("Fin");
    }
}
```

No necesitamos obligatoriamente crear un método `mostrarFin` para una única instrucción.

Podríamos hacerlo, pero eso no mejoraría necesariamente el programa.

En cambio, si encontramos un algoritmo que se repite con distintos datos, o una tarea claramente identificable dentro de un programa más amplio, puede convenir separarla.

**No medimos la calidad de un programa por la cantidad de métodos que contiene.**

Lo importante es que sus responsabilidades estén organizadas de manera comprensible.

---

# 2. Nuestro primer método: definir una tarea e invocarla

Comenzaremos con un ejemplo pequeño para comprender la sintaxis.

Queremos mostrar un saludo.

Hasta ahora escribíamos:

```java
System.out.println("Hola");
```

Ahora construiremos un método llamado `saludar`.

## 2.1. Programa completo

```java
public class Main {

    public static void saludar() {
        System.out.println("Hola");
    }

    public static void main(String[] args) {

        saludar();

        System.out.println("Fin del programa");
    }
}
```

La salida será:

```text
Hola
Fin del programa
```

Observa que tenemos dos métodos:

`saludar`

y:

`main`

## 2.2. ¿Dónde comienza Java?

Cuando ejecutamos este programa, Java comienza en `main`.

No comienza automáticamente por el primer método escrito en el archivo.

Dentro de `main` encuentra:

```java
saludar();
```

Entonces ejecuta las instrucciones del método `saludar`.

Después regresa a `main` y continúa con:

```java
System.out.println("Fin del programa");
```

Por eso la salida comienza con «Hola».

## 2.3. Definir e invocar son acciones diferentes

Considera:

```java
public static void saludar() {
    System.out.println("Hola");
}
```

Esto es la **definición** del método.

Describe qué instrucciones debe ejecutar.

En cambio:

```java
saludar();
```

Es una **invocación**.

Solicita que se ejecuten esas instrucciones.

Si definimos un método, pero nunca lo invocamos, sus instrucciones no se ejecutan por el simple hecho de estar escritas.

## 2.4. Invocar varias veces

```java
public class Main {

    public static void saludar() {
        System.out.println("Hola");
    }

    public static void main(String[] args) {

        saludar();
        saludar();
        saludar();
    }
}
```

Salida:

```text
Hola
Hola
Hola
```

Escribimos una sola vez la definición.

Pero realizamos tres invocaciones.

## 2.5. ¿No podríamos utilizar un ciclo?

Sí.

Podemos escribir:

```java
public class Main {

    public static void saludar() {
        System.out.println("Hola");
    }

    public static void main(String[] args) {

        for (int i = 1; i <= 3; i++) {
            saludar();
        }
    }
}
```

También muestra «Hola» tres veces.

Pero debemos comprender que un ciclo y un método tienen funciones diferentes.

**El ciclo controla cuántas veces se repiten instrucciones.**

**El método identifica una tarea y permite ejecutarla mediante una invocación.**

Ambas herramientas pueden combinarse.

## 2.6. Un método que representa una tarea más completa

El ejemplo `saludar()` es útil para comprender la sintaxis.

Pero todavía no demuestra una gran ventaja organizativa.

Consideremos un menú:

```java
public static void mostrarMenu() {

    System.out.println("1. Consultar notas");
    System.out.println("2. Calcular promedio");
    System.out.println("3. Salir");
}
```

Ahora el método reúne varias instrucciones que forman parte de una misma tarea.

Podemos invocarlo desde `main`:

```java
mostrarMenu();
```

El nombre permite reconocer qué acción se realizará.

Además, si debemos modificar las opciones del menú, sabemos dónde hacerlo.

## 2.7. Programa completo con un menú

```java
public class Main {

    public static void mostrarMenu() {

        System.out.println("1. Consultar notas");
        System.out.println("2. Calcular promedio");
        System.out.println("3. Salir");
    }

    public static void main(String[] args) {

        mostrarMenu();
    }
}
```

El programa muestra el menú una sola vez.

Más adelante podremos incorporarlo en un ciclo para repetirlo.

## 2.8. Comprender la declaración

Observa:

```java
public static void mostrarMenu()
```

Sus elementos son:

**`public`:** es un modificador de acceso. Más adelante estudiaremos sus posibilidades.

**`static`:** permite utilizar este método desde `main`, que también es `static`, sin crear previamente un objeto.

**`void`:** indica que el método no devuelve un valor.

**`mostrarMenu`:** es el nombre que identifica la tarea.

**`()`**: contiene el lugar donde se declaran los parámetros. Aquí está vacío porque el método no necesita recibir datos.

Por ahora utilizaremos métodos `public static` dentro de la clase `Main`.

Esta decisión nos permite concentrarnos en los métodos sin adelantar la programación orientada a objetos.

No significa que todos los métodos Java deban ser `static`.

## 2.9. ¿Dónde escribimos los métodos?

Dentro de la clase, pero fuera de otros métodos.

Correcto:

```java
public class Main {

    public static void mostrarMensaje() {
        System.out.println("Hola");
    }

    public static void main(String[] args) {
        mostrarMensaje();
    }
}
```

No podemos declarar un método ordinario dentro del cuerpo de `main`.

Este es un error frecuente cuando comenzamos.

---

# 3. El recorrido de ejecución entre métodos

Una de las principales dificultades de esta unidad consiste en seguir el flujo del programa.

Hasta ahora, las estructuras condicionales y los ciclos modificaban qué instrucciones se ejecutaban dentro de un mismo método.

Ahora una invocación puede llevar temporalmente la ejecución a otro método.

## 3.1. Un ejemplo para predecir

Observa este programa:

```java
public class Main {

    public static void primero() {
        System.out.println("A");
    }

    public static void segundo() {
        System.out.println("B");
        primero();
    }

    public static void main(String[] args) {

        System.out.println("C");

        segundo();

        System.out.println("D");
    }
}
```

Antes de continuar, intenta predecir la salida.

No ejecutes todavía el programa.

¿Comenzará por A, porque `primero` aparece antes en el archivo?

¿O comenzará por C, porque esa es la primera instrucción de `main`?

## 3.2. Seguir el recorrido real

La ejecución comienza en:

```java
public static void main(String[] args)
```

Primero se ejecuta:

```java
System.out.println("C");
```

Después:

```java
segundo();
```

Java pasa al método `segundo`.

Allí encuentra:

```java
System.out.println("B");
```

Después:

```java
primero();
```

Java pasa al método `primero`.

Muestra A.

Cuando `primero` termina, regresa a `segundo`.

Como no quedan más instrucciones en `segundo`, regresa a `main`.

Finalmente muestra D.

La salida completa será:

```text
C
B
A
D
```

## 3.3. Invocar, ejecutar y regresar

Cuando seguimos un programa con métodos debemos reconocer tres acciones:

**Invocar:** solicitar la ejecución de otro método.

**Ejecutar:** realizar las instrucciones del método invocado.

**Regresar:** continuar desde el lugar correspondiente después de terminar la invocación.

No necesitamos aprender todavía todos los detalles internos de la pila de llamadas.

Pero sí debemos comprender qué método está ejecutándose y a qué punto regresará.

## 3.4. Un método definido no tiene por qué ejecutarse

Considera:

```java
public class Main {

    public static void mensajeA() {
        System.out.println("A");
    }

    public static void mensajeB() {
        System.out.println("B");
    }

    public static void main(String[] args) {
        mensajeB();
    }
}
```

La salida será:

```text
B
```

El método `mensajeA` está definido.

Pero no se invoca.

Por tanto, no muestra nada.

## 3.5. Simulador de ejecución entre métodos

<!-- PM-RECURSO
id="u06-flujo-metodos"
tipo="simulador"
componente="simulador-flujo-metodos"
ubicacion="seccion-3.5"
codigo="Main con primero(), segundo() y main(); segundo() invoca primero()"
salida_esperada="C,B,A,D"
controles="predecir;siguiente;anterior;reiniciar"
descripcion="Representar los tres métodos con código Java real. Marcar la instrucción activa, el método que se ejecuta, la salida acumulada y el lugar de retorno. Mostrar que el orden textual de definición no determina el orden de ejecución. Permitir avanzar manualmente paso a paso, sin reproducción automática."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Usar código completo exacto: public class Main { public static void primero(){System.out.println(&quot;A&quot;);} public static void segundo(){System.out.println(&quot;B&quot;);primero();} public static void main(String[] args){System.out.println(&quot;C&quot;);segundo();System.out.println(&quot;D&quot;);}}; salida C,B,A,D. Mantener registro visible del punto de retorno."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Antes de avanzar cada paso, responde:

1. ¿Qué método está ejecutándose?
2. ¿Qué instrucción corresponde ahora?
3. ¿Se realizará una invocación?
4. ¿A qué lugar regresaremos?
5. ¿Qué aparecerá en la consola?

## 3.6. ¿Cómo comprobamos que comprendimos?

Sin ejecutar, debemos poder responder:

- Dónde comienza el programa.
- Qué método se invoca primero.
- Qué instrucciones ejecuta.
- Si invoca otros métodos.
- Dónde continúa después de terminar.

**La posición de un método dentro del archivo no determina cuándo se ejecutará.**

El recorrido depende de las invocaciones.

---

# 4. Métodos con parámetros: utilizar una solución con datos diferentes

Hasta ahora construimos métodos que realizan siempre la misma tarea con los mismos datos.

Pero nuestro problema inicial necesitaba calcular promedios de grupos diferentes.

Para eso debemos aprender a enviar información a un método.

Comenzaremos con un ejemplo sencillo.

## 4.1. Un método que muestra siempre el mismo saludo

```java
public static void saludar() {
    System.out.println("Hola, Ana");
}
```

Este método siempre muestra el mismo nombre.

Pero queremos saludar a distintas personas.

Una solución poco conveniente sería crear:

`saludarAna`

`saludarLuis`

`saludarSofia`

¿Y si tenemos treinta nombres?

Estaríamos repitiendo la misma tarea.

## 4.2. Introducir un parámetro

Podemos construir:

```java
public static void saludar(String nombre) {
    System.out.println("Hola, " + nombre);
}
```

Ahora el método recibe una cadena de caracteres.

El dato recibido se identifica mediante el parámetro `nombre`.

Podemos invocarlo así:

```java
saludar("Ana");
saludar("Luis");
saludar("Sofía");
```

## 4.3. Programa completo

```java
public class Main {

    public static void saludar(String nombre) {
        System.out.println("Hola, " + nombre);
    }

    public static void main(String[] args) {

        saludar("Ana");
        saludar("Luis");
        saludar("Sofía");
    }
}
```

Salida:

```text
Hola, Ana
Hola, Luis
Hola, Sofía
```

La definición del método es única.

Lo utilizamos con datos diferentes.

## 4.4. Parámetro y argumento

Debemos distinguir dos elementos.

En la definición:

```java
public static void saludar(String nombre)
```

`nombre` es el **parámetro**.

En la invocación:

```java
saludar("Ana");
```

`"Ana"` es el **argumento**.

El parámetro indica qué información espera recibir el método.

El argumento es el dato que enviamos en una invocación concreta.

## 4.5. Los argumentos también pueden ser variables

Considera:

```java
String estudiante = "Lucía";

saludar(estudiante);
```

El argumento no tiene que ser un valor escrito directamente entre comillas.

Podemos enviar el contenido actual de una variable.

## 4.6. El mismo método con una variable que cambia

Observa:

```java
public class Main {

    public static void mostrarDoble(int numero) {
        System.out.println(numero * 2);
    }

    public static void main(String[] args) {

        int edad = 16;

        mostrarDoble(edad);

        edad = 20;

        mostrarDoble(edad);
    }
}
```

Antes de ejecutar, predice la salida.

En la primera invocación:

`edad = 16`

Por tanto, el parámetro `numero` recibe 16.

El método muestra:

`16 × 2 = 32`

Después `edad` cambia a 20.

En la segunda invocación, `numero` recibe 20.

El método muestra:

`20 × 2 = 40`

La salida es:

```text
32
40
```

## 4.7. Trazado de argumentos

| Invocación | Valor de `edad` | Valor recibido por `numero` | Salida |
| ---------- | --------------: | --------------------------: | -----: |
| Primera    |              16 |                          16 |     32 |
| Segunda    |              20 |                          20 |     40 |

El método utiliza el valor recibido en cada invocación.

No conserva una conexión automática con la variable `edad`.

Más adelante profundizaremos esta idea al estudiar el alcance de las variables.

## 4.8. Dos parámetros

Supongamos que queremos calcular el total de una compra:

`precio × cantidad`

Podemos escribir:

```java
public static void mostrarTotal(int precio, int cantidad) {

    int total = precio * cantidad;

    System.out.println(total);
}
```

Invocación:

```java
mostrarTotal(150, 3);
```

Salida:

```text
450
```

## 4.9. El orden importa

Considera:

```java
public static void mostrarResta(int primero, int segundo) {
    System.out.println(primero - segundo);
}
```

Si invocamos:

```java
mostrarResta(10, 4);
```

La salida es 6.

Pero:

```java
mostrarResta(4, 10);
```

produce -6.

Los argumentos se asocian con los parámetros según su orden.

## 4.10. Cantidad y tipos de argumentos

Si definimos:

```java
public static void mostrarTotal(int precio, int cantidad)
```

El método necesita dos argumentos compatibles.

Esta invocación es incorrecta:

```java
mostrarTotal(150);
```

Falta un argumento.

Los parámetros establecen qué información necesita el método.

## 4.11. Diseñar antes de escribir

Antes de construir un método, conviene responder:

**¿Qué tarea realiza?**

**¿Qué información necesita recibir?**

Por ejemplo:

| Pregunta        | Respuesta                      |
| --------------- | ------------------------------ |
| ¿Qué hace?      | Muestra el total de una compra |
| ¿Qué recibe?    | Precio y cantidad              |
| ¿Qué calcula?   | Precio por cantidad            |
| ¿Cómo se llama? | `mostrarTotal`                 |

Este razonamiento debe realizarse antes de escribir la declaración Java.

---

# 5. Métodos que devuelven resultados: return

Hasta ahora nuestros métodos muestran información.

Pero imaginemos que queremos utilizar un resultado para realizar otro cálculo.

Esta necesidad nos llevará a `return`.

## 5.1. Un método que muestra el doble

Considera:

```java
public static void mostrarDoble(int numero) {
    System.out.println(numero * 2);
}
```

Si invocamos:

```java
mostrarDoble(5);
```

El método muestra 10.

Funciona correctamente.

Pero ahora queremos calcular:

> El doble de cinco más tres.

Necesitamos obtener 13.

## 5.2. Un intento que no funciona

Imaginemos que escribimos:

```java
int resultado = mostrarDoble(5) + 3;
```

El programa no compila.

¿Por qué?

Porque `mostrarDoble` está declarado como `void`.

Ese método muestra información, pero no produce un valor que pueda utilizarse en una expresión aritmética.

**Mostrar un resultado no significa devolverlo.**

Esta diferencia obliga a pensar qué necesitamos que haga el método.

## 5.3. Construir un método que devuelve

Podemos escribir:

```java
public static int calcularDoble(int numero) {
    return numero * 2;
}
```

Ahora el método devuelve un entero.

Si invocamos:

```java
int resultado = calcularDoble(5) + 3;
```

El resultado será 13.

## 5.4. Programa completo

```java
public class Main {

    public static int calcularDoble(int numero) {
        return numero * 2;
    }

    public static void main(String[] args) {

        int resultado = calcularDoble(5) + 3;

        System.out.println(resultado);
    }
}
```

Salida:

```text
13
```

## 5.5. Seguir el cálculo

Primero Java evalúa:

```java
calcularDoble(5)
```

El parámetro `numero` recibe 5.

Después calcula:

`5 × 2 = 10`

La instrucción:

```java
return numero * 2;
```

devuelve 10.

En `main`, la expresión equivale a:

`10 + 3`

Por tanto:

`resultado = 13`

Finalmente se muestra 13.

## 5.6. ¿Qué hace return?

La instrucción `return` permite devolver un valor al lugar desde el cual se invocó el método.

También termina esa ejecución del método.

Por ejemplo:

```java
public static int sumar(int a, int b) {
    return a + b;
}
```

Si invocamos:

```java
int total = sumar(3, 5);
```

El método devuelve 8.

Ese valor se asigna a `total`.

## 5.7. El tipo de retorno

Observa:

```java
public static int sumar(int a, int b)
```

El tipo `int` indica que el método devuelve un entero.

También podemos tener:

```java
public static double calcularArea(double base, double altura)
```

O:

```java
public static boolean esAprobatoria(int nota)
```

O:

```java
public static String obtenerMensaje()
```

El tipo declarado debe ser compatible con el valor devuelto.

En cambio, `void` indica que el método no devuelve un valor mediante `return`.

## 5.8. Un método que calcula un área

```java
public static double calcularArea(double base, double altura) {
    return base * altura;
}
```

Invocación:

```java
double area = calcularArea(5.0, 3.0);
```

Resultado:

`15.0`

## 5.9. Un método que devuelve boolean

En la Unidad 3 utilizamos condiciones que producen verdadero o falso.

Podemos aprovecharlas dentro de métodos.

Por ejemplo:

```java
public static boolean esAprobatoria(int nota) {
    return nota >= 6;
}
```

Si invocamos:

```java
boolean resultado = esAprobatoria(8);
```

`resultado` vale `true`.

Si invocamos:

```java
boolean resultado = esAprobatoria(5);
```

El resultado es `false`.

## 5.10. Utilizar el resultado dentro de un if

Podemos escribir:

```java
if (esAprobatoria(8)) {
    System.out.println("Aprobado");
}
```

La invocación devuelve un booleano.

Ese resultado se utiliza como condición del `if`.

No necesitamos guardar previamente el valor en otra variable si no resulta necesario.

## 5.11. ¿Siempre necesitamos if para devolver boolean?

No.

Podríamos escribir:

```java
public static boolean esAprobatoria(int nota) {

    if (nota >= 6) {
        return true;
    } else {
        return false;
    }
}
```

Funciona.

Pero la comparación ya produce un valor booleano.

Por eso es suficiente:

```java
public static boolean esAprobatoria(int nota) {
    return nota >= 6;
}
```

Esta versión resulta más clara para una condición sencilla.

## 5.12. ¿Return siempre debe estar en la última línea?

No necesariamente.

Puede aparecer dentro de una estructura condicional.

Pero un método que declara un tipo de retorno debe proporcionar un resultado compatible en todos los recorridos que puedan terminar normalmente.

Por ejemplo:

```java
public static int obtenerMayor(int a, int b) {

    int mayor;

    if (a >= b) {
        mayor = a;
    } else {
        mayor = b;
    }

    return mayor;
}
```

Este ejemplo utiliza un único `return` al final.

Para nuestros primeros programas preferiremos esta organización cuando resulte clara.

Más adelante podremos estudiar otras formas válidas.

## 5.13. Elegir entre void y return

Antes de escribir un método, debemos preguntarnos:

**¿La tarea consiste en realizar una acción, como mostrar un menú?**

Un método `void` puede ser adecuado.

**¿Necesitamos obtener un valor para utilizarlo en otra operación?**

Conviene construir un método con retorno.

Por ejemplo:

| Tarea                          | Diseño adecuado |
| ------------------------------ | --------------- |
| Mostrar un título              | `void`          |
| Mostrar un menú                | `void`          |
| Calcular un área               | `double`        |
| Sumar dos enteros              | `int`           |
| Determinar si una nota aprueba | `boolean`       |
| Obtener un mensaje             | `String`        |

No existe una única decisión válida para todas las tareas.

Debemos analizar qué necesita el resto del programa.

## 5.14. Simulador de parámetros y retorno

<!-- PM-RECURSO
id="u06-parametros-retorno"
tipo="simulador"
componente="simulador-parametros-retorno"
ubicacion="seccion-5.14"
codigo="public class Main { public static int calcularDoble(int numero) { return numero * 2; } public static void main(String[] args) { int resultado = calcularDoble(5) + 3; System.out.println(resultado); } }"
resultado_inicial="13"
controles="modificar-argumento;predecir;siguiente;anterior;reiniciar"
descripcion="Mostrar el argumento enviado, el parámetro que recibe el valor, la operación, la devolución mediante return, la continuación de la expresión en main y el resultado final. Contrastar opcionalmente con un método void que solo utiliza println. Permitir predicción antes de cada paso y mantener código Java compilable."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Probar argumento 5 y doble + 3 = 13; contrastar intento inválido de usar void en expresión; mostrar diferencia entre salida de consola y valor devuelto."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Antes de comprobar cada paso, responde:

- ¿Qué argumento recibe el método?
- ¿Qué valor tiene el parámetro?
- ¿Qué cálculo realiza?
- ¿Qué devuelve?
- ¿Cómo utiliza ese resultado `main`?

---

# 6. El alcance de las variables: ¿dónde existe cada dato?

Ahora tenemos varios métodos.

Debemos comprender qué ocurre con las variables declaradas dentro de cada uno.

Para introducir este concepto, comenzaremos por un error.

## 6.1. Un programa que no compila

Observa:

```java
public class Main {

    public static void calcular() {
        int resultado = 10;
    }

    public static void main(String[] args) {

        calcular();

        System.out.println(resultado);
    }
}
```

El estudiante podría pensar:

> Ya ejecuté `calcular`, por tanto debería poder mostrar `resultado`.

Pero el programa no compila.

¿Por qué?

Porque `resultado` fue declarado dentro de `calcular`.

No existe una variable con ese nombre disponible en el ámbito de `main`.

## 6.2. Variables locales

Una variable declarada dentro de un método es local al ámbito correspondiente.

Por ejemplo:

```java
public static void calcular() {
    int resultado = 10;
}
```

La variable `resultado` pertenece al método `calcular`.

No puede utilizarse directamente desde cualquier otro método.

## 6.3. Resolver el problema mediante return

Si queremos utilizar el resultado desde `main`, podemos devolverlo.

```java
public class Main {

    public static int calcular() {

        int resultado = 10;

        return resultado;
    }

    public static void main(String[] args) {

        int numero = calcular();

        System.out.println(numero);
    }
}
```

Ahora la salida es:

```text
10
```

El método devuelve 10.

Después `main` guarda ese valor en su propia variable `numero`.

**No estamos accediendo directamente a la variable local `resultado`. Estamos recibiendo el valor que el método devuelve.**

## 6.4. Dos variables con el mismo nombre

Observa:

```java
public class Main {

    public static void mostrarNumero() {

        int numero = 10;

        System.out.println(numero);
    }

    public static void main(String[] args) {

        int numero = 5;

        mostrarNumero();

        System.out.println(numero);
    }
}
```

¿Qué salida esperamos?

Dentro de `mostrarNumero`, la variable local `numero` vale 10.

Dentro de `main`, otra variable llamada `numero` vale 5.

Salida:

```text
10
5
```

Son variables distintas.

Tienen el mismo nombre, pero pertenecen a ámbitos diferentes.

## 6.5. Los parámetros también son locales

Considera:

```java
public static void mostrarDoble(int numero) {
    System.out.println(numero * 2);
}
```

El parámetro `numero` se utiliza dentro del método.

Cuando lo invocamos, recibe el valor enviado.

No significa que automáticamente exista una variable `numero` en `main`.

## 6.6. Modificar un parámetro int

Ahora estudiaremos un comportamiento importante.

```java
public class Main {

    public static void aumentar(int numero) {

        numero = numero + 1;

        System.out.println(numero);
    }

    public static void main(String[] args) {

        int valor = 5;

        aumentar(valor);

        System.out.println(valor);
    }
}
```

Antes de ejecutarlo, predice la salida.

Dentro de `aumentar`, el parámetro recibe 5.

Después cambia a 6.

El método muestra 6.

Pero la variable `valor` de `main` sigue valiendo 5.

Por tanto:

```text
6
5
```

## 6.7. ¿Por qué no cambió valor?

Java transmite los argumentos por valor.

Para un argumento de tipo `int`, el parámetro recibe una copia del valor entero.

Cuando modificamos ese parámetro, no modificamos automáticamente la variable original.

Podemos representarlo así:

| Momento                | `valor` en main |    `numero` en aumentar |
| ---------------------- | --------------: | ----------------------: |
| Antes de invocar       |               5 |                       — |
| Al invocar             |               5 |                       5 |
| Después de incrementar |               5 |                       6 |
| Al regresar            |               5 | Ya no está en ejecución |

## 6.8. ¿Cómo hacemos que main conserve el nuevo valor?

Podemos devolverlo y asignarlo.

```java
public class Main {

    public static int aumentar(int numero) {
        return numero + 1;
    }

    public static void main(String[] args) {

        int valor = 5;

        valor = aumentar(valor);

        System.out.println(valor);
    }
}
```

Ahora muestra:

```text
6
```

Porque:

```java
valor = aumentar(valor);
```

recibe el resultado y realiza una nueva asignación.

## 6.9. Alcance dentro de bloques

El alcance también depende de las llaves.

Por ejemplo:

```java
if (edad >= 18) {
    int descuento = 10;
}
```

La variable local `descuento` declarada dentro del bloque no está disponible directamente fuera de él.

Ya utilizamos bloques al estudiar condiciones y ciclos.

Ahora comprendemos que también delimitan dónde pueden utilizarse determinadas variables.

## 6.10. Qué necesitamos comprender

Por ahora es suficiente recordar:

- Las variables locales pertenecen a sus ámbitos.
- Los parámetros son variables locales del método.
- Un método no puede acceder directamente a cualquier variable local de `main`.
- Podemos enviar información mediante argumentos.
- Podemos recuperar resultados mediante `return`.
- Modificar un parámetro `int` no cambia automáticamente la variable enviada.

Estos conceptos preparan el trabajo con objetos.

---

# 7. Arreglos como argumentos: consultar y modificar datos

En la Unidad 5 aprendimos que un arreglo permite conservar varios valores.

Ahora podemos enviarlo a un método.

Pero antes necesitamos recuperar una diferencia entre variables primitivas y referencias.

## 7.1. Copiar un entero

Considera:

```java
int a = 5;
int b = a;

b = 100;

System.out.println(a);
```

La salida será:

```text
5
```

La asignación:

```java
int b = a;
```

copia el valor entero que contiene `a`.

Después modificar `b` no cambia automáticamente `a`.

## 7.2. Dos referencias al mismo arreglo

Ahora considera:

```java
int[] a = {3, 5, 8};

int[] b = a;

b[0] = 100;

System.out.println(a[0]);
```

La salida será:

```text
100
```

¿Por qué?

Porque `a` y `b` hacen referencia al mismo arreglo.

No creamos otro arreglo mediante:

```java
int[] b = a;
```

Simplemente guardamos en `b` la referencia al arreglo existente.

## 7.3. El mismo comportamiento al utilizar métodos

Podemos construir:

```java
public class Main {

    public static void cambiarPrimero(int[] numeros) {
        numeros[0] = 100;
    }

    public static void main(String[] args) {

        int[] datos = {3, 5, 8};

        cambiarPrimero(datos);

        System.out.println(datos[0]);
    }
}
```

La salida será:

```text
100
```

El parámetro `numeros` recibe una copia de la referencia almacenada en `datos`.

Ambas referencias permiten acceder al mismo arreglo.

Por eso modificar un elemento mediante `numeros[0]` modifica ese arreglo.

## 7.4. Java sigue utilizando paso por valor

Debemos evitar una conclusión incorrecta.

No significa que Java pase enteros por valor y arreglos mediante un mecanismo diferente llamado paso por referencia.

**Java pasa todos los argumentos por valor.** La variable parámetro recibe una copia del **valor de referencia**, no una «referencia a la variable del llamador». Por eso cambiar `numeros[0]` afecta el objeto compartido, mientras que reasignar `numeros = new int[3]` dentro del método no cambia automáticamente a qué arreglo apunta la variable original de `main`. Este segundo contraste permite verificar que seguimos hablando de paso por valor.

La diferencia es qué valor se copia.

Con `int`, copiamos el número entero.

Con un arreglo, copiamos una referencia al arreglo.

Por eso podemos modificar sus elementos a través de esa referencia.

## 7.5. Métodos que solamente consultan arreglos

No todos los métodos que reciben arreglos deben modificarlos.

Por ejemplo:

```java
public static void mostrarNotas(int[] notas) {

    for (int i = 0; i < notas.length; i++) {
        System.out.println(notas[i]);
    }
}
```

Este método recorre y muestra los elementos.

No realiza ninguna asignación sobre las posiciones del arreglo.

## 7.6. Programa completo para mostrar un arreglo

```java
public class Main {

    public static void mostrarNotas(int[] notas) {

        for (int i = 0; i < notas.length; i++) {
            System.out.println(notas[i]);
        }
    }

    public static void main(String[] args) {

        int[] calificaciones = {7, 5, 8, 6, 9};

        mostrarNotas(calificaciones);
    }
}
```

Salida:

```text
7
5
8
6
9
```

## 7.7. Un método que devuelve la suma

```java
public static int sumarNotas(int[] notas) {

    int suma = 0;

    for (int i = 0; i < notas.length; i++) {
        suma += notas[i];
    }

    return suma;
}
```

El método recibe el arreglo.

Recorre sus elementos.

Conserva la suma en una variable local.

Finalmente devuelve el resultado.

No necesita modificar el arreglo.

## 7.8. Reutilizar con diferentes arreglos

Podemos tener:

```java
int[] grupoA = {7, 5, 8};
int[] grupoB = {9, 6, 10, 4};
```

Y utilizar:

```java
int sumaA = sumarNotas(grupoA);
int sumaB = sumarNotas(grupoB);
```

Los resultados serán:

`sumaA = 20`

`sumaB = 29`

No necesitamos escribir dos versiones de `sumarNotas`.

## 7.9. Diseñar la responsabilidad

Antes de crear un método que recibe un arreglo, debemos preguntar:

**¿Debe solamente consultar los valores?**

O:

**¿Debe modificar alguna posición?**

Por ejemplo:

`sumarNotas` debería calcular un resultado sin modificar el arreglo.

En cambio:

`cambiarPrimeraNota` puede tener como responsabilidad modificar un elemento.

Es importante que el nombre y la descripción de la tarea permitan reconocer su comportamiento.

## 7.10. Simulador de alcance y referencias

<!-- PM-RECURSO
id="u06-alcance-referencias"
tipo="simulador"
componente="simulador-alcance-referencias"
ubicacion="seccion-7.10"
escenario_1="int valor=5; cambiar(int numero){numero=100;} salida:valor=5"
escenario_2="int[] datos={3,5,8}; cambiar(int[] numeros){numeros[0]=100;} salida:datos[0]=100"
controles="elegir-escenario;predecir;siguiente;anterior;reiniciar"
descripcion="Comparar visualmente dos ejecuciones. En el caso int, mostrar dos variables con valores independientes. En el caso int[], mostrar dos referencias al mismo arreglo. Representar el paso por valor en ambos casos. Permitir predecir los cambios antes de revelarlos. Usar código Java completo, accesible y sin animación automática."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Caso int: cambiar parámetro a 100 y original 5 permanece; caso int[]: modificar elemento y original observa 100; caso adicional reasignar parámetro a otro arreglo y variable original conserva su referencia."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Este recurso permitirá comparar los dos comportamientos.

Antes de avanzar, debemos predecir:

- Qué valor recibe el parámetro.
- Qué instrucción modifica ese valor.
- Qué sucede con la variable original.
- Si hay un arreglo compartido.
- Qué valor se observará al regresar a `main`.

## 7.11. Qué no necesitamos estudiar todavía

No es necesario aprender ahora todos los detalles de memoria y gestión de objetos en Java.

Tampoco necesitamos introducir constructores ni clases propias para comprender estos ejemplos.

El objetivo es reconocer los comportamientos que afectan a nuestros programas.

En la Unidad 7 profundizaremos en los objetos y las referencias.

---

# 8. Diseñar métodos: identificar responsabilidades

Ahora que sabemos definir métodos, enviar argumentos y devolver resultados, necesitamos responder una pregunta fundamental.

**¿Cómo decidimos qué métodos debe tener un programa?**

No basta con dividir el código cada cierta cantidad de líneas.

Debemos identificar tareas que tengan un propósito claro.

## 8.1. Comenzar por el problema

Imaginemos que necesitamos construir un programa para registrar calificaciones.

Debe:

1. Mostrar un título.
2. Mostrar las notas.
3. Calcular su suma.
4. Calcular el promedio.
5. Contar aprobados.
6. Mostrar un informe.

Estas son las responsabilidades que identificamos a partir de los requisitos.

Todavía no escribimos ningún método.

Primero comprendemos qué tareas existen.

## 8.2. Tres preguntas para diseñar

Antes de construir un método, responderemos:

**¿Qué recibe?**

¿Qué información necesita para realizar su tarea?

**¿Qué hace?**

¿Qué operación o conjunto de instrucciones debe ejecutar?

**¿Qué devuelve?**

¿Necesitamos recuperar un valor o solamente realizar una acción?

Por ejemplo:

| Pregunta            | Respuesta                    |
| ------------------- | ---------------------------- |
| Nombre              | `sumarNotas`                 |
| Recibe              | Un arreglo de enteros        |
| Hace                | Recorre y suma sus elementos |
| Devuelve            | Un entero                    |
| Modifica el arreglo | No                           |

Con esta información podemos construir la declaración:

```java
public static int sumarNotas(int[] notas)
```

Después escribimos el cuerpo.

## 8.3. Diseñar un método void

Ahora necesitamos mostrar las notas.

| Pregunta            | Respuesta                   |
| ------------------- | --------------------------- |
| Nombre              | `mostrarNotas`              |
| Recibe              | Un arreglo de enteros       |
| Hace                | Muestra todos sus elementos |
| Devuelve            | Ningún valor                |
| Modifica el arreglo | No                          |

Declaración:

```java
public static void mostrarNotas(int[] notas)
```

La decisión de utilizar `void` surge de la responsabilidad del método.

## 8.4. Diseñar un método boolean

Ahora queremos determinar si una calificación es aprobatoria.

| Pregunta | Respuesta                       |
| -------- | ------------------------------- |
| Nombre   | `esAprobatoria`                 |
| Recibe   | Una nota entera                 |
| Hace     | Comprueba si cumple el criterio |
| Devuelve | `true` o `false`                |

Declaración:

```java
public static boolean esAprobatoria(int nota)
```

Implementación:

```java
public static boolean esAprobatoria(int nota) {
    return nota >= 6;
}
```

## 8.5. Pseudocódigo antes de Java

Podemos representar una función así:

```text
FUNCION SUMAR_NOTAS(notas)

    suma ← 0

    PARA cada posición válida del arreglo HACER
        suma ← suma + elemento
    FIN PARA

    DEVOLVER suma

FIN FUNCION
```

Después traducimos ese algoritmo a Java.

El método no reemplaza el razonamiento algorítmico.

Lo organiza.

## 8.6. La responsabilidad de main

`main` continúa siendo el punto de entrada.

Puede encargarse de coordinar las tareas:

```java
public static void main(String[] args) {

    int[] notas = {7, 5, 8, 6, 9};

    mostrarNotas(notas);

    int suma = sumarNotas(notas);

    System.out.println("Suma: " + suma);
}
```

Al leerlo, podemos identificar las acciones principales.

No necesitamos revisar inmediatamente los detalles de cada recorrido.

## 8.7. ¿Un método debe tener una sola instrucción?

No.

Un método puede contener:

- Variables.
- Condiciones.
- Ciclos.
- Asignaciones.
- Invocaciones a otros métodos.

Lo importante es que esas instrucciones colaboren para realizar una responsabilidad principal.

## 8.8. ¿Debemos separar todo?

Tampoco.

Crear métodos innecesarios puede dificultar la lectura.

Por ejemplo, un método que solamente ejecuta un `println` una vez puede no aportar una mejora.

Debemos preguntarnos:

> ¿Separar esta tarea facilita comprenderla, comprobarla, modificarla o reutilizarla?

Si la respuesta es afirmativa, probablemente tenga sentido considerar un método.

## 8.9. Elegir nombres claros

Preferiremos nombres como:

`mostrarMenu`

`sumarNotas`

`calcularPromedio`

`contarAprobados`

`buscarNota`

En lugar de:

`metodo1`

`proceso2`

`hacerAlgo`

Un buen nombre permite anticipar la responsabilidad.

## 8.10. Actividad de diseño sin computadora

Tenemos este fragmento:

```java
int suma = 0;

for (int i = 0; i < notas.length; i++) {
    suma += notas[i];
}
```

Antes de transformarlo en un método, responde:

1. ¿Qué hace?
2. ¿Qué información necesita?
3. ¿Qué resultado produce?
4. ¿Debe modificar el arreglo?
5. ¿Qué nombre le pondrías?
6. ¿Qué tipo de retorno utilizarías?

Después construye la declaración Java.

Esta actividad permite comprobar si comprendemos el diseño, no solamente la sintaxis.

---

# 9. Comprobar métodos mediante casos de prueba

En las unidades anteriores aprendimos a probar nuestros programas.

Ahora podemos comprobar tareas más pequeñas.

Esto nos ayuda a encontrar errores antes de integrar todas las operaciones.

## 9.1. Qué recibe, qué hace y qué devuelve

Considera:

```java
public static int sumar(int a, int b) {
    return a + b;
}
```

Podemos describirlo mediante tres preguntas:

**Recibe:** dos enteros.

**Hace:** calcula su suma.

**Devuelve:** un entero que representa el resultado.

Esta descripción permite construir casos de prueba.

## 9.2. Pruebas para sumar

| Argumentos | Resultado esperado |
| ---------- | -----------------: |
| 3 y 5      |                  8 |
| 0 y 7      |                  7 |
| -2 y 4     |                  2 |
| -3 y -5    |                 -8 |

Podemos comprobarlas desde `main`.

```java
public class Main {

    public static int sumar(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {

        System.out.println(sumar(3, 5));
        System.out.println(sumar(0, 7));
        System.out.println(sumar(-2, 4));
        System.out.println(sumar(-3, -5));
    }
}
```

Salida:

```text
8
7
2
-8
```

## 9.3. Condiciones necesarias para utilizar un método

Considera:

```java
public static double calcularPromedio(int[] notas)
```

Para este ejercicio estableceremos que el método se utiliza con un arreglo que contiene al menos una nota.

Podemos describirlo así:

| Elemento      | Descripción                            |
| ------------- | -------------------------------------- |
| Recibe        | Un arreglo con al menos una nota       |
| Hace          | Suma los valores y calcula el promedio |
| Devuelve      | Un `double`                            |
| No debe hacer | Modificar las notas                    |

Esto representa un acuerdo sencillo sobre el funcionamiento del método.

Podemos llamarlo **contrato de uso**.

No necesitamos estudiar contratos formales de software.

Lo importante es reconocer qué necesita la operación y qué resultado esperamos.

## 9.4. El caso del arreglo vacío

Imaginemos:

```java
int[] notas = new int[0];
```

Su longitud es cero.

Si el método calcula:

```java
return suma * 1.0 / notas.length;
```

en este caso el resultado de la división de punto flotante será `NaN`, porque estamos realizando cero dividido entre cero.

**¿Por qué no aparece una `ArithmeticException`?** Porque la multiplicación por `1.0` convierte la operación en una división de punto flotante (`double`). Java sigue las reglas de los números de punto flotante de IEEE 754: `0.0 / 0.0` produce `NaN` (*Not a Number*), mientras que, por ejemplo, `5.0 / 0.0` produce infinito positivo. En cambio, la división entre enteros `0 / 0` o `5 / 0` lanza `ArithmeticException` cuando se ejecuta. Ninguno de esos resultados convierte en válido el promedio de un arreglo vacío.

**Predicción breve antes de probar:** ¿qué ocurrirá con `int a = 0 / 0;` y con `double b = 0.0 / 0.0;`? En el primer caso no hay un resultado entero válido y la operación de división por cero provoca una excepción; en el segundo, `b` recibe `NaN`. La decisión pedagógica sigue siendo comprobar que hay al menos un dato antes de calcular el promedio.

El promedio de un conjunto sin elementos no está definido.

Debemos distinguir dos cosas:

**Regla del problema:** no calcular un promedio cuando no hay notas.

**Comportamiento de Java:** la operación con valores de punto flotante puede producir `NaN`.

La regla no se cumple automáticamente por haberla escrito como comentario.

Nuestro programa debe respetarla.

Por ahora utilizaremos arreglos no vacíos al calcular promedios.

Como ampliación, podemos diseñar una validación explícita.

## 9.5. Probar métodos boolean

Considera:

```java
public static boolean esAprobatoria(int nota) {
    return nota >= 6;
}
```

Pruebas:

| Nota | Resultado |
| ---: | --------- |
|    5 | `false`   |
|    6 | `true`    |
|    7 | `true`    |

¿Por qué incluimos 6?

Porque es el límite exacto del criterio.

## 9.6. Probar métodos con arreglos

Para:

```java
public static int sumarNotas(int[] notas)
```

Podemos utilizar:

| Arreglo    | Resultado |
| ---------- | --------: |
| `{3,5,8}`  |        16 |
| `{0,0,0}`  |         0 |
| `{-2,4,6}` |         8 |
| `{}`       |         0 |

El método de suma sí puede trabajar con un arreglo vacío y devolver cero, porque el acumulador comienza en cero y el recorrido no ejecuta iteraciones.

## 9.7. Comprobar que no se modifican los datos

Si un método tiene como responsabilidad calcular una suma, no debería alterar las notas.

Podemos realizar una prueba adicional:

1. Preparar un arreglo.
2. Invocar el método.
3. Comprobar el resultado.
4. Volver a mostrar el arreglo.
5. Verificar que sus elementos no cambiaron.

Esta prueba ayuda a comprobar una responsabilidad que no se observa solamente mediante el valor devuelto.

## 9.8. Pruebas individuales y de integración

Debemos distinguir:

**Prueba de un método:** comprueba que una tarea produce el resultado esperado.

**Prueba del programa completo:** comprueba que los métodos colaboran correctamente.

Necesitamos ambas.

Un método puede funcionar bien de manera aislada, pero ser invocado con argumentos incorrectos desde `main`.

También puede ocurrir que un método devuelva un valor correcto, pero el programa no lo utilice de la manera prevista.

---

# 10. Errores frecuentes al trabajar con métodos

Aprender métodos introduce nuevas posibilidades de error.

Algunos impiden compilar.

Otros permiten ejecutar el programa, pero producen resultados incorrectos.

Debemos aprender a distinguirlos.

## 10.1. Definir sin invocar

```java
public static void saludar() {
    System.out.println("Hola");
}
```

Si nunca invocamos `saludar()`, el mensaje no aparece.

Definir no significa ejecutar.

## 10.2. Declarar un método dentro de main

Incorrecto:

```java
public static void main(String[] args) {

    public static void saludar() {
        System.out.println("Hola");
    }
}
```

Java no permite declarar un método ordinario dentro de otro método.

Debemos escribirlo dentro de la clase, pero fuera de `main`.

## 10.3. Olvidar los paréntesis en la invocación

Incorrecto:

```java
saludar;
```

Correcto:

```java
saludar();
```

## 10.4. Enviar una cantidad incorrecta de argumentos

Si tenemos:

```java
public static void mostrarTotal(int precio, int cantidad)
```

Esta invocación no coincide:

```java
mostrarTotal(150);
```

Falta un argumento.

## 10.5. Confundir el orden de los argumentos

Si el método calcula:

```java
public static int restar(int a, int b) {
    return a - b;
}
```

Entonces:

`restar(10, 4)` devuelve 6.

Pero:

`restar(4, 10)` devuelve -6.

## 10.6. Intentar devolver un valor desde void

Incorrecto:

```java
public static void calcularDoble(int numero) {
    return numero * 2;
}
```

El método declara `void`, pero intenta devolver un entero.

Debemos cambiar el tipo de retorno si queremos devolver ese resultado.

## 10.7. Olvidar return

Incorrecto:

```java
public static int sumar(int a, int b) {

    int resultado = a + b;
}
```

El método declara un retorno de tipo `int`, pero no devuelve el resultado.

Correcto:

```java
public static int sumar(int a, int b) {

    int resultado = a + b;

    return resultado;
}
```

## 10.8. Confundir println y return

Considera:

```java
public static void mostrarSuma(int a, int b) {
    System.out.println(a + b);
}
```

El método muestra el resultado.

No podemos escribir:

```java
int total = mostrarSuma(3, 5);
```

porque esa invocación no produce un valor entero.

Si necesitamos utilizarlo en otro cálculo, debemos diseñar un método con retorno.

## 10.9. Utilizar una variable local fuera de su ámbito

Si declaramos:

```java
public static void calcular() {
    int resultado = 10;
}
```

No podemos utilizar directamente `resultado` desde `main`.

Debemos transmitir la información de una manera adecuada.

## 10.10. Pensar que modificar un parámetro int modifica el original

```java
public static void cambiar(int numero) {
    numero = 100;
}
```

Modificar el parámetro no cambia automáticamente la variable original utilizada como argumento.

## 10.11. Modificar un arreglo sin querer

```java
public static void procesar(int[] numeros) {
    numeros[0] = 100;
}
```

Este método cambia un elemento del arreglo recibido.

Si solamente queríamos consultar valores, puede representar un error lógico.

## 10.12. Calcular un promedio sin datos

Un arreglo vacío no contiene elementos para promediar.

Debemos establecer una regla y respetarla antes de realizar la división.

## 10.13. Crear métodos demasiado grandes

Un método que muestra menús, lee datos, calcula, busca y presenta informes puede ser difícil de comprender.

Conviene identificar tareas que tengan responsabilidades propias.

## 10.14. Crear métodos innecesarios

No toda instrucción necesita convertirse en un método.

Debemos preguntarnos si la separación mejora la claridad, la reutilización o las pruebas.

## 10.15. Elegir nombres poco informativos

Nombres como:

`metodo1`

`proceso2`

`hacerAlgo`

no explican bien qué tarea se realiza.

Preferimos:

`calcularPromedio`

`contarAprobados`

`mostrarNotas`

## 10.16. Depurar un método

Cuando algo no funciona, preguntaremos:

1. ¿El método se invoca?
2. ¿Qué argumentos recibe?
3. ¿Qué valores tienen sus parámetros?
4. ¿Qué instrucciones ejecuta?
5. ¿Qué variables locales utiliza?
6. ¿Qué resultado debería producir?
7. ¿Qué devuelve?
8. ¿Modifica datos recibidos?
9. ¿Dónde continúa el programa?
10. ¿Qué hace `main` con el resultado?

Un trazado pequeño suele ayudar más que modificar código sin comprender el problema.

---

## 10.17. Taller de refactorización: conservar el comportamiento, mejorar la organización

**Situación inicial.** `main` contiene un arreglo `{7, 5, 8, 6, 9}`, un recorrido que suma sus elementos y otro que cuenta aprobados. El programa muestra 35 y 4. Funciona, pero queremos poder usar la misma solución con otro grupo sin copiar ambos recorridos.

**Primera decisión, en papel.** Identifica dos tareas independientes y completa para cada una «recibe / hace / devuelve / modifica el arreglo». No escribas `static` todavía. ¿Qué resultados necesita recibir `main`?

**Pista 1.** Una suma y un conteo pueden devolver enteros distintos; ninguno necesita modificar las notas. **Pista 2.** Piensa en `sumarNotas(int[] notas)` y `contarAprobados(int[] notas)`, ambos con retorno `int`.

**Comprobación posterior:** extrae los recorridos a esos dos métodos, invócalos desde `main` y verifica que siguen mostrando 35 y 4. Después cambia el arreglo por `{6, 6, 10}`: los resultados deben ser 22 y 3. Si no coinciden, localiza si el problema está en la invocación, la condición del `if`, la actualización o el valor devuelto.

**Error de comunicación entre métodos:** sustituye temporalmente `return suma;` por `System.out.println(suma);` y elimina el tipo `int` del retorno. ¿Qué pasa si `main` necesita usar el resultado en otra suma? Explica por qué mostrar no devuelve información.

**Elección de diseño:** no extraigas un método `mostrarFin` solo por crear otro método. Justifica la división por responsabilidades y reutilización, no por cantidad de líneas.

# 11. Problema integrador: registro modular de calificaciones

Recuperaremos un programa que ya conocemos.

Tenemos:

```java
int[] notas = {7, 5, 8, 6, 9};
```

Necesitamos mostrar los valores y calcular su suma.

Después podremos incorporar otras operaciones.

La novedad no está en el algoritmo de suma.

La novedad está en **organizarlo mediante métodos**.

## 11.1. Versión A — Integrador esencial

El programa debe:

1. Crear un arreglo de notas.
2. Mostrar sus elementos.
3. Calcular la suma.
4. Mostrar el resultado.

Pero las dos tareas principales deberán resolverse mediante métodos.

`mostrarNotas`

`sumarNotas`

## 11.2. Diseñar antes de programar

| Método         | Recibe             | Hace              | Devuelve      |
| -------------- | ------------------ | ----------------- | ------------- |
| `mostrarNotas` | Arreglo de enteros | Muestra elementos | Nada (`void`) |
| `sumarNotas`   | Arreglo de enteros | Suma elementos    | Entero        |

Estos dos métodos permiten practicar las diferencias fundamentales entre un método que realiza una acción y otro que devuelve un resultado.

## 11.3. Pseudocódigo

```text
INICIO
    notas ← [7, 5, 8, 6, 9]

    MOSTRAR_NOTAS(notas)

    suma ← SUMAR_NOTAS(notas)

    MOSTRAR suma
FIN
```

Procedimiento:

```text
PROCEDIMIENTO MOSTRAR_NOTAS(notas)

    PARA i DESDE 0 HASTA longitud(notas)-1 HACER
        MOSTRAR notas[i]
    FIN PARA

FIN PROCEDIMIENTO
```

Función:

```text
FUNCION SUMAR_NOTAS(notas)

    suma ← 0

    PARA i DESDE 0 HASTA longitud(notas)-1 HACER
        suma ← suma + notas[i]
    FIN PARA

    DEVOLVER suma

FIN FUNCION
```

## 11.4. Programa Java completo — Versión A

```java
public class Main {

    // Muestra los elementos del arreglo.
    public static void mostrarNotas(int[] notas) {

        for (int i = 0; i < notas.length; i++) {
            System.out.println("Nota " + (i + 1) + ": " + notas[i]);
        }
    }

    // Devuelve la suma de las notas.
    public static int sumarNotas(int[] notas) {

        int suma = 0;

        for (int i = 0; i < notas.length; i++) {
            suma += notas[i];
        }

        return suma;
    }

    public static void main(String[] args) {

        int[] notas = {7, 5, 8, 6, 9};

        mostrarNotas(notas);

        int total = sumarNotas(notas);

        System.out.println("Suma: " + total);
    }
}
```

Salida:

```text
Nota 1: 7
Nota 2: 5
Nota 3: 8
Nota 4: 6
Nota 5: 9
Suma: 35
```

## 11.5. ¿Qué aprendimos con la versión esencial?

El método `mostrarNotas` recibe un arreglo y muestra sus valores.

No devuelve un resultado.

El método `sumarNotas` recibe un arreglo, calcula una suma y la devuelve.

`main` coordina las tareas y utiliza el resultado.

Con solamente dos métodos podemos demostrar los aprendizajes centrales de esta unidad.

## 11.6. Versión B — Consolidación

Ahora incorporaremos:

`calcularPromedio`

`contarAprobados`

Estos métodos reutilizarán los conceptos de las unidades anteriores.

### Diseñar calcularPromedio

| Pregunta            | Respuesta           |
| ------------------- | ------------------- |
| Recibe              | Arreglo no vacío    |
| Hace                | Calcula el promedio |
| Devuelve            | `double`            |
| Modifica el arreglo | No                  |

Podemos aprovechar el método `sumarNotas` ya construido:

```java
public static double calcularPromedio(int[] notas) {

    int suma = sumarNotas(notas);

    return suma * 1.0 / notas.length;
}
```

Este método tiene como condición de uso que el arreglo no esté vacío.

### Diseñar contarAprobados

```java
public static int contarAprobados(int[] notas) {

    int aprobados = 0;

    for (int i = 0; i < notas.length; i++) {

        if (notas[i] >= 6) {
            aprobados++;
        }
    }

    return aprobados;
}
```

## 11.7. Programa completo — Versión B

```java
public class Main {

    public static void mostrarNotas(int[] notas) {

        for (int i = 0; i < notas.length; i++) {
            System.out.println("Nota " + (i + 1) + ": " + notas[i]);
        }
    }

    public static int sumarNotas(int[] notas) {

        int suma = 0;

        for (int i = 0; i < notas.length; i++) {
            suma += notas[i];
        }

        return suma;
    }

    // Requiere un arreglo no vacío.
    public static double calcularPromedio(int[] notas) {

        int suma = sumarNotas(notas);

        return suma * 1.0 / notas.length;
    }

    public static int contarAprobados(int[] notas) {

        int aprobados = 0;

        for (int i = 0; i < notas.length; i++) {

            if (notas[i] >= 6) {
                aprobados++;
            }
        }

        return aprobados;
    }

    public static void main(String[] args) {

        int[] notas = {7, 5, 8, 6, 9};

        mostrarNotas(notas);

        int suma = sumarNotas(notas);

        double promedio = calcularPromedio(notas);

        int aprobados = contarAprobados(notas);

        System.out.println("Suma: " + suma);
        System.out.println("Promedio: " + promedio);
        System.out.println("Aprobados: " + aprobados);
    }
}
```

La salida final incluye:

```text
Suma: 35
Promedio: 7.0
Aprobados: 4
```

## 11.8. ¿Por qué calcularPromedio invoca sumarNotas?

Porque ya tenemos un método que realiza esa tarea.

No necesitamos copiar nuevamente el algoritmo de suma.

Esta es una demostración directa de reutilización.

También nos permite organizar responsabilidades:

`sumarNotas` obtiene una suma.

`calcularPromedio` utiliza esa suma para calcular un promedio.

## 11.9. Versión C — Ampliación

Como desafío adicional, podemos incorporar:

- Un menú repetitivo con `do...while`.
- Una opción para mostrar las notas.
- Una opción para calcular el promedio.
- Una opción para contar aprobados.
- Una opción para buscar un valor.
- Una opción para salir.

No debemos incorporar todas estas tareas al mismo tiempo.

Conviene comenzar por el menú y una operación.

Después agregar las demás y comprobar cada modificación.

Esta versión integra los contenidos de las unidades 3, 4, 5 y 6.

## 11.10. Casos de prueba

Podemos comprobar los métodos con:

| Arreglo       | Suma | Promedio | Aprobados |
| ------------- | ---: | -------: | --------: |
| `{7,5,8,6,9}` |   35 |      7.0 |         4 |
| `{6,6,6}`     |   18 |      6.0 |         3 |
| `{1,2,3}`     |    6 |      2.0 |         0 |
| `{10}`        |   10 |     10.0 |         1 |
| `{5,7}`       |   12 |      6.0 |         1 |

Estos arreglos son no vacíos, por lo que permiten utilizar `calcularPromedio` según su condición de uso.

Para `sumarNotas` y `contarAprobados` también podemos probar un arreglo vacío.

## 11.11. Defensa individual

Después de construir el programa, cada estudiante deberá poder explicar:

- Qué tarea realiza cada método.
- Qué datos recibe.
- Qué devuelve.
- Cómo se invoca.
- Por qué `main` puede utilizar los resultados.
- Qué sucedería si cambiamos el arreglo.

La explicación puede acompañarse con un pequeño trazado en papel.

---

# 12. Actividades de aprendizaje

Las actividades están organizadas en cuatro mini-ciclos.

Cada uno puede terminar en una evidencia concreta.

No es necesario resolver las 21 actividades como una única tarea extensa.

## Mini-ciclo 1. Definir e invocar

### Actividad A. Reconocer definición e invocación

Observa:

```java
public static void saludar() {
    System.out.println("Hola");
}
```

Y:

```java
saludar();
```

Responde:

1. ¿Cuál es la definición?
2. ¿Cuál es la invocación?
3. ¿Qué sucede si definimos el método, pero nunca lo invocamos?

### Actividad B. Predecir el recorrido

```java
public class Main {

    public static void mensaje() {
        System.out.println("Dos");
    }

    public static void main(String[] args) {

        System.out.println("Uno");

        mensaje();

        System.out.println("Tres");
    }
}
```

Predice la salida.

Explica cuándo Java entra en `mensaje` y dónde continúa después.

### Actividad C. Construir un método void

Construye un método llamado `mostrarLinea` que muestre:

```text
---------------
```

Después invócalo tres veces.

Compara la cantidad de instrucciones escritas con la cantidad de ejecuciones.

### Actividad D. Parámetro y argumento

Considera:

```java
public static void mostrarCuadrado(int numero) {
    System.out.println(numero * numero);
}
```

Invocación:

```java
mostrarCuadrado(4);
```

Identifica:

- Parámetro.
- Argumento.
- Operación.
- Salida.

### Actividad E. Interpretar return

```java
public static int sumar(int a, int b) {
    return a + b;
}
```

Responde:

1. ¿Qué recibe?
2. ¿Qué hace?
3. ¿Qué devuelve?
4. ¿Qué produce `sumar(3, 5)`?
5. ¿Por qué no es lo mismo que mostrar el resultado?

### Actividad F. Predicción de varias invocaciones

```java
public class Main {

    public static void mostrarDoble(int numero) {
        System.out.println(numero * 2);
    }

    public static void main(String[] args) {

        mostrarDoble(3);
        mostrarDoble(7);
    }
}
```

Predice la salida y explica qué valor recibe el parámetro en cada invocación.

---

## Mini-ciclo 2. Enviar y devolver información

### Actividad G. Corregir argumentos

Tenemos:

```java
public static void mostrarTotal(int precio, int cantidad) {
    System.out.println(precio * cantidad);
}
```

Un estudiante escribe:

```java
mostrarTotal(150);
```

¿Por qué no compila?

Corrige la invocación.

### Actividad H. Mostrar y devolver

Compara:

```java
public static void mostrarSuma(int a, int b) {
    System.out.println(a + b);
}
```

Con:

```java
public static int calcularSuma(int a, int b) {
    return a + b;
}
```

¿Cuál utilizarías para guardar el resultado en una variable?

Justifica.

### Actividad I. Variables locales

```java
public class Main {

    public static void mostrar() {
        int numero = 10;
        System.out.println(numero);
    }

    public static void main(String[] args) {

        int numero = 5;

        mostrar();

        System.out.println(numero);
    }
}
```

Predice la salida y explica por qué.

### Actividad J. Modificar un parámetro

```java
public class Main {

    public static void cambiar(int numero) {
        numero = 100;
    }

    public static void main(String[] args) {

        int valor = 5;

        cambiar(valor);

        System.out.println(valor);
    }
}
```

¿Qué muestra?

Explica qué recibe el parámetro y qué sucede con la variable original.

### Actividad K. Arreglo como argumento

```java
public class Main {

    public static void cambiar(int[] numeros) {
        numeros[0] = 100;
    }

    public static void main(String[] args) {

        int[] datos = {3, 5, 8};

        cambiar(datos);

        System.out.println(datos[0]);
    }
}
```

¿Qué muestra?

Compara el resultado con la actividad J.

### Actividad L. Corregir un método con retorno

```java
public static int calcularDoble(int numero) {

    int doble = numero * 2;
}
```

¿Por qué no compila?

Corrige el método manteniendo su propósito.

---

## Mini-ciclo 3. Métodos que procesan datos

### Actividad M. Completar una suma

```java
public static int sumar(int[] numeros) {

    int suma = 0;

    for (int i = 0; i < __________; i++) {
        suma += __________;
    }

    return __________;
}
```

Completa los espacios.

Prueba con:

```java
int[] datos = {3, 5, 8};
```

### Actividad N. Saludo personalizado

Construye un método `saludar` que reciba un nombre y muestre un saludo.

Invócalo con tres nombres diferentes.

Escribe antes el pseudocódigo.

### Actividad O. Calcular un descuento

Construye:

```java
public static double calcularDescuento(
    double precio,
    double porcentaje
)
```

Debe devolver el importe del descuento.

Por ejemplo:

Precio 1000, porcentaje 10.

Resultado: 100.

Después construye otro método que calcule el precio final.

Explica qué recibe y devuelve cada método.

### Actividad P. Nota aprobatoria

Construye:

```java
public static boolean esAprobatoria(int nota)
```

Debe devolver verdadero cuando la nota sea igual o superior a 6.

Prueba con 5, 6 y 7.

### Actividad Q. Mostrar un arreglo

Construye:

```java
public static void mostrarNumeros(int[] numeros)
```

Debe recorrer el arreglo y mostrar sus elementos.

Prueba con arreglos de diferente longitud.

### Actividad R. Sumar un arreglo

Construye:

```java
public static int sumarNumeros(int[] numeros)
```

Prueba:

| Arreglo    | Resultado |
| ---------- | --------: |
| `{3,5,8}`  |        16 |
| `{0,0,0}`  |         0 |
| `{-2,4,6}` |         8 |
| `{}`       |         0 |

Explica por qué el acumulador comienza en cero.

### Actividad S. Contar coincidencias

Construye un método que reciba:

- Un arreglo de enteros.
- Un número buscado.

Debe devolver cuántas veces aparece.

Ejemplo:

```java
int[] datos = {5, 3, 5, 8, 5};
```

Si buscamos 5, el resultado será 3.

Explica por qué necesitamos un contador.

---

## Mini-ciclo 4. Organizar una solución completa

### Actividad T. Registro modular

Construye el integrador de la sección 11.

Primero implementa:

`mostrarNotas`

`sumarNotas`

Después, si corresponde, incorpora:

`calcularPromedio`

`contarAprobados`

Entrega:

- Pseudocódigo.
- Programa Java.
- Casos de prueba.
- Explicación individual.

### Actividad U. ¿Cuándo conviene crear un método?

Analiza estas situaciones.

**Situación 1:** un programa muestra una sola vez «Fin».

¿Necesitamos crear un método para ello?

**Situación 2:** un programa calcula el promedio de cinco grupos copiando cinco veces el mismo recorrido.

¿Conviene crear un método?

**Situación 3:** un programa contiene un bloque que lee notas, otro que calcula promedios y otro que presenta resultados.

¿Qué responsabilidades podrían separarse?

**Situación 4:** un programa contiene una operación sencilla que solamente se utiliza una vez y ya resulta fácil de comprender.

¿Separarla necesariamente mejora el código?

Para cada situación:

1. Decide si crearías un método.
2. Justifica la decisión.
3. Si corresponde, propone un nombre.
4. Determina qué recibe, qué hace y qué devuelve.

El objetivo no es responder siempre que sí.

**Queremos aprender a tomar decisiones de diseño.**

---

# 13. Preparación para la evaluación

Al finalizar esta unidad debemos poder comprender programas organizados mediante métodos.

También debemos construir soluciones sencillas en las que varias tareas colaboren.

## 13.1. Aprendizajes imprescindibles

Todos debemos poder:

1. Reconocer cuándo resulta conveniente crear un método.
2. Diferenciar definición e invocación.
3. Comprender que la ejecución comienza en `main`.
4. Seguir un recorrido sencillo entre métodos.
5. Construir un método `void`.
6. Utilizar parámetros y argumentos.
7. Devolver resultados mediante `return`.
8. Distinguir mostrar un valor de devolverlo.
9. Comprender el alcance básico de variables locales.
10. Enviar un arreglo a un método.
11. Construir un método que procese un arreglo.
12. Identificar responsabilidades mediante «recibe, hace y devuelve».
13. Probar el método y explicar su funcionamiento.

## 13.2. Aprendizajes de consolidación

Como profundización podemos:

- Invocar un método desde otro método.
- Diseñar métodos que colaboren entre sí.
- Comparar el paso de enteros y referencias a arreglos.
- Reconocer modificaciones no deseadas de arreglos.
- Construir un programa modular con menú.
- Analizar condiciones de uso y casos especiales.
- Decidir qué tareas merece la pena separar.

## 13.3. Criterios de logro

| Criterio                     | Logrado                                | En proceso                   | Inicial                     |
| ---------------------------- | -------------------------------------- | ---------------------------- | --------------------------- |
| Identifica responsabilidades | Reconoce tareas coherentes             | Necesita orientación         | No distingue tareas         |
| Define e invoca              | Construye métodos correctamente        | Presenta errores corregibles | No logra la estructura      |
| Utiliza parámetros           | Envía datos adecuados                  | Confunde algunos argumentos  | No comprende el intercambio |
| Devuelve resultados          | Utiliza tipo y `return` correctamente  | Confunde mostrar y devolver  | No recupera resultados      |
| Sigue la ejecución           | Predice recorrido y salida             | Presenta errores parciales   | No reconoce el flujo        |
| Comprueba la solución        | Realiza pruebas y justifica resultados | Pruebas incompletas          | No verifica                 |

## 13.4. Comprobación individual

Después de una práctica, cada estudiante deberá responder brevemente:

**Pregunta 1.**

¿Cuál es la diferencia entre definir e invocar un método?

**Pregunta 2.**

¿Por qué no podemos escribir:

```java
int resultado = mostrarDoble(5);
```

si `mostrarDoble` está declarado como `void`?

**Pregunta 3.**

¿Qué ocurre con una variable entera de `main` cuando un método recibe su valor y modifica el parámetro?

Estas preguntas pueden responderse en papel.

## 13.5. Defensa breve

En aproximadamente un minuto, cada estudiante deberá explicar:

- Qué tarea resolvió.
- Por qué creó un método.
- Qué información recibe.
- Qué hace con ella.
- Qué devuelve, si corresponde.
- Cómo comprobó que funciona.

También podrá pedirse un cambio pequeño.

Por ejemplo:

> El criterio de aprobación cambia de 6 a 7. ¿Qué método deberías modificar y por qué?

## 13.6. Trabajo en parejas

Durante las actividades de construcción trabajaremos con dos roles:

**Conductor:** escribe el código.

**Navegante:** revisa el algoritmo, anticipa resultados, identifica errores y verifica los requisitos.

Los roles cambiarán cada 10–15 minutos.

Cada pareja entregará una solución.

Cada integrante explicará al menos una parte del programa.

Si se detecta una diferencia importante en la participación, se realizará una comprobación individual de predicción o corrección.

## 13.7. Autoevaluación

Marca una opción para cada afirmación.

**Puedo explicar qué recibe, hace y devuelve un método.**

- Sí.
- Todavía necesito ayuda.

**Puedo predecir qué sucede cuando `main` invoca otro método.**

- Sí.
- Todavía necesito ayuda.

Completa:

> Lo que más me costó comprender de los métodos fue...

## 13.8. Evidencia mínima de aprendizaje

Para considerar logrados los aprendizajes fundamentales, no será necesario construir un programa con numerosos métodos.

Será suficiente con que el estudiante pueda:

- Identificar una tarea que conviene separar.
- Construir un método que recibe información.
- Construir un método que devuelve un resultado.
- Invocarlos correctamente desde `main`.
- Explicar el recorrido.
- Probar los resultados con diferentes datos.

La complejidad adicional no reemplaza la comprensión.

---

# Lo que debemos recordar

En esta unidad aprendimos a organizar y reutilizar soluciones mediante métodos.

Comenzamos con una dificultad concreta.

Ya sabíamos calcular promedios, sumar arreglos y contar elementos, pero si necesitábamos realizar esas operaciones con distintos grupos podíamos terminar copiando varias veces el mismo algoritmo.

Para resolverlo aprendimos a definir métodos.

Comprendimos que un método reúne instrucciones que realizan una tarea y que podemos invocarlo cuando necesitamos ejecutarlas.

Distinguimos entre definición e invocación.

Aprendimos que la ejecución comienza en `main` y que una invocación puede llevar temporalmente el programa a otro método.

Después incorporamos parámetros y argumentos.

Gracias a ellos, un método puede trabajar con información diferente en cada invocación.

Más adelante descubrimos que mostrar un resultado no significa devolverlo.

Para recuperar valores que podemos utilizar en otras operaciones, aprendimos a utilizar `return`.

También estudiamos el alcance de las variables locales.

Comprendimos que las variables declaradas dentro de un método no están disponibles automáticamente desde otros métodos.

Después comparamos el comportamiento de valores enteros y referencias a arreglos.

Aprendimos que Java transmite argumentos por valor y que un método puede modificar los elementos de un arreglo al que tiene acceso mediante una referencia.

También aprendimos a diseñar métodos respondiendo tres preguntas:

**¿Qué recibe?**

**¿Qué hace?**

**¿Qué devuelve?**

Estas preguntas nos permiten pensar la responsabilidad antes de escribir la sintaxis.

Finalmente, reorganizamos el registro de calificaciones de la Unidad 5 mediante métodos.

La solución matemática no cambió.

Lo que cambió fue la manera de organizarla.

**Un método no es solamente un bloque de código con un nombre. Es una herramienta para representar una tarea, comunicar información y reutilizar una solución.**

## Hacia la Unidad 7: clases y objetos

Hasta ahora trabajamos con datos y métodos.

Sabemos crear variables, arreglos y operaciones que procesan información.

Pero imaginemos que queremos construir un programa para administrar productos.

Cada producto tiene:

- Código.
- Nombre.
- Precio.
- Stock.

Además, sobre cada producto podemos realizar operaciones:

- Consultar sus datos.
- Modificar su precio.
- Agregar unidades.
- Retirar unidades, si hay stock suficiente.

¿Debemos mantener todos esos datos en variables separadas?

¿Y si tenemos muchos productos?

¿Podríamos representar cada producto como una entidad que reúne sus características y las operaciones que le corresponden?

Estas preguntas nos conducirán a la **programación orientada a objetos**.

En la Unidad 7 aprenderemos primero a reconocer objetos en un problema real y después a representarlos mediante clases, atributos y métodos.

Así podremos comprender que los métodos no solamente sirven para organizar tareas generales dentro de `Main`.

También pueden representar los comportamientos de los objetos que forman parte de un sistema.
