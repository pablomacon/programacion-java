# Unidad 5 — Arreglos y cadenas de caracteres: conservar, recorrer y organizar datos

**Programación I — 2026**  
**Estado:** reconstrucción editorial de la versión definitiva revisada; no transcripción literal.

## 1. ¿Por qué arreglos?

Con `Scanner` y un ciclo podemos leer cinco notas y acumularlas, pero al finalizar no conservamos cada nota individual. Cinco variables `nota1 ... nota5` funcionan con pocos datos, pero no escalan. Un arreglo permite conservar valores del mismo tipo bajo un nombre común.

```java
int[] notas = {7, 5, 8, 6, 9};
```

## 2. Índice, valor y longitud

| Índice | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Valor | 7 | 5 | 8 | 6 | 9 |

`notas[2]` vale 8. El **índice** es una posición; no debe confundirse con el **valor** almacenado. La longitud es `notas.length`, que vale 5. El último índice es `length - 1`.

```java
int[] numeros = {4, 8, 12, 16};
int i = 2;
System.out.println(numeros[i]); // 12
i = 3;
System.out.println(numeros[i]); // 16
```

Cambió el índice utilizado para consultar; el arreglo no cambió.

## 3. Crear y cargar

```java
int[] notas = new int[5];
```

Un arreglo nuevo de enteros contiene inicialmente ceros. La longitud queda fija al crearlo. Carga mediante `Scanner` y `for`:

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int[] notas = new int[5];
        for (int i = 0; i < notas.length; i++) {
            System.out.print("Ingrese la nota " + (i + 1) + ": ");
            notas[i] = teclado.nextInt();
        }
        teclado.close();
    }
}
```

Mostramos `i+1` al usuario; almacenamos en `notas[i]`.

## 4. Recorrer y modificar

```java
int[] numeros = {2, 4, 6};
for (int i = 0; i < numeros.length; i++) {
    numeros[i] = numeros[i] + 1;
}
// 3, 5, 7
```

El ciclo modifica `i`, y `i` determina el elemento utilizado. En un recorrido desde cero con `i < length`, para tres elementos se hacen tres iteraciones y cuatro verificaciones de condición. `i <= length` intentaría acceder al índice inexistente `length`.

## 5. Procesar: sumar y contar

```java
int[] notas = {7, 5, 8, 6, 9};
int suma = 0, aprobados = 0;
for (int i = 0; i < notas.length; i++) {
    suma += notas[i];
    if (notas[i] >= 6) aprobados++;
}
double promedio = suma * 1.0 / notas.length;
```

Resultados: suma 35, promedio 7, aprobados 4. Inicializar acumuladores y contadores **antes** del recorrido. Comprobar longitud positiva antes de dividir si el arreglo pudiera estar vacío.

## 6. Mayor y menor

```java
int mayor = notas[0];
for (int i = 1; i < notas.length; i++) {
    if (notas[i] > mayor) mayor = notas[i];
}
```

Inicializar con el primer elemento, no automáticamente en cero: para `{-7,-3,-9}` el máximo real es -3. Esta técnica requiere un arreglo no vacío. El menor se obtiene cambiando `>` por `<`.

## 7. Búsqueda lineal: tres necesidades distintas

**Existe:** guardar un `boolean` que cambia a `true` cuando se encuentra el dato.

```java
boolean encontrado = false;
for (int i = 0; i < notas.length; i++) {
    if (notas[i] == 8) encontrado = true;
}
```

**Primera posición:** usar `-1` para representar 'no encontrado'.

```java
int posicion = -1;
for (int i = 0; i < notas.length; i++) {
    if (notas[i] == 8 && posicion == -1) posicion = i;
}
```

**Cantidad de apariciones:** incrementar un contador en **todas** las coincidencias.

```java
int cantidad = 0;
for (int i = 0; i < notas.length; i++) {
    if (notas[i] == 8) cantidad++;
}
```

Como ampliación, `while (i < notas.length && !encontrado)` permite detenerse en la primera coincidencia. Elegir algoritmo según pregunta, no por receta.

## 8. Ordenamiento por burbuja

Primero intercambiamos dos valores sin perderlos:

```java
int auxiliar = numeros[i];
numeros[i] = numeros[i + 1];
numeros[i + 1] = auxiliar;
```

Comparamos vecinos y cambiamos cuando `numeros[i] > numeros[i+1]`. Una pasada no siempre ordena todo. Para `7,5,8,6,9`, tras la primera pasada queda `5,7,6,8,9`; tras la segunda `5,6,7,8,9`.

**Versión inicial, límite interior fijo:**

```java
for (int pasada = 0; pasada < numeros.length - 1; pasada++) {
    for (int i = 0; i < numeros.length - 1; i++) {
        if (numeros[i] > numeros[i + 1]) {
            int aux = numeros[i];
            numeros[i] = numeros[i + 1];
            numeros[i + 1] = aux;
        }
    }
}
```

**Mejora:** el límite interior `i < numeros.length - 1 - pasada` evita comparar partes ya acomodadas al final. Explicar primero las pasadas y luego los ciclos anidados; no memorizar encabezados. Casos: ascendente, descendente, repetidos y todos iguales.

## 9. Cadenas `String`

Una cadena no es lo mismo que un arreglo `char[]`, pero podemos examinar sus posiciones:

```java
String palabra = "JAVA";
System.out.println(palabra.length());  // 4
System.out.println(palabra.charAt(2)); // V
```

En arreglos se utiliza `.length`; en cadenas `.length()`. Para contar letras:

```java
int cantidadA = 0;
for (int i = 0; i < palabra.length(); i++) {
    if (palabra.charAt(i) == 'A') cantidadA++;
}
```

`equals()` compara el contenido de cadenas, `equalsIgnoreCase()` ignora mayúsculas/minúsculas. `toUpperCase()` produce una nueva cadena; para conservarla: `palabra = palabra.toUpperCase();`. `substring()` e `indexOf()` quedan como referencias complementarias, no como eje.

## 10. Problema completo: carga, procesamiento y consulta

El registro de cinco notas se divide en tres momentos: cargar mediante `Scanner`, recorrer para suma/aprobados/máximo y consultar si un valor existe. Recuperamos variables, condiciones, ciclos y arreglos.

### Pseudocódigo

```text
CREAR notas[5]
PARA i desde 0 hasta 4: LEER notas[i]
suma <- 0; aprobados <- 0; mayor <- notas[0]
PARA i desde 0 hasta 4:
    suma <- suma + notas[i]
    SI notas[i] >= 6: aprobados <- aprobados + 1
    SI notas[i] > mayor: mayor <- notas[i]
