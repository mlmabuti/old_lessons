package sorting_algorithms;

import java.util.Arrays;

public class MergeSort {
    private static void merge(int[] arr, int low, int mid, int high) {
        // create temporary arrays
        int[] leftArray = new int[mid - low + 1];
        int[] rightArray = new int[high - mid];

        // copy the elements in to create sub array

        // copy for the left sub-array
        for (int i = 0; i < leftArray.length; i++)
            leftArray[i] = arr[low + i];

        // copy for the right sub-array
        for (int j = 0; j < rightArray.length; j++)
            rightArray[j] = arr[mid + j + 1];

        // now merge and sort the sub-arrays into the main-array
        int i = 0, j = 0, k = low;
        while (i < leftArray.length && j < rightArray.length) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            } else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        // to make sure none of the elements are missed out
        // for the left array
        while (i < leftArray.length) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }
        // for the right array
        while (j < rightArray.length) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }
    }

    static void mergeSort(int[] arr, int low, int high) {
        // base case, when the two pointers meet
        if (low < high) {
            // find the middle of the array
            int mid = (low + high) / 2;

            // pass in the left partition
            mergeSort(arr, low, mid);
            // pass in the right partition            mergeSort(arr, mid + 1, high);
            // merge the both sorted partitions
            merge(arr, low, mid, high);
        }
    }

}
