# Unidad 3. Estructuras condicionales: programas que toman decisiones

**Programación I — 2026**  
**1.º Bachillerato Tecnológico en Informática · DGETP / UTU**

## ¿Qué aprenderemos en esta unidad?

En la Unidad 2 aprendimos a transformar algoritmos en programas Java.

Ya sabemos declarar variables, asignarles valores, realizar operaciones matemáticas, solicitar información mediante `Scanner` y mostrar resultados en la consola.

También aprendimos que las instrucciones modifican los valores de las variables cuando se ejecutan, y que podemos seguir esos cambios mediante trazados.

Pero nuestros programas todavía tienen una limitación importante.

Imaginemos que una persona desea comprar un producto. Nuestro programa puede solicitar el precio, conocer el saldo disponible y calcular cuánto dinero quedará después de la compra.

Sin embargo, todavía no sabe **decidir si debe autorizar la operación**.

Si la persona tiene dinero suficiente, corresponde permitir la compra.

Si no tiene dinero suficiente, corresponde rechazarla.

No podemos mostrar siempre el mismo mensaje, porque el resultado depende de los datos recibidos.

Necesitamos que el programa evalúe una condición y seleccione las instrucciones que corresponden.

Para resolver esta necesidad aprenderemos a utilizar **estructuras condicionales**.

En esta unidad estudiaremos:

- Cómo transformar las reglas de un problema en condiciones Java.
- Qué significa que una condición sea verdadera o falsa.
- Cómo utilizar `if` para ejecutar instrucciones solamente cuando se cumple una condición.
- Cómo utilizar `if...else` para seleccionar entre dos alternativas.
- Cómo utilizar `else if` cuando existen varias posibilidades.
- Por qué importa el orden de evaluación.
- Cómo combinar condiciones mediante `&&`, `||` y `!`.
- Cómo validar datos antes de procesarlos.
- Qué diferencia existe entre varios `if` independientes y una cadena de alternativas.
- Cómo comparar correctamente cadenas de caracteres.
- Cuándo utilizar `switch`.
- Cómo seguir el recorrido de ejecución y detectar errores lógicos.

Conservaremos nuestra metodología habitual:

**Comprender el problema → construir el algoritmo → escribir pseudocódigo → implementar Java → predecir → probar → explicar.**

El objetivo no es memorizar estructuras condicionales.

**Queremos comprender cómo transformar las reglas de un problema en decisiones que un programa pueda ejecutar correctamente.**


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

# 1. Una limitación de nuestros primeros programas

Recordemos el programa de compras que construimos en la unidad anterior.

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese el precio: ");
        double precio = teclado.nextDouble();

        System.out.print("Ingrese la cantidad: ");
        int cantidad = teclado.nextInt();

        double total = precio * cantidad;

        System.out.println("Total: $" + total);

        teclado.close();
    }
}
```

Este programa recibe dos datos, realiza una multiplicación y muestra el resultado.

Si el precio es $150 y compramos tres unidades:

`150 × 3 = 450`

El programa muestra:

```text
Total: $450.0
```

El cálculo es correcto.

Pero ahora queremos agregar una regla.

La persona dispone de un saldo determinado y solamente podrá realizar la compra si tiene dinero suficiente.

## 1.1. Un problema que todavía no sabemos resolver

Imaginemos estas situaciones:

| Saldo disponible | Total de la compra | ¿Debe autorizarse? |
| ---------------: | -----------------: | ------------------ |
|              600 |                450 | Sí                 |
|              450 |                450 | Sí                 |
|              400 |                450 | No                 |

Nuestro programa ya sabe calcular el total.

También podría calcular la diferencia entre el saldo y el precio.

Pero todavía no sabe seleccionar el mensaje correcto.

Podríamos agregar:

```java
System.out.println("Compra autorizada");
```

El problema es que esa instrucción se ejecutaría siempre que el programa llegara a ella.

También podríamos escribir:

```java
System.out.println("Saldo insuficiente");
```

Pero entonces siempre mostraríamos ese mensaje.

¿Y si colocamos los dos?

```java
System.out.println("Compra autorizada");
System.out.println("Saldo insuficiente");
```

El programa mostraría respuestas contradictorias.

No necesitamos otra operación matemática.

**Necesitamos decidir qué instrucción corresponde ejecutar según los datos.**

## 1.2. Expresar una decisión en lenguaje cotidiano

Podemos establecer esta regla:

> Si el saldo alcanza para pagar la compra, mostrar «Compra autorizada».

Pero hay una expresión que debemos precisar: «alcanza».

¿Cuándo alcanza el saldo?

Cuando es mayor o igual al importe de la compra.

Podemos escribirlo así:

`saldo >= total`

Esta comparación produce un resultado verdadero o falso.

Por ejemplo:

- `600 >= 450` es verdadero.
- `450 >= 450` es verdadero.
- `400 >= 450` es falso.

La igualdad debe estar incluida porque una persona que dispone exactamente del importe necesario puede pagar la compra.

## 1.3. Nuestro primer pseudocódigo con una condición

```text
INICIO
    LEER saldo
    LEER total

    SI saldo >= total ENTONCES
        MOSTRAR "Compra autorizada"
    FIN SI
FIN
```

Acabamos de introducir una estructura nueva.

Hasta ahora, nuestros algoritmos ejecutaban las instrucciones una detrás de otra.

Ahora una instrucción solamente se ejecutará si se cumple una condición.

La condición está expresada mediante:

`saldo >= total`

Cuando es verdadera, se muestra el mensaje.

Cuando es falsa, ese mensaje se omite.

## 1.4. ¿Qué hemos cambiado?

No hemos cambiado la manera de calcular el total.

Tampoco hemos cambiado qué significa almacenar información mediante variables.

Lo que incorporamos es la posibilidad de **controlar el recorrido de ejecución**.

A partir de ahora, un mismo programa podrá realizar acciones diferentes según los valores que reciba.

Esta capacidad se denomina selección o ejecución condicional.

---

# 2. La estructura if: ejecutar solamente cuando se cumple una condición

En Java utilizamos la palabra reservada `if` para construir una decisión.

La palabra inglesa _if_ significa «si».

Su estructura básica es:

```java
if (condicion) {

    // Instrucciones que se ejecutan
    // cuando la condición es verdadera

}
```

La condición se escribe entre paréntesis.

Las instrucciones que dependen de ella se colocan dentro de un bloque delimitado por llaves.

## 2.1. Nuestro primer if

Considera:

```java
int saldo = 1000;
int precio = 800;

if (saldo >= precio) {
    System.out.println("Compra autorizada");
}
```

Java evalúa:

`1000 >= 800`

El resultado es verdadero.

Por tanto, ejecuta:

```java
System.out.println("Compra autorizada");
```

La salida será:

```text
Compra autorizada
```

## 2.2. ¿Qué sucede si la condición es falsa?

Cambiemos el saldo.

```java
int saldo = 500;
int precio = 800;

if (saldo >= precio) {
    System.out.println("Compra autorizada");
}
```

Ahora Java evalúa:

`500 >= 800`

El resultado es falso.

Por tanto, no ejecuta la instrucción que está dentro del bloque.

El mensaje no aparece.

## 2.3. De la ejecución secuencial a la ejecución condicional

En la Unidad 2 utilizábamos instrucciones como:

```java
System.out.println("Primero");
System.out.println("Segundo");
System.out.println("Tercero");
```

Las tres se ejecutaban en orden.

Ahora podemos escribir:

```java
System.out.println("Primero");

if (edad >= 18) {
    System.out.println("Segundo");
}

System.out.println("Tercero");
```

El recorrido depende de `edad`.

Si `edad` vale 20, la salida será:

```text
Primero
Segundo
Tercero
```

Si `edad` vale 16, la salida será:

```text
Primero
Tercero
```

**Una condición falsa no detiene el programa: hace que se omita el bloque correspondiente.**

Después, la ejecución continúa con las instrucciones posteriores.

## 2.4. ¿Qué significa verdadero o falso?

En la unidad anterior conocimos el tipo `boolean`.

Un valor booleano solamente puede ser:

`true`

o:

`false`

Una comparación como:

```java
saldo >= precio
```

produce un resultado booleano.

Si el saldo alcanza, la expresión es verdadera.

Si no alcanza, es falsa.

La estructura `if` utiliza ese resultado para decidir si ejecuta su bloque.

También podríamos almacenar una condición:

```java
boolean puedeComprar = saldo >= precio;
```

Y después escribir:

```java
if (puedeComprar) {
    System.out.println("Compra autorizada");
}
```

Para este problema sencillo no necesitamos necesariamente crear la variable `puedeComprar`.

Pero el ejemplo permite comprobar que una condición produce un valor booleano.

## 2.5. La condición y la acción cumplen funciones diferentes

Considera:

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
}
```

La expresión:

```java
saldo >= precio
```

no muestra información en la consola.

Su función es determinar si se cumple una regla.

La instrucción `println` es la que muestra el mensaje.

Pero solamente se ejecuta cuando Java entra en el bloque.

**La condición determina el recorrido. Las instrucciones del bloque realizan las acciones.**

## 2.6. Las llaves delimitan el bloque

Observa:

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
    System.out.println("Puede retirar el producto");
}

System.out.println("Gracias por utilizar el programa");
```

Si la condición es verdadera, aparecen los tres mensajes.

Si es falsa, solamente aparece:

```text
Gracias por utilizar el programa
```

La última instrucción se encuentra fuera del bloque.

Por tanto, no depende de esa condición.

Esta diferencia es fundamental.

La indentación facilita la lectura, pero son las llaves las que delimitan el bloque.

## 2.7. Programa completo con if

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su saldo: ");
        int saldo = teclado.nextInt();

        System.out.print("Ingrese el precio: ");
        int precio = teclado.nextInt();

        if (saldo >= precio) {
            System.out.println("Compra autorizada");
        }

        System.out.println("Fin del programa");

        teclado.close();
    }
}
```

Probemos dos casos.

**Caso A**

```text
Ingrese su saldo: 1000
Ingrese el precio: 800
Compra autorizada
Fin del programa
```

**Caso B**

```text
Ingrese su saldo: 500
Ingrese el precio: 800
Fin del programa
```

¿Por qué aparece «Fin del programa» en ambos casos?

Porque esa instrucción está después del bloque `if`.

## 2.8. Trazar una condición

Considera:

```java
int edad = 16;

if (edad >= 15) {
    System.out.println("Puede participar");
}

System.out.println("Consulta finalizada");
```

