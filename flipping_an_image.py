class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        image_new = []
        row_new = []
        # flip
        for row in image:
            row.reverse()
            row = [item ^ 1 for item in row]
            image_new.append(row)
            
        return image_new 