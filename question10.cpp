using System;

public class Fibonacci
{
    public static int FibonacciNumber(int n)
    {
        if (n < 0)
        {
            throw new ArgumentException("Input must be non-negative");
        }
        if (n == 0) return 0;
        if (n == 1) return 1;
        int a = 0, b = 1;
        int c = 0;
        for (int i = 2; i <= n; i++)
        {
            c = a + b;
            a = b;
            b = c;
        }
        return fib;
    }
    
    public static void Main()
    {
        Console.WriteLine("Fibonacci of 10 is: " + FibonacciNumber(10));
    }
}