Podemos registrar la ejecución:

| Paso | Acción                        | Resultado    |
| ---- | ----------------------------- | ------------ |
| 1    | Guardar `edad = 16`           | Edad vale 16 |
| 2    | Evaluar `edad >= 15`          | Verdadero    |
| 3    | Mostrar «Puede participar»    | Se ejecuta   |
| 4    | Mostrar «Consulta finalizada» | Se ejecuta   |

Ahora cambiemos:

`edad = 14`

| Paso | Acción                        | Resultado    |
| ---- | ----------------------------- | ------------ |
| 1    | Guardar `edad = 14`           | Edad vale 14 |
| 2    | Evaluar `edad >= 15`          | Falso        |
| 3    | Mostrar «Puede participar»    | Se omite     |
| 4    | Mostrar «Consulta finalizada» | Se ejecuta   |

Este trazado permite comprender qué instrucciones efectivamente se ejecutan.

No alcanza con mirar cuáles están escritas en el archivo.

---

# 3. Construir e interpretar condiciones

Hasta ahora utilizamos condiciones sencillas.

Pero necesitamos aprender a construirlas correctamente.

Para eso debemos interpretar cuidadosamente el enunciado del problema.

No significa lo mismo «más de 15» que «15 o más».

Tampoco significa lo mismo «menos de 10» que «hasta 10 inclusive».

Una diferencia pequeña en el lenguaje puede modificar el funcionamiento del programa.

## 3.1. Los operadores relacionales

Java proporciona operadores para comparar valores.

| Operador | Significado       | Ejemplo          |
| -------- | ----------------- | ---------------- |
| `>`      | Mayor que         | `edad > 15`      |
| `<`      | Menor que         | `nota < 6`       |
| `>=`     | Mayor o igual que | `edad >= 18`     |
| `<=`     | Menor o igual que | `cantidad <= 10` |
| `==`     | Igual que         | `opcion == 3`    |
| `!=`     | Distinto de       | `saldo != 0`     |

Estas comparaciones producen valores booleanos.

## 3.2. Del enunciado a Java

Imaginemos que el problema establece:

> Un estudiante puede participar si tiene al menos 15 años.

Debemos identificar:

**Dato:** edad.

**Requisito:** tener 15 años o más.

**Condición:**

```java
edad >= 15
```

Ahora podemos escribir:

```java
if (edad >= 15) {
    System.out.println("Puede participar");
}
```

## 3.3. De Java al lenguaje cotidiano

También debemos realizar el camino inverso.

Cuando leemos:

```java
cantidad <= 10
```

Necesitamos comprender qué significa.

Podemos expresarlo así:

> La cantidad es como máximo diez.

Cuando leemos:

```java
saldo != 0
```

Podemos explicar:

> El saldo es distinto de cero.

Y:

```java
precio > 100
```

Significa:

> El precio supera cien.

Esta habilidad será importante cuando tengamos que leer programas que no escribimos nosotros.

**Comprender código implica poder explicar qué regla representa cada condición.**

## 3.4. Mayor que y mayor o igual que

Compara:

```java
edad > 15
```

Con:

```java
edad >= 15
```

La primera condición exige tener más de 15 años.

La segunda acepta también exactamente 15 años.

| Edad | `edad > 15` | `edad >= 15` |
| ---: | ----------- | ------------ |
|   14 | Falso       | Falso        |
|   15 | Falso       | Verdadero    |
|   16 | Verdadero   | Verdadero    |

Si el problema establece «al menos 15 años», necesitamos `>=`.

## 3.5. Menor que y menor o igual que

Ahora comparemos:

```java
cantidad < 10
```

Y:

```java
cantidad <= 10
```

Si el programa permite comprar hasta diez unidades inclusive, la condición correcta es:

```java
cantidad <= 10
```

Si permite comprar solamente menos de diez, corresponde:

```java
cantidad < 10
```

## 3.6. Igualdad y asignación no son lo mismo

En la Unidad 2 aprendimos:

```java
precio = 150;
```

El signo `=` realiza una asignación.

Guarda 150 en `precio`.

Pero para comparar valores utilizamos:

```java
opcion == 3
```

El operador `==` pregunta si ambos valores son iguales.

Debemos recordar:

**`=` asigna un valor. `==` compara valores.**

## 3.7. La desigualdad

Utilizamos:

```java
!=
```

Para comprobar que dos valores son distintos.

Por ejemplo:

```java
int opcion = 4;

if (opcion != 3) {
    System.out.println("La opción no es tres");
}
```

Como `opcion` vale 4, la condición es verdadera.

## 3.8. Los valores límite

Consideremos esta condición:

```java
edad >= 18
```

Si solamente la probamos con 12 y 35 años, probablemente no descubramos ciertos errores.

Conviene utilizar valores cercanos al límite:

- 17: inmediatamente inferior.
- 18: el límite exacto.
- 19: inmediatamente superior.

¿Por qué?

Porque una condición incorrecta como:

```java
edad > 18
```

se comportaría igual con 12 y 35.

Pero fallaría con 18.

Los valores límite nos permiten detectar errores que otros datos podrían ocultar.

## 3.9. Estrategia para construir condiciones

Antes de escribir una condición:

1. Identifica el dato que necesitas comprobar.
2. Determina cuál es el requisito.
3. Comprueba si el límite está incluido.
4. Elige el operador correspondiente.
5. Prueba valores inferiores, iguales y superiores al límite cuando sea necesario.
6. Explica la condición con tus propias palabras.

## 3.10. Actividad de lectura

Supongamos que:

```java
int numero = 8;
```

Predice el resultado de estas expresiones:

```java
numero > 8
numero >= 8
numero == 8
numero != 8
numero < 10
numero <= 7
```

Después explica cada una en lenguaje cotidiano.

No alcanza con responder verdadero o falso.

Debes poder justificar qué comparación se realiza.

---

# 4. Dos alternativas: if...else

Volvamos al problema de la compra.

Nuestro primer programa con `if` solamente mostraba un mensaje cuando el saldo era suficiente.

Pero cuando la persona no tenía dinero suficiente, no explicaba lo que había sucedido.

Ahora necesitamos seleccionar entre dos alternativas.

**Si el saldo alcanza:**

Mostrar «Compra autorizada».

**Si el saldo no alcanza:**

Mostrar «Saldo insuficiente».

Para resolverlo utilizaremos `if...else`.

## 4.1. Pseudocódigo

```text
INICIO
    LEER saldo
    LEER precio

    SI saldo >= precio ENTONCES
        MOSTRAR "Compra autorizada"
    SINO
        MOSTRAR "Saldo insuficiente"
    FIN SI
FIN
```

La palabra `SINO` representa la alternativa que corresponde cuando la condición no se cumple.

## 4.2. Traducción a Java

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
} else {
    System.out.println("Saldo insuficiente");
}
```

Java evalúa una condición.

Si es verdadera, ejecuta el bloque del `if`.

Si es falsa, ejecuta el bloque del `else`.

Después continúa con las instrucciones posteriores a la estructura.

## 4.3. ¿Else tiene una condición propia?

No.

Observa:

```java
else {
    System.out.println("Saldo insuficiente");
}
```

No aparece una expresión entre paréntesis.

`else` significa que corresponde ejecutar esa alternativa porque la condición del `if` fue falsa.

No necesitamos escribir otra comparación.

Esto ayuda a evitar condiciones repetidas innecesariamente.

## 4.4. Diferencia entre if e if...else

Con un `if` sencillo:

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
}
```

Puede ocurrir que no se ejecute ninguna instrucción del bloque.

Con:

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
} else {
    System.out.println("Saldo insuficiente");
}
```

Se ejecutará exactamente uno de los dos bloques.

## 4.5. Programa completo

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su saldo: ");
        int saldo = teclado.nextInt();

        System.out.print("Ingrese el precio: ");
        int precio = teclado.nextInt();

        if (saldo >= precio) {
            System.out.println("Compra autorizada");
        } else {
            System.out.println("Saldo insuficiente");
        }

        teclado.close();
    }
}
```

## 4.6. Comprobar los límites

| Saldo | Precio | Condición | Resultado          |
| ----: | -----: | --------- | ------------------ |
|  1000 |    800 | Verdadera | Compra autorizada  |
|   800 |    800 | Verdadera | Compra autorizada  |
|   500 |    800 | Falsa     | Saldo insuficiente |

El segundo caso es fundamental.

Cuando el saldo es exactamente igual al precio, la compra debe autorizarse.

Por eso utilizamos `>=`.

## 4.7. Simulador de if...else

<!-- PM-RECURSO
id="u03-if-else"
tipo="simulador"
componente="simulador-if-else"
ubicacion="seccion-4.7"
datos="saldo;precio"
valores_iniciales="saldo:1000;precio:800"
condicion="saldo >= precio"
rama_verdadera="Compra autorizada"
rama_falsa="Saldo insuficiente"
controles="modificar-saldo;modificar-precio;predecir;comprobar;reiniciar"
pruebas="(1000,800)->autorizada;(800,800)->autorizada;(500,800)->insuficiente"
descripcion="Mostrar los datos, la comparación evaluada, el resultado booleano y una sola rama ejecutada. Permitir una predicción antes de revelar la salida. Utilizar código Java real, accesible y seleccionable."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Probar saldo superior, igual e inferior al precio; solo una rama ejecutada y explicar por qué igualdad satisface >=."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Antes de comprobar cada combinación, intenta anticipar qué mensaje mostrará el programa.

No cambies solamente el saldo.

También puedes modificar el precio para comprender que la decisión depende de ambos valores.

## 4.8. Una condición puede controlar una asignación

Nuestro programa solamente informa si la compra está autorizada.

Pero ¿qué sucede si queremos descontar el importe del saldo?

Podemos escribir:

```java
if (saldo >= precio) {
    saldo = saldo - precio;

    System.out.println("Compra autorizada");
    System.out.println("Nuevo saldo: " + saldo);
} else {
    System.out.println("Saldo insuficiente");
}
```

Ahora el saldo cambia solamente cuando la compra se autoriza.

Si tenemos:

`saldo = 1000`

`precio = 800`

El nuevo saldo será 200.

Pero si el saldo es 500, la resta no se ejecuta.

Aquí recuperamos una idea de la Unidad 2:

**Una variable cambia cuando se ejecuta una asignación. Una condición puede determinar si esa asignación llega a ejecutarse.**

---

# 5. Más de dos alternativas: else if

Hasta ahora trabajamos con una o dos posibilidades.

