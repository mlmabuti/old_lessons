import java.util.ArrayList;
//UNFINISHED
public class TimeCapsule{
        /***
         * -9 -9 -9  1 1 1 
            0 -9  0  4 3 2
           -9 -9 -9  1 2 3
            0  0  8  6 6 0
            0  0  0 -2 0 0
            0  0  1  2 4 0
         */
    
    static final byte arr[][] = {{-9,-9,-9, 1, 1, 1},
                                 { 0,-9, 0, 4, 3, 2},
                                 {-9,-9,-9, 1, 2, 3},
                                 { 0, 0, 8, 6, 6, 0},
                                 { 0, 0, 0,-2, 0, 0},
                                 { 0, 0, 1, 2, 4, 0}};

    public static void main(String[] args) {
        ArrayList<Integer> aList = new ArrayList<Integer>();
        int total = 0;
        int i;

        for( int x = 0; x < arr.length; ){
            for (i = 0; i < arr[0].length-2; i++) {
                total += (arr[i][i] + arr[i][i+1] + arr[i][i+2] + arr[i+1][i+1] + arr[i+2][i] + arr[i+2][i+1] +
                            arr[i+2][i+2]);
                aList.add(total);
                total = 0;
            }
            x++;
        }
        System.out.println(aList.toString()); 
    }
}