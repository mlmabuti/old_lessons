// just another bad idea


#include <iostream>
#include <stdio.h>
#include <vector>

std::vector<std::string> Union(std::vector <std::string> a, std::vector <std::string> b) {
    std::vector <std::string> temp {};
    for (std::string i : a)
        temp.push_back(i);
    for (std::string i : b)
        temp.push_back(i);

    std::vector <std::string> c{};
    size_t tempSize {temp.size()};

    for (size_t i {0}, j {i+1}; i < tempSize && j < tempSize;) {
        if (temp[i] == temp[j]){
            // c.erase(i); // jessas
            i++;
        }
        ++j; 
    }

    return c;
}

void sw1(){
    std::vector <std::string> U {"a","b","c","d","e","f","g","h"},
                  A {"a","b","d","f","g"},
                  B {"d","g","h","e","a"};

    for (std::string i : Union(A,B))
        std::cout << i << " ";
    std::cout << std::endl;
    
}


int main(int argc, char const *argv[])
{
    sw1();
    return 0;
}
