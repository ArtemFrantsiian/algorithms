/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function(height) {
    let res = 0;

    let l = 0;
    let r = height.length - 1;

    let l_max = 0;
    let r_max = 0;

    while (l < r) {
        if (l_max > height[l]) {
            res += l_max - height[l];
        }

        if (height[l] > l_max) {
            l_max = height[l]
        }

        if (r_max > height[r]) {
            res += r_max - height[r];
        }

        if (height[r] > r_max) {
            r_max = height[r]
        }

        if (r_max > l_max) {
            l++
        } else {
            r--
        }
    }

    return res;
};
