/** 
 try using int instead of size_t. THIS WORKS as long as arrSize is casted to int
 use size instead of sizeof. untested
 try to determine array size from inside the function. DOES NOT WORK
**/

#include <set>
#include <iostream>
#include <stdio.h>

using namespace std;


//void printPair(int arr[], size_t arrSize, int target){
void printPair(int arr[], unsigned int arrSize, int target){

	// linear time, O(n), does not take account for duplicate pair numbers
    //for(size_t i {0}, j {i+1}; i < arrSize && j < arrSize;){
	for(unsigned int i {0}, j {i+1}; i < arrSize && j < arrSize;){
		if (arr[i]+arr[j] == target){
			cout << "Pair found (" << arr[i] << "," << arr[j] << ")" << endl; 
		}
		if (j == arrSize-1){
			++i;
			j = i+1;
		}
		else ++j;
	}
}


int main(){
	int a[] {8,7,2,5,3,1};
	//size_t arrSize = sizeof(a) / sizeof(a[0]);
	unsigned int arrSize = static_cast<unsigned int>(sizeof(a)/sizeof(a[0]));
	printPair(a, arrSize, 10);

	return 0;
}

/**
 *  P.S
 * sizeof returns type size_t, using size_t over int is the correct way of storing object size values
 * you cannot determine the size of an array from the function it is being used for
 * as an argument.
 */