Pero algunos problemas necesitan seleccionar entre tres o más categorías.

Imaginemos que queremos clasificar una calificación.

Para este ejercicio utilizaremos las siguientes reglas:

- Nota igual o superior a 9: «Excelente».
- Nota desde 6 hasta menos de 9: «Aprobado».
- Nota inferior a 6: «Debe mejorar».

Esta clasificación corresponde al ejercicio y no representa necesariamente una escala institucional general.

Necesitamos seleccionar una sola categoría.

## 5.1. Una primera solución que parece correcta

Un estudiante escribe:

```java
int nota = 10;

if (nota >= 6) {
    System.out.println("Aprobado");
} else if (nota >= 9) {
    System.out.println("Excelente");
} else {
    System.out.println("Debe mejorar");
}
```

Antes de continuar, responde:

**¿Qué mostrará este programa si la nota es 10?**

Podríamos pensar que mostrará «Excelente», porque 10 es mayor que 9.

Pero debemos seguir las instrucciones realmente ejecutadas.

## 5.2. Realizar el trazado

Primero Java evalúa:

`nota >= 6`

Como `nota` vale 10:

`10 >= 6`

La condición es verdadera.

Por tanto, Java ejecuta:

```java
System.out.println("Aprobado");
```

Después abandona esa cadena de alternativas.

No evalúa:

```java
nota >= 9
```

La salida será:

```text
Aprobado
```

El programa tiene sintaxis válida.

Pero el resultado no cumple la clasificación que establecimos.

Encontramos un **error lógico**.

## 5.3. ¿Por qué ocurrió?

Porque colocamos primero una condición que incluye todas las notas superiores o iguales a 6.

Eso incluye también 9 y 10.

Cuando una cadena `if...else if` encuentra la primera condición verdadera, ejecuta su bloque y no continúa comprobando las alternativas posteriores.

Por eso importa el orden.

## 5.4. La solución corregida

```java
if (nota >= 9) {
    System.out.println("Excelente");
} else if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("Debe mejorar");
}
```

Ahora Java comprueba primero si la nota pertenece a la categoría superior.

Si no pertenece, continúa con la siguiente.

## 5.5. ¿Qué sucede con diferentes notas?

Si `nota = 10`:

- `nota >= 9`: verdadero.
- Se muestra «Excelente».
- No se evalúa `nota >= 6`.

Si `nota = 8`:

- `nota >= 9`: falso.
- `nota >= 6`: verdadero.
- Se muestra «Aprobado».

Si `nota = 4`:

- `nota >= 9`: falso.
- `nota >= 6`: falso.
- Se muestra «Debe mejorar».

## 5.6. Condición falsa y condición no evaluada

Esta distinción es muy importante.

Observa:

| Nota | `nota >= 9` | `nota >= 6`  | Resultado    |
| ---: | ----------- | ------------ | ------------ |
|    4 | Falsa       | Falsa        | Debe mejorar |
|    6 | Falsa       | Verdadera    | Aprobado     |
|    8 | Falsa       | Verdadera    | Aprobado     |
|    9 | Verdadera   | No se evalúa | Excelente    |
|   10 | Verdadera   | No se evalúa | Excelente    |

Cuando la nota vale 10, la segunda expresión sería verdadera si la calculáramos por separado.

Pero Java no llega a evaluarla dentro de esta cadena.

Por tanto, no debemos representarla como falsa.

**Una condición que no se evaluó no es lo mismo que una condición evaluada cuyo resultado fue falso.**

## 5.7. Estructura general de else if

```java
if (condicion1) {

    // Primera alternativa

} else if (condicion2) {

    // Segunda alternativa

} else if (condicion3) {

    // Tercera alternativa

} else {

    // Alternativa restante

}
```

Java comprueba las condiciones en orden.

Cuando encuentra la primera verdadera, ejecuta el bloque correspondiente.

Si ninguna condición anterior fue verdadera y existe un `else` final, ejecuta ese bloque.

El `else` no tiene una condición propia.

## 5.8. Comparar las tres estructuras

| Estructura            | Necesidad                                               | Qué puede ejecutarse        |
| --------------------- | ------------------------------------------------------- | --------------------------- |
| `if`                  | Ejecutar una acción solamente si se cumple un requisito | El bloque o ninguno         |
| `if...else`           | Elegir entre dos alternativas                           | Exactamente un bloque       |
| `if...else if...else` | Elegir una categoría entre varias                       | Exactamente una alternativa |

La última característica corresponde a una cadena que incluye `else` final.

Si no existe ese `else`, puede ocurrir que ninguna condición sea verdadera y no se ejecute ningún bloque.

## 5.9. ¿Debemos comprobar siempre el número mayor primero?

No existe una regla universal que obligue a comenzar siempre por el número mayor.

Lo importante es comprender las categorías.

En nuestro ejemplo, comenzar por `nota >= 9` resulta adecuado porque queremos separar primero las calificaciones más altas.

Pero otros problemas pueden necesitar un orden diferente.

**Debemos construir las condiciones según las reglas del problema, no memorizar un orden fijo.**

## 5.10. Simulador de clasificación

<!-- PM-RECURSO
id="u03-else-if"
tipo="simulador"
componente="simulador-else-if"
ubicacion="seccion-5.10"
entrada="nota"
rango_principal="1..10"
reglas="nota>=9:Excelente;nota>=6:Aprobado;else:Debe mejorar"
controles="cambiar-nota;predecir;comprobar;reiniciar"
casos="4;6;8;9;10"
descripcion="Mostrar cada condición realmente evaluada y su resultado. Cuando una condición anterior sea verdadera, señalar las posteriores como 'No se evalúa'. Resaltar una sola rama. Permitir observar opcionalmente el orden incorrecto para nota 10. No tratar la escala del ejercicio como escala institucional general."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Probar nota 5, 6, 8, 9 y 10; remarcar primera condición verdadera y ramas posteriores no evaluadas."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Antes de probar una nota, responde:

- ¿Qué condición se evaluará primero?
- ¿Será verdadera o falsa?
- ¿Java necesitará comprobar la segunda?
- ¿Qué mensaje aparecerá?

Después compara tu predicción con el resultado.

## 5.11. Programa completo con else if

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese una nota: ");
        int nota = teclado.nextInt();

        if (nota >= 9) {
            System.out.println("Excelente");
        } else if (nota >= 6) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Debe mejorar");
        }

        teclado.close();
    }
}
```

El programa clasifica la nota según las condiciones establecidas.

Sin embargo, todavía tiene un problema.

¿Qué sucede si introducimos 15 o -3?

¿Esos valores deberían aceptarse como calificaciones?

Retomaremos esta pregunta al estudiar la validación de datos.

---

# 6. Construir condiciones compuestas

Hasta ahora utilizamos condiciones que comparan un valor con otro.

Pero algunos problemas exigen comprobar varios requisitos.

Imaginemos un videojuego.

El jugador solamente puede pasar a una nueva etapa si cumple dos condiciones:

- Tiene al menos diez puntos.
- Conserva por lo menos una vida.

No alcanza con cumplir una sola.

Necesitamos comprobar ambas.

## 6.1. Primer problema: se necesitan todos los requisitos

Partimos del enunciado:

> El jugador puede avanzar si tiene al menos diez puntos y conserva alguna vida.

Primero construimos la condición correspondiente a los puntos:

```java
puntos >= 10
```

Después construimos la condición correspondiente a las vidas:

```java
vidas > 0
```

Ahora necesitamos combinarlas.

Java utiliza el operador:

```java
&&
```

Para expresar una operación lógica AND.

La condición completa será:

```java
puntos >= 10 && vidas > 0
```

## 6.2. ¿Qué significa &&?

El resultado de `A && B` es verdadero solamente cuando ambas condiciones son verdaderas.

Podemos comprobarlo:

| Puntos | Vidas | Puntos suficientes | Conserva vidas | ¿Puede avanzar? |
| -----: | ----: | ------------------ | -------------- | --------------- |
|     12 |     3 | Verdadero          | Verdadero      | Sí              |
|     12 |     0 | Verdadero          | Falso          | No              |
|      8 |     3 | Falso              | Verdadero      | No              |
|      8 |     0 | Falso              | Falso          | No              |

Si falta alguno de los requisitos, el jugador no puede avanzar.

## 6.3. Implementación con &&

```java
int puntos = 12;
int vidas = 3;

