package data_structures;

public class SinglyLinkedList{
    public Node head; // head
     public static class Node{ //Inner class
        byte data;
        public Node next;
        public Node (byte d){ //Node constructor
            data = d;
            next = null; }
    }

    //O(n) TRAVERSE
    public void traverse(){
         Node temp = head;
         while(temp != null){
             System.out.print(temp.data + " -> ");
             temp = temp.next; }
    }

    //O(1) PUSH
    public void push(byte new_data){
        Node new_node = new Node(new_data); //create new node with new data
        new_node.next = head; //make new node point to head
        head = new_node; //move head to new node
    }

    //O(1) INSERT
    public void insertAfter(Node prev_node, byte new_data){
         if (prev_node == null){ //check if previous node exists
             System.out.println("Previous node is null");
             return;
         }
         Node new_node = new Node(new_data); //create new node with new data
         new_node.next = prev_node.next; //set new node point to previous node
         prev_node.next = new_node; //set previous node point to new node
    }

    //O(1) APPEND
    public void append(byte new_data){
        Node new_node = new Node(new_data); //create new node with new data
        if (head == null){ //check if linkedList is empty
            head = new Node(new_data); //add new node to populate empty linkedList
            return;
        }
        new_node.next = null; //set new node point to null
        Node last = head; //find last node by traversing from the head
        while (last.next != null) last = last.next; //while last pointer is not null---traverse
        last.next = new_node; //change last pointer to new node;
    }

    //O(n) DELETE
    public void deleteNode(byte position){
         if (head == null) return; // check if the list is empty
         Node temp = head; // set temp (finder pointer) to head
         if (position == 0){ head = temp.next; return;} // change head to temp node to delete head
         for (int i = 0; temp != null && i < position-1; i++) temp = temp.next; // find previous node of the deleted node
         if (temp == null || temp.next == null) return; // if the  is reached
        //Node next = temp.next.next; //temp.next will be deleted
        temp.next = temp.next.next; //point the pointer to the next node of the deleted node
    }

/*
    NO HEAD DELETION
    public void delete(byte position){
         Node temp = head;
         for (int i = 0; temp != null && i < position-1; i++) {temp = temp.next;}
         if (temp == null || temp.next == null){ return;}

         temp.next = temp.next.next;
    }
*/

//    public Node reverse(Node node) {
//            Node prev = null;
//            Node current = node;
//            Node next = null;
//            while (current != null) {
//                next = current.next;
//                current.next = prev;
//                prev = current;
//                current = next;
//            }
//            node = prev;
//            return node;
//    }
}