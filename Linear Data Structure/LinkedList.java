//Main linkedlist class
public class LinkedList {
   
    Node head; 
   
    static class Node {
   
        int data;
        Node next;
   

        Node(int d){
            data = d;
            next = null;
    }


}

//insert function implemented 
public static LinkedList insert(LinkedList list, int data){
    
    Node new_node = new Node(data);
    new_node.next = null;
   
    
    if (list.head == null) {
        list.head = new_node;
    }
    else {
        Node last = list.head;
        while (last.next != null) {
            last = last.next;
        }
        last.next = new_node;
    }
   
    return list;
}
   

// for printing the linkedlist
public static void printList(LinkedList list){
    Node node = list.head;
    
    System.out.print("LinkedList: ");

    while (node != null) {
            
        System.out.print(node.data +" ");

        node = node.next;
    }

}



    
//main funtion
public static void main(String[] args){
    //linkedlist object created
    LinkedList list = new LinkedList();
   
   
    // Inserting values in the linkedlist
        
    list = insert(list, 14);
    list = insert(list, 52);
    list = insert(list, 6);
    list = insert(list, 21);
    list = insert(list, 2);
    list = insert(list, 53);
    list = insert(list, 7);
    list = insert(list, 8);
   
    printList(list);

    }
}


/*
Output:

LinkedList: 14 52 6 21 2 53 7 8 

*/