if (puntos >= 10 && vidas > 0) {
    System.out.println("Acceso permitido");
} else {
    System.out.println("Acceso denegado");
}
```

Como se cumplen ambas condiciones, se permite el acceso.

Pero si `vidas` vale cero, el acceso será denegado.

## 6.4. Segundo problema: alcanza con una alternativa

Ahora cambiemos el requisito.

El jugador puede entrar a una zona especial cuando:

- Tiene al menos diez puntos.
- O posee un permiso especial.

Esta vez no necesita cumplir las dos condiciones.

Alcanza con una.

Para representar esta situación, Java utiliza:

```java
||
```

Es el operador lógico OR.

## 6.5. Construir la condición con ||

Supongamos que tenemos:

```java
int puntos = 8;
boolean permisoEspecial = true;
```

Queremos comprobar:

```java
puntos >= 10 || permisoEspecial
```

La primera parte es falsa porque 8 es menor que 10.

Pero `permisoEspecial` es verdadero.

Por tanto, la condición completa es verdadera.

## 6.6. Comparar AND y OR

| Condición A | Condición B | `A && B`  | `A        |     | B`  |
| ----------- | ----------- | --------- | --------- | --- | --- |
| Verdadera   | Verdadera   | Verdadera | Verdadera |
| Verdadera   | Falsa       | Falsa     | Verdadera |
| Falsa       | Verdadera   | Falsa     | Verdadera |
| Falsa       | Falsa       | Falsa     | Falsa     |

Con `&&`, necesitamos que ambas condiciones sean verdaderas.

Con `||`, alcanza con que una sea verdadera.

Pero no debemos elegir el operador solamente porque en el enunciado aparece la palabra «y» u «o».

Debemos comprender qué requisitos necesita cumplir realmente el programa.

## 6.7. Tercer problema: agrupar condiciones

Imaginemos una regla de acceso.

Puede ingresar:

- Una persona adulta que tenga permiso.
- O una persona administradora.

Tenemos estas variables:

```java
int edad;
boolean tienePermiso;
boolean esAdministrador;
```

Primero necesitamos expresar:

> Ser mayor de edad y tener permiso.

```java
edad >= 18 && tienePermiso
```

Después agregamos la alternativa:

> O ser administrador.

La condición completa es:

```java
(edad >= 18 && tienePermiso) || esAdministrador
```

Los paréntesis ayudan a identificar qué requisitos forman un grupo.

## 6.8. Cambiar los paréntesis cambia el significado

Comparemos:

```java
(edad >= 18 && tienePermiso) || esAdministrador
```

Con:

```java
edad >= 18 && (tienePermiso || esAdministrador)
```

No significan lo mismo.

En la primera condición, una persona administradora puede ingresar aunque sea menor de 18 años.

En la segunda, todas las personas necesitan ser mayores de edad, incluso si son administradoras.

Probemos este caso:

```text
edad = 16
tienePermiso = false
esAdministrador = true
```

**Primera expresión:**

`(false && false) || true`

Resultado: verdadero.

**Segunda expresión:**

`false && (false || true)`

Resultado: falso.

El mismo conjunto de datos produce resultados diferentes porque cambiamos la agrupación.

Por eso debemos construir las condiciones a partir de la regla del problema.

## 6.9. El operador NOT: !

También podemos negar un valor booleano.

Para eso utilizamos:

```java
!
```

Supongamos que tenemos:

```java
boolean bloqueado = false;
```

La expresión:

```java
!bloqueado
```

Es verdadera.

Podemos escribir:

```java
if (!bloqueado) {
    System.out.println("Acceso permitido");
}
```

Esto representa la regla:

> Si no está bloqueado, permitir el acceso.

El operador `!` invierte el valor lógico de la expresión a la que se aplica.

## 6.10. ¿Cómo evalúa Java las condiciones compuestas?

Hasta ahora analizamos el resultado lógico completo.

Pero debemos comprender también algo sobre el recorrido de ejecución.

Java utiliza evaluación de cortocircuito con `&&` y `||`.

Esto significa que no siempre necesita evaluar todas las partes de una expresión.

### Cortocircuito con &&

Considera:

```java
puntos >= 10 && vidas > 0
```

Si `puntos` vale 8, la primera condición es falsa.

Como `&&` exige que ambas sean verdaderas, el resultado completo ya será falso.

Java no necesita evaluar la segunda expresión.

### Cortocircuito con ||

Ahora considera:

```java
puntos >= 10 || permisoEspecial
```

Si `puntos` vale 12, la primera condición es verdadera.

Como `||` solamente necesita una condición verdadera, Java no evalúa la segunda.

## 6.11. Condición falsa y condición no evaluada

Debemos recuperar una distinción que ya encontramos con `else if`.

Una condición puede:

- Evaluarse y resultar verdadera.
- Evaluarse y resultar falsa.
- No llegar a evaluarse.

No debemos confundir estas situaciones.

Por ejemplo, si tenemos:

```java
puntos >= 10 && vidas > 0
```

Y `puntos` vale 8, la segunda expresión no se evalúa.

No corresponde marcarla como falsa simplemente porque el resultado completo es falso.

Este detalle nos ayuda a comprender cómo se ejecuta realmente Java.

## 6.12. Simulador de condiciones compuestas

<!-- PM-RECURSO
id="u03-condiciones-compuestas"
tipo="simulador"
componente="simulador-condiciones-compuestas"
ubicacion="seccion-6.12"
escenarios="AND:puntos>=10&&vidas>0;OR:puntos>=10||permisoEspecial;AGRUPACION:(edad>=18&&tienePermiso)||esAdministrador"
controles="modificar-datos;seleccionar-escenario;predecir;comprobar;reiniciar"
descripcion="Mostrar requisitos individuales, agrupaciones y resultado de la expresión completa. Respetar evaluación de cortocircuito y señalar expresiones no evaluadas. Permitir comparar las dos agrupaciones del ejemplo de acceso. Mostrar código Java real, con controles de teclado y sin animaciones automáticas."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Distinguir &&, ||, ! y cortocircuito: la segunda condición puede no evaluarse, lo que no equivale a evaluarse como falso."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Antes de comprobar cada situación:

1. Identifica los requisitos.
2. Decide si deben cumplirse todos o solamente alguno.
3. Predice el resultado.
4. Observa qué expresiones se evalúan.
5. Explica por qué el programa permite o rechaza el acceso.

## 6.13. Elegir correctamente el operador

Cuando resolvemos un problema, no debemos comenzar escribiendo `&&` o `||` por costumbre.

Primero debemos preguntarnos:

- ¿Necesitamos que se cumplan todos los requisitos?
- ¿Alcanza con uno?
- ¿Existen grupos de condiciones?
- ¿Debemos negar alguna condición?
- ¿Qué sucederá con los valores límite?

**Una condición compuesta es una representación lógica de las reglas del problema.**

---

# 7. Validar datos antes de tomar decisiones

Volvamos al programa que clasifica calificaciones.

Habíamos establecido:

- Nota 9 o más: Excelente.
- Nota desde 6 hasta menos de 9: Aprobado.
- Nota menor que 6: Debe mejorar.

El programa funciona correctamente para notas comprendidas entre 1 y 10.

Pero ahora vamos a probar valores que no habíamos considerado.

## 7.1. Un programa que acepta datos incorrectos

Recordemos:

```java
if (nota >= 9) {
    System.out.println("Excelente");
} else if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("Debe mejorar");
}
```

¿Qué sucede si introducimos:

`nota = 15`?

La primera condición será verdadera.

El programa mostrará:

`Excelente`

¿Y si introducimos:

`nota = -3`?

Las dos primeras condiciones serán falsas.

El programa mostrará:

`Debe mejorar`

Las decisiones se ejecutan según las condiciones escritas.

Pero los resultados no son adecuados para nuestro problema, porque habíamos establecido un rango de notas válido.

**El error no está en la sintaxis. El programa está clasificando valores que no debería aceptar.**

## 7.2. ¿Qué significa validar?

Validar consiste en comprobar que los datos cumplan los requisitos necesarios antes de utilizarlos.

En este problema, las notas válidas son los enteros comprendidos entre 1 y 10 inclusive.

Por tanto, antes de clasificar una nota necesitamos comprobar que respeta ese rango.

## 7.3. Construir una condición de invalidez

Una nota es inválida cuando:

- Es menor que 1.
- O es mayor que 10.

Podemos escribir:

```java
nota < 1 || nota > 10
```

Utilizamos `||` porque alcanza con que ocurra cualquiera de esas situaciones.

## 7.4. Un error frecuente con &&

Imaginemos que escribimos:

```java
nota < 1 && nota > 10
```

¿Qué número entero podría ser simultáneamente menor que 1 y mayor que 10?

Ninguno.

Por tanto, esa condición nunca será verdadera para una nota entera.

No detectaría los valores inválidos.

La expresión tiene una sintaxis correcta, pero su lógica no representa el problema.

## 7.5. Primero validar, después clasificar

Ahora podemos escribir:

```java
if (nota < 1 || nota > 10) {
    System.out.println("Nota inválida");
} else if (nota >= 9) {
    System.out.println("Excelente");
} else if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("Debe mejorar");
}
```

Primero comprobamos la validez.

Solamente cuando la nota es válida continuamos con la clasificación.

## 7.6. ¿Por qué importa el orden?

Si comprobamos primero:

```java
nota >= 9
```

Una nota de 15 será clasificada como Excelente.

El programa seleccionará esa alternativa antes de llegar a la validación.

Por tanto, no basta con agregar una condición que detecte errores.

**Debemos colocarla antes de las operaciones que necesitan datos válidos.**

## 7.7. Programa completo con validación

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese una nota entre 1 y 10: ");
        int nota = teclado.nextInt();

        if (nota < 1 || nota > 10) {
            System.out.println("Nota inválida");
        } else if (nota >= 9) {
            System.out.println("Excelente");
        } else if (nota >= 6) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Debe mejorar");
        }

        teclado.close();
    }
}
```

## 7.8. Comprobar los límites

| Nota | Resultado esperado |
| ---: | ------------------ |
|   -1 | Nota inválida      |
|    0 | Nota inválida      |
|    1 | Debe mejorar       |
|    5 | Debe mejorar       |
|    6 | Aprobado           |
|    8 | Aprobado           |
|    9 | Excelente          |
|   10 | Excelente          |
|   11 | Nota inválida      |

Observa que utilizamos:

- Valores fuera del rango.
- El mínimo permitido.
- El máximo permitido.
- Valores cercanos a los límites entre categorías.

Estos casos ayudan a detectar errores de comparación y de orden.

## 7.9. Validación de rango y validación de formato

Nuestro programa utiliza:

```java
int nota = teclado.nextInt();
```

Esto supone que la entrada puede leerse como un entero.

La condición:

```java
nota < 1 || nota > 10
```

comprueba el rango después de realizar la lectura.

No evita que `nextInt()` falle si el usuario introduce un texto que no representa un entero válido.

Por tanto, existen dos problemas diferentes:

**Validación del formato:** comprobar que la entrada puede interpretarse como el tipo esperado.

**Validación del valor:** comprobar que el número pertenece al rango permitido.

En esta unidad nos concentraremos principalmente en la validación de valores.

Más adelante podremos estudiar mecanismos adicionales para tratar entradas incorrectas.

## 7.10. Validar no significa necesariamente repetir la lectura

Nuestro programa actual muestra «Nota inválida» y termina.

No vuelve a solicitar el dato.

Esto es suficiente para practicar una validación sencilla.

Cuando aprendamos estructuras iterativas, podremos construir programas que repitan la solicitud hasta recibir un valor aceptable.

Así, la validación se conectará con los contenidos de la Unidad 4.

---

# 8. Varios if independientes y alternativas excluyentes

Hasta ahora utilizamos `if...else` y `else if` para seleccionar alternativas.

Pero hay problemas donde necesitamos comprobar varias propiedades que pueden cumplirse al mismo tiempo.

Imaginemos que queremos analizar un número.

Necesitamos informar:

- Si es positivo.
- Si es par.

Un mismo número puede cumplir ambas condiciones.

Por ejemplo, 8 es positivo y par.

## 8.1. Dos condiciones independientes

```java
int numero = 8;

if (numero > 0) {
    System.out.println("Positivo");
}

if (numero % 2 == 0) {
    System.out.println("Par");
}
```

La salida será:

```text
Positivo
Par
```

¿Por qué aparecen dos mensajes?

Porque tenemos dos `if` independientes.

Java evalúa el primero.

Después continúa y evalúa el segundo.

## 8.2. ¿Qué sucedería con else if?

