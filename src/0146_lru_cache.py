"""
146. LRU Cache

Design a DS that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists,
otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation,
evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:

1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.
"""
"""
    Need DS that supports:
        - O(1) access for k:v lookup -> hashmap
        - Linear DS to keep track of LRU element.
            - O(1) addition on end
            - O(1) removal on all idcs becauase of updates!
            -> Linked List
"""
from dataclasses import dataclass
from typing import TypeVar

Node = TypeVar("Node")


@dataclass
class Node:
    key: int
    val: int
    prev: Node = None
    next: Node = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capactiy = capacity

        # maps int -> Node
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head

    def insert(self, node):
        node.next = self.tail.next
        node.prev = self.tail
        node.next.prev = node
        node.prev.next = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.capactiy:
            lru = self.head.prev
            self.remove(lru)
            del self.cache[lru.key]
