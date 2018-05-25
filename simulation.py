import blackjack
import matplotlib.pyplot as plt
import numpy as np

class MarkovSimulator:

	def updateDealingVals(self, currValues):
		updateVals = []
		for val in currValues:
			if val < 22:
				updateVals.append(val)

		return updateVals


	def runSimulation(self):
		table = blackjack.Table(numPlayers=1)
		player = table.getPlayer(0)
		states_freq = {}

		# Deal 2 initial cards to the player
		table.dealCard(0)
		table.dealCard(0)

		# Deal cards until bust, enumerating states
		currValues = self.updateDealingVals(player.computeHandValue())
		while len(currValues) > 0:
			for val in currValues:
				if val not in states_freq:
					states_freq[val] = 1
				else:
					states_freq[val] += 1

			table.dealCard(0)
			currValues = self.updateDealingVals(player.computeHandValue())

		#print(str(player), player.computeHandValue())
		print(str(player), states_freq)
		return states_freq, player.getAceNum()

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
			states_freq, ace_num = self.runSimulation()
			sorted_states = sorted(states_freq.keys())
			for state in sorted_states:
				stateCounts[state] += states_freq[state]
				curr = state
				transitionCounts[prev][curr] += states_freq[state]
				prev = curr
			transitionCounts[prev][22] += (2^ace_num)
			#print(transitionCounts)

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


