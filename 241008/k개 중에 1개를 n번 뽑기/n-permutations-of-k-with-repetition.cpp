#include <iostream>
#include <vector>
using namespace std;

vector<int> answer;
int K, N;

void choose(){
    if(answer.size() == 2){
        for(auto a: answer){
            cout << a << " ";
        }
        cout << "\n";
    }

    else{
        for(int i=1; i <= K; i++){
            answer.emplace_back(i);
            choose();
            answer.pop_back();

        }
    }
}

int main() {
    cin >> K >> N;
    choose();
    return 0;
}