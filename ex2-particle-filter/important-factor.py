#------------------------------------------------------------------------------
#	Libraries
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#	Function represents the process model
#------------------------------------------------------------------------------
def compute_important_factor(x, z, sigma_r, sigma_b):
	"""
	[Arguments]
		x : (ndarray) Current position, including x coordinate, y coordinate,
			and angle (radian). The shape of x is (3, 1).

		z : (ndarray) Ground truth of measurement, as described in the readme
			file. The shape of z is (3, 5).

		sigma_r : (float) Standard deviation of the range noise of the lazer.

		sigma_b : (float) Standard deviation of the bearing angle noise
			(radian) of the lazer.

	[Return]
		w : (float) Important factor.
	"""
	pass


#------------------------------------------------------------------------------
#	Test bench to verify the written function
#------------------------------------------------------------------------------