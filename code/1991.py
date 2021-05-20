n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = map(str, input().split())
    tree[parent] = [left,right]
def preorder(parent):
    print(parent,end="")
    if tree[parent][0] != ".":
        preorder(tree[parent][0])
    if tree[parent][1] != ".":
        preorder(tree[parent][1])
13
14
15
16
17
18
19
def postorder(parent):
    if tree[parent][0] != ".":
        postorder(tree[parent][0])
    if tree[parent][1] != ".":
        postorder(tree[parent][1])
    print(parent, end="")
27
preorder("A")
print()
inorder("A")
print()
postorder("A")
34
