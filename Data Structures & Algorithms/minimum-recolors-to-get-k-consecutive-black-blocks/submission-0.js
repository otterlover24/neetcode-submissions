class Solution {
    /**
     * @param {string} blocks
     * @param {number} k
     * @return {number}
     */
    minimumRecolors(blocks, k) {
        let minRecolor = 0;
	    let currRecolor = 0;
        let left = 0;
        let right = k - 1;

        // Count once
        for (let i = left; i <= right; i++) {
            if (blocks[i] === 'W') {
                currRecolor += 1;
            }
        }
        minRecolor = currRecolor;	

        // Update
        while (right < blocks.length - 1) {
            left += 1;
            right += 1;
            if (blocks[left - 1] == 'W') {
                currRecolor -= 1;
            }
            if (blocks[right] == 'W') {
                currRecolor += 1;
            }
            minRecolor = Math.min(minRecolor, currRecolor);
        }
        
        return minRecolor;
    }
}