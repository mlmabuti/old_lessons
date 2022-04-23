import java.util.ArrayDeque;
import java.util.Queue;
 
class Pair // just a class for coordinates / positions
{           
    int x, y;
 
    public Pair(int x, int y) // a constructor which basically means everytime you create a pair
                            // there will be an x and a y value
    {
        this.x = x;
        this.y = y;
    }

    public String get_xy(){
        return this.x + " " + this.y;
    }

}
 
class Main
{
    // Below arrays detail all eight possible movements from a cell
    // (top, right, bottom, left, and four diagonal moves)
    private static final int[] row = { -1, -1, -1, 0, 1, 0, 1, 1 };
    private static final int[] col = { -1,  1,  0,-1,-1, 1, 0, 1 };
 
    // Function to check if it is safe to go to position (x, y)
    // from the current position. The function returns false if (x, y)
    // is not valid matrix coordinates or (x, y) represents water or
    // position (x, y) is already processed
 
    public static boolean isSafe(int[][] mat, int x, int y, boolean[][] processed)
    {
        return (x >= 0 && x < processed.length) && (y >= 0 && y < processed[0].length) // x must be in range of the matrix
                && mat[x][y] == 1 // current position must be 1, not water
                && !processed[x][y]; // current position must not exist in processed
    }
 
    public static void BFS(int[][] mat, boolean[][] processed, int i, int j)
    {
        // create an empty queue and enqueue source node
        Queue<Pair> q = new ArrayDeque<>(); // just a queue instance
        q.add(new Pair(i, j)); // create a new pair of the current position (x,y) and sotre in queue
 
        // mark source node as processed
        processed[i][j] = true; // change current position in processed from null to true
        
        // loop till queue is empty

        while (!q.isEmpty())
        {
            // dequeue front node and process it
            int x = q.peek().x; // will first be 0 
            int y = q.peek().y; // also 0 because this is the 1 / first element in matrix

            System.out.print(x);
            System.out.print(" ");
            System.out.print(y+"\n");

            q.poll();
 
            // check for all eight possible movements from the current cell
            // and enqueue each valid movement
            for (int k = 0; k < row.length; k++)
            {
                // skip if the location is invalid, or already processed, or has water
                if (isSafe(mat, x + row[k], y + col[k], processed)) // x+row[k] and y+col[k] means to move in directions
                {
                    // skip if the location is invalid, or it is already
                    // processed, or consists of water
                    processed[x + row[k]][y + col[k]] = true; // change the current position to visited/processed
                    q.add(new Pair(x + row[k], y + col[k])); // since the next position is safe, enqueue the next Pair
                                                            // notice that the program will keep eneueueing a pair until
                                                            // there are no valid moves anymore
                                                            // and each pair added will search for the next valid move
                                                            // each valid moves will mark the spot visited/processed
                }
            }
        }
    }
 
    public static int countIslands(int[][] mat) // this will be the acutal main function
    {
        // base case will stop program if matrix is empty
        if (mat == null || mat.length == 0) {
            return 0;
        }
 
        // `M × N` matrix
        int M = mat.length; // for rows
        int N = mat[0].length; // for cols
 
        // stores if a cell is processed or not
        boolean[][] processed = new boolean[M][N]; // create matrix with same dimensions but with null values
 
        int island = 0;
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                // start BFS from each unprocessed node and
                // increment island count
                if (mat[i][j] == 1 && !processed[i][j])
                {
                    BFS(mat, processed, i, j); // refer to BFS 
                    island++; // increment count after running BFS
                }
            }
        }
 
        return island; // finally return the count
    }
 
    public static void main(String[] args)
    {
        int[][] mat=
                {
                        { 1, 0, 1},
                         { 0, 0, 1 },
                         { 1, 1, 1} };

//        int [][] mat = {
//            {1,1,0,0},
//            {1,0,0,1},
//            {0,0,1,1}};
//

        Queue<Pair> a = new ArrayDeque<>();

        a.add(new Pair(1,1));
        a.add(new Pair(0,1));
        a.add(new Pair(0,2));
        a.add(new Pair(1,3));

        for (Pair i : a){
            System.out.print(i.get_xy());
            System.out.print(" ");
            System.out.println();
        }

        System.out.println("The total number of islands is " + countIslands(mat));
    }
}