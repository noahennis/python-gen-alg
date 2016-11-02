

from random import shuffle
import itertools


# Three starting modes-- random genome, all coop, and all defect to begin?


class Agent(object):

	def __init__(self, genome = None):

		self.genome = genome
		# Initialize a new random genome
		if self.genome = None:
			random_genome = [None] * 11 #syntax?
			for index, gene in enumerate(random_genome):
				gene = random.randint(0, 1)
				random_genome[index] = gene
			self.genome = random_genome	

		self.chromosomes = ["000", "001", "010", "011", "100", "101", "110", "111"]  #name?
		self.fitness = 0
		self.memory = [None, None, None]
		self.contingent_plays = dict(zip(chromosomes, genome[:8])) #ob1

		#map gene to chromosome by index; final 3 in genome are first 3 moves
		#have a chromosome dict? so based on what their memory is, they look up the eky, and play that move?
	

def fight(agent1, agent2, rounds = 10):
	"""A pair of agents plays PD for 10 rounds and adjusts their fitness scores."""
	
	current_round = 1

	# Opening Three Rounds
	while current_round in [1, 2, 3]:
		agent1.play = agent1.genome[8 + current_round] #right index?
		agent2.play = agent2.genome[8 + current_round]

		self.PD(agent1, agent1_move, agent2, agent2_move)
		current_round += 1

	# Remaining Rounds
	while current_round < rounds + 1: #starts at 1
		agent1_move = agent1.contingent_plays[agent1.memory]
		agent2_move = agent2.contingent_plays[agent2.memory]
		self.PD(agent1, agent1_move, agent2, agent2_move)
		current_round += 1



def PD(self, agent1, agent1_move, agent2, agent2_move):
	"""Takes in two agents and their moves for that turn, calculates the result, and updates their fitness and memory accordingly."""
	# NB-- whether it works different on first hree moves

	# Payout Schedule
	if agent1_move == 1 and agent2_move == 1: # Mutual cooperation
		agent1.fitness += 3
		agent2.fitness += 3
		self.update_memory(agent1, agent2_move)
		self.update_memory(agent2, agent1_move)

	elif agent1_move == 1 and agent2_move == 1: # agent1 cooperates, agent2 defects
		agent1.fitness += 0
		agent2.fitness += 5
		self.update_memory(agent1, agent2_move)
		self.update_memory(agent2, agent1_move)

	elif agent1_move == 1 and agent2_move == 1: # agent1 defects, agent2 cooperates
		agent1.fitness += 5
		agent2.fitness += 0
		self.update_memory(agent1, agent2_move)
		self.update_memory(agent2, agent1_move)

	elif agent1_move == 1 and agent2_move == 0: # Mutual defection
		agent1.fitness += 1
		agent2.fitness += 1
		self.update_memory(agent1, agent2_move)
		self.update_memory(agent2, agent1_move)

def update_memory(self, agent, opponent_last_move):
	agent.memory = [agent.memory[1]] + [agent.memory[2]] + [opponent_last_move]
	return 



def mate(agent1, agent2):
	"""A pair of agents combines their genomes to produce a new offspring."""
	# read in genome1, genome2
	# randomly combine from one or the other parent
	# mutate 1 location
	# create a new agent with that genome, and append to population
	# repeat x4
	# delete original population at the end?

	pass

def pair_off(self, population):
	"""Takes in list of agents, and returns list of randomly paired agents."""
	random.shuffle(population)
	paired_off_population = zip(population[::2], population[1::2]) # TODO: confirm this works
	return paired_off_population 


def fighting_season(self, population):
	"""Takes in a list of paired off agents, has them fight, and adjusts fitness."""
	for pair in population:
		agent1, agent2 = pair[0], pair[1]
		self.fight(agent1, agent2) # just changes state, no return
	return


def die_off(self, population):
	"""Sorts the population by fitness, and kills off the weaker half."""

	flattened_population = list(itertools.chain(*population))  #?
	flattened_population.sort(key = lambda x: x.fitness, reverse = True) # in place

	culled_population = flattened_population[:len(flattened_population/2)] # confirm this is 1/2
	return culled_population


def mating_season(self, population):
	"""Agents randomly pair off to mate, and each pair produces 4 offspring. The parents die at the end, and the offspring form the new population."""
	#pass in the reduced list 
	# call pair_off to make them pairs
	# have each pair mate and append to next generation population
	# return that population and delete current population 
	# fin 

	pass


def game(self, rounds = 100, population_size = 100):
	""" """
	# Setup
	population = []
	i = 0
	while i < population_size: 
		a = self.Agent()
		population.append(a)
		i += 1

	# Main
	current_round = 1
	while current_round < rounds:
		self.fighting_season(population)
		population = self.die_off(population)
		population = mating_season(population)
		current_round += 1
		#return summary stats?
	return

def summary_stats(self, population):
	cooperates = 0
	defections = 0
	for agent in population:
		agent.genome ### 

	return cooperates / (cooperates + defections) #cooperation ratio 













