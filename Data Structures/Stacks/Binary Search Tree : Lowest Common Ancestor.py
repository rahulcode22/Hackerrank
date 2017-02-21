
node * lca(node * root, int n1,int n2)
{

if (root==NULL) return NULL;
 if (root->data > n1 && root->data > n2)
        return lca(root->left, n1, n2);
     if (root->data < n1 && root->data < n2)
        return lca(root->left, n1, n2);
    return root;
}
