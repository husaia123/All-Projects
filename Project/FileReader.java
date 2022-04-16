import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;

/**
 * Write a description of class FileIO here.
 *
 * @author Anwarul patwary
 * @version 
 */
public class FileReader
{
    //instance variables
    private String fileName;
    private ArrayList<String> lines; 
    

    /**
     * Constructor for objects of class FileIO
     */
    public FileReader(String fileName)
    {
        // initialise instance variables
        this.fileName = fileName;
          try{ 
              FileInputStream fileStream = new FileInputStream(fileName);
              BufferedReader input = new BufferedReader(new InputStreamReader(fileStream));
              lines = new ArrayList<String>();
              
          while (input.ready()) {
              
              lines.add(input.readLine());
    
          }  
          
        }catch(Exception e) {
        System.out.println("The File" +fileName+ "could not find or error reading");
        }
  
    }
   /**
     * A method to get the input details
     * @return the number of lines from input file
     */
 
    public int totalLines(){
    return lines.size(); 
    }
    
    public ArrayList<String> getLines(){
    return lines;    
    }
    
}

