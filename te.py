class Node:
    def __init__(self,value):#이진트리이므로 left와 right만 있어도 됨
        self.value = value
        self.left = None
        self.right = None
 
class NodeMgmt:
    def __init__(self,head): #root노드가 head
        self.head=head
        
    #원하는 값을 트리안에 넣어주는 기능
    def insert(self,value):
        self.current_node = self.head #현재 노드는 head로 잡고
        while True: #순회
            #insert하려는  current_node.value보다 작을 때
            if value < self.current_node.value: 
                if self.current_node.left != None: #left가 있으면 current를 current.left로 이동
                    self.current_node = self.current_node.left
                else: #left가 없으면 left부분에 value값을 넣어줌
                    self.current_node.left = Node(value)
                    break
                    
            #insert하려는 값이 current_node.value보다 클 때
            else:
                if self.current_node.right != None: #아래 아무것도 없다면 current.right로 이동
                    self.current_node = self.current_node.right
                else: #right가 없으면 right부분에 value값을 넣어줌
                    self.current_node.right = Node(value)
                    break
    
    #어떤 값이 존재하는지 판단하는 기능
    def search(self, value):
        self.current_node = self.head
        
        while self.current_node: #current_node가 none이 되면 종료
            if self.current_node.value == value: #현재 노드가 내가 원하는 값인지
                return True
                break
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False    
    
    # 원하는 value의 노드를 삭제하는 기능
    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        
    	# 삭제할 Node 탐색
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break #찾으면 break
            
            elif value < current_node.value: #찾으려 하는 값이 더 작으면 왼쪽으로 이동
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else: #찾으려 하는 값이 더 크거나 같으면 오른쪽으로 이동
                self.parent = self.current_node
                self.current_node = self.current_node.right
            
        if searched == False:
            return False
    
    #탐색이 끝나면
    #Case를 분리하여 삭제해나가는 process
    
#1 leaf node 삭제
        if self.current_node.left == None and self.current_node.right==None:
            if value<self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
           
    
    
#2 child의 left만 가지고 있는 노드 삭제
        if self.current_node.left != None and self.current_node.right==None:
        #current가 parent 왼쪽인지 오른쪽인지
            if vale<self.parent.value: #왼쪽일 때
                self.parent.left = self.current_node.left
            else: #오른쪽일 때
                self.parent.right = self.current_node.left
    
    #child의 right만 가지고 있는 노드를 삭제할 때 똑같은 방식으로 처리
        elif self.current_node.left == None and self.current_node.right!=None:
        
            if value<self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
            
            
#3 Child Node가 두개인 node 삭제
    #삭제할 Node의 오른쪽 자식 중 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
        
    #3-1 삭제할 node가 parent node 왼쪽에 위치
    #3-1-1 삭제할 node의 오른쪽 child가 child 없을 때
    #3-1-2 삭제할 node의 오른쪽 child가 child 있을 때
    
    #3-2 삭제할 node가 parent node 오른쪽에 위치
    #3-2-1 삭제할 node의 오른쪽 child가 child 없을 때
    #3-2-2 삭제할 node의 오른쪽 child가 child 있을 때
    
        if self.current_node.left != None and self.current_node.right != None:
            if value<self.parent.value: #3-1
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:#left 타고 최대한 간 후
                    self.change_node.parent = self.change_node
                    self.change_node = self.change_node.left
                
                if self.change_node.right != None: #3-1-2
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right