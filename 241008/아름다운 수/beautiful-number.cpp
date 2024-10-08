#include <iostream>
#include <vector>

using namespace std;

int N;
int answer = 0;
vector<int> vec;

void check(){
    int idx = 0;
    
    bool flag = true;

    while(idx < vec.size()){
        int standard = vec[idx];
        int cnt = 0;
        while(idx < vec.size() && standard == vec[idx]){
            cnt++;
            idx++;
        }

        if(standard != cnt || cnt % standard != 0){
            flag = false;
        }
    }
    if(flag) answer++;
}

void makeBeautifulNum(){
    if(vec.size() == N){
        check();
        return;
    }
    else{
        for(int i = 1; i <= 4; i++){
            vec.emplace_back(i);
            makeBeautifulNum();
            vec.pop_back();
        }
    }
}

int main() {
    cin >> N;
    makeBeautifulNum();
    cout << answer <<"\n";
    return 0;
}