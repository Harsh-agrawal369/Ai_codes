import java.util.*;
import java.io.*;


public class sol {

    static List<Integer> removeDuplicates(List<Integer> originalList) {
        List<Integer> lst_new = new ArrayList<>();
        HashSet<Integer> set = new HashSet<>();

        for (Integer element : originalList) {
            if (set.add(element)) {
                lst_new.add(element);
            }
        }

        return lst_new;
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
      
        
        List<Integer> lst_new = removeDuplicates(C);
        
        Map<Integer, List<Integer>> map = new HashMap<>();
        List<Integer> visit = new ArrayList<>();

        for(int i=0; i<Dstring.length; i++){
            if(map.containsKey(C.get(i))){
                float dam = (map.get(C.get(i)).get(0))/(map.get(C.get(i)).get(1));
                if(dam<(D.get(i)/S.get(i))){
                    List<Integer> lst = new ArrayList<>();
                    lst.add(D.get(i));
                    lst.add(S.get(i));

                    map.put(C.get(i),lst);
                }else{
                    continue;
                }
            }else{
                List<Integer> lst = new ArrayList<>();
                lst.add(D.get(i));
                lst.add(S.get(i));
                map.put(C.get(i), lst);
            }
        }
        // System.out.print(map.size());
        // for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
        //     System.out.println("Key = " + entry.getKey() + 
        //                      ", Value = " + entry.getValue().get(0)+ " " + entry.getValue().get(1)); 
        // }

        int maxDam =0;
        for(int i=0; i<lst_new.size(); i++){
            int Space = 0;
            int Dam = 0;

            for(int j=i; j<lst_new.size(); j++){
                Space+=map.get(lst_new.get(j)).get(1);
                if(Space<B){
                    Dam+=map.get(lst_new.get(j)).get(0);
                    // maxDam = Math.max(Dam, maxDam);
                    if(Dam>maxDam){
                        maxDam=Dam;
                        if(!visit.contains(lst_new.get(j))){
                            visit.add(lst_new.get(j));
                        }
                    }
                }else{
                    break;
                }
            }
        }

        System.out.print(maxDam);


   }
}
