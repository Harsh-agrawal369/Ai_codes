import java.util.*;
import java.io.*;


public class Solution_Q2 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] arr = new int[n][m];

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        int i_curr = sc.nextInt();
        int j_curr = sc.nextInt();

        int i_work = sc.nextInt();
        int j_work = sc.nextInt();

        if(i_curr>i_work || j_curr>j_work){
            System.out.print(-1);
        }

        // int i=i_curr;
        // int j=j_curr;

        int min = Integer.MAX_VALUE;

        for(int i=i_curr; i<=n; i++){
            int sum=0;
            for(int j=j_curr; j<=m; j++){
                
            }
        }



    }
    
}