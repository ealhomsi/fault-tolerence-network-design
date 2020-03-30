class Edge:
	def __init__(self, u, v, c, r):
		self.u = u
		self.v = v
		self.c = c
		self.r = r

	def __repr__(self):
		return 'endpoints: {}, cost: {}, reliability: {} \n'.format(self.u+"<->"+self.v,
                                  self.c,
                                  self.r)