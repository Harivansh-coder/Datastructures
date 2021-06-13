/*Array implementation in java*/

class array{

    private int[] arr;
    private int size = 10;
    private int len = 0;

    
    
    array(){
        arr = new int[size];
        
    }

    //Insert function
    public void insert(int val){
        if (len == size){
            var temp = new int[2*size];
            for (int i = 0; i < len-1;i++){
                temp[i] = arr[i];
            }
            arr = temp;
        }
        arr[len] = val;
        len++;
    }

    
    public int lengthArr(){
        return len;
    }

    //remove funtion take index of element as input
    public void removeAt(int e){
        int i;
        for (i = e;i < len-1;i++){
            arr[i] = arr[i+1];
        }
        arr[i] = 0;
        len--;

    }

    public int getItem(int e){
        return arr[e];
    }

    //Returns the parameter element index  
    public int indexOf(int val){
        for (int i = 0; i < len;i++){
            if (arr[i] == val){
                return i;
            }
        }
        return -1;
    }

    public void printArr(){
        System.out.print("[ ");
        for (int i = 0; i < len; i++){
            System.out.print(arr[i]+" ");
        }
        System.out.print("]\n");
    }

    public static void main(String[] args) {
        var arr = new array();

        arr.insert(10);
        arr.insert(20);
        arr.insert(50);
        arr.insert(40);
        arr.insert(30);
        arr.insert(10);
        arr.insert(20);
        arr.insert(50);
        arr.insert(40);
        arr.insert(30);
        arr.insert(30);
        arr.insert(30);

        System.out.print(arr.getItem(6)+"\n");
        
        arr.printArr();
        System.out.print(arr.lengthArr()+"\n");
        arr.removeAt(5);
        System.out.print(arr.indexOf(50)+"\n");
        arr.printArr();

        System.out.print(arr.indexOf(30)+"\n");

    }
}

/*

Output:

20
[ 10 20 50 40 30 10 20 50 40 0 30 30 ]
12
2
[ 10 20 50 40 30 20 50 40 0 30 30 ]
4

*/ 