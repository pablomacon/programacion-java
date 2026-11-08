# Unidad 4. Estructuras iterativas: repetir instrucciones de manera controlada

**Programación I — 2026**  
**1.º Bachillerato Tecnológico en Informática · DGETP / UTU**

## ¿Qué aprenderemos en esta unidad?

En las unidades anteriores aprendimos a analizar problemas, expresar algoritmos mediante pseudocódigo y escribir programas Java. Ya podemos recibir datos con `Scanner`, guardar valores en variables, realizar cálculos y utilizar `if`, `else` y `switch` para tomar decisiones. Pero todavía tenemos una dificultad: cuando necesitamos realizar la misma tarea muchas veces, terminamos copiando instrucciones.

Imaginemos que tenemos que procesar las notas de treinta estudiantes. Sabemos leer una nota y decidir si es aprobatoria. ¿Debemos copiar treinta veces la lectura, la condición y el mensaje? ¿Y si mañana son cincuenta estudiantes? ¿Qué sucede si todavía no sabemos cuántos datos ingresarán?

En esta unidad aprenderemos a construir **estructuras iterativas**: mecanismos que permiten repetir instrucciones de manera controlada. Estudiaremos `while`, `for` y `do...while`, contadores, acumuladores, valores centinela, banderas booleanas, menús repetitivos, trazados, límites y errores de finalización.

La meta no es memorizar tres formas de escribir ciclos. **Queremos poder determinar qué se repite, qué cambia en cada iteración y cómo sabemos que el programa debe terminar.**

Nuestro recorrido será: **comprender el problema → predecir → pseudocódigo → Java → trazado → pruebas → explicación**.


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

# 1. Un problema nuevo: necesitamos repetir instrucciones

## 1.1. Ya sabemos procesar una nota

En la Unidad 3 construimos decisiones como esta:

```java
int nota = 8;

if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("No aprobado");
}
```

La regla de este ejercicio es sencilla: las notas desde 6 se consideran aprobatorias. Con `nota = 8`, el programa muestra `Aprobado`.

Ahora nos solicitan clasificar las notas de cinco estudiantes. Podríamos escribir `nota1`, `nota2`, `nota3`, `nota4` y `nota5`, con cinco condiciones semejantes. La solución sería extensa y, sobre todo, poco flexible. Si cambiáramos el requisito, tendríamos que revisar cada copia.

## 1.2. ¿Qué permanece igual y qué cambia?

En cada estudiante realizamos exactamente estas operaciones:

1. Solicitar una calificación.
2. Comprobar si alcanza el valor 6.
3. Mostrar el mensaje correspondiente.

El procedimiento **permanece igual**. Lo que cambia es el valor de la nota y el número de estudiantes que ya procesamos.

Esta observación permite descubrir una solución: escribir una vez el procedimiento y pedirle al programa que lo ejecute repetidamente.

## 1.3. No alcanza con decir «repetir»

Un algoritmo debe ser preciso. Si escribimos «repetir la lectura», quedan preguntas sin resolver: ¿cuántas veces?, ¿quién cuenta las notas?, ¿cómo avanzamos?, ¿en qué momento terminamos? Si no respondemos estas preguntas, la computadora no puede deducir nuestras intenciones.

Cuando construyamos un ciclo tendremos que establecer **qué instrucciones forman el cuerpo** y **qué condición controla su continuación**. En los ejemplos con contadores también tendremos que definir el valor inicial y la actualización.

## 1.4. Antes de usar Java

Imagina que debes entregar cinco boletos numerados, del 1 al 5. Describe en palabras un procedimiento que no repita cinco veces una instrucción completa. Una posible idea es: «Comenzar por el boleto 1; mientras el número no supere 5, entregar ese boleto y pasar al número siguiente».

Esa descripción ya contiene la estructura de un ciclo, aunque todavía no tiene sintaxis Java.

---

# 2. ¿Qué es una estructura iterativa?

Una **estructura iterativa**, también llamada *ciclo* o *bucle*, permite ejecutar varias veces un bloque de instrucciones. Cada ejecución del cuerpo se denomina **iteración**.

## 2.1. Repetición manual y repetición controlada

Podemos mostrar tres veces un texto escribiendo:

```java
System.out.println("Hola");
System.out.println("Hola");
System.out.println("Hola");
```

En cambio:

```java
int contador = 1;

while (contador <= 3) {
    System.out.println("Hola");
    contador++;
}
```

El segundo fragmento contiene un solo `println`, pero esa misma instrucción se ejecuta tres veces. No escribimos tres copias: controlamos tres ejecuciones.

## 2.2. Cuatro elementos para analizar

En los ciclos sencillos con contador reconocemos:

- **Inicialización:** el estado inicial, por ejemplo `contador = 1`.
- **Condición:** la pregunta que permite continuar, por ejemplo `contador <= 3`.
- **Cuerpo:** las instrucciones que repetimos.
- **Actualización:** lo que cambia para avanzar, por ejemplo `contador++`.

La condición produce un valor booleano. Si es verdadera, el ciclo `while` realiza otra iteración. Si es falsa, continúa después del ciclo.

Aunque estos cuatro elementos resultan muy útiles para estudiar recorridos con contador, no todos los ciclos funcionan mediante un contador. En otros ejemplos, la condición dependerá de un dato recibido del usuario o de una variable booleana.

## 2.3. ¿Qué cambia entre iteraciones?

El programa no vuelve automáticamente al mismo estado inicial cada vez que ejecuta un bloque. Las variables conservan los valores que les dejan las asignaciones, siempre que sean las mismas variables y no se vuelvan a inicializar dentro del ciclo.

Si `contador` comienza en 1 y luego ejecutamos `contador++`, en la siguiente comprobación valdrá 2. Esta relación entre **estado actual → operación → nuevo estado** es esencial para comprender los ciclos.

## 2.4. La condición no es una decoración

En la Unidad 3 aprendimos que las condiciones seleccionan instrucciones. En esta unidad también determinan si un conjunto de instrucciones debe volver a ejecutarse. Por eso, un ciclo depende de los conceptos anteriores: variables, asignaciones y condiciones trabajan juntos.

---

# 3. El ciclo while: repetir mientras se cumpla una condición

La palabra inglesa *while* significa «mientras». En Java escribimos:

```java
while (condicion) {
    // Instrucciones que se repiten
}
```

Primero Java evalúa la condición. Si es verdadera, ejecuta el cuerpo y regresa a comprobarla. Si es falsa, salta el cuerpo y continúa con las instrucciones que siguen.

## 3.1. Mostrar los números del 1 al 3

```java
int numero = 1;

while (numero <= 3) {
    System.out.println(numero);
    numero++;
}
```

**Antes de continuar, predice:** ¿qué números se mostrarán?, ¿qué valor tendrá `numero` al terminar?, ¿cuántas veces se comprobará la condición?

La salida es:

```text
1
2
3
```

La inicialización establece `numero = 1`. La condición pregunta si `numero <= 3`. El cuerpo muestra el valor e incrementa la variable. La actualización prepara la próxima comprobación.

## 3.2. Trazado completo

| Evaluación | `numero` antes | `numero <= 3` | ¿Ejecuta el cuerpo? | `numero` después |
|---:|---:|---|---|---:|
| 1 | 1 | Verdadero | Sí: muestra 1 | 2 |
| 2 | 2 | Verdadero | Sí: muestra 2 | 3 |
| 3 | 3 | Verdadero | Sí: muestra 3 | 4 |
| 4 | 4 | Falso | No | 4 |

El cuerpo se ejecuta **tres veces**. La condición se comprueba **cuatro veces**. La última comprobación es falsa y permite salir.

Una pregunta importante: **¿el ciclo terminó cuando incrementamos `numero` a 4, o cuando Java comprobó que `4 <= 3` era falso?** La actualización dejó preparado el nuevo estado; la decisión de salir ocurrió al evaluar la condición y obtener falso.

## 3.3. Qué significa una iteración

