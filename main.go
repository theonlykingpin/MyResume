package main

import "math"

func abs(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func getCost(nums, cost []int, target int) int {
	ret := 0

	for i := 0; i < len(nums); i++ {
		ret += abs(target, nums[i]) * cost[i]
	}

	return ret
}

func minCost(nums []int, cost []int) int64 {
	var ret int64
	size := len(nums)
	end := math.MinInt64
	begin := math.MaxInt64

	for i := 0; i < size; i++ {
		if end < nums[i] {
			end = nums[i]
		}

		if begin > nums[i] {
			begin = nums[i]
		}
	}

	for begin < end {
		mid := begin + (end-begin)/2

		c1 := getCost(nums, cost, mid)
		c2 := getCost(nums, cost, mid+1)

		if c1 > c2 {
			begin = mid + 1
			ret = int64(c2)
		} else {
			end = mid
			ret = int64(c1)
		}
	}

	return ret
}
