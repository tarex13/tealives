import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cont = 0;
        String name1;
        String name2;
        String name3;
        String xString = "";
        String yString = "";
        String gString = "";

        int X = input.nextInt();
        String[] x = new String[X];
        if(X != 0){
            input.nextLine();
            for (int i = 0; i < X; i++) {
                
                x[i] = input.nextLine();
            }
            xString = Arrays.toString(x).replace("[", "").replace("]", "").replaceAll(",", "");
        }
            int Y = input.nextInt();
            String[] y = new String[Y];
        if(Y != 0){
            input.nextLine();
            for (int i = 0; i < Y; i++) {
                y[i] = input.nextLine();
            }
            yString = Arrays.toString(y).replace("[", "").replace("]", "").replaceAll(",", "");
        }
        int G = input.nextInt();
        String[] g = new String[G];
        input.nextLine();

        for (int i = 0; i < G; i++) {
            g[i] = input.nextLine();
            if(X > 0){
                if (g[i].contains(xString.split(" ")[0])) {
                    if (!(g[i].contains(xString.split(" ")[1]))) {
                        cont++;
                    }
                }else if(g[i].contains(xString.split(" ")[1])){
                    if (!(g[i].contains(xString.split(" ")[0]))) {
                        cont++;
                    }
                }
            }
            if(Y > 0){
                if (g[i].contains(yString.split(" ")[0]) ) {
                    if ((g[i].contains(yString.split(" ")[1]))) {
                        cont++;
                    }
                }else if(g[i].contains(yString.split(" ")[1])){
                    if ((g[i].contains(yString.split(" ")[0]))) {
                        cont++;
                    }
                }
                
            }
        }
        System.out.println(cont);
    }
}