Una iteración es la ejecución del cuerpo. La comprobación final falsa no es otra iteración: no entra al cuerpo. Conviene distinguir tres magnitudes: condiciones verdaderas, condiciones falsas e iteraciones. En este ejemplo tenemos tres condiciones verdaderas, una falsa y tres iteraciones.

## 3.4. Simulador del recorrido

<!-- PM-RECURSO
id="u04-while-trazado"
tipo="simulador"
componente="simulador-while"
ubicacion="seccion-3.4"
codigo="int numero=1; while(numero<=3){System.out.println(numero); numero++;}"
estado_inicial="numero:1;salida:vacia"
secuencia="evaluar-1:true;mostrar-1;incrementar-2;evaluar-2:true;mostrar-2;incrementar-3;evaluar-3:true;mostrar-3;incrementar-4;evaluar-4:false;finalizar"
resultado="salida:1,2,3;iteraciones:3;evaluaciones:4"
controles="anterior;siguiente;reiniciar;predecir"
descripcion="Simular cada comprobación, instrucción de salida y actualización sin avance automático. Mostrar estado, condición, resultado booleano, salida acumulada, número de iteraciones y evaluaciones. La salida sucede tras comprobar false, no simplemente tras actualizar a 4. Permitir predicción antes de avanzar."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Comprobar 3 iteraciones y 4 evaluaciones con contador 1..3; comprobar 0 iteraciones si comienza en 5."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Utiliza el simulador en modo manual. Antes de cada paso, responde: ¿cuál es el valor actual?, ¿qué se ejecutará ahora?, ¿habrá una nueva iteración? Después contrasta tu predicción.

## 3.5. Un while puede no ejecutarse nunca

```java
int numero = 5;

while (numero <= 3) {
    System.out.println(numero);
    numero++;
}
```

La primera condición (`5 <= 3`) es falsa. El cuerpo se ejecuta **cero veces**. El hecho de que las instrucciones estén escritas entre llaves no obliga a que se ejecuten.

## 3.6. El programa continúa después del ciclo

```java
int numero = 1;

while (numero <= 3) {
    System.out.println(numero);
    numero++;
}

System.out.println("Terminado");
```

La salida es:

```text
1
2
3
Terminado
```

«Terminado» aparece una sola vez porque está **fuera** del bloque `while`.

## 3.7. Programa completo para probar

```java
public class Main {
    public static void main(String[] args) {
        int numero = 1;

        while (numero <= 3) {
            System.out.println(numero);
            numero++;
        }

        System.out.println("Terminado");
    }
}
```

Antes de ejecutar, cambia mentalmente el valor inicial a 2 y a 4. Predice las salidas; después compruébalas en VS Code.

---

# 4. Diseñar un ciclo: inicio, condición y actualización

Leer un ciclo ya escrito es importante, pero el objetivo es poder **construirlo desde un problema nuevo**. Para hacerlo, conviene determinar primero el recorrido esperado.

## 4.1. Un método de construcción en cinco preguntas

Problema: mostrar los números pares desde 2 hasta 20 inclusive.

**Primera pregunta: ¿qué valores queremos recorrer?**  
`2, 4, 6, 8, 10, 12, 14, 16, 18, 20`.

**Segunda: ¿desde dónde comenzamos?**  
`numero = 2`.

**Tercera: ¿hasta dónde continuamos?**  
`numero <= 20`.

**Cuarta: ¿cómo avanzamos?**  
`numero = numero + 2`.

**Quinta: ¿qué hacemos con cada valor?**  
Mostrar `numero`.

El pseudocódigo queda así:

```text
INICIO
    numero ← 2
    MIENTRAS numero <= 20 HACER
        MOSTRAR numero
        numero ← numero + 2
    FIN MIENTRAS
FIN
```

Y su traducción:

```java
int numero = 2;

while (numero <= 20) {
    System.out.println(numero);
    numero += 2;
}
```

## 4.2. Cambiar el inicio

```java
int numero = 4;

while (numero <= 8) {
    System.out.println(numero);
    numero += 2;
}
```

Ahora la salida es `4`, `6`, `8`. Hemos cambiado el recorrido sin cambiar su mecanismo.

## 4.3. Cambiar el límite

```java
int numero = 1;

while (numero < 3) {
    System.out.println(numero);
    numero++;
}
```

Muestra 1 y 2. No muestra 3 porque `3 < 3` es falso. Comprueba siempre si el límite está incluido en el enunciado: «hasta 3 inclusive» no significa lo mismo que «menor que 3».

## 4.4. Cambiar el paso

```java
int numero = 1;

while (numero <= 5) {
    System.out.println(numero);
    numero += 2;
}
```

Muestra 1, 3 y 5. La actualización puede ser de una unidad, de dos, de cinco o incluso disminuir el contador, siempre que corresponda al recorrido previsto.

## 4.5. Contar hacia atrás

```java
int numero = 5;

while (numero >= 1) {
    System.out.println(numero);
    numero--;
}
```

Muestra 5, 4, 3, 2 y 1. Como el recorrido desciende, el incremento sería una actualización equivocada.

## 4.6. Detectar una repetición que no termina

Observa:

```java
int numero = 1;

while (numero <= 3) {
    System.out.println(numero);
}
```

No se modifica `numero`. La condición siempre se vuelve a evaluar con el mismo valor 1, de modo que el programa repite indefinidamente la impresión, salvo que se interrumpa externamente. Si ejecutas por error un programa así, utiliza el control de detener ejecución de VS Code o de la terminal.

## 4.7. Una actualización que se aleja del objetivo

```java
int numero = 5;

while (numero >= 1) {
    System.out.println(numero);
    numero++;
}
```

La variable aumenta cuando el objetivo era acercarse a valores inferiores a 1. Por tanto, **no finaliza como estaba previsto** y puede realizar una cantidad enorme de iteraciones. Como `int` tiene un rango limitado, un incremento sostenido puede producir desbordamiento; no corresponde afirmar que este ciclo necesariamente permanecerá para siempre en valores positivos. Lo importante es que su actualización es incoherente con la condición para el recorrido esperado.

## 4.8. Cómo demostrar que un ciclo termina

Para un contador que avanza hacia un límite, podemos explicar:

- Parte de un valor conocido.
- En cada iteración cambia en una dirección determinada.
- Ese cambio acerca el estado a una condición falsa.
- Al comprobar esa condición falsa, Java sale del ciclo.

No basta con escribir «termina porque tiene `++`». Si el contador avanza en la dirección incorrecta, el incremento puede alejarlo del objetivo.

**Actividad inmediata:** diseña primero en papel un ciclo que muestre `10, 8, 6, 4, 2`. No copies un ejemplo: determina inicio, condición, actualización y cuerpo. Después tradúcelo a Java y prueba el valor final.

---

# 5. Contadores: controlar el recorrido y contar eventos

Ya utilizamos un contador para determinar cuántas iteraciones debe realizar el ciclo. Pero ahora necesitamos registrar **cuántas veces se cumple un requisito**.

Supongamos que leemos cinco calificaciones y queremos contar cuántas son aprobatorias (`nota >= 6`).

## 5.1. Dos responsabilidades diferentes

Podemos declarar:

```java
int contador = 1;  // Controla qué nota vamos a leer.
int aprobados = 0; // Cuenta notas que cumplen el requisito.
```

Aunque ambas variables sean `int` y puedan incrementarse con `++`, no significan lo mismo.

| Variable | Responsabilidad | Cuándo se modifica |
|---|---|---|
| `contador` | Controlar qué nota corresponde leer | En cada iteración |
| `aprobados` | Registrar notas aprobatorias | Solo si `nota >= 6` |

## 5.2. Un contador de eventos comienza en cero

Antes de leer ninguna nota, tenemos cero aprobados. Por eso escribimos:

```java
int aprobados = 0;
```

Después:

```java
if (nota >= 6) {
    aprobados++;
}
```

