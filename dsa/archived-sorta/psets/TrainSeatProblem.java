
import java.util.Scanner;

public class TrainSeatProblem {
    public void execute() {
        Scanner sc = new Scanner(System.in);

        int a = 0;
        int loopTimes = sc.nextInt();

        do {
            int seat = sc.nextInt();
            int ctr = 11;
            
            for (int i = 1; i < 13; i++) {
                for (int j = i; j <= 108; j += 12) {
                    if (seat == j) {
                        System.out.print(seat + ctr);

                        if (ctr % 9 == 0 || ctr % 3 == 0)
                            System.out.println(" MS");

                        else if (ctr % 7 == 0 || ctr % 5 == 0)
                            System.out.println(" AS");

                        else
                            System.out.println(" WS");
                    }
                }
                ctr -= 2;
            }
            a++;
        }while(a < loopTimes);
        sc.close();
    }
}