Observa:

```java
int numero = 8;

if (numero > 0) {
    System.out.println("Positivo");
} else if (numero % 2 == 0) {
    System.out.println("Par");
}
```

La primera condición es verdadera.

Por tanto, Java muestra:

```text
Positivo
```

Y no evalúa la segunda.

El programa no informa que el número es par.

La estructura no cumple lo que necesitábamos.

## 8.3. ¿Cuándo necesitamos alternativas excluyentes?

Imaginemos que queremos clasificar un número como:

- Positivo.
- Negativo.
- Cero.

Estas categorías son excluyentes para un entero.

Un número no puede ser simultáneamente positivo y negativo.

Podemos escribir:

```java
if (numero > 0) {
    System.out.println("Positivo");
} else if (numero < 0) {
    System.out.println("Negativo");
} else {
    System.out.println("Cero");
}
```

Aquí corresponde seleccionar una sola categoría.

## 8.4. ¿Cuándo necesitamos varias comprobaciones?

Imaginemos que queremos informar:

- Si un estudiante tiene asistencia suficiente.
- Si entregó un trabajo.

Ambas propiedades pueden cumplirse de manera independiente.

Podemos escribir:

```java
if (asistencia >= 80) {
    System.out.println("Asistencia suficiente");
}

if (entregoTrabajo) {
    System.out.println("Trabajo entregado");
}
```

En este caso puede aparecer un mensaje, ambos o ninguno.

Depende de los datos.

## 8.5. Elegir la estructura antes de programar

Analiza estos problemas.

**Problema A:** clasificar un número como positivo, negativo o cero.

**Problema B:** informar si un número es positivo y si además es par.

**Problema C:** autorizar o rechazar una compra.

**Problema D:** informar si un estudiante tiene asistencia suficiente y si entregó un trabajo.

Antes de escribir Java, responde:

1. ¿Debemos seleccionar una sola alternativa?
2. ¿Pueden cumplirse varias propiedades simultáneamente?
3. ¿Conviene utilizar `if`, `if...else`, `else if` o varios `if`?
4. ¿Por qué?

Este análisis evita elegir estructuras simplemente porque conocemos su sintaxis.

**La estructura condicional debe responder a las necesidades del problema.**

---

# 9. Comparar cadenas de caracteres

Hasta ahora comparamos principalmente valores numéricos.

Pero también podemos necesitar decisiones basadas en textos.

Por ejemplo, imaginemos que un videojuego entrega una recompensa especial cuando el rango del jugador es `"oro"`.

Podemos almacenar:

```java
String rango = "oro";
```

Ahora necesitamos comprobar su contenido.

## 9.1. ¿Podemos utilizar == para comparar textos?

En Java, `String` es una clase.

Cuando utilizamos `==` con referencias de objetos, comparamos si ambas referencias señalan el mismo objeto.

Esto no equivale necesariamente a comprobar que las cadenas contienen las mismas letras.

Por tanto, para comparar contenidos utilizaremos:

```java
equals()
```

## 9.2. Comparar con equals

```java
String rango = "oro";

if (rango.equals("oro")) {
    System.out.println("Recompensa disponible");
}
```

Como el contenido coincide, la condición es verdadera.

La salida será:

```text
Recompensa disponible
```

## 9.3. Programa completo con Scanner

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Ingrese su rango: ");
        String rango = teclado.next();

        if (rango.equals("oro")) {
            System.out.println("Recompensa disponible");
        } else {
            System.out.println("Sin recompensa especial");
        }

        teclado.close();
    }
}
```

Si el usuario introduce `oro`, recibe la recompensa.

Si introduce `plata`, no la recibe.

## 9.4. Las mayúsculas y minúsculas

El método `equals()` distingue las mayúsculas de las minúsculas.

Por ejemplo:

```java
"oro".equals("Oro")
```

Es falso.

Si necesitamos aceptar diferencias de mayúsculas y minúsculas, podemos utilizar:

```java
equalsIgnoreCase()
```

Por ejemplo:

```java
if (rango.equalsIgnoreCase("oro")) {
    System.out.println("Recompensa disponible");
}
```

## 9.5. No confundir números y cadenas

Si tenemos:

```java
int opcion = 3;
```

Podemos utilizar:

```java
opcion == 3
```

Pero si tenemos:

```java
String opcion = "3";
```

Para comparar su contenido utilizamos:

```java
opcion.equals("3")
```

Debemos elegir la operación adecuada según el tipo de dato.

## 9.6. Ampliación: referencias y null

Esta explicación no es necesaria para resolver los ejercicios iniciales, pero permite anticipar un concepto que estudiaremos al trabajar con objetos.

Una variable `String` puede contener `null`, lo que indica que no tiene una referencia a una cadena.

Si intentamos ejecutar:

```java
rango.equals("oro")
```

cuando `rango` vale `null`, se produce un error durante la ejecución.

Una alternativa es:

```java
"oro".equals(rango)
```

Esta expresión puede evaluar la igualdad sin producir ese error si `rango` es `null`.

Por ahora, lo imprescindible es recordar:

**Para comparar el contenido de cadenas, utilizamos `equals()` o el método adecuado a la comparación que necesitamos.**

---

# 10. La estructura switch: seleccionar entre valores concretos

Ya conocemos `if`, `if...else` y `else if`.

Ahora imaginemos que necesitamos seleccionar entre varios valores concretos.

Por ejemplo, una variable llamada `opcion` puede contener:

1, 2 o 3.

Queremos mostrar un mensaje diferente para cada valor.

Podríamos utilizar una cadena `else if`.

Pero Java también ofrece una estructura llamada `switch`.

## 10.1. Un primer ejemplo sencillo

```java
int opcion = 2;

switch (opcion) {

    case 1:
        System.out.println("Uno");
        break;

    case 2:
        System.out.println("Dos");
        break;

    default:
        System.out.println("Otra opción");
}
```

Antes de continuar, predice la salida.

Como `opcion` vale 2, Java selecciona:

```java
case 2:
```

Y muestra:

```text
Dos
```

Después ejecuta `break` y sale del `switch`.

## 10.2. ¿Qué hace switch?

La estructura `switch` permite seleccionar un recorrido según el valor de una expresión.

En este ejemplo, Java examina:

```java
opcion
```

Después busca un caso cuyo valor coincida.

## 10.3. Los case

Cada `case` identifica una posibilidad.

Por ejemplo:

```java
case 1:
```

Corresponde al valor 1.

```java
case 2:
```

Corresponde al valor 2.

Si el valor coincide, Java comienza a ejecutar las instrucciones de ese caso.

## 10.4. El significado de break

En el `switch` tradicional con dos puntos, utilizamos `break` para terminar la ejecución de la estructura.

Por ejemplo:

```java
case 2:
    System.out.println("Dos");
    break;
```

Cuando Java encuentra `break`, abandona el `switch`.

Así evitamos que continúe ejecutando instrucciones de casos posteriores.

## 10.5. ¿Qué sucede si olvidamos break?

Considera:

```java
int opcion = 2;

switch (opcion) {

    case 1:
        System.out.println("Uno");

    case 2:
        System.out.println("Dos");

    case 3:
        System.out.println("Tres");

    default:
        System.out.println("Otro");
}
```

¿Qué mostrará?

Java comienza desde `case 2`.

Muestra:

```text
Dos
```

Pero no encuentra un `break`.

Por tanto, continúa ejecutando las instrucciones siguientes.

La salida completa será:

```text
Dos
Tres
Otro
```

Este comportamiento se llama _fall-through_.

No es un error de sintaxis.

Forma parte del funcionamiento del `switch` tradicional.

Puede utilizarse deliberadamente en determinados programas, pero debemos comprender sus consecuencias.

## 10.6. El caso default

La palabra `default` permite indicar qué hacer cuando no existe un caso que coincida.

Por ejemplo:

```java
default:
    System.out.println("Opción inválida");
```

Si el usuario introduce 7 y solamente existen los casos 1, 2 y 3, se ejecutará `default`.

## 10.7. Un menú de opciones

Imaginemos que nuestro programa muestra:

```text
1. Consultar saldo
2. Realizar depósito
3. Salir
```

Podemos escribir:

```java
int opcion = 2;

switch (opcion) {

    case 1:
        System.out.println("Consultar saldo");
        break;

    case 2:
        System.out.println("Realizar depósito");
        break;

    case 3:
        System.out.println("Salir");
        break;

    default:
        System.out.println("Opción inválida");
}
```

Como la opción vale 2, la salida será:

```text
Realizar depósito
```

Este programa todavía no realiza realmente un depósito.

Solamente identifica la alternativa seleccionada y muestra el mensaje correspondiente.

## 10.8. Programa completo con Scanner

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.println("1. Consultar saldo");
        System.out.println("2. Realizar depósito");
        System.out.println("3. Salir");

        System.out.print("Seleccione una opción: ");
        int opcion = teclado.nextInt();

        switch (opcion) {

            case 1:
                System.out.println("Consultar saldo");
                break;

            case 2:
                System.out.println("Realizar depósito");
                break;

            case 3:
                System.out.println("Salir");
                break;

            default:
                System.out.println("Opción inválida");
        }

        teclado.close();
    }
}
```

El menú se presenta una sola vez.

El programa lee una opción, muestra el mensaje correspondiente y termina.

Más adelante aprenderemos a repetir el menú hasta que el usuario elija salir.

## 10.9. Switch con flechas

Java moderno también permite escribir:

```java
switch (opcion) {

    case 1 -> System.out.println("Consultar saldo");

    case 2 -> System.out.println("Realizar depósito");

    case 3 -> System.out.println("Salir");

    default -> System.out.println("Opción inválida");
}
```

Esta forma no necesita `break` para impedir que continúe la ejecución hacia las instrucciones de los otros casos.

Durante nuestros primeros ejercicios utilizaremos principalmente la forma tradicional para comprender los casos y el flujo de ejecución.

La forma con flechas quedará como una alternativa que también debemos reconocer.

## 10.10. ¿Cuándo utilizar if y cuándo switch?

`if` resulta adecuado cuando debemos comprobar:

- Rangos.
- Condiciones compuestas.
- Comparaciones entre diferentes variables.
- Requisitos que no dependen de un único valor concreto.

`switch` resulta especialmente conveniente cuando seleccionamos entre varios valores concretos de una misma expresión.

Por ejemplo, un menú de opciones.

No necesitamos utilizar `switch` siempre que existan varias alternativas.

Debemos elegir la estructura que represente mejor las reglas del problema.

