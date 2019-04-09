import java.util.*;
import java.lang.*;

class Main {
	public static void main (String[] args) throws java.lang.Exception {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine();
        Queue deque =  new LinkedList<>();
        for(int i = 0; i < n; i++) {
            String[] query = scanner.nextLine().split(" ");
            String op = query[0];
            if (op.equals("1")) {
                deque.add(query[1]);
            } else if (op.equals("2")) {
                if (deque.size() > 0) deque.remove();
            } else {
                if (deque.size() > 0) {
                    System.out.println(deque.peek());
                } else {
                    System.out.println("Empty!");
                }
            }
        }

        scanner.close();
	}
}