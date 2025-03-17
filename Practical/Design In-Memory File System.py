class FileSystem:

    def __init__(self):
        self.os = {}
        

    def ls(self, path: str) -> List[str]:
        path = [i for i in path.split("/") if i]
        ans = self.os
        for i in path:
            ans = ans[i]
        if isinstance(ans, str):
            return [path[-1]]
        return sorted(list(ans.keys()))

    def mkdir(self, path: str) -> None:
        path = [i for i in path.split("/") if i]
        ans = self.os
        for i in path:
            if i not in ans:
                ans[i] = {}
            ans = ans[i]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path = [i for i in filePath.split("/") if i]
        ans = self.os
        for i in path[:-1]:
            ans = ans[i]
        writeFile = path[-1]
        if writeFile not in ans:
            ans[writeFile] = content
        else:
            ans[writeFile] = ans[writeFile] + content

    def readContentFromFile(self, filePath: str) -> str:
        path = [i for i in filePath.split("/") if i]
        ans = self.os
        for i in path:
            ans = ans[i]
        return ans


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)