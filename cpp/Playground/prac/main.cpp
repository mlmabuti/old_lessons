#include <iostream>
#include <stdio.h>
#include <set>

using namespace std;


int f(int n){
	if (n == 1){
		return n;
	}
	return n*f(n-1);
}

int a(int n){
	if (n==1){
		return n;
	}
	return n+a(n-1);
}

int x(int n){
	if (n == 0){
		return n;
	}

	if (n < 3 ){
		return 1;
	}
	return x(n-1)+x(n-2);
}

void prec(){
	int a{}; 
    double b{0.0};
    string c{};
    cin >> a;
    cin >> b;
    
	// getting string input.
    getline(cin >> ws, c);
    
    cout << a+b << endl;

	// setting float precision.
    //cout << fixed << setprecision(1) << b+b << endl;
    printf("%.1f",b+b);
}


int main(){
	int arr[] {1,2,3,4,5};

	cout << sizeof(arr) << endl;

	cout << sizeof(arr)/sizeof(arr[0]) << endl;
}

