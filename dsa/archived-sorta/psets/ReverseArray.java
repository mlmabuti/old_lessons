

import java.util.Scanner;

public class ReverseArray {
    public void execute(){
        Scanner sc = new Scanner(System.in);
        int arraySize= sc.nextInt();

        int[] array = new int[arraySize];

        for(int i = 0; i < arraySize ; i++)
            array[i] = sc.nextInt();

        for(int j = arraySize-1; j >= 0; j--)
            System.out.println(array[j]);

        sc.close();
    }
}