promedio <- suma * 1.0 / 5
MOSTRAR promedio, aprobados, mayor
LEER buscado
encontrado <- FALSO
PARA cada nota: SI coincide, encontrado <- VERDADERO
MOSTRAR resultado de la búsqueda
```

### Java integrado

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        int[] notas = new int[5];
        for (int i = 0; i < notas.length; i++) {
            System.out.print("Nota " + (i + 1) + ": ");
            notas[i] = teclado.nextInt();
        }
        int suma = 0, aprobados = 0, mayor = notas[0];
        for (int i = 0; i < notas.length; i++) {
            suma += notas[i];
            if (notas[i] >= 6) aprobados++;
            if (notas[i] > mayor) mayor = notas[i];
        }
        System.out.println("Promedio: " + suma * 1.0 / notas.length);
        System.out.println("Aprobados: " + aprobados);
        System.out.println("Mayor: " + mayor);
        System.out.print("Buscar: ");
        int buscado = teclado.nextInt();
        boolean encontrado = false;
        for (int i = 0; i < notas.length; i++) {
            if (notas[i] == buscado) encontrado = true;
        }
        System.out.println(encontrado ? "Encontrado" : "No encontrado");
        teclado.close();
    }
}
```

## 11. Errores frecuentes

Índice fuera de rango; confundir índice con valor; poner `<= length`; reiniciar acumulador; inicializar máximo en 0 sin considerar negativos; intercambiar valores sin auxiliar; usar `length` de arreglo como si fuera `length()` de `String`; usar `==` para comparar el contenido de cadenas.

## 12. Evaluación de comprensión

Predecir salida de accesos por índice; trazar suma; corregir bucle; contar coincidencias; seguir una pasada de burbuja; recorrer `String`; diseñar un registro de temperaturas.

### Casos mínimos

| Datos | Esperado |
|---|---|
| 7,5,8,6,9 | promedio 7; aprobados 4; mayor 9 |
| 6,6,6,6,6 | promedio 6; aprobados 5 |
| 1,2,3,4,5 | promedio 3; aprobados 0 |
| 10,9,8,7,6 | promedio 8; mayor 10 |
| Buscar 8 en 8,5,8,6,8 | 3 apariciones |

**Puente:** los algoritmos para arreglos podrán organizarse en métodos en la Unidad 6.
