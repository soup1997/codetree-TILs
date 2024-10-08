#include <iostream>
#include <vector>

using namespace std;

int N;
int answer = 0; // 아름다운 수의 갯수
vector<int> vec; // 조합을 담을 벡터 선언

void check(){ // 아름다운 수인지 아닌지 확인하는 함수
    int idx = 0;
    bool flag = true;

    while(idx < vec.size()){
        int standard = vec[idx];
        int cnt = 0;
        while(idx < vec.size() && standard == vec[idx]){
            cnt++;
            idx++;
        }

        if(standard != cnt && cnt % standard != 0){ // 반례조건 명심할 것
            flag = false;
        }
    }
    if(flag) answer++;
}

void makeNum(){ // 경우의 수를 생성하는 함수
    if(vec.size() == N){
        check();
        return;
    }
    else{
        for(int i = 1; i <= 4; i++){
            vec.emplace_back(i);
            makeNum();
            vec.pop_back();
        }
    }
}

int main() {
    cin >> N;
    makeNum();
    cout << answer <<"\n";
    return 0;
}