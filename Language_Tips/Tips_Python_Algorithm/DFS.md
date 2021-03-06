DFS(Depth-First-Search)
===

이전에 그래프 탐색 게시글에서 DFS의 개념과 수도코드, 그리고 각종 특징들을 설명한 적이 있다. 이번에는 실제 파이썬 코드로는 어떻게 구현되는지와 그 코드를 풀이하여 설명해보겠다.

코드를 설명하기에 앞서 구현한 DFS 알고리즘에 쓰이는 그래프는 다음과 같다.

![image](https://user-images.githubusercontent.com/68508521/165530529-c84258db-4e79-470e-87cc-d330de890c54.png)

이를 python dictionary처럼 표현해서 함수로 다룰 수 있도록 변형해보자. 각 노드를 key로, 그 노드(key)에서 향할 수 있는 다음 노드들을 value로 정한다면 다음처럼 표현할 수 있을 것이다.

```py
graph={
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}
```



# 재귀 구조 풀이
DFS는 기본적으로 스택을 이용하여 구현하는 것이 일반적이나, 재귀적 풀이를 이용하여 더 쉽고 간단하게 구현할 수 있다. 먼저 수도코드를 보자.

## __DFS Pseudo code with recursion__
```md
DFS(G, v)
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

이를 실제 파이썬 코드로 구현하면 다음과 같다.

## __DFS python code with recursion__
```py
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```

위에서 dictionary 형태로 만든 그래프를 넣고 test-run한 결과는 다음과 같다.

```py
ans = recursive_dfs(1) #시작 vertex = 1
print(ans)
>>> [1, 2, 5, 6, 7, 3, 4]
```

결과를 보면 그래프 위의 모든 점을 성공적으로 읽었음을 확인할 수 있다. 이제 올바르게 동작한다는 것을 확인했으니, 함수를 하나하나 나누어 분석해보자.

## 분석

먼저 매개변수부터 확인하자. v는 정점(vertex)으로, 처음 순회를 시작하는 시작점을 뜻한다. discovered라는 리스트는 따로 입력하지 않으면 알아서 빈 리스트를 디폴트로 인수로 가진다. 따로 입력받은 경우에는 그것을 그대로 가져다 쓸 것이다.  

그 다음을 보자. 해당 vertex는 지금 방문해서 읽고 있기 때문에 append로  discovered 리스트에 먼저 추가해준다.  

이제 for문을 보자. for문을 통해 해당 그래프에서 노드 하나에 연결된 다른 노드들을 모두 확인하고 있다. vertex 1을 예시로 보자. 1과 연결된 vertex는 2, 3, 4이다. 따라서 w는 처음에는 2로 시작한다. 이때 2는 discovered 리스트에 들어가 있지 않기 때문에, 2를 현재 노드로 인수로 넣고 이미 1이 들어가있는 discovered 리스트를 인수로 넣어준다. 이렇게 되면 노드 1에서 노드2로 진출한 상태에서 다시 처음 과정을 반복하게 된다.  

이런 방식으로 진행되면 각 노드에 연결된 첫 자식 노드의 끝까지 파고들고, 노드의 끝을 만나면 바로 그 노드의 부모 노드의 다음 번 자식 노드를 탐색하게 된다. 재귀의 특성 때문이다. 이런 이유로 DFS는 일단 "끝"을 볼 때까지 자식 노드를 탐색하게 된다. 그래서 첫 노드(root-node)의 다른 자식 노드를 탐색하기까지는 한참 걸린다. 


# 스택 구조 풀이

## __DFS Pseudo code with stack__
```md
DFS_iterative(G, v)
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do 
                S.push(w)
```

이를 실제 파이썬 코드로 구현하면 다음과 같다.

## __DFS python code with stack__
```py
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```

위에서 dictionary 형태로 만든 그래프를 넣고 test-run한 결과는 다음과 같다.

```py
ans = iterative_dfs(1) #시작 vertex = 1
print(ans)
>>> [1, 4, 3, 5, 7, 6, 2]
```

위의 재귀적 풀이와는 순서가 다소 다른 결과가 나온다. 이는 아래에 추가적으로 설명하겠다.

## 분석

먼저 함수의 매개변수 'start_v'는 시작하는 노드이다. 위 그래프에서는 '1'이 해당한다.  

탐색을 진행함에 따라 특정 노드에 방문했는지를 확인해야 하기 때문에 discovered 리스트를 만들어준다. 

스택을 이용하기 때문에 stack 리스트를 만들어주고, 거기에 현재 노드인 'start_v'를 넣어준다.  

이제 while문을 이용해서 stack이 텅 빌 때까지 루프를 반복해준다. 루프가 시작되면, stack에서 맨 마지막 원소를 pop해서 v에 할당하고, v가 방문한 노드인지 검사한다.  

1. 방문한 경우, while문 처음으로 돌아와 stack에서 원소를 다시 pop해서 검사를 다시 실시한다.

2. 방문하지 않은 경우, 해당 노드를 discovered 리스트에 append하고 해당 노드와 연결된 모든 자식 노드들을 stack에 append한다.

stack에 들어갔었던 모든 원소들이 discovered에 기록된 경우 루프는 종료되며 그래프 탐색을 마친다.


## 비교

재귀 구조 풀이와 스택 구조 풀이의 차이점을 꼽으면 그 결과에서 찾을 수 있다.

```py
#재귀 구조 풀이
ans = recursive_dfs(1)
print(ans)
>>> [1, 2, 5, 6, 7, 3, 4]

#스택 구조 풀이
ans = iterative_dfs(1)
print(ans)
>>> [1, 4, 3, 5, 7, 6, 2]
```

그래프 탐색 결과를 보면 다른 순서로 정렬되어 있음을 볼 수 있다.  

- 재귀 구조 풀이를 보면 사전적 순서에 따라 자식 노드가 정렬되어 있다. 즉 1의 자식 노드 2, 3, 4 중에 2가 먼저 discovered 되고, 5의 자식 노드 6, 7 중에 6이 먼저 discovered 되는 방식이다.  

- 스택 구조 풀이를 보면 stack-pop 구조에 따라 가장 마지막으로 stack에 append된 순서에 따라 진행된다. 처음 시작 노드 1을 기준으로 2, 3, 4가 stack에 append 되는데, 가장 마지막으로 append된 4부터 discovered 된다.  

이런 차이를 이해한다면 같은 DFS임에도 불구하고 탐색 결과의 순서에 차이가 발생하는 것을 이해할 수 있다.