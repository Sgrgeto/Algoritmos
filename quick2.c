#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int divide_array(int *array, int size);
void print_array(int *array, int size);
int quicksort(int *array, int size);

int main(){
    srand(time(NULL));
    int * array;
    int * pointer;
    int i = 0;
    int size_array = 10000000;
    //Creamos el arreglo con numero aleatorios, si no hay memoria, no se crea el arreglo(improbable), estas lineas de codigo las saque de la pagina de IBM, se ven chulas
    if ( (array = (int *) malloc( size_array * sizeof( int ))) != NULL )
    {
     for ( pointer = array, i = 0; i < size_array ; ++i ) 
            *pointer++ =rand()%size_array;
    }
        else { /*  malloc error  */
    perror( "Out of storage" );
    abort();
        }
    double inicio =  clock();
    quicksort(array,size_array);
    double fin =clock();
	printf(" %10f\n ",((fin-inicio)/CLOCKS_PER_SEC));

    }

void print_array( int  * ptr_array, int size )
{
  int i;
  printf("The array of size %d is:\n", size);
  printf("[ ");
  for ( i = 0; i < size; ++i ){
           /* print the array out    */
    printf( " %i,", ptr_array[i] );
  }
  printf(" ] \n");
}

int quicksort(int *array, int size)
/*Lo chido de esta funcion, es que no creamos arreglos, nos vamos desplazando sobre el y hacemos las funciones solo apuntando a las direcciones de memoria*/
{
    int * pointer = array;/*El pointer es el q va a recorrer todo el arreglo, como nuestro contador*/
    int * pivot = &array[size-1];/*El pivote va a ser el ultimo numero de nuestro arreglo*/
    int * right = &array[size];/*este apuntador nos va decir la posicion de memoria del numero mayor a nuestro pivote, despues de las particiones*/
    int * left = &array[size-size];/*este apuntador no sirve de casi nada, solo es para marcar la posicion de memoria menor a nuestro pivote(no sirve de mucho ya con el contador size_left, podemos saber la posicion final antes de nuestro pivote)*/
    int * pequeño = array;/*este apuntador va a servir para hacer referencia a la posicion de memoria de nuestro ultimo numero pequeño para hacer el swap de numeros pequeños y gradnes de nuestro pivote*/
    int size_left = 0;/*contador para saber cual es nuestro tamaño de arreglo de numeros pequeños*/
    int size_right = 0;/*contador para saber cual es nuestro tamaño de arreglo de numeros grandes*/
    if (size<=1)
    {
        return *array; /*si ya no hay mas particiones regresamos el numero dentro del array*/
    }
    else{
    do
    {
        if (*pointer<=  *pivot){/*comparacion si es menor el numero dentro de nuestro pointer del numero de nuestro pivote */
            int tmp = *pequeño;/*variable para almacenar el numero que esta adentro de pequeño*/
            *pequeño=*pointer;/*el numero que esta en pointer lo pasamos a la direccion de memoria en pequeño*/
            *pointer = tmp;/*el numero que estaba en tmp lo pasamos a pointer*/
            left++;/*aumentama la posicion de memoria de left*/
            size_left++;/*aumenta el tamaño del arreglo de numeros pequeños*/
            pequeño++;/*aumenta la posicion para hacer el nuevo swap*/
        }
        else{
            right--;/*cambia la posicion de inicio del arreglo de numeros mayores*/
            size_right++;/*amuenta el tamño del arreglo de numeros grandes*/
        }
        pointer++;/*avanza a la sig locacion de memoria*/
    } while ((size_right+size_left)<size);/*para saber si recorrimos todo el arreglo sumamos los dos tamaños de los arreglos*/
    if((size_left == 0|| size_right ==0))/*CASO ESPECIAL, hay situaciones donde nuestro pivote es el más grande por lo que no hay arreglo del lado derecho, en ese caso cambiamos la posicion de nuestro pivote*/
        {
            pivot = &array[size-2];
        }
    }
    return quicksort(array,size_left-1), quicksort(right, (size_right));/*Se llama a la funcion pero con los nuevos valores, [array(inicio del arrgelo), (size_left-1)(tamaño del arreglo antes del pivote)][right(posicion de inicio del array despues de nuestro pivote),size_right(tamaño de nuestro array de numeros grandes)]*/
}