Si la nota es 5, no incrementamos. Si es 7, sí.

## 5.3. Pseudocódigo para cinco notas

```text
INICIO
    contador ← 1
    aprobados ← 0

    MIENTRAS contador <= 5 HACER
        LEER nota

        SI nota >= 6 ENTONCES
            aprobados ← aprobados + 1
        FIN SI

        contador ← contador + 1
    FIN MIENTRAS

    MOSTRAR aprobados
FIN
```

## 5.4. Programa completo en Java

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int contador = 1;
        int aprobados = 0;

        while (contador <= 5) {
            System.out.print("Ingrese la nota " + contador + ": ");
            int nota = teclado.nextInt();

            if (nota >= 6) {
                aprobados++;
            }

            contador++;
        }

        System.out.println("Aprobados: " + aprobados);
        teclado.close();
    }
}
```

## 5.5. Trazado del conteo

Con las notas `7, 5, 8, 6, 9`:

| Iteración | Nota | `contador` al entrar | ¿Aprueba? | `aprobados` después |
|---:|---:|---:|---|---:|
| 1 | 7 | 1 | Sí | 1 |
| 2 | 5 | 2 | No | 1 |
| 3 | 8 | 3 | Sí | 2 |
| 4 | 6 | 4 | Sí | 3 |
| 5 | 9 | 5 | Sí | 4 |

El ciclo procesa cinco notas, pero `aprobados` aumenta cuatro veces. Al salir, el contador de control vale 6.

A veces resulta útil mostrar otro contador conceptual: «notas ya procesadas», que comienza en cero. No debe confundirse con el ejemplo Java, cuyo `contador` comienza en 1 e identifica la próxima nota. Ambos modelos son válidos, siempre que se explique qué representa cada variable.

## 5.6. Dos categorías en una misma lectura

Podemos contar también los no aprobados:

```java
if (nota >= 6) {
    aprobados++;
} else {
    noAprobados++;
}
```

Si antes del ciclo inicializamos ambos contadores en cero, al terminar cinco notas tendremos `aprobados + noAprobados == 5`. Esta relación sirve para verificar el resultado.

## 5.7. Un error frecuente

Si escribimos `aprobados++` fuera del `if`, estaremos contando todas las notas. La posición de una instrucción determina **cuándo** se ejecuta. No alcanza con utilizar un nombre de variable adecuado.

---

# 6. Acumuladores: conservar un resultado parcial

El contador registra cuántos datos cumplen un criterio. Pero ahora queremos calcular la **suma de todas las notas** para obtener después un promedio.

Con `7, 5, 8, 6, 9`, la suma debe ser 35.

## 6.1. El problema de reemplazar valores

Observa este fragmento:

```java
int suma = 0;

suma = 7;
suma = 5;
suma = 8;
```

**Predice el valor final antes de continuar.** ¿Vale 20 porque ingresaron 7, 5 y 8?

No. Vale **8**. Cada asignación sustituye el valor anterior. La variable no recuerda las cifras que recibió antes.

Ahora compara:

```java
int suma = 0;

suma = suma + 7;
suma = suma + 5;
suma = suma + 8;
```

Aquí el resultado final sí es 20. Cada asignación consulta el valor anterior, añade el nuevo dato y almacena el nuevo total.

**Acumular significa combinar el valor que ya conservamos con un nuevo dato antes de reasignarlo.** Esto recupera directamente lo aprendido sobre asignaciones en la Unidad 2.

## 6.2. Construir el acumulador

```java
int suma = 0;
```

Y, después de leer cada nota:

```java
suma = suma + nota;
```

La suma comienza en cero porque es el elemento neutro de la adición: todavía no hemos agregado ningún dato.

## 6.3. Trazado con cinco notas

| Iteración | Nota | Suma anterior | Operación | Nueva suma |
|---:|---:|---:|---|---:|
| Inicio | — | — | Inicializar | 0 |
| 1 | 7 | 0 | 0 + 7 | 7 |
| 2 | 5 | 7 | 7 + 5 | 12 |
| 3 | 8 | 12 | 12 + 8 | 20 |
| 4 | 6 | 20 | 20 + 6 | 26 |
| 5 | 9 | 26 | 26 + 9 | 35 |

## 6.4. Pseudocódigo

```text
INICIO
    suma ← 0
    contador ← 1

    MIENTRAS contador <= 5 HACER
        LEER nota
        suma ← suma + nota
        contador ← contador + 1
    FIN MIENTRAS

    MOSTRAR suma
FIN
```

## 6.5. Programa completo

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int contador = 1;
        int suma = 0;

        while (contador <= 5) {
            System.out.print("Nota " + contador + ": ");
            int nota = teclado.nextInt();
            suma = suma + nota;
            contador++;
        }

        System.out.println("Suma: " + suma);
        teclado.close();
    }
}
```

## 6.6. La escritura abreviada

` suma += nota; ` permite realizar, en este ejemplo, la misma acumulación que `suma = suma + nota;`. Al principio conviene usar la forma desarrollada porque hace visible el valor anterior. Después podemos utilizar la abreviatura cuando comprendemos qué representa.

## 6.7. Calcular el promedio sin perder decimales

Después de cinco notas:

```java
double promedio = suma * 1.0 / 5;
```

¿Por qué no escribimos siempre `double promedio = suma / 5;`? Porque si ambos operandos son enteros, Java realiza **división entera** antes de asignar el resultado a `double`. Con suma 17 y cantidad 2, `17 / 2` produce 8, que se almacena como 8.0; la expresión `17 * 1.0 / 2` produce 8.5.

## 6.8. Contador, dato actual y acumulador

Un programa puede necesitar simultáneamente:

| Variable | Función |
|---|---|
| `contador` | Controlar las iteraciones |
| `nota` | Guardar la calificación actual |
| `suma` | Conservar la suma parcial |
| `aprobados` | Contar las notas que cumplen el requisito |
| `promedio` | Guardar el cálculo final |

La pregunta fundamental es: **¿qué información necesito conservar entre una iteración y la siguiente?** Debemos conservar `suma` y `aprobados`; en cambio, podemos reemplazar `nota` cuando leemos otro estudiante, porque todavía no necesitamos recuperar cada nota individualmente.

## 6.9. Programa integrado con un solo while

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int contador = 1;
        int suma = 0;
        int aprobados = 0;

        while (contador <= 5) {
            System.out.print("Nota " + contador + ": ");
            int nota = teclado.nextInt();

            suma += nota;
            if (nota >= 6) {
                aprobados++;
            }
            contador++;
        }

        double promedio = suma * 1.0 / 5;
        System.out.println("Suma: " + suma);
        System.out.println("Promedio: " + promedio);
        System.out.println("Aprobados: " + aprobados);
        teclado.close();
    }
}
```

Con `7, 5, 8, 6, 9`, obtenemos suma 35, promedio 7.0 y cuatro aprobados.

## 6.10. Simulador de contadores y acumuladores

<!-- PM-RECURSO
id="u04-acumuladores-contadores"
tipo="simulador"
componente="simulador-acumuladores"
ubicacion="seccion-6.10"
datos="7;5;8;6;9"
criterio_aprobacion="nota>=6"
estado_inicial="indice:0;suma:0;aprobados:0"
resultados="suma:35;aprobados:4;promedio:7.0"
controles="anterior;siguiente;reiniciar;predecir"
descripcion="Mostrar nota actual, suma anterior, operación, suma nueva, comprobación de aprobado y contador de aprobados. Mantener estado inicial y cinco iteraciones. Pedir predicción antes de avanzar; por ejemplo, con suma=12 y aprobados=1, la siguiente nota 8 produce suma=20 y aprobados=2."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Comprobar suma 35, cuatro aprobados, suma parcial y no contar una nota inferior a seis."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Detén el simulador antes de cada actualización. Primero predice los nuevos valores; después comprueba tu respuesta.

## 6.11. Un error: reiniciar la suma dentro del ciclo

```java
for (int i = 1; i <= 5; i++) {
    int suma = 0;
    // Leer nota y sumar.
}
```

En cada iteración se crea e inicializa una nueva variable local `suma`. No conserva la suma anterior y además no está disponible fuera del bloque para mostrar el total. Debemos declararla e inicializarla **antes** del ciclo que la actualiza.

---

# 7. El ciclo for: organizar juntos los elementos de control

Ya construimos un recorrido mediante:

```java
int i = 1;

