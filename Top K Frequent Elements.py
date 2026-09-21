class Solution:
    def topKFrequent(self, nums, k):
        freq= {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        heap = []
        for element, frequency in freq.items():
            heapq.heappush(heap, (frequency, element))
            if len(heap) > k:
                heapq.heappop(heap)
        ans= []
            ans.append(element)
        while heap:
            frequency, element = heapq.heappop(heap)
        return ans