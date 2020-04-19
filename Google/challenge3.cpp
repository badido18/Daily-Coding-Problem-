/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions
that converts between nodes and memory addresses.
*/

// I used C++ fo easy pointers manipulation
//implemetation of Xor liked list

#include <iostream>
#include <string>
#include <sstream>

typedef struct Node {
	int val ;
	Node* npx ;
}Node;

Node Add(Node* list, int element) {
	if node.npx == 0 {
		Node n ;
		n.val = element;
		node->npx = getXor(0, &n):
	}
	else {
		curr = node
	}
}

*Node getXor(a *int, b *int){
	return (a ^ b) ;
}

void  main() {
	Node list ;
	list.val = 5 ; 
	list.npx = getXor(0,0); 
	Add(list,6);
	Add(list,5);
	Add(list,9);
	Add(list,1);
	Add(list,3);
	cout << Get(list,3)
}
