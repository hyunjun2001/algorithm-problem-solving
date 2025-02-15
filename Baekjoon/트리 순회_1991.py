# 백준 트리 순회 문제이다.
# 문제 번호는 1991번

import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder('A')
print()
inorder("A")
print()
postorder('A')

