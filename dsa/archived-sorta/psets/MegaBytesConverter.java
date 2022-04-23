public class MegaBytesConverter {
    public static void printMegaBytesAndKiloBytes(int kilobytes){
        if (kilobytes < 0) System.out.println("Invalid Value");
        else System.out.println(kilobytes + " KB = " + (int) kilobytes/1024 +" MB and "+ kilobytes%1024 + " KB");
    }
}
