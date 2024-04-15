#include <iostream>
#include <vector>


int main() {
    // Example array
    int n=5;
    vector<int> arr;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<arr[i]; 
        } 
    } 
    return 0;
}
