class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people, limit) {
        people.sort((a, b) => a - b);
        let minInd = 0;
        let maxInd = people.length - 1;
        let count = 0;
        while (minInd <= maxInd) {
            if (people[minInd] + people[maxInd] <= limit) {
                count += 1;
                minInd += 1;
                maxInd -= 1;
            } else {
                count += 1;
                maxInd -= 1
            }
        }

        return count;
    }
}
