class Y2:
    def value(self, t, v0=None):
	    if v0 is not None:
		self.v0 = v0
	    if not hasattr(self, 'v0'):
                 print('You cannot call value(t) without first calling value (t,v0 to set v0')
                 return None
	    g = 9.81
	    return self.v0*t - 0.5*g*t**2
