public class GroupSum{
  public static boolean groupSum(int start, int[] arr, int target){
        if (start >= arr.length) return target==0;
        if (groupSum(1+start ,arr, target - arr[start])) return true;
        if (groupSum(1+start ,arr, target)) return true;
        return false;
    }
}
