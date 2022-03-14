#include <iostream>
long long f(int n)
{
    if (n <= 0)
        return 0;
 
    long long arr[3] = { 1, 1 };
 
    for (int i = 1; i < n; ++i)
    {
        long long S = arr[0] + arr[1] + arr[2];
        arr[2] = arr[1];
        arr[1] = arr[0];
        arr[0] = S;
    }
 
    return arr[0] + arr[1] + arr[2];
}
 
int main() 
{
    int n; 
    std::cin >> n;
    std::cout << f(n);
}