while (i <= 5) {
    System.out.println(i);
    i++;
}
```

Podemos reconocer tres componentes de control distribuidos: inicio, condición y actualización. Java ofrece una escritura que los reúne en un mismo encabezado.

## 7.1. El encabezado de for

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

La salida sigue siendo 1, 2, 3, 4, 5. **No aprendimos una nueva forma de sumar o mostrar datos: reorganizamos el control del mismo recorrido.**

## 7.2. Sus tres partes

En `for (int i = 1; i <= 5; i++)`:

- `int i = 1`: inicialización, se ejecuta una sola vez.
- `i <= 5`: condición, se comprueba antes de cada iteración.
- `i++`: actualización, se ejecuta después del cuerpo en cada iteración normal.

El orden es: inicializar → comprobar → ejecutar cuerpo → actualizar → volver a comprobar.

## 7.3. Esquema de for

<!-- PM-RECURSO
id="u04-for-esquema"
tipo="esquema-html"
componente="esquema-for"
ubicacion="seccion-7.3"
codigo="for(int i=1;i<=5;i++){System.out.println(i);}"
descripcion="Diagrama HTML semántico que distinga inicialización una vez, comprobación, cuerpo, actualización y regreso a condición. Mostrar i=1..5 y comprobación final con i=6 falsa. Contrastar con while equivalente. Sin animación automática ni imagen de código."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Representar inicialización, evaluación, cuerpo, actualización y condición final falsa; probar recorrido ascendente y descendente sin acceso inválido."
pm_interaccion="Esquema o imagen informativa: no agregar botones falsos; acompañar con preguntas de prediccion/consulta en texto."
-->

El esquema ayuda a comprender que la actualización no ocurre antes del cuerpo; ocurre después de cada iteración que continúa normalmente.

## 7.4. Trazado de for

| `i` al evaluar | `i <= 5` | Acción |
|---:|---|---|
| 1 | Verdadero | Mostrar 1 |
| 2 | Verdadero | Mostrar 2 |
| 3 | Verdadero | Mostrar 3 |
| 4 | Verdadero | Mostrar 4 |
| 5 | Verdadero | Mostrar 5 |
| 6 | Falso | Salir |

Cinco iteraciones; seis comprobaciones.

## 7.5. Cambiar inicio, condición y paso

**Contar desde cero:**

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

Muestra `0, 1, 2, 3, 4`: cinco iteraciones.

**Incluir el cinco:**

```java
for (int i = 0; i <= 5; i++) {
    System.out.println(i);
}
```

Muestra seis valores: `0, 1, 2, 3, 4, 5`. La diferencia de un símbolo cambia el recorrido.

**Contar hacia atrás:**

```java
for (int i = 5; i >= 1; i--) {
    System.out.println(i);
}
```

**Avanzar de dos en dos:**

```java
for (int i = 2; i <= 10; i += 2) {
    System.out.println(i);
}
```

Este último muestra `2, 4, 6, 8, 10`.

## 7.6. Convertir de while a for

```java
int i = 1;
while (i <= 4) {
    System.out.println(i);
    i++;
}
```

Se transforma en:

```java
for (int i = 1; i <= 4; i++) {
    System.out.println(i);
}
```

La cantidad de iteraciones y la salida son equivalentes en estos ejemplos; no estamos afirmando que toda transformación de ciclos sea automáticamente equivalente, ya que otros programas pueden depender del ámbito de las variables o de modificaciones adicionales.

**Actividad de doble dirección:** convierte `for (int i = 10; i >= 2; i -= 2)` a `while`. Después convierte un `while` que muestra 3, 6, 9, 12 en un `for`. Verifica mediante trazado, no solamente leyendo los símbolos.

## 7.7. ¿for es siempre mejor que while?

No. Ambos pueden expresar recorridos semejantes. En estos ejercicios, la elección depende principalmente de cuál deja más claro el algoritmo. Cuando el inicio, el límite y el paso están definidos, `for` resulta cómodo. Cuando la finalización depende de datos que llegan durante la ejecución, `while` suele expresar de manera natural esa condición.

## 7.8. Programa completo: cinco notas con for

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int suma = 0;
        int aprobados = 0;

        for (int i = 1; i <= 5; i++) {
            System.out.print("Nota " + i + ": ");
            int nota = teclado.nextInt();
            suma += nota;
            if (nota >= 6) {
                aprobados++;
            }
        }

        double promedio = suma * 1.0 / 5;
        System.out.println("Promedio: " + promedio);
        System.out.println("Aprobados: " + aprobados);
        teclado.close();
    }
}
```

---

# 8. Cuando no sabemos cuántas repeticiones habrá

Hasta ahora decidíamos procesar exactamente cinco notas. Pero algunos programas no pueden conocer anticipadamente cuántos datos ingresarán.

## 8.1. Un valor especial para terminar: centinela

Establezcamos esta regla: «Ingresar notas entre 1 y 10; escribir -1 para terminar». El valor -1 es un **centinela**: no representa una nota, sino una señal de finalización.

Debe ser un valor reservado y diferente de los datos válidos. Si -1 pudiera ser una nota, no sabríamos si representa una calificación o la orden de salir.

## 8.2. ¿Por qué necesitamos leer antes de while?

Para evaluar `nota != -1`, Java necesita conocer `nota`. Debemos obtener su valor **antes de la primera comprobación**.

```text
LEER nota

MIENTRAS nota != -1 HACER
    PROCESAR nota
    LEER nota
FIN MIENTRAS
```

La primera lectura suministra el valor inicial de la condición. La lectura dentro del ciclo permite que ese valor cambie y que eventualmente llegue el centinela.

## 8.3. Trazado del centinela

| Entrada | ¿Es -1? | ¿Se procesa? |
|---:|---|---|
| 7 | No | Sí |
| 5 | No | Sí |
| -1 | Sí | No |

Si la primera entrada es -1, el cuerpo realiza cero iteraciones, algo correcto porque no se ingresaron notas.

## 8.4. Pseudocódigo para acumular notas válidas

```text
INICIO
    suma ← 0
    cantidad ← 0
    LEER nota

    MIENTRAS nota != -1 HACER
        SI nota >= 1 Y nota <= 10 ENTONCES
            suma ← suma + nota
            cantidad ← cantidad + 1
        SINO
            MOSTRAR "Nota inválida"
        FIN SI
        LEER nota
    FIN MIENTRAS

    MOSTRAR suma
    MOSTRAR cantidad
FIN
```

## 8.5. Programa Java completo con centinela

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int suma = 0;
        int cantidad = 0;

        System.out.print("Nota (-1 para salir): ");
        int nota = teclado.nextInt();

        while (nota != -1) {
            if (nota >= 1 && nota <= 10) {
                suma += nota;
                cantidad++;
            } else {
                System.out.println("Nota inválida");
            }

            System.out.print("Nota (-1 para salir): ");
            nota = teclado.nextInt();
        }

        System.out.println("Suma: " + suma);
        System.out.println("Cantidad: " + cantidad);

        if (cantidad > 0) {
            double promedio = suma * 1.0 / cantidad;
            System.out.println("Promedio: " + promedio);
        } else {
            System.out.println("No se ingresaron notas válidas");
        }

        teclado.close();
    }
}
```

## 8.6. ¿Por qué comprobamos cantidad > 0?

Si el usuario escribe -1 inmediatamente, `cantidad` vale cero. No tiene sentido calcular el promedio de un conjunto vacío de notas. La condición evita realizar el cálculo cuando no existe ningún dato válido y proporciona un mensaje comprensible.

## 8.7. Otra forma de controlar la repetición: bandera booleana

No todos los ciclos dependen de números. También podemos utilizar una variable `boolean` como **bandera de control**.

```java
boolean continuar = true;

