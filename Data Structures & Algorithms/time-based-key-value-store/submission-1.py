class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hash_map[key]
        left, right = 0, len(arr) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                result = arr[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result
