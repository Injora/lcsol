class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        i = 0
        j=0
        while i<len(nums1) and j<len(nums2) :
            if nums1[i]>nums2[j]:
                l.append(nums2[j])
                j+=1
            elif nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else :
                l.append(nums1[i])
                l.append(nums2[j])
                i+=1
                j+=1
        while i<len(nums1) :
            l.append(nums1[i])
            i+=1
        while j<len(nums2) :
            l.append(nums2[j])
            j+=1
        if len(l) % 2 == 1:
            return l[len(l) // 2]
        else:
            return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
