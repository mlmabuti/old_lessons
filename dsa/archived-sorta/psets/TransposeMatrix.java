
import java.util.Scanner;

public class TransposeMatrix {

    public void execute(){

        Scanner sc = new Scanner(System.in);

        int arrRows = sc.nextInt();
        int arrCols = sc.nextInt();

        sc.close();

        int[][] array = new int[arrRows][arrCols];

        for(int i = 0; i < arrRows; i++){
            for(int j = 0; j < arrCols ; j++)
                array[i][j] = sc.nextInt();
        }

        for(int i = 0; i < arrCols; i++){
            for(int j = 0; j < arrRows; j++)
                System.out.print(array[j][i] + " ");
            System.out.println();
        }
    } 
}
