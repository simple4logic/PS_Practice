## 간단한 리눅스 커맨드 안내
___

### __1. 기본__
ls : 해당 디렉토리에 있는 파일을 모두 표시  
cd : 해당 디렉토리로 이동  
> ex : cd test/cpp/

<br>

### __2. 입출력__  
&#62; : 명령어의 결과물 저장  
>ex : ls > out.txt 이면 디렉토리의 모든 파일명을 out.txt를 만들어 저장함

&#60; : 해당 파일을 실행시키면서 입력  
> ex : ./a.out < in.txt 이면 a.out 파일을 실행할 때 입력으로 in.txt를 넣어줌

<br>

### __3. 컴파일__
gcc : .c 파일 컴파일  
g++ : .cpp 파일 컴파일  
> ex : g++ test.cpp  
이때 컴파일 결과물은 a.out의 형태로 생성된다.  

gcc의 자주 쓰이는 옵션   
1. -o : 이름을 지정. ex gcc -o file 하면 a.out이 아니라 컴파일 결과물 이름이 file로 생성이 된다.
2. -c : 전처리, 컴파일, 어셈블까지 실행하여 오브젝트 파일(.o)을 생성. 용도는 추후 더 알아볼 것.

<br>

### __4. 실행__
./ : 해당 파일을 실행  
> ex : ./a.out 이면 a.out이라는 파일을 실행