import java.util.ArrayList;

import java.io.*;
import java.util.*;

class MissingRepeating {
    ArrayList<Integer> al = new ArrayList<Integer>();
    int N;

    public void input()
    {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for(int i=0; i<N; i++)
        {
            al.add(sc.nextInt());
        }

        sc.close();
    }

    public void solve(ArrayList<Integer> arr)
    {
        
        float Sn = N * (N+1) / 2.0f;
        float Sa = 0.0f;
        for(int x: arr)
            Sa += x;

        float sqSn = Sn * (2*N+1) / 3.0f;
        float sqSa = 0.0f;
        for(int x: arr)
            sqSa += (float)Math.pow(x, 2);

        float R = ((sqSa - sqSn)/(Sa-Sn) + (Sa - Sn))/2.0f;
        float M = ((sqSa - sqSn)/(Sa-Sn) - (Sa - Sn))/2.0f;

        System.out.println("Missing: " + (int)M);
        System.out.println("Repeating: " + (int)R);

    }

    public static void main(String[] args) {
        MissingRepeating obj = new MissingRepeating();

        obj.input();
        obj.solve(obj.al);
    }

}
