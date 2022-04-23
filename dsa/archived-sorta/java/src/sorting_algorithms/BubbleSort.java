package sorting_algorithms;


public class BubbleSort {

    public static int[] bubbleSort(int[] arr){
        int temp;
        for(int i = arr.length; i > 0; i--)
            for (int j = 0; j < i-1; j++) {
                if(arr[j] > arr[j+1]){
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        return arr;
    }
}
