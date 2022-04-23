import data_structures.SinglyLinkedList;

public class App {
    public static void main(String[] args) {

        SinglyLinkedList a = new SinglyLinkedList();
        a.append((byte)1);
        a.append((byte)2);
        a.append((byte)3);
        a.append((byte)4);
        a.traverse();
    }
}