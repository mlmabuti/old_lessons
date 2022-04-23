#include <iostream>
#include <stdio.h>
#include <ctime>
#include <vector>
#include <cstdlib>

using namespace std;

vector<int> vector_generator(int size_of_vector, int max){

	vector <int> v {};

	srand(time(0));
	for (int i {0}; i < size_of_vector; i++){
		v.push_back(rand()%max+1);
	}
	return v;
	// rand() % size_of_vector + 1;
}

void print(vector<int> vec){
	for(auto i : vec){
		cout << i << endl;
	}
}

int main(){
	vector <int> random_vector {vector_generator(10, 100)};
	print(random_vector);	
	
	return 0;
}