while (continuar) {
    System.out.println("Procesando...");
    continuar = false;
}
```

Este ejemplo ejecuta el cuerpo una vez. Antes de la siguiente comprobación, la bandera pasa a `false`, de modo que el ciclo termina.

En un programa real, la bandera puede cambiar a partir de una condición o de una decisión del usuario:

```java
boolean continuar = true;
int opcion = 0;

while (continuar) {
    System.out.println("1. Continuar");
    System.out.println("2. Salir");
    opcion = teclado.nextInt();

    if (opcion == 2) {
        continuar = false;
    }
}
```

Este es un **fragmento para analizar**: supone que `teclado` fue creado como `Scanner`. La bandera controla la repetición; `opcion` conserva la decisión del usuario.

Podemos reconocer tres mecanismos habituales: contador con límite, centinela y bandera booleana. No es necesario introducir ahora `break` o `continue` como recurso principal para terminar ciclos.

---

# 9. do...while: ejecutar primero y comprobar después

Queremos crear un menú que aparezca al menos una vez y se repita hasta elegir «Salir». Ya sabemos utilizar `switch` para seleccionar una opción y `while` para repetir. Pero conviene examinar **cuándo necesitamos comprobar la condición**.

## 9.1. Contrastar dos recorridos

Con `numero = 5`:

```java
int numero = 5;

while (numero <= 3) {
    System.out.println(numero);
    numero++;
}
```

La primera comprobación es falsa. No muestra nada.

En cambio:

```java
int numero = 5;

do {
    System.out.println(numero);
    numero++;
} while (numero <= 3);
```

Muestra **5** y después termina. ¿Por qué? Porque `do...while` ejecuta primero el cuerpo y recién entonces comprueba la condición. El cuerpo se realiza al menos una vez cuando el programa llega normalmente a esa estructura.

## 9.2. Sintaxis

```java
do {
    // Instrucciones
} while (condicion);
```

Observa el punto y coma después de la condición. Forma parte de esta sintaxis.

## 9.3. Esquema del recorrido

<!-- PM-RECURSO
id="u04-do-while-esquema"
tipo="esquema-html"
componente="esquema-do-while"
ubicacion="seccion-9.3"
descripcion="Esquema HTML comparativo: while comprueba antes y puede ejecutar cero veces; do...while ejecuta cuerpo antes y comprueba después. Mostrar caso numero=5 con condicion numero<=3 y resultado de una iteración, frente a cero con while. Para menú, usar descripciones como 'Mostrar menú' y 'Leer opción' sin fingir que son métodos Java ya definidos."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Simular una condición inicialmente falsa y demostrar una ejecución del cuerpo; contrastar con while de cero iteraciones."
pm_interaccion="Esquema o imagen informativa: no agregar botones falsos; acompañar con preguntas de prediccion/consulta en texto."
-->

## 9.4. El problema del menú

Un menú debe mostrar las opciones, leer una y procesarla. Después decide si vuelve a mostrarse. Este orden se adapta naturalmente a `do...while`.

```text
INICIO
    HACER
        MOSTRAR "1. Consultar saldo"
        MOSTRAR "2. Mostrar información"
        MOSTRAR "3. Salir"
        LEER opcion

        SEGUN opcion HACER
            1: MOSTRAR "Consulta de saldo"
            2: MOSTRAR "Información"
            3: MOSTRAR "Saliendo"
            OTRO: MOSTRAR "Opción inválida"
        FIN SEGUN

    MIENTRAS opcion != 3
FIN
```

## 9.5. Programa completo: menú con switch y do...while

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("1. Consultar saldo");
            System.out.println("2. Mostrar información");
            System.out.println("3. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = teclado.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("Consulta de saldo");
                    break;
                case 2:
                    System.out.println("Información del sistema");
                    break;
                case 3:
                    System.out.println("Saliendo");
                    break;
                default:
                    System.out.println("Opción inválida");
            }
        } while (opcion != 3);

        teclado.close();
    }
}
```

El menú **muestra mensajes**, no consulta un saldo real ni realiza operaciones bancarias. Para ello necesitaríamos agregar otras instrucciones y datos.

## 9.6. Trazado de las opciones 1, 2 y 3

| Iteración | Opción | Acción | ¿`opcion != 3`? |
|---:|---:|---|---|
| 1 | 1 | Consulta de saldo | Verdadero, repite |
| 2 | 2 | Información | Verdadero, repite |
| 3 | 3 | Saliendo | Falso, termina |

¿Qué sucede si la primera opción es 3? El menú aparece una vez y termina. Este comportamiento es coherente con nuestra necesidad.

## 9.7. ¿Los menús siempre deben utilizar do...while?

No. Se pueden construir con `while` y una inicialización adecuada. `do...while` es conveniente aquí porque expresa directamente que primero debemos mostrar y procesar una opción, y después decidir si repetimos. No debemos memorizar «menú = do...while» como una regla absoluta.

---

# 10. Elegir entre while, for y do...while

Las tres estructuras repiten instrucciones, pero organizan de manera diferente el control.

| Estructura | Momento de comprobar | ¿Puede realizar cero iteraciones? | Situación habitual |
|---|---|---|---|
| `while` | Antes del cuerpo | Sí | Repetir mientras siga cumpliéndose una condición |
| `for` | Antes del cuerpo | Sí | Recorrido con inicio, límite y actualización claros |
| `do...while` | Después del cuerpo | No, al alcanzar normalmente la estructura | Procesos que requieren una ejecución inicial |

## 10.1. Tres problemas, tres razonamientos

**Mostrar del 1 al 10.** Tenemos un recorrido bien definido; `for` permite reunir inicio, condición y paso.

**Leer enteros hasta recibir -1.** No sabemos cuántas entradas habrá. `while` expresa claramente la condición de continuación.

**Mostrar un menú hasta elegir salir.** Necesitamos mostrarlo al menos una vez. `do...while` es una solución clara.

## 10.2. La elección no se hace por palabras clave

Un `while` también puede mostrar del 1 al 10. Un `while` con una bandera puede controlar un menú. Elegimos según cómo se construye el algoritmo y qué estructura deja claro el mecanismo de finalización.

Antes de elegir, pregunta: ¿qué se repite?, ¿conozco la cantidad de iteraciones?, ¿debo ejecutar el cuerpo inicialmente?, ¿qué dato cambia?, ¿qué hace terminar el proceso?

## 10.3. Actividad de decisión sin escribir código

Elige y justifica una estructura para cada caso:

- Mostrar múltiplos de 3 desde 3 hasta 30.
- Procesar una cantidad de notas indicada al inicio.
- Pedir un dato hasta que pertenezca al rango 1–10.
- Leer importes hasta que el usuario escriba 0.
- Mostrar un menú de acciones que debe aparecer por lo menos una vez.

Puede haber más de una respuesta correcta, siempre que expliques cómo controlarías la repetición.

---

# 11. Errores frecuentes y depuración de ciclos

No basta con que Java compile. Un ciclo puede tener sintaxis válida y ejecutarse un número incorrecto de veces, no terminar como esperábamos o calcular mal el resultado.

## 11.1. Olvidar actualizar la variable de control

```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
}
```

El valor de `i` no cambia. La condición sigue siendo verdadera y el ciclo no alcanza la finalización prevista.

## 11.2. Actualizar en dirección incorrecta

```java
int i = 5;
while (i >= 1) {
    System.out.println(i);
    i++;
}
```

Queríamos llegar a valores inferiores a 1, pero incrementamos. Se produce un recorrido incorrecto que puede mantenerse durante una cantidad enorme de iteraciones hasta un eventual desbordamiento de `int`. La corrección del algoritmo es `i--`.

## 11.3. Excluir o incluir mal el límite

