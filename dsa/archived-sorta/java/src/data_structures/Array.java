package data_structures;


//THESE ARE JUST ARRAY FUNCTIONS
//STILL UNDER CONSTRUCTION
public class Array {
    public static int[] append(int[] arr, int element){
        int[] newArr = new int[arr.length+1];
        for (int i = 0; i < arr.length ; i++)
            newArr[i] = arr[i];
        newArr[arr.length] = element;
        return newArr;
    }

    public static int[] remove(int[] arr, int index){
        int[] newArr = new int[arr.length-1];
        for (int i = 0, j = 0; i < arr.length-1; i++, j++) {
            if (i == index)
                newArr[i] = arr[++j];
            newArr[i] = arr[j];
        }
        return newArr;
    }

    public static void traverse(int[] arr) {
        for (int i = 0; i < arr.length; i++)
            System.out.print(arr[i] + " ");
    }

    //binary search to be added.
    public static int linearSearch(int[] arr, int element){
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == element)
                return i;
        }
        return -1;
    }
}
