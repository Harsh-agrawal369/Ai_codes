import java.util.*;
import java.io.*;


public class SolutionD {

    public static int maximizePower(List<Integer> D, List<Integer> S, List<Integer> C, int B){
        List<List<Integer>> lst = new ArrayList<>();
        for(int i=0; i<D.size(); i++){
            List<Integer> lst1 = new ArrayList<>();
            lst1.add(D.get(i));
            lst1.add(S.get(i));
            lst1.add(C.get(i));
            lst.add(lst1);
        }

        Collections.sort(lst, Comparator.comparing((List<Integer> lst1) -> lst1.get(0)).reversed());

        List<List<Integer>> selected = new ArrayList<>();
        int space=0;

        for(List<Integer> li : lst){
            if(space + li.get(1) <= B){
                selected.add(li);
                space+=li.get(1);
            }
        }
        
        int max=0;
        for(List<Integer> li : selected){
            max+=li.get(0);
        }
       


        return max;

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
       
        List<Integer> D = new ArrayList<>();
        List<Integer> S = new ArrayList<>();
        List<Integer> C = new ArrayList<>();

        String[] Dstring = sc.nextLine().split(" ");
        String[] Sstring = sc.nextLine().split(" ");
        String[] Cstring = sc.nextLine().split(" ");

        for(int i=0; i<Dstring.length; i++){
            D.add(Integer.parseInt(Dstring[i]));
            S.add(Integer.parseInt(Sstring[i]));
            C.add(Integer.parseInt(Cstring[i]));
        }

        int B = sc.nextInt();

        System.out.print(maximizePower(D, S, C, B));


   }
}