## 10.11. Simulador de switch

<!-- PM-RECURSO
id="u03-switch"
tipo="simulador"
componente="simulador-switch"
ubicacion="seccion-10.11"
valores="1;2;3;4"
casos="1:Consultar saldo;2:Realizar depósito;3:Salir;default:Opción inválida"
modo_inicial="switch-tradicional-con-break"
modos="switch-tradicional-con-break;switch-tradicional-sin-break;switch-con-flechas"
controles="seleccionar-opcion;seleccionar-modo;predecir;comprobar;reiniciar"
descripcion="Mostrar el case seleccionado y las instrucciones realmente ejecutadas. En el modo sin break representar el fall-through hasta finalizar switch. En el modo de flechas ejecutar solamente la alternativa correspondiente. Mantener los mensajes del menú y no simular depósitos ni saldos reales."
pm_version="2"
pm_momento="prediccion-antes-de-revelar-resultado;explicacion-despues;transferencia-al-final"
pm_realimentacion="Explicar el estado anterior, operación/condición realizada, nuevo estado y causa del error; permitir reintento sin castigo."
pm_accesibilidad="Teclado, texto legible/seleccionable, etiquetas descriptivas, contraste adecuado, resultado textual, sin depender de color ni movimiento; controles anterior y reiniciar cuando tenga pasos."
pm_respaldo="Si falla JavaScript, presentar el enunciado, una tabla de estados o ejemplo explicado y las preguntas en texto; nunca bloquear el capítulo por un widget."
pm_criterios="Probar opción reconocida, no reconocida y rama por defecto. Diferenciar casos seleccionados y salida, incluyendo break si el ejemplo usa switch clásico."
pm_control="Sin avance automatico; entrada del estudiante antes de comprobar; verificar reinicio completo y casos de frontera."
-->

Prueba varias opciones.

Después compara qué sucede cuando:

- Utilizamos `break`.
- Eliminamos `break`.
- Utilizamos la forma con flechas.

El objetivo es comprender el recorrido de ejecución, no solamente reconocer la sintaxis.

---

## 10.12. Estrategia general para convertir una regla en una condición

No memorices solamente dónde van los paréntesis de `if`. Ante un problema nuevo, sigue este recorrido: **(1)** identifica los datos; **(2)** explica con tus palabras cuándo debe ejecutarse cada acción; **(3)** escribe casos que sí cumplen y casos que no; **(4)** selecciona operadores y estructura; **(5)** traza el orden de evaluación; **(6)** prueba el límite exacto y un valor a cada lado.

**Ejercicio sin código guiado.** Una compra obtiene envío gratuito cuando su total es al menos $1500 y el cliente está registrado. Describe primero dos compras que cumplan y dos que no. ¿Qué variables necesitas? ¿Qué condición escribirías? ¿Cambiaría algo si la regla fuera «total de al menos $1500 *o* cliente registrado»? Justifica el operador antes de escribir Java.

**Pista 1.** La palabra *y* en este requisito exige que dos condiciones resulten verdaderas; la palabra *o* permite que alcance una de ellas. **Pista 2.** Prueba el borde `total = 1500`, tanto con cliente registrado como sin registro.

**Contraste posterior:** para la primera regla sirve `total >= 1500 && registrado`; para la segunda, `total >= 1500 || registrado`. Si se usa `boolean registrado`, no es necesario escribir `registrado == true`. Una solución correcta debe producir una sola respuesta coherente y resistir los casos de borde.

**Transferencia:** un usuario solo accede si tiene contraseña correcta *y* su cuenta no está bloqueada. Escribe la regla en palabras, define las variables booleanas, propone cuatro combinaciones y, recién entonces, formula la condición Java.

**Nota técnica sobre los ejemplos con Scanner.** En esta unidad, `teclado.close()` aparece al final de programas que terminan inmediatamente. Cerrar un `Scanner` creado sobre `System.in` también cierra la entrada estándar; no lo hagas en un método auxiliar si el programa seguirá leyendo. Si varios métodos necesitan entrada, comparte un solo `Scanner` como argumento.

# 11. Problema integrador: auditoría de almacenamiento

Vamos a resolver un problema relacionado con el trabajo informático.

Imaginemos que necesitamos analizar el espacio disponible de una unidad de almacenamiento.

Queremos informar si se encuentra en una situación normal, de alerta o crítica.

Pero antes debemos comprobar que los datos recibidos sean válidos.

Este problema nos permitirá integrar:

- Variables.
- Entrada con `Scanner`.
- Operaciones aritméticas.
- Validación.
- Condiciones compuestas.
- Alternativas mediante `else if`.
- Casos de prueba.
- Valores límite.

## 11.1. Enunciado

Un programa debe solicitar:

- Capacidad total de una unidad de almacenamiento.
- Espacio utilizado.

Ambos valores se expresarán en gigabytes.

Después debe calcular:

- Espacio libre.
- Porcentaje de espacio libre.

Finalmente debe clasificar el estado según estas reglas:

**Crítico:** porcentaje libre menor o igual al 10 %.

**Alerta:** porcentaje libre mayor al 10 % y menor o igual al 25 %.

**Normal:** porcentaje libre mayor al 25 %.

Antes de realizar los cálculos, debemos validar la entrada.

## 11.2. Identificar los datos

Necesitamos:

```java
double capacidadTotal;
double espacioUtilizado;
```

Utilizaremos `double` porque los valores pueden contener decimales.

Ambos deben expresarse en la misma unidad.

No tendría sentido restar una cantidad expresada en gigabytes de otra expresada en megabytes sin realizar antes la conversión correspondiente.

## 11.3. Identificar las restricciones

La capacidad total debe ser mayor que cero:

```java
capacidadTotal > 0
```

El espacio utilizado no puede ser negativo:

```java
espacioUtilizado >= 0
```

Y no puede superar la capacidad:

```java
espacioUtilizado <= capacidadTotal
```

Estas condiciones describen datos válidos.

## 11.4. Construir una condición de error

Los datos son inválidos cuando ocurre alguna de estas situaciones:

- La capacidad total es cero o negativa.
- El espacio utilizado es negativo.
- El espacio utilizado supera la capacidad total.

La condición será:

```java
capacidadTotal <= 0 ||
espacioUtilizado < 0 ||
espacioUtilizado > capacidadTotal
```

Utilizamos `||` porque cualquiera de estas situaciones basta para rechazar los datos.

## 11.5. Calcular el espacio libre

Si los valores son válidos:

```java
double espacioLibre =
    capacidadTotal - espacioUtilizado;
```

Por ejemplo:

Capacidad total: 500 GB.

Espacio utilizado: 400 GB.

Espacio libre:

`500 - 400 = 100 GB`

## 11.6. Calcular el porcentaje

Queremos saber qué parte de la capacidad total está libre.

Utilizamos:

```java
double porcentajeLibre =
    espacioLibre * 100 / capacidadTotal;
```

Si tenemos 100 GB libres de un total de 500:

`100 × 100 / 500 = 20`

Por tanto, el porcentaje libre es 20 %.

## 11.7. Clasificar el almacenamiento

Podemos escribir:

```java
if (porcentajeLibre <= 10) {
    System.out.println("Estado crítico");
} else if (porcentajeLibre <= 25) {
    System.out.println("Estado de alerta");
} else {
    System.out.println("Estado normal");
}
```

Observa que no necesitamos repetir en la segunda condición que el porcentaje debe ser mayor que 10.

Si Java llega al `else if`, significa que la primera condición fue falsa.

Por tanto, ya sabemos que el porcentaje no es menor o igual a 10.

La segunda comparación determina si se encuentra dentro del intervalo de alerta.

## 11.8. Pseudocódigo completo

```text
INICIO
    LEER capacidadTotal
    LEER espacioUtilizado

    SI capacidadTotal <= 0 O
       espacioUtilizado < 0 O
       espacioUtilizado > capacidadTotal ENTONCES

        MOSTRAR "Datos inválidos"

    SINO

        espacioLibre ← capacidadTotal - espacioUtilizado

        porcentajeLibre ← espacioLibre * 100 / capacidadTotal

        MOSTRAR porcentajeLibre

        SI porcentajeLibre <= 10 ENTONCES
            MOSTRAR "Estado crítico"

        SINO SI porcentajeLibre <= 25 ENTONCES
            MOSTRAR "Estado de alerta"

        SINO
            MOSTRAR "Estado normal"

        FIN SI

    FIN SI
FIN
```

Primero validamos.

Después calculamos.

Finalmente clasificamos.

El orden de las tareas responde a las necesidades del problema.

## 11.9. Programa Java completo

```java
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        System.out.print("Capacidad total (GB): ");
        double capacidadTotal = teclado.nextDouble();

        System.out.print("Espacio utilizado (GB): ");
        double espacioUtilizado = teclado.nextDouble();

        // Comprobamos las restricciones.
        if (capacidadTotal <= 0 ||
            espacioUtilizado < 0 ||
            espacioUtilizado > capacidadTotal) {

            System.out.println("Datos inválidos");

        } else {

            // Calculamos el espacio disponible.
            double espacioLibre =
                capacidadTotal - espacioUtilizado;

            // Calculamos el porcentaje libre.
            double porcentajeLibre =
                espacioLibre * 100 / capacidadTotal;

            System.out.println(
                "Porcentaje libre: " + porcentajeLibre + "%"
            );

            // Clasificamos el estado.
            if (porcentajeLibre <= 10) {
                System.out.println("Estado crítico");

            } else if (porcentajeLibre <= 25) {
                System.out.println("Estado de alerta");

            } else {
                System.out.println("Estado normal");
            }
        }

        teclado.close();
    }
}
```

## 11.10. ¿Por qué validamos antes de calcular?

Imaginemos que la capacidad total es cero.

Según las reglas, ese dato no es válido.

Además, la fórmula del porcentaje utiliza `capacidadTotal` como divisor.

No queremos ejecutar ese cálculo cuando los datos incumplen las restricciones.

Por eso el programa solamente entra en el bloque de procesamiento cuando la validación fue satisfactoria.

Es importante hacer una precisión técnica.

En Java, una división de valores `double` entre cero no se comporta igual que una división entera entre cero.

Según los valores, puede producir `Infinity` o `NaN`.

No necesitamos profundizar todavía en estos resultados.

Lo importante para este problema es que **la capacidad cero está prohibida por las reglas y debemos impedir que se utilice para calcular el porcentaje**.

## 11.11. Casos de prueba

