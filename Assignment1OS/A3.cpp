#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];
    int sum = 0;

    cout << "Enter the elements:\n";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
        sum += arr[i];
    }

    double average = (double)sum / n;
    cout << "Average: " << average << endl;

    return 0;
}
