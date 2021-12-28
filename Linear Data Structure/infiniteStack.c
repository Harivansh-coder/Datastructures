// infinite only if your memory is infinite
#include<stdio.h>
#include <malloc.h>

int size = 10;
int count = 0;


void printStack(const int *arr) {
    for (int i = 0; i < count; i++) {
        printf("%i ", *(arr + i));
    }

}

// this will add element in the stack
void push(int *arr, int val) {
    if (count < size) {
        arr[count] = val;
        count++;
    } else {
        size *= 2;
        arr = (int *) realloc(arr, size * sizeof(int));

        arr[count] = val;
        count++;
    }
}


// this will remove element from stack
void pop() {

    if (count == 0) {
        printf("Array is empty");
        return;
    }
    printf("\n");
    count -= 1;

}




int main(void) {
    int *arr = (int *) malloc(size * (sizeof(int)));

    push(arr, 1);
    push(arr, 2);
    push(arr, 3);
    push(arr, 4);
    push(arr, 5);
    push(arr, 6);
    push(arr, 7);
    push(arr, 8);
    push(arr, 9);
    push(arr, 10);

    printStack(arr);
    printf("%i",size);

    push(arr, 11);
    push(arr, 12);
    push(arr, 1);
    push(arr, 2);
    push(arr, 3);
    push(arr, 4);
    push(arr, 5);
    push(arr, 6);
    push(arr, 7);
    push(arr, 8);
    push(arr, 9);
    push(arr, 10);
    push(arr, 11);
    push(arr, 12);

    printStack(arr);
    printf("%i",size);

    pop();
    pop();
    pop();

    printStack(arr);
    printf("%i",size);




    return 0;
}


