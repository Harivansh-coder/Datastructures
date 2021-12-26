// infinite only if your memory is infinite

#include<stdio.h>
#include <malloc.h>

int size = 10;
int count = 0;

// this will add element in the stack
void push(int *arr, int val){
    if (count < size){
        printf("normal");
        *(arr + count) = val;
        count++;
    } else{
        printf("hhh");

        size *= 2*size;
        int *arrNew = (int *)realloc(arr,size* sizeof(int));
        for (int i = 0; i < count; i ++){
            *(arrNew + i) = *(arr + i);
        }

        arr = arrNew;

    }



}

// this will remove element from stack
void pop(){
    if (count == 0){
        printf("Array is empty");
        return;
    }
    count -= 1;

}


void printStack(const int *arr){
    for (int i = 0; i < count; i ++){
        printf("%i ",*(arr + i));
    }

}


int main(void)
{
    int *arr = (int *) malloc(size*(sizeof(int)));


    push(arr, 5);
    push(arr, 6);
    push(arr, 7);
    push(arr, 8);
    push(arr, 9);
    push(arr, 10);
    push(arr, 5);
    push(arr, 6);
    push(arr, 7);
    push(arr, 8);
    push(arr, 9);
    push(arr, 10);


    printStack(arr);



    return 0;
}


