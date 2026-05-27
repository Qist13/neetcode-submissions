class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        cars = []
        for i in range(n):
            car = {"p": position[i], "s": speed[i]}
            cars.append(car)
        
        cars.sort(key=lambda x: x["p"], reverse=True)

        times = []
        for car in cars:
            time = (target - car["p"]) / car["s"]
            times.append(time)

        stack = []

        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
