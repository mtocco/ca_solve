/*
 Problem: Code Abbey 13.
 Description: calculate the weighted Sum of Digits, first by 
 multiplying each digit by its decimal position, and adding each 
 of those products together. 
 URL: https://www.codeabbey.com/index/task_view/weighted-sum-of-digits
 */
package abbey13;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Abbey13 {

    public static void main(String[] args) throws IOException {
        String data;
        String answer;
        String[] indexedData;
        data = readFileIn();
        indexedData = splitData(data);
        data = returnProblemLine(indexedData);
        answer = returnAnswer(data);
        System.out.println(answer);
    }

    public static String readFileIn() throws FileNotFoundException, IOException {
        FileReader file = new FileReader("YourTextFileHere.txt"); //<-- Hardcode input data file path here 
        BufferedReader reader = new BufferedReader(file);
        String a = "";
        String strLines;
        while ((strLines = reader.readLine()) != null) {
            a = a + strLines + ",";
        }
        return a;
    }

    public static String[] splitData(String data) {
        String[] splitData;
        splitData = data.split(",");
        return (splitData);
    }

    public static String returnProblemLine(String[] data) {
        String[] intermediate = data;
        String pLine = "";
        for ( int i = 0; i < intermediate.length; i++){
            if (i > 0){
                pLine = pLine + intermediate[i];
            }
        }
        return (pLine);
    }

    public static String returnAnswer(String data) {
        String intermediate = data; 
        String answer = "";
        String[] splitLine = intermediate.split(" ");
        for (int i = 0; i < splitLine.length; i++) {
            answer = answer + calcElementSum(splitLine[i]) + " ";
        }
        return answer;
    }

    public static String calcElementSum(String element) {
        String[] data = element.split("");
        String answer;
        int solution = 0;
        for (int i = 0; i < data.length; i++) {
            solution = solution + ((Integer.parseInt(data[i])) * (i + 1)); // Where the calculation takes place
        }
        return (String.valueOf(solution));
    }
}
