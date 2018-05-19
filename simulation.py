import blackjack
import matplotlib.pyplot as plt

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
		while currValue < 21:
			states.append(currValue)
			table.dealCard(0)
			currValue = player.computeHandValue()
		return states

	def runNSimulations(self, N):
		stateCounts = {i : 0 for i in range(21)}
		for i in range(N):
			for state in self.runSimulation():
				stateCounts[state] += 1
		return stateCounts

	def generateStateHistogram(self, stateCounts):
		x, y, normalizationFactor = [], [], sum(stateCounts.values())
		for state, count in stateCounts.items():
			x.append(state)
			y.append(count / normalizationFactor)
		
		plt.bar(x, y)
		plt.show()

	def estimateTransitionProbabilityMatrix(self):
		return # TODO

if __name__ == '__main__':
	simulator = MarkovSimulator()
	stateCounts = simulator.runNSimulations(10000)

	simulator.generateStateHistogram(stateCounts)

