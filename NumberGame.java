import java.util.*;

public class NumberGame {
    public static void main(String[] args) {
        char playAgain;

        do {
            Random rand = new Random();
            int rNum = rand.nextInt(100) + 1;
            int uGuess = 0;
            int numGuess = 0;
            Scanner s = new Scanner(System.in);

            do {
                System.out.println("Enter your Guess(1-100): ");
                try {
                    uGuess = s.nextInt();
                } catch (InputMismatchException e) {
                    System.out.println("Invalid input! Please enter a number between 1 and 100.");
                    s.nextLine();
                    continue;
                }
                if (uGuess < 1 || uGuess > 100) {
                    System.out.println("Number out of range!");
                    continue;
                }
                numGuess++;
                if (uGuess == rNum) {
                    System.out.println("Correct!!!");
                } else if (uGuess > rNum) {
                    System.out.println("Number is less than " + uGuess);
                } else if (uGuess < rNum) {
                    System.out.println("Number is greater than " + uGuess);
                }
            } while (uGuess != rNum);

            System.out.println("Number of Guesses: " + numGuess);
            System.out.println("Play Again? (Y/N): ");
            playAgain = s.next().charAt(0);
            s.close();
        } while (playAgain == 'y' || playAgain == 'Y');
    }
}