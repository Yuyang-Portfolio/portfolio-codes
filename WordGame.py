//Import pygame library
import java.util.Scanner;
//Import random number generator
import java.util.concurrent.ThreadLocalRandom;
 
//Parent class for WordGame 
public class WordGame {
    
    //array of words used in the game
    private static final String[] words_array = new String[] {"university", "software", "hardware", "computer", "desktop", "database", "algorithm", "developer", "motherboard"};
    public static void main(String[] args) {
        WordGame wordgame = new WordGame();
        wordgame.startWordGame();
    }
 
    /*shuffles word and keeps track of original unshuffled word
      initalizes number of guesses to start counting at 0
      keeps game running if keep_playing is true
      displays message and simple instructions */
    private void startWordGame() {
        int numOfGuesses = 0;
        String originalWord = generateRandomWord();
        String shuffledWord = fetchShuffledWord(originalWord);
        boolean keep_playing = true;
	  System.out.println("Try your best to guess the word!");
	  System.out.println("Don't worry if you can't guess it right away ...");
	  System.out.println("You'll get a hint after the first wrong guess :)");	

        //loop continues until player guesses correctly
        while(keep_playing) {
        
            //displays shuffled word and adds to guess count
            System.out.println("Shuffled word: "+shuffledWord);
            numOfGuesses++;
            
            //asks user for input
            String userGuess = getUserGuessAnswer();
            
            /*checks if answer is correct
              displays message accordingly
              exits game if guessed correctly*/
            if(originalWord.equalsIgnoreCase(userGuess)) {
                System.out.println("Congratulations! The guess is correct and You found the word in "+numOfGuesses+" guesses");
                keep_playing = false;
            }else {
                System.out.println("Sorry, Wrong answer");
			System.out.println("Here's a hint!");
			System.out.println("The shuffled word is one of these: university, software, hardware, computer, desktop, database, algorithm, developer, motherboard");  }        
    }
}
    
    //gets user's guessed word from command line input
   	public String getUserGuessAnswer() {
        Scanner sn = new Scanner(System.in);
        return sn.nextLine();
    }
     
    //selects random word from given array
    public String generateRandomWord() {
        int rPos = ThreadLocalRandom.current().nextInt(0, words_array.length);
        return words_array[rPos];
    }
     
    //randomly shuffle letters 8 times
    public String fetchShuffledWord(String originalword) {
        String shuffled_Word = originalword;
        int wordLength = originalword.length();
        int shuffleCount = 8;
        for(int i = 0; i < shuffleCount; i++) {
            //swap letters in two indexes
            int position1 = ThreadLocalRandom.current().nextInt(0, wordLength);
            int position2 = ThreadLocalRandom.current().nextInt(0, wordLength);
            shuffled_Word = swap_Characters(shuffled_Word,position1,position2);
        }
        return shuffled_Word;
    }
 
    //shuffles letters by using character positions
    private String swap_Characters(String shuffled_Word, int position1, int position2) {
        char[] charArraySwap = shuffled_Word.toCharArray();
        
        char tempo = charArraySwap[position1];
        charArraySwap[position1] = charArraySwap[position2];
        charArraySwap[position2] = tempo;
        return new String(charArraySwap);
    }
}