| Capacidad | Utilizado | Libre | Porcentaje | Estado          |
| --------: | --------: | ----: | ---------: | --------------- |
|       500 |       450 |    50 |       10 % | Crítico         |
|       500 |       400 |   100 |       20 % | Alerta          |
|       500 |       375 |   125 |       25 % | Alerta          |
|       500 |       350 |   150 |       30 % | Normal          |
|       500 |       500 |     0 |        0 % | Crítico         |
|       500 |       600 |     — |          — | Datos inválidos |
|         0 |         0 |     — |          — | Datos inválidos |
|       500 |       -10 |     — |          — | Datos inválidos |

Los casos incluyen:

- Datos válidos.
- Datos inválidos.
- Porcentajes en los límites exactos.
- Estados diferentes.

## 11.12. Una precisión sobre double

En esta unidad utilizamos `double` porque trabajamos con cantidades que pueden contener decimales.

Debemos recordar que los números de punto flotante no siempre representan exactamente todos los valores decimales.

Por tanto, algunas operaciones pueden producir pequeñas diferencias de precisión.

Para comprender el algoritmo utilizaremos principalmente casos fáciles de comprobar manualmente.

En aplicaciones reales pueden necesitarse cuidados adicionales al comparar resultados decimales próximos a ciertos límites.

No necesitamos incorporar ahora técnicas avanzadas.

Pero sí debemos reconocer que el resultado calculado depende también de cómo Java representa los datos.

## 11.13. Comprobar el programa en tres etapas

**Primero: las restricciones.**

¿El programa rechaza capacidades menores o iguales a cero?

¿Rechaza espacios utilizados negativos?

¿Rechaza valores superiores a la capacidad?

**Segundo: los cálculos.**

¿El espacio libre es correcto?

¿El porcentaje corresponde a los datos?

**Tercero: la clasificación.**

¿Los porcentajes 10 % y 25 % pertenecen a las categorías establecidas?

¿El programa muestra exactamente un estado?

Esta estrategia recupera los criterios de verificación de la Unidad 1.

## 11.14. ¿Qué ocurre si cambian los requisitos?

Imaginemos que ahora el estado Crítico corresponde a un porcentaje libre menor o igual al 15 %.

¿Qué deberíamos modificar?

Primero necesitamos redefinir las categorías.

Después debemos revisar las condiciones.

No alcanza con cambiar el texto de un mensaje.

La modificación afecta a las reglas del algoritmo.

Esta será una actividad de ampliación durante la evaluación.

---

# 12. Errores frecuentes: comprender por qué una decisión falla

Las estructuras condicionales permiten construir programas más flexibles.

Pero también pueden introducir errores difíciles de descubrir si solamente observamos algunas salidas.

Analizaremos errores de sintaxis y errores lógicos.

## 12.1. Confundir asignación con comparación

Considera:

```java
if (opcion = 3) {
    System.out.println("Opción tres");
}
```

Si `opcion` es de tipo `int`, este código no compila como condición de `if`.

La asignación produce un entero, mientras que `if` necesita una expresión booleanа.

La comparación correcta es:

```java
if (opcion == 3) {
    System.out.println("Opción tres");
}
```

## 12.2. Excluir un valor límite

Enunciado:

> Permitir el acceso desde los 18 años inclusive.

Incorrecto:

```java
edad > 18
```

Correcto:

```java
edad >= 18
```

La primera expresión excluye exactamente 18.

## 12.3. Ordenar mal else if

```java
if (nota >= 6) {
    System.out.println("Aprobado");
} else if (nota >= 9) {
    System.out.println("Excelente");
}
```

Con nota 10, el programa muestra «Aprobado».

El problema está en el orden de las condiciones.

## 12.4. Utilizar && cuando corresponde ||

Para rechazar notas fuera del rango 1–10:

Incorrecto:

```java
nota < 1 && nota > 10
```

Correcto:

```java
nota < 1 || nota > 10
```

La primera condición no puede cumplirse para ningún entero.

## 12.5. Utilizar else if para propiedades independientes

Si queremos informar si un número es positivo y si es par, una cadena `else if` puede impedir que aparezcan ambas propiedades.

Debemos analizar si necesitamos una sola alternativa o varias comprobaciones.

## 12.6. Olvidar break en switch

En el `switch` tradicional, omitir `break` puede provocar que se ejecuten instrucciones de casos posteriores.

No es necesariamente un error de sintaxis.

Pero puede producir un resultado incorrecto si queríamos seleccionar una sola alternativa.

## 12.7. Comparar cadenas mediante ==

Para comprobar el contenido de cadenas `String`, debemos utilizar `equals()` o el método de comparación adecuado.

El operador `==` compara referencias de objetos, no garantiza igualdad de contenido.

## 12.8. Validar después de clasificar

Si primero clasificamos una nota y después comprobamos si está entre 1 y 10, podemos mostrar un resultado inadecuado antes de detectar el error.

Debemos validar antes de procesar los datos que dependen de esa restricción.

## 12.9. Confundir una condición falsa con una no evaluada

En una cadena `else if`, cuando una condición anterior es verdadera, Java no evalúa las siguientes.

No debemos afirmar que todas las condiciones posteriores fueron falsas.

Simplemente no llegaron a evaluarse.

## 12.10. Colocar una asignación fuera del bloque

Considera:

```java
if (saldo >= precio) {
    System.out.println("Compra autorizada");
}

saldo = saldo - precio;
```

La resta está fuera del `if`.

Por tanto, se ejecutará aunque el saldo sea insuficiente.

Si necesitamos descontar solamente las compras autorizadas, la asignación debe estar dentro del bloque.

## 12.11. Un punto y coma después del if

Observa:

```java
if (edad >= 18); {
    System.out.println("Mayor de edad");
}
```

A primera vista podría parecer correcto.

Pero el punto y coma después de la condición termina una sentencia vacía controlada por el `if`.

El bloque posterior queda separado de esa condición.

Por tanto, puede ejecutarse incluso cuando `edad` vale 16.

La forma correcta es:

```java
if (edad >= 18) {
    System.out.println("Mayor de edad");
}
```

Este ejemplo demuestra que un símbolo mal ubicado puede cambiar completamente el comportamiento del programa.

## 12.12. Dos if no son lo mismo que if...else

Compara:

```java
if (nota >= 6) {
    System.out.println("Aprobado");
}

if (nota < 6) {
    System.out.println("No aprobado");
}
```

Con:

```java
if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("No aprobado");
}
```

Para las notas enteras habituales, ambos fragmentos pueden mostrar el mismo mensaje.

Pero no funcionan de la misma manera.

En el primero, Java evalúa dos condiciones independientes.

En el segundo, evalúa una y selecciona entre dos alternativas.

La segunda estructura expresa directamente una elección excluyente.

No debemos afirmar que utilizar dos `if` sea siempre incorrecto.

Debemos comprender qué comportamiento queremos representar.

## 12.13. Cómo depurar una condición

Cuando el programa no toma la decisión esperada, conviene preguntar:

1. ¿Qué valores tienen las variables?
2. ¿Qué regla establece el problema?
3. ¿Cuál es la condición escrita en Java?
4. ¿La comparación es verdadera o falsa?
5. ¿Java llegó realmente a evaluarla?
6. ¿Qué bloque debería ejecutarse?
7. ¿Qué bloque se ejecutó?
8. ¿Las instrucciones están dentro de las llaves correctas?
9. ¿Probamos los valores límite?
10. ¿Qué modificación mínima corrige el problema?

Después debemos volver a ejecutar los casos de prueba.

**Depurar una condición significa comprender qué decisión está tomando el programa y por qué.**

---

# 13. Preparación para la evaluación: decidir, explicar y comprobar

Al finalizar esta unidad debemos poder construir condiciones, pero también leerlas, interpretarlas y explicar qué instrucciones se ejecutan.

No alcanza con recordar la estructura de `if`.

Queremos comprender qué regla representa.

Las actividades están organizadas en tres niveles.

---

## Nivel 1. Reconocer y comprender

### 13.1. Conceptos fundamentales

Explica con tus palabras:

1. ¿Qué es una estructura condicional?
2. ¿Qué resultado produce una comparación?
3. ¿Para qué sirve `if`?
4. ¿Qué significa `else`?
5. ¿Cuándo necesitamos `else if`?
6. ¿Por qué importa el orden de las alternativas?
7. ¿Qué diferencia existe entre `=` y `==`?
8. ¿Qué significa `&&`?
9. ¿Qué significa `||`?
10. ¿Para qué utilizamos `!`?
11. ¿Por qué debemos comprobar valores límite?
12. ¿Qué diferencia existe entre varios `if` y una cadena `else if`?
13. ¿Para qué utilizamos `switch`?
14. ¿Qué hace `break`?
15. ¿Por qué utilizamos `equals()` con cadenas?

No respondas solamente mediante definiciones.

Intenta utilizar ejemplos.

### 13.2. Actividad A: construir e interpretar condiciones

Escribe una condición Java para cada enunciado:

1. La edad debe ser al menos 15 años.
2. El precio debe ser mayor que cero.
3. La cantidad puede ser como máximo 20.
4. La opción debe ser exactamente 3.
5. El saldo debe ser distinto de cero.
6. La nota debe ser inferior a 6.
7. El número debe ser igual a 10.
8. La temperatura debe ser menor o igual a 30.

Después realiza el camino inverso.

Explica en palabras:

```java
edad >= 18
nota < 6
saldo != 0
cantidad == 5
precio > 100
```

Finalmente, elige tres condiciones y propone para cada una un valor que la haga verdadera y otro que la haga falsa.

### 13.3. Actividad B: identificar valores límite

Tenemos:

```java
edad >= 18
```

Indica si es verdadera o falsa para:

- 17.
- 18.
- 19.

Después analiza:

```java
cantidad <= 10
```

Con:

- 9.
- 10.
- 11.

Explica por qué necesitamos probar los valores exactos de los límites.

### 13.4. Actividad C: completar una estructura

Un estudiante puede participar en una actividad desde los 15 años inclusive.

Completa:

```java
if (______________) {
    System.out.println("Puede participar");
} else {
    System.out.println("No puede participar");
}
```

La variable disponible es:

```java
int edad;
```

Supón que ya recibió un valor válido.

Explica por qué elegiste ese operador.

---

## Nivel 2. Interpretar, predecir y corregir

### 13.5. Actividad D: predecir una decisión

```java
int saldo = 500;
int precio = 800;

if (saldo >= precio) {
    System.out.println("Compra autorizada");
} else {
    System.out.println("Saldo insuficiente");
}

System.out.println("Fin");
```

