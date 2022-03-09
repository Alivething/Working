#include <iostream>
#include <vector>\

using namespace std;
 
/* A binary tree node has data,
pointer to left child and a
pointer to right child */
struct Node
{
    int data;
    Node* left, * right;
    int sum;
}*root;
 
/* Helper function that allocates a
new node */
Node* newNode(int data)
{
    Node* node = new Node();
    node->data = data;
    node->left = node->right = NULL;
    node->sum = 2147483646;
    return (node);
}
 
// Function to insert nodes in level order
Node* insertLevelOrder(int arr[], Node* root,
                       int i, int n)
{
    // Base case for recursion
    if (i < n)
    {
        Node* temp = newNode(arr[i]);
        root = temp;
 
        // insert left child
        root->left = insertLevelOrder(arr,
                   root->left, 2 * i + 1, n);
 
        // insert right child
        root->right = insertLevelOrder(arr,
                  root->right, 2 * i + 2, n);
    }
    return root;
}
 
// Function to print tree nodes in
// InOrder fashion
void sumOrder(Node* root)
{
    if (root != NULL)
    {
        Node *tleft = root->left;
        Node *tright = root->right;
        if(tleft !=NULL)
            tleft->sum = root->sum + tleft->data;
        if(tright !=NULL)
            tright->sum = root->sum + tright->data;
        sumOrder(root->left);
        sumOrder(root->right);
    }
}

void inOrder(Node* root)
{
    if (root != NULL)
    {
        inOrder(root->left);
        if(root->left == NULL)
        {
            cout<<"Sum:"<<root->sum<<", Leaf Node:"<< root->data<<endl;
        }
        inOrder(root->right);
    }
}
 
// Driver program to test above function
int main()
{
    int arr[] = {22, -7, 8, 4, 5, 3, -1};

    int n = sizeof(arr)/sizeof(arr[0]);
    root = insertLevelOrder(arr, root, 0, n);
    root->sum = root->data;
    sumOrder(root);
    inOrder(root);
}