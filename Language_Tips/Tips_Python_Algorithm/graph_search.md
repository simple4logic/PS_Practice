그래프 탐색 (Graph Traversals)
===


# 개념
그래프 탐색은 하나의 정점에서 시작해서 순차적으로 그래프 위의 모든 정점들을 한 번씩 방문하는 것을 말한다. 

# 유형

그래프 탐색에는 크게 두 가지 유형이 있다. 두 유형 모두 방문한 정점을 표시하여 중복된 방문을 방지해야 한다.

## 1. 깊이 우선 탐색(DFS)

### __개념__
깊이 우선 탐색(Depth-First-Search, 이하 DFS)은 형제 노드를 탐색하기 이전에 자식 노드부터 탐색한다. 즉, 미로를 탐색할 때 더 이상 진행할 수 없을 때까지 한 방향으로 쭉 가다가 끝을 만나면 가장 가까운 분기점(갈림길)으로 돌아와서 다른 방향을 다시 탐색한다.

### __특징__
- 한 방향으로 "깊게" 탐색하는 것
- 주로 스택(Stack)을 이용하여 구현
- 재귀로도 구현 가능하며 재귀로 구현 시 더 간단히 구현 가능
- 사용하는 경우 : 모든 노드를 방문하려 할 때 선택
- 후술할 너비 우선 탐색(BFS)에 비해 단순함
- 단순 검색 속도 자체는 BFS에 비해 느림
- 재귀적 알고리즘 형태를 띔
- 어떤 노드를 방문했는지 여부를 검사하지 않으면 재귀적 특성에 의해 무한 루프에 빠질 가능성이 있음

### __DFS의 진행 과정__
![image](https://user-images.githubusercontent.com/68508521/165319337-3b977b0f-c670-4f0f-92a3-3e68db057cca.png)

### __DFS 수도코드__ (재귀)
```md
DFS(G, v)
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
```

### __DFS 수도코드__ (스택)
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

## 2. 너비 우선 탐색(BFS)

### __개념__
너비 우선 탐색(Breadth-First-Search, 이하 BFS)은 자식 노드를 탐색하기 이전에 형제 노드를 전부 탐색한다. 인접한 노드를 먼저 탐색하는 것이다.

### __특징__
- 시작한 노드로부터 가까운 노드들을 먼저 방문하고 그 후에 멀리 떨어진 정점을 방문하는 순회 방법
- 깊게 탐색하기보다 "넓게" 탐색하는 것
- 주로 큐(Queue)를 이용하여 구현
- 사용하는 경우 : 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 경우 선택  
ex 지구 상의 모든 친구 관계를 그래프로 표현한 후 사람 A와 B 사이에 존재하는 경로를 찾는 경우  
*깊이 우선 탐색의 경우 모든 친구 관계를 다 살펴봐야할 가능성이 높음  
*너비 우선 탐색의 경우 A와 가까운 관계부터 탐색해서 소요 시간을 줄일 수 있음
- BFS가 DFS보다 좀 더 복잡함

### __BFS의 진행 과정__
![image](https://user-images.githubusercontent.com/68508521/165323746-0aa493d4-87bf-41da-844b-3bae167591e8.png)

### __BFS 수도코드__
```md
BFS(G, start_v)
    let Q be a queue
    label start_v as discovered
    Q.enqueue(start_v)
    while Q is not empty do
        v := Q.dequeue()
        if v is the goal then
            return v
        for all edges from v to w in G.adjacentEdges(v) do
            if w is not labeled as discovered then
                label w as discovered
                w.parent := v
                Q.enqueue(w)
```

## 참고

> https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html

> https://yoongrammer.tistory.com/85
