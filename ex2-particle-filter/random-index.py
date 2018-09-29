#------------------------------------------------------------------------------
#	Libraries
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#	Function represents the process model
#------------------------------------------------------------------------------
def process_model(x, u, sigma_v, sigma_g):
	"""
	[Arguments]
		x : (ndarray) Current position, including x coordinate, y coordinate,
			and angle (radian). The shape of x is (3, 1).

		u : (ndarray) Control signal, including velocity and stearing angle
			(radian). The shape of u is (2, 1).

		sigma_v : (float) Standard deviation of velocity noise.

		sigma_g : (float) Standard deviation of stearing angle noise.

	[Return]
		x_pred : (ndarray) Predicted position, including x coordinate, y
			coordinate and angle (radian). The shape of x_pred is (3, 1).
	"""
	pass


#------------------------------------------------------------------------------
#	Test bench to verify the written function
#------------------------------------------------------------------------------