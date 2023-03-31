import random

mutation_rate = 0.65


def fitness(num1):
    return num1 ** 2


def decode_binary_string(bs):
    t2 = 1
    bin_str = 0
    for i in range(5):
        bin_str += int(bs[(5 - i - 1)]) * (t2)
        t2 = t2 * 2

    return bin_str


def best_candidate(gen):
    maximum = 0
    best_index = 0
    for i in range(len(gen)):
        if decode_binary_string(gen[i]) > maximum:
            maximum = decode_binary_string(gen[i])
            best_index = i

    return gen[best_index]


def parentselector(parents):
    total_fitness = 0
    for i in parents:
        total_fitness += fitness(decode_binary_string(i))

    output = []

    for j in range(2):
        r = random.random()
        cum_sum = 0
        for k in parents:
            cum_sum += (fitness(decode_binary_string(k)) / total_fitness)
            if cum_sum > r:
                output.append(k)
                break

    return output


def crossover_t1(mummy, papa):
    offspring = []
    tp = random.randint(1, 4)
    offspring.append(mummy[0:tp] + papa[tp:5])
    offspring.append(papa[0:tp] + mummy[tp:5])
    return offspring


def crossover_t2(mummy, papa):
    offspring = []
    point1 = random.randint(1,2)
    point2 = random.randint(3,4)

    offspring.append(mummy[0:point1] + papa[point1:point2] + mummy[point2:5])
    offspring.append(papa[0:point1] + mummy[point1:point2] + papa[point2:5])
    return offspring


def mutation(children, typ):
    for fg1 in range(len(children)):
        t = random.random()
        if typ == 0:
            if t < mutation_rate:
                children[fg1] = flip(children[fg1])

        if typ == 1:
            if t < mutation_rate:
                children[fg1] = swapbit(children[fg1])

    return children


def flip(s):
    r = random.randint(0, 4)

    list_str = list(s)

    if list_str[r] == "0":
        list_str[r] = "1"
    elif list_str[r] == "1":
        list_str[r] = "0"

    s2 = "".join(list_str)
    return s2


def swapbit(s):
    t = random.sample(range(0, 5), 2)

    list_str = list(s)

    temp = list_str[t[0]]
    list_str[t[0]] = list_str[t[1]]
    list_str[t[1]] = temp

    s2 = "".join(list_str)
    return s2


def Genetic(p, c, m, t, x, i):
    arr = []
    for j in range(p):
        ind = ''.join(random.choice(['0', '1']) for j in range(5))
        arr.append(ind)

    print("Our Initial Population is - ")
    print(arr)

    counter = 0
    lmo = i
    x = x + 1

    best_value = 0
    best_itr = 0
    ans = 0

    if (t == 1):

        for itr in range(i):
            print(f"Generation No. - {itr + 1}")
            parents = []
            children = []
            for kt in range(p):
                parents.append(decode_binary_string(arr[kt]))

            for i in range(p // 2):
                child = []
                shaadi = parentselector(arr)
                if (c == 0):
                    child = crossover_t1(shaadi[0], shaadi[1])
                else:
                    child = crossover_t2(shaadi[0], shaadi[1])

                children.append(child[0])
                children.append(child[1])

            if (p % 2 == 1):
                children.append(arr[random.randint(0, p - 1)])

            arr = mutation(children, m)
            print(arr)

            for it in range(p):
                if fitness(decode_binary_string(arr[it])) >= best_value:
                    best_value = fitness(decode_binary_string(arr[it]))
                    ans = decode_binary_string(arr[it])
                    best_itr = itr + 1

        print("")
        print(f"Best Solution - {ans}, Best Fitness - {ans ** 2}, in Generation {best_itr}")

    if (t == 0):

        for itr in range(1000000):
            print(f"Generation No. - {itr + 1}")
            parents = []
            children = []
            for kt in range(p):
                parents.append(decode_binary_string(arr[kt]))

            for i in range(p // 2):
                child = []
                shaadi = parentselector(arr)
                if (c == 0):
                    child = crossover_t1(shaadi[0], shaadi[1])
                else:
                    child = crossover_t2(shaadi[0], shaadi[1])

                children.append(child[0])
                children.append(child[1])

            if (p % 2 == 1):
                children.append(arr[random.randint(0, p - 1)])
            arr = mutation(children, m)
            print(arr)

            for it in range(p):
                if fitness(decode_binary_string(arr[it])) > best_value:
                    best_value = fitness(decode_binary_string(arr[it]))
                    ans = decode_binary_string(arr[it])
                    best_itr = itr + 1
                    counter = 0

            counter += 1

            if counter == x - 1:
                print("")
                print(f"Best Solution - {ans}, Best Fitness - {ans ** 2}, in Generation {best_itr}")
                print(f"Terminated at Generation No. - {itr + 1} as no Improvement seen in {counter} Iterations")
                break


cross = 0
mut = 0
Termination_condition = 0
iterations = 10
improv = 3

pop = int(input("Enter Population Size : "))
cross = int(input("Enter Crossover Type (1-Point crossover (0) or 2-Point crossover (1)) : "))
mut = int(input("Enter Mutation Type (Bit flip (0) or swap mutation (1)) : "))
Termination_condition = int(
    input("Enter Termination Condition (No improvement for x iteration (0) or Fixed Number of Iterations (1)): "))

if Termination_condition == 1:
    iterations = int(input("Enter The Number of Iteration : "))
else:
    improv = int(input("Enter The Number of Iteration without Improvement till termination: "))

print("")
Genetic(pop, cross, mut, Termination_condition, improv, iterations)



