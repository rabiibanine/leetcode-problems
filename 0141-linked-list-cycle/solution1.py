class Solution:
    def hasCycle(self, head):
        reference_set = set()
        pointer = head

        while pointer:
            if pointer in reference_set:
                return True
            reference_set.add(pointer.next)
            pointer = pointer.next

        return False
