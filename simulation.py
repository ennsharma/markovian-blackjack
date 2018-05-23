import blackjack
import matplotlib.pyplot as plt
import numpy as np

class MarkovSimulator:

	def runSimulation(self):
		table = blackjack.Table(numPlayers=1)
		player = table.getPlayer(0)
		states = []

		# Deal 2 initial cards to the player
		table.dealCard(0)
		table.dealCard(0)

		# Deal cards until bust, enumerating states
		currValue = player.computeHandValue()
		while currValue < 22:
			states.append(currValue)
			table.dealCard(0)
			currValue = player.computeHandValue()
		return states

	def runNSimulations(self, N):
		stateCounts = {i : 0 for i in range(22)}
		transitionCounts = {}

		for i in range(22):
			transitionCounts[i] = {}
			for j in range(23):
				transitionCounts[i][j] = 0

		for i in range(N):
			prev = 0
			curr = 0
			for state in self.runSimulation():
				stateCounts[state] += 1
				curr = state
				transitionCounts[prev][curr] += 1
				prev = curr
			transitionCounts[prev][22] += 1

		return stateCounts, transitionCounts

	def generateStateHistogram(self, stateCounts):
		x, y, normalizationFactor = [], [], sum(stateCounts.values())
		for state, count in stateCounts.items():
			x.append(state)
			y.append(count / normalizationFactor)
		
		plt.bar(x, y)
		plt.show()

	def estimateTransitionProbabilityMatrix(self, transitionCounts):
		tran_M = np.zeros(shape=(22,23))
		for start_state in transitionCounts:
			end_states = transitionCounts[start_state]
			total_trans = sum(end_states[end_state] for end_state in end_states)*1.0
			
			for end_state in end_states:
				if total_trans > 0:
					tran_M[start_state][end_state] = end_states[end_state] / total_trans

		return tran_M

if __name__ == '__main__':
	simulator = MarkovSimulator()
	stateCounts, transitionCounts  = simulator.runNSimulations(10000)

	simulator.generateStateHistogram(stateCounts)
	transitionMatrix = simulator.estimateTransitionProbabilityMatrix(transitionCounts)
	print(transitionMatrix)