`for (int i = 1; i < 5; i++)` produce cuatro iteraciones; `for (int i = 1; i <= 5; i++)` produce cinco. Debemos decidir si 5 forma parte del recorrido.

## 11.4. Confundir iteración con evaluación

En un `while` que muestra 1, 2 y 3, existen tres iteraciones y cuatro comprobaciones. La condición falsa final no ejecuta el cuerpo.

## 11.5. Reemplazar en lugar de acumular

```java
suma = nota;
```

Sustituye la suma por la nota actual. En cambio:

```java
suma = suma + nota;
```

Conserva el resultado anterior y le agrega el nuevo dato.

## 11.6. Reiniciar el acumulador dentro del cuerpo

```java
for (int i = 1; i <= 5; i++) {
    int suma = 0;
    // Procesamiento
}
```

La variable vuelve a comenzar en cero cada vez. Debe inicializarse una sola vez antes del ciclo.

## 11.7. Incrementar el contador de eventos fuera del if

Si `aprobados++` aparece en cada iteración, estaremos contando todas las notas. Para contar aprobados debe ejecutarse solamente cuando `nota >= 6`.

## 11.8. Utilizar una variable local antes de asignarle valor

Este fragmento no compila:

```java
int nota;
while (nota != -1) {
    // ...
}
```

Java necesita que la variable local tenga un valor asignado antes de utilizarla en la condición.

## 11.9. No volver a leer el dato del centinela

Si la condición es `nota != -1` pero nunca realizamos una nueva lectura dentro del ciclo, no podremos recibir la señal de finalización.

## 11.10. Incorporar el centinela en los cálculos

El valor -1 es una señal, no una nota. Debemos reconocerlo **antes** de procesarlo para evitar que modifique suma y cantidad.

## 11.11. Dividir por una cantidad igual a cero

Cuando calculamos un promedio de cantidad variable, primero comprobamos `cantidad > 0`. Si no hay datos, informamos que no puede calcularse el promedio del conjunto vacío.

## 11.12. Agregar un punto y coma accidental tras while

```java
while (i <= 5); {
    System.out.println(i);
    i++;
}
```

Ese punto y coma es una sentencia vacía que queda como cuerpo del `while`; el bloque posterior ya no forma parte del ciclo. Si `i` comienza dentro del rango y no cambia durante la sentencia vacía, puede quedar repitiéndola indefinidamente.

## 11.13. Incrementar el contador en dos lugares

```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
    i++;
}
```

Muestra `1, 3, 5` porque incrementamos dentro del cuerpo y otra vez en el encabezado.

## 11.14. Suponer que todo ciclo se ejecuta una vez

`while` y `for` pueden ejecutar cero veces el cuerpo. `do...while` ejecuta primero y comprueba después. No debemos confundirlos.

## 11.15. Cómo depurar un ciclo

Para analizar un error, responde:

1. ¿Cuál es el estado inicial?
2. ¿Qué condición se comprueba exactamente?
3. ¿Qué instrucciones pertenecen al cuerpo?
4. ¿Qué variables cambian y en qué momento?
5. ¿La actualización acerca la ejecución a la salida?
6. ¿Qué sucede en el valor límite?
7. ¿Cuántas iteraciones esperamos y cuántas ocurren?
8. ¿La suma o el contador conservan el estado entre iteraciones?

Un trazado de tres o cuatro iteraciones suele ser más útil que modificar código al azar.

---

## 11.16. Taller de diseño autónomo: elegir el ciclo sin recibir su encabezado

Para cada situación completa la ficha **dato inicial → condición de continuación → información que cambia → tarea repetida → prueba de finalización**. No elijas `for`, `while` o `do...while` por su nombre: justifica primero qué controla las repeticiones.

**Problema A.** Mostrar los múltiplos de 3 comprendidos entre 3 y 21. Escribe antes la secuencia esperada y explica el valor que tendría la variable al finalizar.

**Problema B.** Pedir cantidades positivas hasta que el usuario ingrese -1. Calcular cuántas cantidades válidas se recibieron. No se conoce de antemano la cantidad de entradas. ¿Cómo evitas contar el centinela?

**Problema C.** Presentar un menú que debe mostrarse al menos una vez; continuar hasta que el usuario elija salir. ¿Cuándo se debe comprobar la opción?

**Pista 1.** Diferencia repetición de cantidad conocida, repetición controlada por dato y ejecución obligatoria inicial. **Pista 2.** Para el centinela comprueba los casos «-1 como primera entrada», «una cantidad y -1» y «varias cantidades y -1». Para el menú comprueba que elegir salir en el primer intento realmente termine el programa.

**Contraste, después del intento:** el problema A admite un `for (int numero = 3; numero <= 21; numero += 3)`; para B es natural leer un primer dato y continuar `while (cantidad != -1)`, actualizando dentro del cuerpo; para C, un `do...while` permite mostrar una primera vez antes de comprobar. No son recetas exclusivas: importa justificar que cada solución cumple los requisitos y termina.

**Error intencional:** si en el problema B se suma 1 al contador *antes* de comprobar si el dato es -1, ¿qué sucede cuando -1 es la primera entrada? Traza la ejecución y corrige la condición de conteo.

**Nota técnica sobre Scanner.** El `teclado.close()` de los programas breves es seguro al final de `main`, porque allí termina el programa. Sin embargo, si el `Scanner` se creó con `System.in`, cerrarlo también cierra la entrada estándar durante esa ejecución. No crees y cierres múltiples `Scanner(System.in)` en métodos diferentes cuando deban continuar las lecturas; comparte uno y ciérralo solamente al terminar, si corresponde.

# 12. Problema integrador: registro de calificaciones

Vamos a resolver un problema completo en **dos etapas**. La primera representa el aprendizaje esencial. La segunda incorpora una ampliación con validación mediante ciclos anidados. Ambas son valiosas, pero no tienen la misma exigencia.

## 12.1. Comprender el problema

Necesitamos solicitar una cantidad positiva de notas, leerlas, calcular la suma y el promedio, y contar cuántas cumplen el criterio de aprobación (`nota >= 6`).

Antes de programar, identifiquemos las variables:

| Variable | Responsabilidad |
|---|---|
| `cantidad` | Cantidad de notas solicitadas |
| `i` | Controlar qué nota se procesa |
| `nota` | Guardar el dato actual |
| `suma` | Acumular las notas |
| `aprobados` | Contar notas desde 6 |
| `promedio` | Guardar el resultado final |

## 12.2. Versión A: integrador esencial

**Requisitos:** pedir una cantidad mayor que cero; si es inválida, informar y terminar. Si es válida, procesar exactamente esa cantidad de notas mediante **un solo ciclo**. Para esta versión asumimos que las calificaciones ingresadas son enteros del 1 al 10. Calcular suma, promedio y cantidad de aprobados.

No necesitamos todavía validar cada nota mediante un segundo ciclo. Queremos demostrar primero que comprendemos una repetición controlada, un acumulador y un contador condicional.

### Pseudocódigo de la versión A

```text
INICIO
    LEER cantidad
    SI cantidad <= 0 ENTONCES
        MOSTRAR "Cantidad inválida"
    SINO
        suma ← 0
        aprobados ← 0

        PARA i DESDE 1 HASTA cantidad HACER
            LEER nota
            suma ← suma + nota
            SI nota >= 6 ENTONCES
                aprobados ← aprobados + 1
            FIN SI
        FIN PARA

        promedio ← suma * 1.0 / cantidad
        MOSTRAR suma
        MOSTRAR promedio
        MOSTRAR aprobados
    FIN SI
FIN
```

