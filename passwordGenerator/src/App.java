import java.util.Random;
import java.io.Console;

public class App {
    public static void main(String[] args) throws Exception {
        Integer[] intarray = new Integer[32-5];
        for(int i = 0; i <= 26; i++) {
            intarray[i] = i + 6;
        }
        String req11 = "";
        for(int i : intarray) {
            req11 = req11 + String.valueOf(i) + "Д";
        }
        String req1 = removeLastChar(req11);
        int length = Integer.parseInt(ask("What is the length of the password? (6 to 32): ", req1, "6 to 32"));
        String inclNum = ask("Do we include numbers? (y/n): ", "yДn", "y/n");
        String inclChar = ask("Do we include characters? (y/n): ", "yДn", "y/n");
        
        char[] charList = new char["abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+';:\\|/,.1234567890".length()];
        if(inclNum.equals("n") && inclChar.equals("n")) {
            charList = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        } 
        if(inclNum.equals("y") && inclChar.equals("n")) {
            charList = "abcdefghijklmnopqrstuvwxyz1234567890".toCharArray();
        }
        if(inclNum.equals("n") && inclChar.equals("y")) {
            charList = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+';:\\|/,.".toCharArray();
        }
        if(inclNum.equals("y") && inclChar.equals("y")) {
            charList = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+';:\\|/,.1234567890".toCharArray();
        }

        String pass = "";
        int capitlztn = 0;
        Random rand = new Random();
        System.out.println();
        for(int i = 0; i < length; i++) {
            capitlztn = rand.nextInt(2);
            switch (capitlztn) {
                case 0:
                    pass = pass + String.valueOf(charList[rand.nextInt(charList.length)]);
                    break;
                case 1:
                    pass = pass + String.valueOf(charList[rand.nextInt(charList.length)]).toUpperCase();
                    break;
                default:
                    pass = pass + String.valueOf(charList[rand.nextInt(charList.length)]);
                    break;    
            }
        }
        
        System.out.println("Generated password: ");
        System.out.println(pass);
    }

    public static String ask(String str, String reqstr, String thatsnot) {
        int done = 0;
        String[] reqs = reqstr.split("Д");
        Console console = System.console();
        String s = "";
        boolean inthere = false;
        while(done == 0) {
            s = console.readLine(str);
            for(String i : reqs) {
                if(i.equals(s)) {
                    inthere = true;
                }
            }
            if(inthere == true) {
                done = 1;
                break;
            } else {
                System.out.println("That's not " + thatsnot + "!");
            }
        }
        return s;
    }

    public static String removeLastChar(String str) {
        if (str != null && str.length() > 0) {
            str = str.substring(0, str.length() - 1);
        }
        return str;
    }
}
