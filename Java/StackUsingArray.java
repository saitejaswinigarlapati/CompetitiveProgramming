class Stack {
    private int[] arr;
    private int top;
    private int capacity;

    // Constructor
    public Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;  // stack is empty
    }

    // Push an element into the stack
    public void push(int x) {
        if (isFull()) {
            System.out.println("Stack Overflow! Cannot push " + x);
            return;
        }
        arr[++top] = x;
    }

    // Pop an element from the stack
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack Underflow! No element to pop.");
            return -1;
        }
        return arr[top--];
    }

    // Peek (see top element)
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty.");
            return -1;
        }
        return arr[top];
    }

    // Check if stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Check if stack is full
    public boolean isFull() {
        return top == capacity - 1;
    }

    // Get size of stack
    public int size() {
        return top + 1;
    }
}

public class StackUsingArray {
    public static void main(String[] args) {
        Stack stack = new Stack(5);

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println("Top element is: " + stack.peek());
        System.out.println("Stack size is: " + stack.size());

        System.out.println("Popped element: " + stack.pop());
        System.out.println("Top element after pop: " + stack.peek());
    }
}
