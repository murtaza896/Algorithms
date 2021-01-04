import java.io.*;
import java.util.*;

class Solution
{
    ArrayList<Integer> al = new ArrayList<Integer>();

    public void input()
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=0; i<n; i++)
        {
            al.add(sc.nextInt());
        }

        sc.close();
    }

    public void solve(ArrayList<Integer> arr)
    {
        int tot_1 = arr.get(0);

        ArrayList<Integer> maxL = new ArrayList<Integer>(Collections.nCopies(arr.size(), 0));
        maxL.set(0, arr.get(0));
        for(int i=1; i<arr.size(); i++)
        {
            if(arr.get(i) == 0) {
                continue;
            }
            else {
                tot_1 += 1;
                maxL.set(i, maxL.get(i-1) + 1);
            }
        }

        ArrayList<Integer> maxR = new ArrayList<Integer>(Collections.nCopies(arr.size(), 0));
        maxR.set(arr.size()-1, arr.get(arr.size()-1));
        
        for(int i=arr.size() - 2; i>=0; i--)
        {
            if(arr.get(i) == 0) {
                continue;
            }
            else {
                maxR.set(i, maxR.get(i+1) + 1);
            }
        }

        System.out.println(maxL);
        System.out.println(maxR);

        int maxLen = -1;

        for(int i=1; i<arr.size()-1; i++)
        {
            int L = maxL.get(i-1);
            int R = maxR.get(i+1);
            
            if(arr.get(i) == 0)
            {
                if(L+R == tot_1)
                    maxLen = Math.max(maxLen, L+R);
                else 
                    maxLen = Math.max(maxLen, L+R+1);
            }
        }

        if(maxLen == -1)
            System.out.println(tot_1);
        else
            System.out.println(maxLen);
    }

    public static void main(String args[]) {
        Solution obj = new Solution();
        obj.input();
        obj.solve(obj.al);
    }
}