Sin ejecutar:

1. ¿Cuál es la condición?
2. ¿Es verdadera o falsa?
3. ¿Qué bloque se ejecuta?
4. ¿Cuál es la salida completa?
5. ¿Qué cambiaría si el saldo fuera exactamente 800?

### 13.6. Actividad E: seguir else if

```java
int nota = 10;

if (nota >= 9) {
    System.out.println("Excelente");
} else if (nota >= 6) {
    System.out.println("Aprobado");
} else {
    System.out.println("Debe mejorar");
}
```

Responde:

1. ¿Qué condición se evalúa primero?
2. ¿Cuál es su resultado?
3. ¿Se evalúa la segunda?
4. ¿Qué mensaje se muestra?
5. ¿La segunda condición sería verdadera si se evaluara?
6. ¿Por qué debemos distinguir una condición falsa de otra no evaluada?

### 13.7. Actividad F: corregir el orden

Un estudiante escribió:

```java
if (nota >= 6) {
    System.out.println("Aprobado");
} else if (nota >= 9) {
    System.out.println("Excelente");
} else {
    System.out.println("Debe mejorar");
}
```

Con nota 10, muestra «Aprobado».

Explica por qué sucede.

Después corrige el programa.

No cambies los mensajes ni las categorías.

Modifica solamente lo necesario.

### 13.8. Actividad G: condiciones compuestas

Un jugador puede avanzar si tiene al menos diez puntos y conserva alguna vida.

Escribe la condición.

Comprueba:

| Puntos | Vidas | ¿Puede avanzar? |
| -----: | ----: | --------------- |
|     12 |     3 | Sí              |
|     12 |     0 | No              |
|      8 |     3 | No              |
|      8 |     0 | No              |
|     10 |     1 | Sí              |

Explica por qué utilizaste el operador lógico correspondiente.

### 13.9. Actividad H: corregir una validación

```java
if (nota < 1 && nota > 10) {
    System.out.println("Nota inválida");
}
```

Responde:

1. ¿Qué intenta comprobar?
2. ¿Por qué no funciona?
3. ¿Qué operador debería utilizar?
4. ¿Qué sucede con nota -2?
5. ¿Qué sucede con nota 11?
6. ¿Qué pruebas realizarías después de corregirla?

### 13.10. Actividad I: propiedades independientes

```java
int numero = 8;

if (numero > 0) {
    System.out.println("Positivo");
}

if (numero % 2 == 0) {
    System.out.println("Par");
}
```

Responde:

1. ¿Cuál es la salida?
2. ¿Se evalúan ambas condiciones?
3. ¿Qué sucedería si utilizáramos `else if`?
4. ¿Por qué no sería adecuado para este problema?

### 13.11. Actividad J: interpretar switch

```java
int opcion = 2;

switch (opcion) {

    case 1:
        System.out.println("Uno");
        break;

    case 2:
        System.out.println("Dos");
        break;

    case 3:
        System.out.println("Tres");
        break;

    default:
        System.out.println("Opción inválida");
}
```

Responde:

1. ¿Qué mensaje aparece?
2. ¿Qué `case` coincide?
3. ¿Qué hace `break`?
4. ¿Qué sucedería si `opcion` valiera 7?
5. ¿Qué podría ocurrir si elimináramos los `break`?

---

## Nivel 3. Construir, comprobar y justificar

### 13.12. Actividad K: autorizar una compra

Una persona quiere comprar un producto.

El programa debe solicitar:

- Saldo disponible.
- Precio del producto.

Si el saldo alcanza, debe mostrar «Compra autorizada».

En caso contrario, debe mostrar «Saldo insuficiente».

Antes de escribir Java:

1. Identifica los datos.
2. Escribe la condición.
3. Construye el pseudocódigo.
4. Determina los resultados posibles.

Después escribe el programa completo con `Scanner`.

Prueba:

| Saldo | Precio | Resultado    |
| ----: | -----: | ------------ |
|  1000 |    800 | Autorizada   |
|   800 |    800 | Autorizada   |
|   500 |    800 | Insuficiente |

Explica por qué incluiste la igualdad.

### 13.13. Actividad L: calcular un descuento

Una tienda ofrece un descuento del 10 % cuando el importe de la compra alcanza $1000.

El programa debe:

1. Solicitar el importe.
2. Comprobar si corresponde el descuento.
3. Calcular el importe final.
4. Mostrar el resultado.

Escribe primero el pseudocódigo.

Después construye el programa Java.

Prueba:

| Importe | Resultado esperado |
| ------: | -----------------: |
|     800 |                800 |
|    1000 |                900 |
|    1500 |               1350 |

Explica qué sucede cuando el importe es exactamente $1000.

### 13.14. Actividad M: clasificar una nota

Construye un programa que solicite una nota entera entre 1 y 10.

Debe mostrar:

- «Nota inválida» fuera del rango.
- «Excelente» desde 9.
- «Aprobado» desde 6 hasta menos de 9.
- «Debe mejorar» para los demás valores válidos.

Primero escribe el pseudocódigo.

Después implementa Java.

Prueba con:

0, 1, 5, 6, 8, 9, 10 y 11.

Explica por qué validaste antes de clasificar.

### 13.15. Actividad N: menú de opciones

Construye un programa que muestre:

```text
1. Consultar información
2. Mostrar ayuda
3. Salir
```

Después debe solicitar una opción y mostrar el mensaje correspondiente.

Utiliza `switch`.

Si se introduce un valor diferente, debe informar que la opción es inválida.

Este menú solamente se ejecutará una vez.

No necesitas repetirlo.

En la Unidad 4 aprenderemos a mantener un menú disponible hasta que el usuario elija salir.

### 13.16. Actividad O: préstamo de materiales

Un sistema permite retirar un equipo solamente si:

- El estudiante está registrado.
- No tiene préstamos pendientes.
- El equipo está disponible.

Tenemos:

```java
boolean registrado;
int prestamosPendientes;
boolean disponible;
```

Construye la condición que autoriza el préstamo.

Después escribe un `if...else`.

Prueba:

| Registrado | Pendientes | Disponible | Resultado  |
| ---------- | ---------: | ---------- | ---------- |
| true       |          0 | true       | Autorizado |
| true       |          1 | true       | Rechazado  |
| false      |          0 | true       | Rechazado  |
| true       |          0 | false      | Rechazado  |

Explica por qué deben cumplirse todos los requisitos.

### 13.17. Actividad P: auditoría de almacenamiento

Recupera el problema de la sección 11.

El programa recibe:

- Capacidad total.
- Espacio utilizado.

Debe calcular el porcentaje libre y clasificar el estado.

Realiza:

1. Identifica las restricciones.
2. Construye la condición de datos inválidos.
3. Escribe las fórmulas.
4. Define las tres categorías.
5. Construye el pseudocódigo.
6. Implementa el programa.
7. Prueba los límites 10 % y 25 %.
8. Explica por qué validas antes de calcular.

Después modifica una regla:

> El estado Crítico ahora corresponde a un porcentaje libre menor o igual al 15 %.

Ajusta las condiciones.

Explica qué cambiaste y por qué.

## 13.18. Defensa breve de comprensión

Después de resolver uno de los ejercicios integradores, prepárate para explicar en aproximadamente un minuto:

- Qué problema resolviste.
- Qué condición utilizaste.
- Por qué elegiste esa estructura.
- Qué sucede en el valor límite.
- Qué caso de prueba demuestra que funciona.

También debes poder responder una pregunta de modificación:

> ¿Qué cambiaría en tu algoritmo si modificáramos una de las reglas?

La finalidad es comprobar que comprendes tu solución y no solamente que el programa se ejecuta.

---

# Lo que debemos recordar

En esta unidad aprendimos a construir programas que seleccionan instrucciones según determinadas condiciones.

Comenzamos identificando una limitación de los programas secuenciales: podían recibir datos, realizar operaciones y mostrar resultados, pero necesitábamos decidir qué instrucciones correspondía ejecutar.

Para resolver esa dificultad incorporamos `if`.

Aprendimos que una condición produce un resultado booleano y que ese resultado determina si se ejecuta un bloque.

Después utilizamos `if...else` para seleccionar entre dos alternativas.

También estudiamos `else if`, que permite organizar varias alternativas y seleccionar la primera cuya condición sea verdadera.

Descubrimos que el orden de las condiciones es fundamental.

Una condición puede ser verdadera para ciertos datos y, sin embargo, no llegar a evaluarse porque una alternativa anterior ya fue seleccionada.

Por eso aprendimos a distinguir entre condiciones verdaderas, falsas y no evaluadas.

Estudiamos los operadores relacionales:

`>`, `<`, `>=`, `<=`, `==` y `!=`.

Aprendimos a traducir requisitos escritos en lenguaje cotidiano a condiciones Java y también a explicar en palabras condiciones que encontramos en un programa.

Después incorporamos los operadores lógicos:

`&&`, `||` y `!`.

Con ellos pudimos representar reglas que necesitan varios requisitos, alternativas o negaciones.

Comprobamos que los paréntesis pueden cambiar el significado de una expresión compuesta y que Java utiliza evaluación de cortocircuito.

También comprendimos la importancia de validar los datos antes de procesarlos.

No es lo mismo clasificar una nota que comprobar primero si pertenece al rango permitido.

Aprendimos a distinguir las alternativas excluyentes de las propiedades independientes.

Estudiamos la comparación de cadenas mediante `equals()` y conocimos la estructura `switch` para seleccionar entre valores concretos.

El problema integrador de auditoría de almacenamiento nos permitió combinar entrada de datos, validación, cálculos, condiciones y pruebas.

Pero la idea principal de esta unidad es la siguiente:

**Una estructura condicional no decide por nosotros qué es correcto. Somos nosotros quienes debemos comprender las reglas del problema y expresarlas mediante condiciones adecuadas.**

En la siguiente unidad encontraremos una nueva limitación.

Ya sabemos ejecutar instrucciones y seleccionar alternativas.

Pero ¿qué sucede cuando necesitamos repetir una operación muchas veces?

¿Tendremos que copiar las mismas instrucciones una y otra vez?

Para resolver ese problema estudiaremos las **estructuras iterativas**.

Aprenderemos a utilizar ciclos, contadores y acumuladores para construir algoritmos que repiten acciones de manera controlada.

Las condiciones seguirán siendo fundamentales, porque también nos permitirán determinar cuándo debe continuar o finalizar una repetición.