### Programa completo de la versión A

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Cantidad de notas: ");
        int cantidad = teclado.nextInt();

        if (cantidad <= 0) {
            System.out.println("Cantidad inválida");
        } else {
            int suma = 0;
            int aprobados = 0;

            for (int i = 1; i <= cantidad; i++) {
                System.out.print("Nota " + i + ": ");
                int nota = teclado.nextInt();
                suma += nota;

                if (nota >= 6) {
                    aprobados++;
                }
            }

            double promedio = suma * 1.0 / cantidad;
            System.out.println("Suma: " + suma);
            System.out.println("Promedio: " + promedio);
            System.out.println("Aprobados: " + aprobados);
        }

        teclado.close();
    }
}
```

### Pruebas esenciales

| Cantidad | Notas | Suma | Promedio | Aprobados |
|---:|---|---:|---:|---:|
| 5 | 7, 5, 8, 6, 9 | 35 | 7.0 | 4 |
| 3 | 6, 6, 6 | 18 | 6.0 | 3 |
| 3 | 1, 2, 3 | 6 | 2.0 | 0 |
| 1 | 10 | 10 | 10.0 | 1 |
| 0 | — | — | — | Cantidad inválida |

En parejas, antes de ejecutar, completen un trazado de tres notas: una aprobatoria, una no aprobatoria y otra aprobatoria. Cada estudiante deberá explicar qué variable controla el recorrido y cuál conserva la suma.

## 12.3. Versión B: integrador con validación de cada nota

Ahora agregamos una condición: solamente aceptaremos notas entre 1 y 10. Si un dato está fuera del rango, debemos volver a solicitar **esa misma nota**, sin avanzar al estudiante siguiente.

Tenemos dos necesidades distintas:

1. Procesar una cantidad conocida de notas válidas.
2. Repetir la lectura de una nota hasta que sea válida.

Esto justifica utilizar un ciclo dentro de otro. Se llama **anidamiento de ciclos**.

### Pseudocódigo de la versión B

```text
INICIO
    LEER cantidad
    SI cantidad <= 0 ENTONCES
        MOSTRAR "Cantidad inválida"
    SINO
        suma ← 0
        aprobados ← 0

        PARA i DESDE 1 HASTA cantidad HACER
            HACER
                LEER nota
                SI nota < 1 O nota > 10 ENTONCES
                    MOSTRAR "Nota inválida"
                FIN SI
            MIENTRAS nota < 1 O nota > 10

            suma ← suma + nota
            SI nota >= 6 ENTONCES
                aprobados ← aprobados + 1
            FIN SI
        FIN PARA

        promedio ← suma * 1.0 / cantidad
        MOSTRAR promedio
        MOSTRAR aprobados
    FIN SI
FIN
```

### Programa completo de la versión B

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Cantidad de notas: ");
        int cantidad = teclado.nextInt();

        if (cantidad <= 0) {
            System.out.println("Cantidad inválida");
        } else {
            int suma = 0;
            int aprobados = 0;

            for (int i = 1; i <= cantidad; i++) {
                int nota;

                do {
                    System.out.print("Nota " + i + ": ");
                    nota = teclado.nextInt();

                    if (nota < 1 || nota > 10) {
                        System.out.println("Nota inválida");
                    }
                } while (nota < 1 || nota > 10);

                suma += nota;
                if (nota >= 6) {
                    aprobados++;
                }
            }

            double promedio = suma * 1.0 / cantidad;
            System.out.println("Suma: " + suma);
            System.out.println("Promedio: " + promedio);
            System.out.println("Aprobados: " + aprobados);
        }

        teclado.close();
    }
}
```

### Trazado de una lectura incorrecta

Entrada:

```text
Cantidad de notas: 3
Nota 1: 7
Nota 2: 15
Nota inválida
Nota 2: 5
Nota 3: 8
```

La entrada 15 no se suma ni se cuenta, y el `for` todavía está procesando la segunda nota. La lectura se repite mediante el `do...while` interior. Al recibir 5, la nota es válida y recién entonces se avanza a la tercera.

Las notas válidas son `7, 5, 8`. Suma 20, promedio `20 / 3.0` (aproximadamente 6.6667) y dos aprobados.

## 12.4. Casos de prueba para las dos versiones

| Situación | Versión A | Versión B |
|---|---|---|
| Cantidad 0 | Rechaza | Rechaza |
| Una nota 10 | Promedio 10; 1 aprobado | Igual |
| Tres notas 1, 2, 3 | Promedio 2; 0 aprobados | Igual |
| Dato 15 en una nota | No se valida en esta versión | Lo rechaza y solicita nuevamente |
| Cantidad 2, notas 7 y 8 | Promedio 7.5; 2 aprobados | Igual |

La versión A es la evidencia mínima que buscamos consolidar. La versión B añade la coordinación de dos ciclos con responsabilidades diferentes y constituye una extensión guiada.

## 12.5. Un límite que todavía no resolvemos

El programa utiliza la variable `nota` para recibir valores sucesivos. Imaginemos:

```java
int nota = 7;
nota = 5;
nota = 8;
nota = 6;
nota = 9;
```

Al terminar, `nota` vale 9. ¿Podemos recuperar la primera o la tercera nota simplemente consultando esa variable? No. Aunque el programa conservó la suma y el contador de aprobados, **no guardó por separado todas las calificaciones originales**.

¿Qué sucedería si después de calcular el promedio el docente pidiera mostrar nuevamente la tercera nota? Necesitaríamos conservar varios valores individualmente. Esta necesidad abre la Unidad 5, en la que estudiaremos los **arreglos**.

---

# 13. Preparación para la evaluación: leer, predecir, corregir y construir

Las actividades siguientes están organizadas en tres niveles. No se propone resolverlas todas como una única prueba larga. Algunas sirven para practicar de forma autónoma, otras para discutir en parejas y otras para demostrar aprendizaje de manera individual.

## Nivel 1. Reconocer y comprender

### Actividad A. Identificar partes de un while

```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
```

Señala inicialización, condición, cuerpo y actualización. Después explica por qué `i` vale 6 al finalizar. ¿Cuántas iteraciones hay? ¿Cuántas comprobaciones?

### Actividad B. Interpretar un for

```java
for (int i = 2; i <= 10; i += 2) {
    System.out.println(i);
}
```

Indica valor inicial, límite, actualización, salida y cantidad de iteraciones. Explica en palabras qué recorrido construye.

### Actividad C. Elegir una estructura

Elige y justifica una estructura inicial para: mostrar del 1 al 20; leer números hasta -1; mostrar un menú al menos una vez; procesar diez notas; y repetir una lectura mientras sea inválida. La explicación del mecanismo es más importante que el nombre del ciclo.

## Nivel 2. Interpretar, predecir y corregir

### Actividad D. Trazar while

```java
int numero = 1;
while (numero <= 3) {
    System.out.println(numero);
    numero++;
}
```

Haz una tabla con cada evaluación, valor actual, resultado verdadero/falso y salida. Indica la primera comprobación falsa.

### Actividad E. Detectar un ciclo infinito

```java
int numero = 1;
while (numero <= 5) {
    System.out.println(numero);
}
```

Explica qué variable debería cambiar, por qué no cambia y cómo corregirías el programa. No es necesario ejecutarlo para descubrir el problema.

### Actividad F. Corregir un límite

Un estudiante quiere mostrar del 1 al 5:

```java
for (int i = 1; i < 5; i++) {
    System.out.println(i);
}
```

¿Qué muestra? ¿Qué falta? Corrige una sola parte y justifica la modificación.

### Actividad G. Seguir un acumulador

```java
int suma = 0;
for (int i = 1; i <= 4; i++) {
    suma = suma + i;
}
System.out.println(suma);
```

Completa las sumas parciales: inicio 0; después de i=1, i=2, i=3 e i=4. Predice la salida.

### Actividad H. Contar aprobados

Para `7, 5, 8, 6, 9`, construye un trazado del contador `aprobados` desde cero. Indica cuándo aumenta, cuándo conserva su valor y por qué.

### Actividad I. Detectar acumulador mal ubicado

```java
for (int i = 1; i <= 5; i++) {
    int suma = 0;
    suma += i;
}
```

¿Qué ocurre con `suma` en cada iteración? ¿Dónde debería declararse? Corrige y agrega una salida final.

