# Q2741

## Problem
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

## Input
첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

## Output
첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

## 예제 입력
```
5
```

## 예제 출력

```
1
2
3
4
5
```

## 나의 제출
```cpp
#include<iostream>
using namespace std;

int main(){
    int a;
    int i =0;
    cin >> a;
    while(i<a){
        printf("%d\n", i+1); // cout가 ㅈㄴ 느리다.
        i++;
    }
}
```

## 추가 내용
> 어라 얘 왜 C++ 함수의 cout 아니라 C의 printf로 했지? 

이걸 발견했으면 정답이다. 바로 함수의 차이.cout이 ㅈㄴ 느린함수다. 여기서 시간 ㅈㄴ쳐먹음. 다른거 다 똑같이 놔도 이거 하나 바꾼거 때문에 시간이 초과됐다.

## 총평