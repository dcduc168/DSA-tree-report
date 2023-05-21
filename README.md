# IT003_Tree

## AVL Tree

- Là cây tìm kiếm nhị phân (**BST**) tự cân bằng sao cho chiều cao của cây con trái và phải của tất cả các node không được vượt quá 1.
- Đa số các thao tác cơ bản của **BST** đều có độ phức tạp là $O(h)$ với h là chiều cao của **BST**. Với các trường hợp cây bị lệch, độ phức tạp xấu nhất sẽ là $O(n)$. Và cây AVL đã khắc phục được điều đó bằng cách tự cân bằng lại cây sau mỗi thao tác **chèn**, **xoá**. Còn với cây AVL thì các node được phân phối đều ở các nhánh.

> Vậy nên chiều cao của cây AVL luôn là $\log_2(n)$

- Trong code cài đặt sẽ gồm 3 thao tác cơ bản của cây là **chèn**, **xoá** và **cân bằng lại**.
- Mỗi lượt chèn hoặc xoá 1 node nếu xảy ra mất cân bằng thì có thể xảy ra 1 trong 4 trường hợp sau:

  - Left Left Case
  - Left Right Case
  - Right Right Case
  - Right Left Case

- Code cài đặt được đính kèm ở file `AVLTree.cpp`
- Với 10 test case gồm $1000000$ số nguyên khác nhau thì ta thu được kết quả chiều cao của cây ở $10$ bộ test là $20$. Vì chiều cao của cây luôn là $\log_2(n)$ nên với $1000000$ số ta sẽ luôn có được chiều cao của cây là $\log_2(1000000)\approx20$

## Red Black Tree

- Là cây tìm kiếm nhị phân (**BST**) tự cân bằng và mỗi nút trong cây đều được **tô màu** (đỏ hoặc đen).
- Cây đỏ đen có các **tính chất** sau:
  - Node ở **root** có màu **đen**
  - Những **NULL node** sẽ được tô màu **đen**
  - **Con** của node **đỏ** sẽ là node **đen** &rarr; **Cha** của node **đỏ** là node **đen**
  - Mọi **đường đi** từ một **node** đến bất kỳ **NULL node** nào đều có cùng số lượng node **đen**.
- Đa số các thao tác cơ bản của **BST** đều có độ phức tạp là $O(h)$ với h là chiều cao của **BST**. Với các trường hợp cây bị lệch, độ phức tạp xấu nhất sẽ là $O(n)$. Và cây đỏ đen đã khắc phục được điều đó bằng cách tự cân bằng lại cây sau mỗi thao tác **chèn**, **xoá**. Còn với cây đỏ đen thì các node được phân phối đều ở các nhánh.

> Vậy nên chiều cao của cây đỏ đen luôn nhỏ hơn $2\log_2(n+1)$
> &rarr; Trong cây đỏ đen luôn tồn tại ít nhất $n/2$ node đen.

- Code cài đặt được đính kèm ở file `RBTree.cpp`
- Với 10 test case gồm $1000000$ số nguyên khác nhau thì ta thu được kết quả chiều cao của cây ở $10$ bộ test là $20$. Vì chiều cao của cây luôn là $2\log_2(n+1)$ nên với $1000000$ số ta sẽ luôn có được chiều cao của cây là $2\log_2(n+1)\approx38$