### Actividad J. Predecir do...while

```java
int numero = 5;
do {
    System.out.println(numero);
    numero++;
} while (numero <= 3);
```

Predice la salida y explica la diferencia con un `while` de la misma condición.

### Actividad K. Trazar un menú

Un `do...while` muestra un menú y termina con `opcion != 3`. El usuario ingresa 1, después 2 y finalmente 3. Indica cuántas veces se muestra el menú, cuál es la condición al final de cada iteración y cuándo sale.

## Nivel 3. Construir, comprobar y justificar

### Actividad L. Mostrar una secuencia

Construye un programa que solicite un entero positivo `n` y muestre del 1 a `n`. Si `n <= 0`, informa el error. Haz pseudocódigo antes de Java. Prueba n=1, 5, 10 y 0.

### Actividad M. Sumar números

Solicita un entero positivo `n` y calcula `1 + 2 + ... + n`. Utiliza acumulador. Para n=5 el resultado es 15. Prueba 1, 3, 5 y 10. Explica por qué `suma` comienza en cero.

### Actividad N. Procesar cinco notas

Solicita cinco notas enteras (se supone entrada válida). Muestra suma, promedio y cantidad de aprobados (`>= 6`). Prueba: `7,5,8,6,9` → suma 35, promedio 7, cuatro aprobados; `6,6,6,6,6` → suma 30, promedio 6, cinco aprobados; `1,2,3,4,5` → suma 15, promedio 3, cero aprobados.

### Actividad O. Leer hasta un centinela

Lee enteros hasta -1. No incluyas el centinela en suma ni cantidad. Prueba `5,3,-1`; `10,-1`; y `-1` inmediatamente. Explica por qué la primera lectura es necesaria antes de comprobar el `while`.

### Actividad P. Repetir un menú

Muestra: 1. Saludar; 2. Mostrar información; 3. Salir. Utiliza `do...while` y `switch` y repite hasta elegir 3. Prueba salir inmediatamente, saludar y salir, y una opción inválida seguida de salir.

### Actividad Q. Registro de notas con validación

Implementa la **versión B** del integrador: solicita cantidad positiva, lee notas del 1 al 10, vuelve a solicitar una nota inválida, calcula promedio y cuenta aprobados. Primero escribe pseudocódigo. Prueba cantidad cero y una nota incorrecta entre dos válidas. Explica qué controla cada ciclo y por qué no avanza de estudiante cuando la nota es inválida.

## 13.18. Dos desafíos de lectura complementarios

**Desafío 1: reemplazar no es acumular.** Predice el resultado de `suma = 0; suma = 7; suma = 5; suma = 8;`. Después modifica las asignaciones para que el resultado sea 20.

**Desafío 2: transformar ciclos.** Reescribe en `for` un `while` que muestra del 1 al 4, y en `while` un `for` que muestra `10, 8, 6, 4, 2`. Comprueba que cada transformación conserva los valores mostrados.

## 13.19. Checkpoint individual: tres preguntas de salida

1. En un `while` que muestra del 1 al 3 inclusive, ¿cuántas iteraciones realiza el cuerpo y cuántas veces se evalúa la condición? Explica la diferencia.
2. Si `suma` vale 12 y la siguiente nota es 8, ¿qué asignación permite conservar lo anterior y obtener 20? ¿Por qué `suma = 8` no sirve?
3. Si una condición `while` permanece verdadera y ninguna instrucción modifica el estado del que depende, ¿qué comportamiento esperas y cómo lo corregirías?

Las respuestas deben justificarse sin ejecutar Java.

## 13.20. Trabajo en parejas y defensa

Cuando se trabaje en parejas, una persona será **conductor** (escribe el código) y otra **navegante** (lee el algoritmo, anticipa resultados y comprueba pruebas). Cambien de rol cada 10–15 minutos. Entreguen un programa por pareja, pero cada integrante explicará individualmente al menos una variable, una condición de finalización y un caso de prueba.

Lista rápida de trabajo en pareja: ¿intercambiaron roles?, ¿ambos explicaron el algoritmo?, ¿probaron más de un caso?, ¿corrigieron errores a partir de un trazado? Si hay una participación desigual, cada estudiante resolverá individualmente una predicción breve o completará una actualización faltante.

## 13.21. Criterios de evaluación

| Criterio | Logrado | En proceso | Inicial |
|---|---|---|---|
| Diseño del ciclo | Inicio, condición y actualización coherentes | Corrige parte del recorrido con ayuda | No identifica cómo controlar la repetición |
| Trazado | Predice estados e iteraciones correctamente | Algunos errores de seguimiento | No puede seguir el cambio de valores |
| Contadores y acumuladores | Conserva y actualiza resultados adecuadamente | Confunde alguna actualización | No conserva la información necesaria |
| Pruebas | Comprueba límites y explica finalización | Pruebas parciales | Solo ejecuta sin contrastar resultados |
| Explicación | Justifica el algoritmo y sus variables | Explica parcialmente | No puede explicar las decisiones tomadas |

**Autoevaluación y coevaluación:** responde Sí/No: «Puedo explicar qué hace terminar mi ciclo» y «Probé al menos un valor límite». Después escribe una reflexión breve: «El error que encontré o que podría aparecer en mi programa es... y lo comprobaría mediante...».

---

# Lo que debemos recordar

Las estructuras iterativas permiten resolver problemas que requieren ejecutar instrucciones repetidamente. No es necesario copiar el mismo bloque muchas veces: construimos un mecanismo de control.

Aprendimos que `while` comprueba la condición antes del cuerpo y puede ejecutar cero iteraciones. Distinguimos una **iteración** de una **evaluación de la condición** y descubrimos que la salida del ciclo sucede después de obtener una comprobación falsa.

Aprendimos a diseñar recorridos mediante preguntas: qué valores queremos mostrar, desde dónde comenzamos, qué límite utilizamos, cómo avanzamos y qué hacemos en cada iteración. Esta estrategia nos permite **crear ciclos**, no solamente leer ejemplos existentes.

Los **contadores de control** permiten seguir el recorrido; los **contadores de eventos** registran cuántos datos cumplen una condición. Los **acumuladores** combinan el valor anterior con el nuevo dato para conservar resultados parciales. Una asignación simple reemplaza el valor: no acumula por sí sola.

Conocimos `for`, que reúne inicialización, condición y actualización, y practicamos su relación con un `while` equivalente. También estudiamos ciclos cuya finalización depende de un **centinela**, como -1, y de una **bandera booleana**.

El ciclo `do...while` ejecuta primero el cuerpo y comprueba después. Resulta útil para menús que deben mostrarse inicialmente, aunque otros ciclos también pueden resolver ese problema cuando se diseñan correctamente.

En el integrador construimos una solución esencial con un solo ciclo, un acumulador y un contador de aprobados. Después estudiamos una ampliación con **ciclos anidados**, que permite repetir la lectura de cada nota inválida sin avanzar al estudiante siguiente.

El aprendizaje fundamental no es recordar `while`, `for` y `do...while` como tres recetas. **Es comprender qué se repite, qué cambia, qué información se conserva y qué condición hará que el programa termine.**

En la Unidad 5 recuperaremos una limitación deliberada: cuando leemos notas sucesivas sobre una misma variable, conservamos sumas y contadores, pero no todas las notas originales. Si necesitamos consultar la tercera nota, buscarlas o compararlas después, necesitaremos almacenarlas en una estructura adecuada. Allí aparecerán los **arreglos**.

---

<!-- PM-NOTA-EDITORIAL
Este capítulo es la versión completa revisada de la Unidad 4. Mantiene 13 apartados principales, 17 actividades A-Q, cuatro marcadores PM-RECURSO, dos desafíos complementarios y checkpoint individual. La versión A del integrador es la evidencia mínima; la versión B con anidamiento es ampliación guiada. Esta nota no debe mostrarse en la vista del estudiante.
-->
